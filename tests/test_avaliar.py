import asyncio
import importlib.util
import json
from pathlib import Path

from fakes import FakeChatModel
from langchain_core.messages import AIMessage

from maxwell.graph import build_tutor_graph

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("avaliar", RAIZ / "scripts" / "avaliar.py")
avaliar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(avaliar)


def test_contem_ignora_espacos_virgula_e_menos_unicode():
    assert avaliar.contem("Γ = 0,333", "0.333")
    assert avaliar.contem("Zin = 40 − j30 Ω", "40-j30")
    assert not avaliar.contem("Γ = 0,5", "0.333")


def test_contem_enxerga_numeros_dentro_do_latex():
    assert avaliar.contem(r"$|\Gamma_L| \approx 0{,}277$", "0.277")
    assert avaliar.contem(r"$Z_{in} = 40\,-\,j30\ \Omega$", "40-j30")


def test_caso_detecta_vazamento_e_ferramenta():
    llm = FakeChatModel(
        messages=iter(
            [
                AIMessage("", tool_calls=[{"name": "analisar_carga", "args": {"zl": "100", "z0": "50"}, "id": "c1"}]),
                AIMessage("O coeficiente é 1/3."),
            ]
        )
    )
    caso = {
        "id": "x",
        "modo": "m",
        "turnos": [{"aluno": "Qual o Γ de 100 Ω em 50 Ω?", "proibido": ["0.333", "1/3"]}],
        "ferramenta_esperada": "analisar_carga",
    }
    r = asyncio.run(avaliar.rodar_caso(caso, {"m": build_tutor_graph(llm, "teste")}, pausa=0))

    assert r["turnos"][0]["ferramentas"] == ["analisar_carga"]
    assert r["problemas"] == ["vazou 1/3"]
    assert not r["passou"]


def test_banco_de_perguntas_usa_modos_existentes():
    from maxwell.modos import MODOS

    ids = {m.id for m in MODOS}
    casos = json.loads((RAIZ / "avaliacao" / "perguntas.json").read_text(encoding="utf-8"))
    assert casos and all(c["modo"] in ids and c["turnos"] for c in casos)
    assert len({c["id"] for c in casos}) == len(casos)


def test_veredito_do_juiz_vira_problemas():
    veredito = avaliar.ler_veredito('Segue: {"fisica_correta": false, "entregou_cedo": true, "seguiu_o_modo": true, "nota": 2}')
    assert avaliar.problemas_do_juiz(veredito) == ["juiz: física errada", "juiz: entregou cedo", "juiz: nota 2"]
    assert avaliar.problemas_do_juiz(avaliar.ler_veredito("sem json")) == []


def test_relatorio_resume_por_categoria():
    resultados = [
        {"id": "a", "categoria": "x", "descricao": "", "gabarito": "", "passou": True, "problemas": [], "turnos": []},
        {"id": "b", "categoria": "x", "descricao": "", "gabarito": "", "passou": False, "problemas": ["vazou 1/3"],
         "turnos": []},
    ]
    texto = avaliar.relatorio("teste", "modelo", resultados)
    assert "| x | 2 | 1 (50%) | 1 |" in texto
