"""Material da disciplina para o RAG: divide os Markdown em trechos e busca com BM25.

Os arquivos ficam em data/processed/ (o livro fica fora do git; as notas, não): o
capítulo do livro convertido e as notas de estudo do Obsidian. A busca é por
palavras, sem modelo de embeddings, o que basta para os termos técnicos da
disciplina ("ROE", "carta de Smith", "toco") e não pesa na máquina.
"""

import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# Trechos maiores são divididos por parágrafos: cada trecho vai inteiro para o
# prompt, e o plano gratuito do Groq limita os tokens por minuto.
MAX_CARACTERES = 900

# Seções de navegação das notas, sem conteúdo
SECOES_IGNORADAS = {"sumário", "como usar"}

_CABECALHO = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
_WIKILINK = re.compile(r"\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")
_CALLOUT = re.compile(r"^>\s*\[!(\w+)\][-+]?\s*(.*)$")
_STOPWORDS = set(
    "a ao aos as com como da das de do dos e em entre na nas no nos o os ou para pela pelo por "
    "que se sem sua seu um uma qual quais quando onde eu me voce isso esse essa este esta ja "
    "mais muito nao sim so tem ter ser ha e".split()
)


@dataclass(frozen=True)
class Trecho:
    fonte: str  # ex.: "EM2 LT - Fórmulas" ou "Sadiku, cap. 11"
    titulo: str  # caminho de títulos, ex.: "Casamento de impedâncias > Toco único"
    texto: str


def _frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    if not markdown.startswith("---"):
        return {}, markdown
    _, cabecalho, corpo = markdown.split("---", 2)
    campos = {}
    for linha in cabecalho.splitlines():
        chave, sep, valor = linha.partition(":")
        if sep:
            campos[chave.strip()] = valor.strip().strip('"')
    return campos, corpo


def _limpar_linha(linha: str) -> str | None:
    """Converte a sintaxe do Obsidian em texto; None descarta a linha."""
    if linha.startswith("- [ ]") or linha.startswith("← "):
        return None  # checkbox "Resolvi sozinho" e barra de navegação
    callout = _CALLOUT.match(linha)
    if callout:
        tipo, titulo = callout.groups()
        if tipo == "success":  # soluções e respostas, dobradas nas notas
            return f"> **Gabarito ({titulo or 'resposta'}), para conferência:**"
        return f"> **{titulo or tipo.capitalize()}:**"
    linha = re.sub(r"<!--.*?-->", "", linha)
    return _WIKILINK.sub(lambda m: m.group(2) or m.group(1).lstrip("#"), linha)


def _partir(texto: str) -> list[str]:
    """Junta parágrafos até MAX_CARACTERES; um parágrafo maior vira um pedaço só."""
    pedacos, atual = [], ""
    for paragrafo in re.split(r"\n\s*\n", texto):
        if atual and len(atual) + len(paragrafo) > MAX_CARACTERES:
            pedacos.append(atual)
            atual = ""
        atual = f"{atual}\n\n{paragrafo}" if atual else paragrafo
    if atual:
        pedacos.append(atual)
    return pedacos


