"""Ferramentas de cálculo que o tutor pode chamar (wrappers de ``maxwell.linhas``).

As entradas complexas chegam como texto ("75+j25") porque é assim que o modelo
e o aluno escrevem; as saídas voltam formatadas para o modelo ler.
"""

import cmath
import math
import re

from langchain_core.tools import tool

from maxwell import linhas

_ABERTO = {"inf", "infinito", "∞", "aberto", "circuito aberto", "oo"}
_CURTO = {"curto", "curto-circuito", "curto circuito"}


def parse_impedancia(texto: str) -> complex:
    """Aceita "75+j25", "75 - j25", "75+25j", "j50", "0,5", "50∠-30°", "curto", "aberto"."""
    t = texto.strip().lower()
    for unidade in ("ohms", "ohm", "ω"):
        t = t.replace(unidade, "")
    t = t.strip()
    if t in _ABERTO:
        return linhas.ABERTO
    if t in _CURTO:
        return 0j
    t = t.replace(" ", "").replace(",", ".")
    try:
        if "∠" in t:
            modulo, angulo = t.split("∠")
            return cmath.rect(float(modulo), math.radians(float(angulo.rstrip("°"))))
        # Notação de engenharia ("j25") para a do Python ("25j")
        return complex(re.sub(r"j(\d+\.?\d*(?:e[+-]?\d+)?|\.\d+)", r"\1j", t))
    except ValueError:
        raise ValueError(
            f"Não entendi a impedância {texto!r}. Use, por exemplo: 75+j25, 100, 50∠30°, curto ou aberto."
        ) from None


def _limpar(x: float, escala: float) -> float:
    return 0.0 if abs(x) < 1e-9 * max(1.0, escala) else x


def formatar(z: complex) -> str:
    if cmath.isinf(z):
        return "∞ (circuito aberto)"
    escala = abs(z)
    real, imag = _limpar(z.real, escala), _limpar(z.imag, escala)
    sinal = "-" if imag < 0 else "+"
    modulo, fase = cmath.polar(complex(real, imag))
    return f"{real:.4g} {sinal} j{abs(imag):.4g} (= {modulo:.4g}∠{math.degrees(fase):.2f}°)"


def _numero(x: float, digitos: int = 4) -> float | str:
    return "∞" if math.isinf(x) else round(x, digitos)


@tool(parse_docstring=True)
def analisar_carga(zl: str, z0: str = "50") -> dict:
    """Analisa o descasamento entre a carga e a linha: Γ, ROE, perda de retorno, potência refletida e posição dos máximos/mínimos de tensão.

    Args:
        zl: Impedância da carga, ex.: "75+j25", "100", "curto", "aberto".
        z0: Impedância característica da linha, ex.: "50".
    """
    gamma = linhas.coeficiente_reflexao(parse_impedancia(zl), parse_impedancia(z0))
    resultado = {
        "gamma_carga": formatar(gamma),
        "modulo_gamma": _numero(abs(gamma)),
        "roe": _numero(linhas.roe(gamma)),
        "perda_retorno_db": _numero(linhas.perda_retorno_db(gamma), 2),
        "potencia_refletida_percentual": round(100 * abs(gamma) ** 2, 2),
    }
    extremos = linhas.posicoes_extremos(gamma)
    if extremos is None:
        resultado["onda_estacionaria"] = "não há (linha casada)"
    else:
        resultado["primeiro_maximo_tensao_lambda"] = _numero(extremos[0])
        resultado["primeiro_minimo_tensao_lambda"] = _numero(extremos[1])
    return resultado


@tool(parse_docstring=True)
def calcular_impedancia_entrada(zl: str, z0: str, comprimento_lambda: float, atenuacao_np: float = 0.0) -> dict:
    """Calcula a impedância de entrada de uma linha terminada em ZL, a uma distância dada (em comprimentos de onda) da carga. Devolve também os passos intermediários (Γ na carga, βl, tg βl) para mostrar a resolução.

    Args:
        zl: Impedância da carga, ex.: "75+j25", "curto", "aberto".
        z0: Impedância característica da linha, ex.: "50".
        comprimento_lambda: Comprimento da linha em λ, ex.: 0.125 para λ/8.
        atenuacao_np: Atenuação total αl em nepers; 0 para linha sem perdas.
    """
    z0_c = parse_impedancia(z0)
    zl_c = parse_impedancia(zl)
    zin = linhas.impedancia_entrada(zl_c, z0_c, comprimento_lambda, atenuacao_np)
    gamma_entrada = linhas.coeficiente_reflexao(zin, z0_c)
    beta_l = 2 * math.pi * comprimento_lambda
    resultado = {
        "gamma_carga": formatar(linhas.coeficiente_reflexao(zl_c, z0_c)),
        "beta_l_graus": round(math.degrees(beta_l), 2),
        "gamma_entrada": formatar(gamma_entrada),
        "zin": formatar(zin),
    }
    if atenuacao_np == 0:
        # tg(βl) da fórmula da linha sem perdas; infinita em múltiplos ímpares de λ/4
        resultado["tg_beta_l"] = "∞" if abs(math.cos(beta_l)) < 1e-9 else _numero(math.tan(beta_l))
    return resultado


