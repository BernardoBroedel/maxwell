import asyncio

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import BaseTool
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from maxwell.llm import segundos_para_tentar_de_novo
from maxwell.material import Busca, formatar_material
from maxwell.tools import TOOLS

MATERIAL_NODE = "material"
TUTOR_NODE = "tutor"
TOOLS_NODE = "ferramentas"

# Quantas mensagens recentes do aluno formam a consulta: com só a última,
# respostas curtas ("não entendi", "e no caso do curto?") perdem o assunto.
MENSAGENS_NA_CONSULTA = 2

# Quantas vezes esperar e repetir uma chamada que bateu no limite por minuto da API
TENTATIVAS_NO_LIMITE = 2


class TutorState(MessagesState):
    material: str


def consulta_do_aluno(state: TutorState) -> str:
    do_aluno = [m.content for m in state["messages"] if isinstance(m, HumanMessage)]
    return "\n".join(str(c) for c in do_aluno[-MENSAGENS_NA_CONSULTA:])


def build_tutor_graph(
    llm: BaseChatModel, system_prompt: str, tools: list[BaseTool] = TOOLS, busca: Busca | None = None
):
    """Grafo do tutor: busca no material (RAG), depois o tutor responde ou chama ferramentas de cálculo e volta a responder."""
    llm_with_tools = llm.bind_tools(tools)

    def material(state: TutorState):
        trechos = busca.buscar(consulta_do_aluno(state)) if busca else []
        return {"material": formatar_material(trechos)}

    async def tutor(state: TutorState):
        sistema = system_prompt
        if state.get("material"):
            sistema += "\n\n" + state["material"]
        mensagens = [SystemMessage(sistema), *state["messages"]]
        # No limite por minuto da API (plano gratuito), espera o tempo pedido e tenta
        # de novo: a resposta demora, mas chega.
        for tentativa in range(TENTATIVAS_NO_LIMITE + 1):
            try:
                response = await llm_with_tools.ainvoke(mensagens)
                break
            except Exception as erro:
                espera = segundos_para_tentar_de_novo(erro)
                if espera is None or tentativa == TENTATIVAS_NO_LIMITE:
                    raise
                await asyncio.sleep(espera)
        return {"messages": [response]}

    builder = StateGraph(TutorState)
    builder.add_node(MATERIAL_NODE, material)
    builder.add_node(TUTOR_NODE, tutor)
    # Erros nas ferramentas (ex.: impedância mal escrita) voltam como mensagem para o
    # modelo, que pode pedir ao aluno para reescrever, em vez de derrubar a conversa.
    builder.add_node(TOOLS_NODE, ToolNode(tools, handle_tool_errors=True))
    builder.add_edge(START, MATERIAL_NODE)
    builder.add_edge(MATERIAL_NODE, TUTOR_NODE)
    builder.add_conditional_edges(TUTOR_NODE, tools_condition, {"tools": TOOLS_NODE, END: END})
    builder.add_edge(TOOLS_NODE, TUTOR_NODE)
    return builder.compile()
