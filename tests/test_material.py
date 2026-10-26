import asyncio

from fakes import FakeChatModel
from langchain_core.messages import AIMessage, HumanMessage

from maxwell.graph import build_tutor_graph
from maxwell.material import Busca, Trecho, carregar, dividir, formatar_material

NOTA = """---
tags: [eletromagnetismo2]
---
# EM2 LT - Exercícios
← [[Eletromagnetismo 2]] · [[EM2 LT - Fórmulas|Fórmulas]]

## Sumário
1. [[#Exemplos resolvidos do capítulo]]

## Exemplos resolvidos do capítulo

### Exemplo 11.1
- [ ] Resolvi sozinho

Linha no ar, $Z_0=70\\ \\Omega$. Volte nas [[EM2 LT - Revisão#Armadilhas|armadilhas]].

> [!success]- Solução
> $C=68{,}2$ pF/m
"""

LIVRO = """---
fonte: "Sadiku, M. N. O. Elementos de Eletromagnetismo"
capitulo: 11
---
## 11.4 Impedância de Entrada
<!-- p. 440 -->
Texto sobre impedância de entrada.

### A. Linha em curto
Texto sobre o curto.
"""


def test_dividir_nota_do_obsidian():
    trechos = dividir(NOTA, "EM2 LT - Exercícios")

    assert [t.titulo for t in trechos] == ["Exemplos resolvidos do capítulo > Exemplo 11.1"]
    texto = trechos[0].texto
    assert "Resolvi sozinho" not in texto
    assert "Volte nas armadilhas." in texto
    assert "**Gabarito (Solução), para conferência:**" in texto


def test_dividir_livro_usa_a_fonte_do_frontmatter():
    trechos = dividir(LIVRO, "02_impedancia")

    assert {t.fonte for t in trechos} == {"Sadiku, cap. 11"}
    assert [t.titulo for t in trechos] == ["11.4 Impedância de Entrada", "11.4 Impedância de Entrada > A. Linha em curto"]
    assert "<!--" not in trechos[0].texto


def test_secao_longa_vira_varios_trechos():
    paragrafos = "\n\n".join("Parágrafo " + "x" * 500 for _ in range(5))
    trechos = dividir(f"## Resumo\n{paragrafos}", "nota")
    assert len(trechos) > 1
    assert all(t.titulo == "Resumo" for t in trechos)


def test_busca_ignora_acentos_e_plurais():
    busca = Busca(
        [
            Trecho("nota", "Carta de Smith", "Círculos de resistência constante na carta."),
            Trecho("nota", "Transformador de λ/4", "Casamento de impedâncias com um quarto de onda."),
            Trecho("nota", "Transitórios", "Degrau aplicado na linha e diagrama de reflexões."),
        ]
    )
    assert busca.buscar("como faço casamento de impedancia?")[0].titulo == "Transformador de λ/4"
    assert busca.buscar("reflexão no transitorio")[0].titulo == "Transitórios"
    assert busca.buscar("receita de bolo") == []


def test_carregar_le_markdown_das_subpastas(tmp_path):
    (tmp_path / "notas").mkdir()
    (tmp_path / "notas" / "EM2 LT - Exercícios.md").write_text(NOTA, encoding="utf-8")
    trechos = carregar(tmp_path)
    assert trechos[0].fonte == "EM2 LT - Exercícios"


def test_grafo_anexa_material_ao_prompt():
    busca = Busca([Trecho("EM2 LT - Fórmulas", "Carta de Smith", "O centro da carta é a linha casada.")])
    llm = FakeChatModel(messages=iter([AIMessage("O que o centro da carta representa?")]))
    graph = build_tutor_graph(llm, "prompt de teste", busca=busca)

    result = asyncio.run(graph.ainvoke({"messages": [HumanMessage("Me explica a carta de Smith")]}))

    assert result["material"] == formatar_material(busca.trechos)
    assert "## [EM2 LT - Fórmulas] Carta de Smith" in result["material"]