@tool(parse_docstring=True)
def calcular_parametros_linha(r: float, l: float, g: float, c: float, frequencia_hz: float) -> dict:
    """Calcula Z0, constante de atenuação α, constante de fase β, velocidade de fase e comprimento de onda a partir dos parâmetros distribuídos.

    Args:
        r: Resistência por unidade de comprimento, em Ω/m.
        l: Indutância por unidade de comprimento, em H/m.
        g: Condutância por unidade de comprimento, em S/m.
        c: Capacitância por unidade de comprimento, em F/m.
        frequencia_hz: Frequência de operação, em Hz.
    """
    p = linhas.parametros_linha(r, l, g, c, frequencia_hz)
    return {
        "z0": formatar(p.z0),
        "alfa_np_por_m": float(f"{p.alfa:.4g}"),
        "alfa_db_por_m": float(f"{p.alfa * 20 / math.log(10):.4g}"),
        "beta_rad_por_m": float(f"{p.beta:.4g}"),
        "velocidade_fase_m_por_s": float(f"{p.velocidade_fase:.4g}"),
        "comprimento_onda_m": float(f"{p.comprimento_onda:.4g}"),
    }


@tool(parse_docstring=True)
def calcular_comprimento_eletrico(
    comprimento_m: float,
    frequencia_hz: float,
    velocidade_fase_m_por_s: float | None = None,
    permissividade_relativa: float = 1.0,
) -> dict:
    """Converte um comprimento físico em comprimento elétrico (l/λ e βl).

    Args:
        comprimento_m: Comprimento físico da linha, em metros.
        frequencia_hz: Frequência de operação, em Hz.
        velocidade_fase_m_por_s: Velocidade de fase na linha; se omitida, usa c/√εr.
        permissividade_relativa: εr do dielétrico, usado se a velocidade de fase não for dada.
    """
    fracao = linhas.comprimento_eletrico(
        comprimento_m, frequencia_hz, velocidade_fase_m_por_s, permissividade_relativa
    )
    return {
        "comprimento_lambda": float(f"{fracao:.4g}"),
        "beta_l_graus": float(f"{360 * fracao:.4g}"),
        "beta_l_rad": float(f"{2 * math.pi * fracao:.4g}"),
    }


@tool(parse_docstring=True)
def projetar_transformador_quarto_onda(z0: float, zl: float) -> dict:
    """Calcula a impedância característica do transformador de λ/4 que casa uma carga real ZL com a linha Z0.

    Args:
        z0: Impedância característica da linha principal, em Ω (real).
        zl: Impedância da carga, em Ω (real).
    """
    return {"z_transformador": round(linhas.transformador_quarto_onda(z0, zl), 4)}


@tool(parse_docstring=True)
def calcular_potencias(v_incidente_pico: float, z0: float, zl: str) -> dict:
    """Calcula as potências médias incidente, refletida e entregue à carga numa linha sem perdas.

    Args:
        v_incidente_pico: Amplitude de pico da onda de tensão incidente na carga, em V.
        z0: Impedância característica da linha, em Ω (real).
        zl: Impedância da carga, ex.: "75+j25".
    """
    incidente, refletida, entregue = linhas.potencias(v_incidente_pico, z0, parse_impedancia(zl))
    return {
        "potencia_incidente_w": float(f"{incidente:.4g}"),
        "potencia_refletida_w": float(f"{refletida:.4g}"),
        "potencia_carga_w": float(f"{entregue:.4g}"),
    }


TOOLS = [
    analisar_carga,
    calcular_impedancia_entrada,
    calcular_parametros_linha,
    calcular_comprimento_eletrico,
    projetar_transformador_quarto_onda,
    calcular_potencias,
]
