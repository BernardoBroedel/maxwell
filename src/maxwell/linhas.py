"""Cálculos de linhas de transmissão.

Convenções: impedâncias complexas em ohms; comprimentos em comprimentos de onda
(l/λ) salvo indicação; amplitudes de tensão de pico. Circuito aberto é
representado por impedância infinita (``complex(math.inf)``).
"""

import cmath
import math
from dataclasses import dataclass

C0 = 299_792_458.0  # velocidade da luz no vácuo, m/s
ABERTO = complex(math.inf)


def coeficiente_reflexao(zl: complex, z0: complex) -> complex:
    if cmath.isinf(zl):
        return 1 + 0j
    return (zl - z0) / (zl + z0)


def roe(gamma: complex) -> float:
    modulo = abs(gamma)
    if modulo >= 1 - 1e-12:
        return math.inf
    return (1 + modulo) / (1 - modulo)


def perda_retorno_db(gamma: complex) -> float:
    modulo = abs(gamma)
    return math.inf if modulo == 0 else -20 * math.log10(modulo)


def posicoes_extremos(gamma: complex) -> tuple[float, float] | None:
    """Distâncias (em λ, a partir da carga) do primeiro máximo e do primeiro mínimo de tensão.

    Retorna None para linha casada (Γ = 0), que não tem onda estacionária.
    """
    if abs(gamma) < 1e-12:
        return None
    fase = cmath.phase(gamma) % (2 * math.pi)
    d_max = fase / (4 * math.pi)
    if 0.5 - d_max < 1e-12:
        d_max = 0.0
    d_min = (d_max + 0.25) % 0.5
    return d_max, d_min


def impedancia_entrada(zl: complex, z0: complex, comprimento: float, atenuacao_np: float = 0.0) -> complex:
    """Impedância vista a ``comprimento`` (em λ) da carga.

    ``atenuacao_np`` é a atenuação total αl, em nepers (0 para linha sem perdas).
    """
    gamma_entrada = (
        coeficiente_reflexao(zl, z0)
        * cmath.exp(-2 * atenuacao_np)
        * cmath.exp(-4j * math.pi * comprimento)
    )
    if cmath.isclose(gamma_entrada, 1, abs_tol=1e-9):
        return ABERTO
    return z0 * (1 + gamma_entrada) / (1 - gamma_entrada)


@dataclass(frozen=True)
class ParametrosLinha:
    z0: complex
    alfa: float  # Np/m
    beta: float  # rad/m
    velocidade_fase: float  # m/s
    comprimento_onda: float  # m


def parametros_linha(r: float, l: float, g: float, c: float, frequencia: float) -> ParametrosLinha:
    """Parâmetros a partir de R (Ω/m), L (H/m), G (S/m), C (F/m) e frequência (Hz)."""
    w = 2 * math.pi * frequencia
    z = r + 1j * w * l
    y = g + 1j * w * c
    gamma = cmath.sqrt(z * y)
    return ParametrosLinha(
        z0=cmath.sqrt(z / y),
        alfa=gamma.real,
        beta=gamma.imag,
        velocidade_fase=w / gamma.imag,
        comprimento_onda=2 * math.pi / gamma.imag,
    )


def comprimento_eletrico(
    comprimento_m: float,
    frequencia: float,
    velocidade_fase: float | None = None,
    permissividade_relativa: float = 1.0,
) -> float:
    """Comprimento físico convertido em λ (l/λ)."""
    vp = velocidade_fase or C0 / math.sqrt(permissividade_relativa)
    return comprimento_m * frequencia / vp


def transformador_quarto_onda(z0: float, zl: float) -> float:
    """Impedância característica do transformador λ/4 que casa ZL (real) com Z0."""
    if z0 <= 0 or zl <= 0:
        raise ValueError("O transformador λ/4 simples exige Z0 e ZL reais e positivos.")
    return math.sqrt(z0 * zl)


def potencias(v_incidente: complex, z0: float, zl: complex) -> tuple[float, float, float]:
    """(incidente, refletida, entregue à carga) em W, para linha sem perdas com Z0 real."""
    incidente = abs(v_incidente) ** 2 / (2 * z0)
    fracao_refletida = abs(coeficiente_reflexao(zl, z0)) ** 2
    return incidente, incidente * fracao_refletida, incidente * (1 - fracao_refletida)
