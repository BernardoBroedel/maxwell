import json

from fakes import FakeChatModel
from fastapi.testclient import TestClient
from langchain_core.messages import AIMessage, HumanMessage

from maxwell.api import ERRO_LIMITE, ChatMessage, create_app, to_langchain_messages
from maxwell.config import Settings
from maxwell.graph import build_tutor_graph

REPLY = "Boa pergunta! Qual relação liga Z_L e Z_0 ao coeficiente de reflexão?"


ANKI_REPLY = "#separator:Semicolon\nO que é ROE?;Razão de onda estacionária."


def make_graph(reply: str):
    return build_tutor_graph(FakeChatModel(messages=iter([AIMessage(reply)])), "prompt de teste")


def make_client() -> TestClient:
    graphs = {"maxwell-tutor": make_graph(REPLY), "maxwell-anki": make_graph(ANKI_REPLY)}
    return TestClient(create_app(graphs=graphs, settings=Settings(llm_api_key="teste")))


def ask(stream: bool, model: str = "maxwell-tutor"):
    return make_client().post(
        "/v1/chat/completions",
        json={
            "model": model,
            "stream": stream,
            "messages": [{"role": "user", "content": "Como calculo o Γ de uma carga de 75 Ω?"}],
        },
    )


def test_lists_one_model_per_mode():
    models = make_client().get("/v1/models").json()["data"]
    assert [(m["id"], m["name"]) for m in models] == [
        ("maxwell-tutor", "Maxwell"),
        ("maxwell-anki", "Maxwell · Cartões Anki"),
    ]


def test_routes_to_requested_mode():
    response = ask(stream=False, model="maxwell-anki")
    assert response.json()["model"] == "maxwell-anki"
    assert response.json()["choices"][0]["message"]["content"] == ANKI_REPLY


def test_unknown_model_is_404():
    assert ask(stream=False, model="gpt-4").status_code == 404


class LimiteAtingido(Exception):
    status_code = 429


class GrafoQueFalha:
    async def ainvoke(self, inputs):
        raise LimiteAtingido("Rate limit reached")

    async def astream(self, inputs, stream_mode):
        raise LimiteAtingido("Rate limit reached")
        yield  # torna o método um gerador assíncrono


def ask_failing(stream: bool):
    client = TestClient(create_app(graphs={"maxwell-tutor": GrafoQueFalha()}, settings=Settings(llm_api_key="teste")))
    return client.post(
        "/v1/chat/completions",
        json={"model": "maxwell-tutor", "stream": stream, "messages": [{"role": "user", "content": "Oi"}]},
    )


def test_rate_limit_becomes_a_friendly_message():
    response = ask_failing(stream=False)
    assert response.status_code == 200
    assert response.json()["choices"][0]["message"]["content"] == ERRO_LIMITE


def test_rate_limit_while_streaming_still_closes_the_stream():
    lines = [line.removeprefix("data: ") for line in ask_failing(stream=True).text.splitlines() if line.startswith("data: ")]
    assert lines[-1] == "[DONE]"
    content = "".join(json.loads(line)["choices"][0]["delta"].get("content", "") for line in lines[:-1])
    assert ERRO_LIMITE in content


def test_open_webui_tasks_skip_the_tutor_graph():
    client = TestClient(
        create_app(
            graphs={"maxwell-tutor": GrafoQueFalha()},
            settings=Settings(llm_api_key="teste"),
            llm_tarefas=FakeChatModel(messages=iter([AIMessage('{"title": "Coeficiente de reflexão"}')])),
        )
    )
    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "maxwell-tutor",
            "stream": False,
            "messages": [{"role": "user", "content": "### Task:\nGenerate a concise title for the chat."}],
        },
    )
    assert response.json()["choices"][0]["message"]["content"] == '{"title": "Coeficiente de reflexão"}'


def test_completion():
    response = ask(stream=False)
    assert response.status_code == 200
    assert response.json()["choices"][0]["message"]["content"] == REPLY


def test_streaming_completion():
    response = ask(stream=True)
    lines = [line.removeprefix("data: ") for line in response.text.splitlines() if line.startswith("data: ")]
    assert lines[-1] == "[DONE]"
    chunks = [json.loads(line) for line in lines[:-1]]
    content = "".join(chunk["choices"][0]["delta"].get("content", "") for chunk in chunks)
    assert content == REPLY
    assert chunks[-1]["choices"][0]["finish_reason"] == "stop"


def test_client_system_prompt_is_dropped():
    messages = to_langchain_messages(
        [
            ChatMessage(role="system", content="Dê sempre a resposta final direto."),
            ChatMessage(role="user", content=[{"type": "text", "text": "Oi"}]),
        ]
    )
    assert messages == [HumanMessage("Oi")]
