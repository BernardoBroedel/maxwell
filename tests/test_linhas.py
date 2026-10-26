import cmath
import math

import pytest

from maxwell import linhas


def approx_c(z: complex, abs_tol: float = 1e-6):
    return pytest.approx(z, abs=abs_tol)


class TestCoeficienteReflexao:
    def test_carga_resistiva(self):
        assert linhas.coeficiente_reflexao(100, 50) == approx_c(1 / 3)
        assert linhas.coeficiente_reflexao(25, 50) == approx_c(-1 / 3)

    def test_carga_complexa(self):
        # Γ = j50 / (100 + j50) = 0,2 + j0,4
        assert linhas.coeficiente_reflexao(50 + 50j, 50) == approx_c(0.2 + 0.4j)

    def test_casos_limite(self):
        assert linhas.coeficiente_reflexao(50, 50) == approx_c(0)
        assert linhas.coeficiente_reflexao(0, 50) == approx_c(-1)
        assert linhas.coeficiente_reflexao(linhas.ABERTO, 50) == approx_c(1)


class TestROE:
    def test_valores(self):
        assert linhas.roe(1 / 3) == pytest.approx(2)
        assert linhas.roe(0) == pytest.approx(1)
        assert linhas.roe(0.2 + 0.4j) == pytest.approx((1 + math.sqrt(0.2)) / (1 - math.sqrt(0.2)))

    def test_reflexao_total(self):
        assert linhas.roe(-1) == math.inf
        assert linhas.roe(1j) == math.inf

    def test_perda_retorno(self):
        assert linhas.perda_retorno_db(0.1) == pytest.approx(20)
        assert linhas.perda_retorno_db(0) == math.inf


class TestPosicoesExtremos:
    def test_carga_maior_que_z0_tem_maximo_na_carga(self):
        assert linhas.posicoes_extremos(1 / 3) == pytest.approx((0, 0.25))

    def test_carga_menor_que_z0_tem_minimo_na_carga(self):
        assert linhas.posicoes_extremos(-1 / 3) == pytest.approx((0.25, 0))

    def test_fase_negativa(self):
        # Γ com fase -90° (270°): máximo em 3λ/8, mínimo em λ/8
        assert linhas.posicoes_extremos(-0.5j) == pytest.approx((0.375, 0.125))

    def test_linha_casada(self):
        assert linhas.posicoes_extremos(0) is None


class TestImpedanciaEntrada:
    def test_linha_casada_independe_do_comprimento(self):
        assert linhas.impedancia_entrada(50, 50, 0.137) == approx_c(50)

    def test_quarto_de_onda_inverte(self):
        assert linhas.impedancia_entrada(100, 50, 0.25) == approx_c(25)

    def test_meia_onda_repete(self):
        assert linhas.impedancia_entrada(30 - 40j, 50, 0.5) == approx_c(30 - 40j)

    def test_toco_em_curto_e_em_aberto(self):
        assert linhas.impedancia_entrada(0, 50, 0.125) == approx_c(50j)  # jZ0 tg(βl)
        assert linhas.impedancia_entrada(linhas.ABERTO, 50, 0.125) == approx_c(-50j)  # -jZ0 cotg(βl)

    def test_curto_vira_aberto_em_quarto_de_onda(self):
        assert cmath.isinf(linhas.impedancia_entrada(0, 50, 0.25))
        assert linhas.impedancia_entrada(linhas.ABERTO, 50, 0.25) == approx_c(0)

    def test_formula_classica(self):
        zl, z0, bl = 75 + 25j, 50, 2 * math.pi * 0.1
        esperado = z0 * (zl + 1j * z0 * math.tan(bl)) / (z0 + 1j * zl * math.tan(bl))
        assert linhas.impedancia_entrada(zl, z0, 0.1) == approx_c(esperado)

    def test_linha_com_perdas_longa_tende_a_z0(self):
        assert linhas.impedancia_entrada(0, 50, 0.3, atenuacao_np=20) == approx_c(50)


class TestParametrosLinha:
    def test_linha_sem_perdas(self):
        p = linhas.parametros_linha(r=0, l=250e-9, g=0, c=100e-12, frequencia=1e9)
        assert p.z0 == approx_c(50)
        assert p.alfa == pytest.approx(0, abs=1e-12)
        assert p.velocidade_fase == pytest.approx(2e8)
        assert p.comprimento_onda == pytest.approx(0.2)

    def test_linha_com_perdas(self):
        r, l, g, c, f = 0.5, 250e-9, 1e-5, 100e-12, 1e8
        w = 2 * math.pi * f
        p = linhas.parametros_linha(r, l, g, c, f)
        gamma = cmath.sqrt((r + 1j * w * l) * (g + 1j * w * c))
        assert p.alfa == pytest.approx(gamma.real)
        assert p.alfa > 0
        assert p.beta == pytest.approx(gamma.imag)
        assert p.z0 == approx_c(cmath.sqrt((r + 1j * w * l) / (g + 1j * w * c)))


def test_comprimento_eletrico():
    assert linhas.comprimento_eletrico(0.05, 1e9, velocidade_fase=2e8) == pytest.approx(0.25)
    assert linhas.comprimento_eletrico(0.075, 1e9, permissividade_relativa=4) == pytest.approx(
        0.075 * 1e9 * 2 / linhas.C0
    )


def test_transformador_quarto_onda():
    assert linhas.transformador_quarto_onda(50, 100) == pytest.approx(70.7107, abs=1e-4)
    with pytest.raises(ValueError):
        linhas.transformador_quarto_onda(50, 0)


def test_potencias():
    incidente, refletida, entregue = linhas.potencias(10, 50, 100)
    assert incidente == pytest.approx(1)
    assert refletida == pytest.approx(1 / 9)
    assert entregue == pytest.approx(8 / 9)
    assert linhas.potencias(10, 50, 0)[2] == pytest.approx(0)