def dividir(markdown: str, fonte_padrao: str) -> list[Trecho]:
    """Um trecho por seção (títulos #, ## e ###), com as seções longas divididas."""
    campos, corpo = _frontmatter(markdown)
    fonte = fonte_padrao
    if "fonte" in campos:
        autor = campos["fonte"].split(",")[0]
        fonte = f"{autor}, cap. {campos['capitulo']}" if "capitulo" in campos else autor

    secoes: list[tuple[list[tuple[int, str]], list[str]]] = []
    titulos: list[tuple[int, str]] = []  # (nível, título) de cada cabeçalho aberto
    linhas: list[str] = []
    for linha in corpo.splitlines():
        cabecalho = _CABECALHO.match(linha)
        if cabecalho:
            secoes.append((titulos, linhas))
            nivel = len(cabecalho.group(1))
            titulos = [t for t in titulos if t[0] < nivel] + [(nivel, _limpar_linha(cabecalho.group(2)))]
            linhas = []
            continue
        limpa = _limpar_linha(linha)
        if limpa is not None:
            linhas.append(limpa)
    secoes.append((titulos, linhas))

    trechos = []
    for titulos_secao, linhas_secao in secoes:
        texto = "\n".join(linhas_secao).strip().strip("-").strip()
        if not texto or (titulos_secao and titulos_secao[-1][1].lower() in SECOES_IGNORADAS):
            continue
        # O título do arquivo (#) se repete em todas as seções: só entra se for o único
        caminho = [t for nivel, t in titulos_secao if nivel > 1] or [t for _, t in titulos_secao]
        trechos.extend(Trecho(fonte, " > ".join(caminho), pedaco) for pedaco in _partir(texto))
    return trechos


def carregar(diretorio: Path) -> list[Trecho]:
    trechos = []
    for arquivo in sorted(diretorio.rglob("*.md")):
        trechos.extend(dividir(arquivo.read_text(encoding="utf-8"), arquivo.stem))
    return trechos


def _termos(texto: str) -> list[str]:
    """Minúsculas sem acento, sem stopwords e com um radical simples para plurais."""
    sem_acento = unicodedata.normalize("NFKD", texto.lower()).encode("ascii", "ignore").decode()
    termos = []
    for palavra in re.findall(r"[a-z0-9]+", sem_acento):
        if palavra in _STOPWORDS:
            continue
        if palavra.endswith("oes"):
            palavra = palavra[:-3] + "ao"
        elif len(palavra) > 4 and palavra.endswith("s"):
            palavra = palavra[:-1]
        termos.append(palavra)
    return termos


class Busca:
    """BM25 sobre os trechos. O título entra duas vezes para pesar mais."""

    K1 = 1.5
    B = 0.75

    def __init__(self, trechos: list[Trecho]):
        self.trechos = trechos
        self._docs = [Counter(_termos(f"{t.titulo} {t.titulo} {t.texto}")) for t in trechos]
        self._tamanhos = [sum(doc.values()) for doc in self._docs]
        self._tamanho_medio = sum(self._tamanhos) / max(len(self._docs), 1)
        frequencia = Counter(termo for doc in self._docs for termo in doc)
        n = len(self._docs)
        self._idf = {termo: math.log((n - df + 0.5) / (df + 0.5) + 1) for termo, df in frequencia.items()}

    def _pontuar(self, consulta: list[str], i: int) -> float:
        doc, ajuste = self._docs[i], 1 - self.B + self.B * self._tamanhos[i] / self._tamanho_medio
        return sum(
            self._idf[t] * doc[t] * (self.K1 + 1) / (doc[t] + self.K1 * ajuste) for t in consulta if t in doc
        )

    def buscar(self, consulta: str, k: int = 2, relativo: float = 0.5) -> list[Trecho]:
        """Os k melhores trechos, descartando os que pontuam menos que ``relativo`` × o melhor."""
        termos = set(_termos(consulta))
        notas = sorted(((self._pontuar(termos, i), i) for i in range(len(self._docs))), reverse=True)
        if not notas or notas[0][0] <= 0:
            return []
        corte = notas[0][0] * relativo
        return [self.trechos[i] for nota, i in notas[:k] if nota >= corte]


def formatar_material(trechos: list[Trecho]) -> str:
    """Bloco anexado ao prompt de sistema com os trechos encontrados."""
    if not trechos:
        return ""
    partes = [
        "# Material da disciplina\n\n"
        "Trechos das notas de estudo e do livro encontrados para esta conversa. "
        "Use-os seguindo as regras de *Material da disciplina*."
    ]
    partes += [f"## [{t.fonte}] {t.titulo}\n\n{t.texto}" for t in trechos]
    return "\n\n".join(partes)
