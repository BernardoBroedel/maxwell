import importlib.util
from pathlib import Path

from maxwell.modos import MODOS

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("gerar_bateria", RAIZ / "scripts" / "gerar_bateria.py")
gerar_bateria = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gerar_bateria)


def test_bateria_tem_casos_validos():
    casos = gerar_bateria.gerar(escala=1, semente=1)
    modos = {m.id for m in MODOS}
    assert len(casos) > 300
    assert len({c["id"] for c in casos}) == len(casos)
    for caso in casos:
        assert caso["modo"] in modos and caso["turnos"] and caso["gabarito"] and caso["categoria"]


def test_proibido_nunca_esta_no_proprio_enunciado():
    for caso in gerar_bateria.gerar(escala=1, semente=2):
        enunciado = caso["turnos"][0]["aluno"].replace(",", ".").replace(" ", "")
        for valor in caso["turnos"][0].get("proibido", []):
            assert valor not in enunciado, (caso["id"], valor)


def test_escala_aumenta_a_bateria():
    assert len(gerar_bateria.gerar(escala=3)) > 900
