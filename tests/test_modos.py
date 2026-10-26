import pytest

from maxwell.llm import load_prompt
from maxwell.modos import MODOS, PADRAO


def test_ids_unicos_e_padrao_e_o_tutor():
    ids = [modo.id for modo in MODOS]
    assert len(ids) == len(set(ids))
    assert PADRAO == "maxwell-tutor"


@pytest.mark.parametrize("modo", MODOS, ids=lambda modo: modo.id)
def test_prompt_do_modo_inclui_as_regras_comuns(modo):
    prompt = load_prompt(modo.prompt)
    assert prompt.startswith("Você é o **Maxwell**")
    assert "# Modo:" in prompt
