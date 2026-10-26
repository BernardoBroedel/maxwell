import asyncio

from fakes import FakeChatModel
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from maxwell.graph import build_tutor_graph
from maxwell.llm import segundos_para_tentar_de_novo


def test_tutor_chama_ferramenta_e_responde():
    llm = FakeChatModel(
        messages=iter(
            [
                AIMessage(
                    "",
                    tool_calls=[{"name": "analisar_carga", "args": {"zl": "100", "z0": "50"}, "id": "c1"}],
                ),
                AIMessage("Seu Γ está certo! E a ROE, quanto deu?"),
            ]
        )
    )
    graph = build_tutor_graph(llm, "prompt de teste")

    result = asyncio.run(graph.ainvoke({"messages": [HumanMessage("Achei Γ = 1/3 para 100 Ω numa linha de 50 Ω")]}))

    tool_message = next(m for m in result["messages"] if isinstance(m, ToolMessage))
    assert '"roe": 2' in tool_message.content
    assert result["messages"][-1].content == "Seu Γ está certo! E a ROE, quanto deu?"


def test_erro_na_ferramenta_volta_para_o_modelo():
    llm = FakeChatModel(
        messages=iter(
            [
                AIMessage("", tool_calls=[{"name": "analisar_carga", "args": {"zl": "abc"}, "id": "c1"}]),
                AIMessage("Pode me dizer a impedância da carga de novo?"),
            ]
        )
    )
    graph = build_tutor_graph(llm, "prompt de teste")

    result = asyncio.run(graph.ainvoke({"messages": [HumanMessage("oi")]}))

    tool_message = next(m for m in result["messages"] if isinstance(m, ToolMessage))
    assert "Não entendi" in tool_message.content
    assert result["messages"][-1].content == "Pode me dizer a impedância da carga de novo?"


class LimiteAtingido(Exception):
    status_code = 429


class FakeComLimite(FakeChatModel):
    """Bate no limite por minuto uma vez e depois responde."""

    falhas: int = 1

    async def ainvoke(self, *args, **kwargs):
        if self.falhas:
            self.falhas -= 1
            raise LimiteAtingido("Rate limit reached. Please try again in 1.5s.")
        return await super().ainvoke(*args, **kwargs)


def test_tutor_espera_o_limite_da_api_e_tenta_de_novo(monkeypatch):
    esperas = []

    async def esperar(segundos):
        esperas.append(segundos)

    monkeypatch.setattr("maxwell.graph.asyncio.sleep", esperar)
    llm = FakeComLimite(messages=iter([AIMessage("Qual relação liga Γ à carga?")]))
    graph = build_tutor_graph(llm, "prompt de teste")

    result = asyncio.run(graph.ainvoke({"messages": [HumanMessage("Como calculo Γ?")]}))

    assert esperas == [2.5]
    assert result["messages"][-1].content == "Qual relação liga Γ à carga?"


def test_segundos_para_tentar_de_novo():
    assert segundos_para_tentar_de_novo(LimiteAtingido("Please try again in 34.5s.")) == 35.5
    assert segundos_para_tentar_de_novo(LimiteAtingido("Please try again in 1m20s.")) == 60
    assert segundos_para_tentar_de_novo(LimiteAtingido("sem tempo na mensagem")) == 21
    assert segundos_para_tentar_de_novo(ValueError("outro erro")) is None
