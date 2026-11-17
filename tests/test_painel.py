import asyncio

from fakes import FakeChatModel
from fastapi.testclient import TestClient
from langchain_core.messages import AIMessage

from maxwell.api import create_app
from maxwell.config import Settings
from maxwell.painel import PainelProfessor, achar_aluno, analisar, periodo_em_dias, relatorio_da_turma, temas_de

AGORA = 1_800_000_000

USUARIOS = [
    {"id": "adm", "name": "Professor", "email": "prof@ufes.br", "role": "admin"},
    {"id": "u1", "name": "João Silva", "email": "joao@ufes.br", "role": "user"},
    {"id": "u2", "name": "Maria Souza", "email": "maria@ufes.br", "role": "user"},
    {"id": "u3", "name": "Pedro", "email": "pedro@ufes.br", "role": "pending"},
]

CHATS = [
    {
        "id": "c1",
        "user_id": "u1",
        "chat": {
            "history": {
                "messages": {
                    "m1": {"id": "m1", "role": "user", "content": "Qual a ROE de 100 Ω? só a resposta", "timestamp": AGORA - 100},
                    "m2": {
                        "id": "m2", "parentId": "m1", "role": "assistant", "model": "maxwell-tutor",
                        "content": "Tente primeiro.", "timestamp": AGORA - 90, "annotation": {"rating": -1},
                    },
                    "m3": {"id": "m3", "role": "user", "content": "### Task: gere um título", "timestamp": AGORA - 80},
                    "m4": {"id": "m4", "role": "user", "content": "Como uso a carta de Smith?", "timestamp": AGORA - 40 * 86400},
                }
            }
        },
    },
    {"id": "c2", "user_id": "adm", "chat": {"history": {"messages": {"x": {"role": "user", "content": "ROE", "timestamp": AGORA}}}}},
]


def test_periodo_em_dias():
    assert periodo_em_dias("relatório da turma dos últimos 30 dias") == 30
    assert periodo_em_dias("relatório do mês") == 30
    assert periodo_em_dias("2 semanas") == 14
    assert periodo_em_dias("todo o semestre") == 3650
    assert periodo_em_dias("relatório") == 7


def test_temas_sem_falso_positivo():
    assert temas_de("Qual a ROE? E o Γ?") == ["Coeficiente de reflexão", "ROE / TOE"]
    assert temas_de("carta de Smith com toco") == ["Carta de Smith", "Casamento e tocos"]
    assert temas_de("isso pode corroer o heroe") == []


def test_analisa_so_alunos_no_periodo():
    analise = analisar(USUARIOS, CHATS, dias=7, agora=AGORA)
    joao = analise["alunos"]["u1"]
    assert [a.nome for a in analise["ativos"]] == ["João Silva"]
    assert [a.nome for a in analise["inativos"]] == ["Maria Souza"]
    assert len(joao.perguntas) == 1  # a tarefa do Open WebUI e a pergunta antiga ficam de fora
    assert joao.pedidos_de_resposta == 1
    assert joao.descurtidas == 1
    assert analise["ruins"][0]["pergunta"].startswith("Qual a ROE")
    assert "| João Silva | 1 | 1 | ROE / TOE | 1 | 0 / 1 |" in relatorio_da_turma(analise)


def test_acha_aluno_pelo_nome_sem_acento():
    alunos = analisar(USUARIOS, CHATS, dias=7, agora=AGORA)["alunos"]
    assert achar_aluno("relatório do aluno joão", alunos).nome == "João Silva"
    assert achar_aluno("relatório da maria souza", alunos).nome == "Maria Souza"
    assert achar_aluno("relatório geral", alunos) is None


class FonteFalsa:
    async def dados(self):
        return USUARIOS, CHATS


def test_painel_responde_relatorio_da_turma_com_resumo():
    llm = FakeChatModel(messages=iter([AIMessage("### Principais dificuldades\n- ROE")]))
    painel = PainelProfessor(FonteFalsa(), llm)
    texto = asyncio.run(painel.responder("Relatório da turma de todo o semestre"))
    assert "Relatório da turma (todo o período)" in texto
    assert "Análise das dificuldades" in texto and "- ROE" in texto


def test_painel_aparece_so_com_credenciais_e_atende_pela_api():
    painel = PainelProfessor(FonteFalsa(), None)
    client = TestClient(create_app(graphs={}, settings=Settings(llm_api_key="teste"), painel=painel))
    ids = [m["id"] for m in client.get("/v1/models").json()["data"]]
    assert ids == ["maxwell-professor"]
    resposta = client.post(
        "/v1/chat/completions",
        json={"model": "maxwell-professor", "stream": False, "messages": [{"role": "user", "content": "relatório do aluno João"}]},
    )
    assert "Relatório de João Silva" in resposta.json()["choices"][0]["message"]["content"]
