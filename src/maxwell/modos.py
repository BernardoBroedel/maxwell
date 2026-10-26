"""Modos especialistas do Maxwell. Cada modo vira um modelo no Open WebUI.

Sem dependências além da biblioteca padrão: o script de configuração do
Open WebUI também lê este módulo para criar os cartões dos modelos.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Modo:
    id: str
    nome: str
    prompt: str  # arquivo em maxwell/prompts/, somado ao base.md
    descricao: str
    # Sugestões da tela inicial: (linha 1 do título, linha 2 do título, mensagem enviada)
    sugestoes: tuple[tuple[str, str, str], ...] = ()


MODOS = (
    Modo(
        id="maxwell-tutor",
        nome="Maxwell",
        prompt="tutor.md",
        descricao="Tutor de Linhas de Transmissão: tira dúvidas com dicas em níveis, sem entregar a resposta pronta.",
        sugestoes=(
            (
                "Como calculo",
                "o coeficiente de reflexão?",
                "Como calculo o coeficiente de reflexão de uma carga numa linha de transmissão?",
            ),
            (
                "Confere minha resolução",
                "de impedância de entrada",
                "Quero conferir minha resolução de um exercício de impedância de entrada. Posso te mostrar o que fiz?",
            ),
            (
                "O que a ROE",
                "diz sobre a linha?",
                "O que a ROE (razão de onda estacionária) diz sobre uma linha de transmissão?",
            ),
            (
                "Me explica",
                "o transformador de λ/4",
                "Me explica como funciona o casamento de impedância com um transformador de λ/4.",
            ),
        ),
    ),
    Modo(
        id="maxwell-revisao",
        nome="Maxwell · Revisão",
        prompt="revisao.md",
        descricao="Revisão para a prova: perguntas rápidas, uma por vez, com correção e as armadilhas mais comuns.",
        sugestoes=(
            ("Me testa", "em carta de Smith", "Quero revisar carta de Smith. Me faz perguntas, uma de cada vez."),
            ("Revisão geral", "de Linhas de Transmissão", "Faz uma revisão geral de Linhas de Transmissão comigo."),
            ("Quais são", "as armadilhas comuns?", "Quais são as armadilhas mais comuns em Linhas de Transmissão?"),
        ),
    ),
    Modo(
        id="maxwell-anki",
        nome="Maxwell · Cartões Anki",
        prompt="anki.md",
        descricao="Gera cartões do Anki sobre um tema, prontos para importar.",
        sugestoes=(
            ("Cartões sobre", "coeficiente de reflexão e ROE", "Gera cartões do Anki sobre coeficiente de reflexão e ROE."),
            ("Cartões sobre", "impedância de entrada", "Gera cartões do Anki sobre impedância de entrada."),
            ("Cartões das", "fórmulas principais", "Gera cartões do Anki com as fórmulas principais de Linhas de Transmissão."),
        ),
    ),
    Modo(
        id="maxwell-exercicios",
        nome="Maxwell · Exercícios",
        prompt="exercicios.md",
        descricao="Resolve exercícios com você: organiza o problema, corrige sua tentativa e mostra a resolução comentada.",
        sugestoes=(
            ("Tenho um exercício", "de impedância de entrada", "Tenho um exercício de impedância de entrada para resolver. Posso mandar o enunciado?"),
            ("Corrige", "minha resolução", "Resolvi um exercício e quero que você corrija. Vou mandar o enunciado e o que fiz."),
            ("Me passa", "um exercício para treinar", "Me passa um exercício de Linhas de Transmissão para eu treinar."),
        ),
    ),
    Modo(
        id="maxwell-estudo",
        nome="Maxwell · Plano de estudo",
        prompt="estudo.md",
        descricao="Monta um plano de estudo a partir do seu tempo disponível e do que você já domina.",
        sugestoes=(
            ("Tenho prova", "em uma semana", "Tenho prova de Linhas de Transmissão em uma semana. Me ajuda a montar um plano?"),
            ("Por onde", "eu começo?", "Estou começando Linhas de Transmissão agora. Por onde eu começo?"),
            ("Tenho só", "2 horas para estudar", "Tenho só 2 horas para estudar Linhas de Transmissão. O que priorizo?"),
        ),
    ),
)

PADRAO = MODOS[0].id
