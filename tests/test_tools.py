import cmath

import pytest

from maxwell.tools import (
    analisar_carga,
    calcular_comprimento_eletrico,
    calcular_impedancia_entrada,
    calcular_parametros_linha,
    calcular_potencias,
    formatar,
    parse_impedancia,
    projetar_transformador_quarto_onda,
)


@pytest.mark.parametrize(
    ("texto", "esperado"),
    [
        ("75+j25", 75 + 25j),
        ("75 - j25", 75 - 25j),
        ("75+25j", 75 + 25j),
        ("j50", 50j),
        ("-j50", -50j),
        ("100", 100),
        ("100 Ω", 100),
        ("0,5", 0.5),
        ("2.5e1+j1e1", 25 + 10j),
        ("curto", 0),
    ],
)
def test_parse_impedancia(texto, esperado):
    assert parse_impedancia(texto) == pytest.approx(esperado)


def test_parse_impedancia_polar_e_aberto():
    assert parse_impedancia("50∠-90°") == pytest.approx(-50j, abs=1e-9)
    assert cmath.isinf(parse_impedancia("aberto"))
    assert cmath.isinf(parse_impedancia("∞"))


def test_parse_impedancia_invalida():
    with pytest.raises(ValueError, match="Não entendi"):
        parse_impedancia("setenta e cinco")


def test_formatar():
    assert formatar(0.2 + 0.4j) == "0.2 + j0.4 (= 0.4472∠63.43°)"
    assert formatar(25 - 1e-15j) == "25 + j0 (= 25∠0.00°)"
    assert formatar(complex("inf")) == "∞ (circuito aberto)"


def test_analisar_carga():
    resultado = analisar_carga.invoke({"zl": "100", "z0": "50"})
    assert resultado["roe"] == 2
    assert resultado["modulo_gamma"] == pytest.approx(0.3333)
    assert resultado["potencia_refletida_percentual"] == pytest.approx(11.11)
    assert resultado["primeiro_maximo_tensao_lambda"] == 0
    assert resultado["primeiro_minimo_tensao_lambda"] == 0.25


def test_analisar_carga_casada_e_curto():
    assert analisar_carga.invoke({"zl": "50"})["onda_estacionaria"] == "não há (linha casada)"
    assert analisar_carga.invoke({"zl": "curto"})["roe"] == "∞"


def test_calcular_impedancia_entrada():
    resultado = calcular_impedancia_entrada.invoke({"zl": "100", "z0": "50", "comprimento_lambda": 0.25})
    assert resultado["zin"].startswith("25 + j0")
    assert resultado["beta_l_graus"] == 90
    assert resultado["tg_beta_l"] == "∞"


def test_calcular_impedancia_entrada_mostra_passos_intermediarios():
    resultado = calcular_impedancia_entrada.invoke({"zl": "100+j50", "z0": "50", "comprimento_lambda": 0.3})
    assert "0.4472∠26.57°" in resultado["gamma_carga"]
    assert resultado["beta_l_graus"] == 108
    assert resultado["tg_beta_l"] == -3.0777
    assert resultado["zin"].startswith("19.21 + j3.52")


def test_calcular_parametros_linha():
    resultado = calcular_parametros_linha.invoke(
        {"r": 0, "l": 250e-9, "g": 0, "c": 100e-12, "frequencia_hz": 1e9}
    )
    assert resultado["z0"].startswith("50 + j0")
    assert resultado["velocidade_fase_m_por_s"] == 2e8
    assert resultado["comprimento_onda_m"] == 0.2


def test_calcular_comprimento_eletrico():
    resultado = calcular_comprimento_eletrico.invoke(
        {"comprimento_m": 0.05, "frequencia_hz": 1e9, "velocidade_fase_m_por_s": 2e8}
    )
    assert resultado["comprimento_lambda"] == 0.25
    assert resultado["beta_l_graus"] == 90


def test_projetar_transformador_quarto_onda():
    assert projetar_transformador_quarto_onda.invoke({"z0": 50, "zl": 100})["z_transformador"] == 70.7107


def test_calcular_potencias():
    resultado = calcular_potencias.invoke({"v_incidente_pico": 10, "z0": 50, "zl": "100"})
    assert resultado["potencia_incidente_w"] == 1
    assert resultado["potencia_carga_w"] == pytest.approx(0.8889)
