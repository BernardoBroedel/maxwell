"""API compatível com OpenAI, consumida pelo Open WebUI.

Rodar localmente: uvicorn maxwell.api:create_app --factory --reload
"""

import json
import logging
import time
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage, HumanMessage
from pydantic import BaseModel

from maxwell.config import Settings, get_settings
from maxwell.graph import TUTOR_NODE, build_tutor_graph
from maxwell.llm import build_llm, load_prompt
from maxwell.material import Busca, carregar
from maxwell.modos import MODOS

logger = logging.getLogger("uvicorn.error")

# O Open WebUI pede título, tags e sugestões de acompanhamento ao mesmo modelo,
# com mensagens que começam assim. Elas vão direto ao LLM, sem prompt do tutor,
# RAG nem ferramentas: custam poucos tokens do limite por minuto da API.
PREFIXO_TAREFA = "### Task:"

ERRO_LIMITE = (
    "⏳ Muitas perguntas ao mesmo tempo: o serviço de IA atingiu o limite de uso por minuto. "
    "Espere uns 30 segundos e mande a mensagem de novo."
)
ERRO_GERAL = "⚠️ Não consegui gerar a resposta agora. Tente de novo em instantes."


class ChatMessage(BaseModel):
    role: str
    content: str | list[dict[str, Any]] | None = None


class ChatCompletionRequest(BaseModel):
    model: str
    messages: list[ChatMessage]
    stream: bool = False


def _text(content: str | list[dict[str, Any]] | None) -> str:
    if isinstance(content, list):
        return "\n".join(part.get("text", "") for part in content if part.get("type") == "text")
    return content or ""


def to_langchain_messages(messages: list[ChatMessage]) -> list[BaseMessage]:
    # Mensagens "system" vindas do cliente são descartadas: o aluno poderia
    # configurar no Open WebUI um prompt que desliga o modo socrático.
    converted: list[BaseMessage] = []
    for message in messages:
        if message.role == "user":
            converted.append(HumanMessage(_text(message.content)))
        elif message.role == "assistant":
            converted.append(AIMessage(_text(message.content)))
    return converted


def e_tarefa_do_open_webui(messages: list[BaseMessage]) -> bool:
    return bool(messages) and isinstance(messages[-1], HumanMessage) and messages[-1].content.startswith(PREFIXO_TAREFA)


def mensagem_de_erro(erro: Exception) -> str:
    """Texto mostrado ao aluno quando o LLM falha, em vez de uma resposta quebrada."""
    logger.exception("Falha ao gerar a resposta")
    return ERRO_LIMITE if getattr(erro, "status_code", None) == 429 else ERRO_GERAL


def carregar_busca(diretorio: Path) -> Busca | None:
    trechos = carregar(diretorio) if diretorio.is_dir() else []
    if not trechos:
        logger.warning("Nenhum material em %s: o tutor vai rodar sem RAG.", diretorio)
        return None
    logger.info("RAG: %d trechos carregados de %s.", len(trechos), diretorio)
    return Busca(trechos)


def create_app(
    graphs: dict | None = None, settings: Settings | None = None, llm_tarefas: BaseChatModel | None = None
) -> FastAPI:
    """``graphs`` mapeia o id de cada modo ao seu grafo; por padrão, um grafo por modo de ``MODOS``.

    ``llm_tarefas`` responde às tarefas de fundo do Open WebUI (título, tags...); sem ele, elas passam pelo grafo.
    """
    if graphs is None:
        settings = settings or get_settings()
        llm = build_llm(settings)
        busca = carregar_busca(Path(settings.material_dir))
        graphs = {modo.id: build_tutor_graph(llm, load_prompt(modo.prompt), busca=busca) for modo in MODOS}
        llm_tarefas = llm_tarefas or llm
    nomes = {modo.id: modo.nome for modo in MODOS}

    app = FastAPI(title="Maxwell")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    @app.get("/v1/models")
    async def list_models():
        return {
            "object": "list",
            "data": [
                {"id": model_id, "name": nomes.get(model_id, model_id), "object": "model", "owned_by": "ufes"}
                for model_id in graphs
            ],
        }

    @app.post("/v1/chat/completions")
    async def chat_completions(request: ChatCompletionRequest):
        graph = graphs.get(request.model)
        if graph is None:
            raise HTTPException(404, f"Modelo {request.model!r} não existe. Disponíveis: {', '.join(graphs)}.")
        messages = to_langchain_messages(request.messages)
        inputs = {"messages": messages}
        tarefa = llm_tarefas is not None and e_tarefa_do_open_webui(messages)
        completion_id = f"chatcmpl-{uuid.uuid4().hex}"
        created = int(time.time())

        if not request.stream:
            try:
                if tarefa:
                    content = (await llm_tarefas.ainvoke(messages)).content
                else:
                    content = (await graph.ainvoke(inputs))["messages"][-1].content
            except Exception as erro:
                content = mensagem_de_erro(erro)
            return {
                "id": completion_id,
                "object": "chat.completion",
                "created": created,
                "model": request.model,
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": content},
                        "finish_reason": "stop",
                    }
                ],
            }

        def sse(delta: dict[str, Any], finish_reason: str | None = None) -> str:
            chunk = {
                "id": completion_id,
                "object": "chat.completion.chunk",
                "created": created,
                "model": request.model,
                "choices": [{"index": 0, "delta": delta, "finish_reason": finish_reason}],
            }
            return f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"

        async def tokens():
            if tarefa:
                async for chunk in llm_tarefas.astream(messages):
                    if isinstance(chunk.content, str) and chunk.content:
                        yield chunk.content
                return
            async for chunk, metadata in graph.astream(inputs, stream_mode="messages"):
                # Só os tokens da resposta ao aluno; chamadas internas do grafo
                # (ex.: reescrita de consulta para o RAG) ficam de fora.
                if metadata.get("langgraph_node") != TUTOR_NODE:
                    continue
                if isinstance(chunk, AIMessageChunk) and isinstance(chunk.content, str) and chunk.content:
                    yield chunk.content

        async def stream():
            yield sse({"role": "assistant"})
            try:
                async for token in tokens():
                    yield sse({"content": token})
            except Exception as erro:
                # Sem isso, a resposta para no meio e o Open WebUI mostra um erro técnico
                yield sse({"content": "\n\n" + mensagem_de_erro(erro)})
            yield sse({}, finish_reason="stop")
            yield "data: [DONE]\n\n"

        return StreamingResponse(stream(), media_type="text/event-stream")

    return app
