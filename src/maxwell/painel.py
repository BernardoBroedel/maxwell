"""Painel do professor: relatórios da turma e de cada aluno a partir das conversas no Open WebUI.

É um "modo" a mais, visível só para administradores. O professor escreve, por exemplo,
"Relatório da turma dos últimos 7 dias" ou "Relatório do aluno João no último mês", e o
backend lê as conversas pela API do Open WebUI, calcula as estatísticas (com código, não
com a IA) e pede à IA só o resumo das dificuldades, a partir das perguntas dos alunos.
"""

import re
import time
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

import httpx
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from maxwell.modos import MODOS

# Palavras que indicam o tema de uma pergunta. A busca ignora acentos e maiúsculas.
TEMAS = {
    "Coeficiente de reflexão": ["coeficiente de reflexao", "reflexao", "Γ"],
    "ROE / TOE": ["roe", "toe", "onda estacionaria", "vswr"],
    "Impedância de entrada": ["impedancia de entrada", "zin", "z_in", "z_{in}", "zent", "z_{ent}"],
    "Carta de Smith": ["smith"],
    "Casamento e tocos": ["casamento", "toco", "tocos", "stub", "quarto de onda", "λ/4", "transformador"],
    "Potência na linha": ["potencia"],
    "Parâmetros e Z0": ["telegrafista", "impedancia caracteristica", "parametros distribuidos",
                        "constante de propagacao", "z0", "z_0"],
    "Transitórios": ["transitorio", "transitorios", "degrau", "pulso", "diagrama de reflexoes"],
    "Guias de onda": ["guia de onda", "guias de onda", "modo te", "modo tm", "frequencia de corte"],
    "Matrizes e dispositivos de RF": ["matriz s", "parametros s", "espalhamento", "acoplador", "divisor",
                                      "circulador"],
}

# Frases de quem pede a resposta pronta, sem tentar
PEDIDOS_DE_RESPOSTA = [
    "so a resposta", "me da a resposta", "me passa a resposta", "resolve pra mim", "resolve para mim",
    "so o numero", "me passa o valor", "me fala o numero", "so quero o resultado", "so quero a resposta",
    "me da o resultado", "qual a resposta",
]

PERIODOS = [
    (r"(\d+)\s*dias?", lambda m: int(m.group(1))),
    (r"(\d+)\s*semanas?", lambda m: 7 * int(m.group(1))),
    (r"(\d+)\s*m[eê]s(es)?", lambda m: 30 * int(m.group(1))),
    (r"\bhoje\b", lambda m: 1),
    (r"\bsemana\b", lambda m: 7),
    (r"\bm[eê]s\b", lambda m: 30),
    (r"\b(tudo|todo o per[ií]odo|desde o in[ií]cio|semestre)\b", lambda m: 3650),
]

NOMES_DOS_MODOS = {m.id: m.nome for m in MODOS}

INSTRUCOES_RESUMO = """Você ajuda um professor de Eletromagnetismo II a entender as dificuldades dos alunos.
Abaixo estão perguntas reais que alunos fizeram a um tutor de IA, e respostas que eles marcaram como ruins.
Escreva em português, de forma objetiva, para o professor ler em um minuto:

### Principais dificuldades
3 a 5 itens: o tema e, em uma frase, o que exatamente confunde os alunos. Cite um exemplo curto de pergunta quando ajudar.

### Conceitos que aparecem errados nas perguntas
Erros ou confusões que as próprias perguntas revelam (ex.: trocar ROE por |Γ|). Se não houver, diga isso.

### Sugestões para a próxima aula
2 ou 3 sugestões concretas.

Não invente: use só o que está nas perguntas. Não cite nomes de alunos."""

INSTRUCOES_ALUNO = """Você ajuda um professor de Eletromagnetismo II a acompanhar um aluno.
Abaixo estão as perguntas que o aluno fez a um tutor de IA, em ordem cronológica.
Escreva em português, em no máximo 8 linhas:
- os temas em que o aluno mais pediu ajuda;
- o que as perguntas mostram sobre o que ele já entende e onde trava;
- se ele tenta resolver antes de pedir ajuda ou pede a resposta pronta;
- uma sugestão para o professor.
Não invente: use só o que está nas perguntas."""


def sem_acento(texto: str) -> str:
    return unicodedata.normalize("NFKD", texto.lower()).encode("ascii", "ignore").decode()


def periodo_em_dias(pedido: str, padrao: int = 7) -> int:
    texto = pedido.lower()
    for padrao_re, dias in PERIODOS:
        achado = re.search(padrao_re, texto)
        if achado:
            return dias(achado)
    return padrao


def segundos(ts) -> float:
    """Timestamps do Open WebUI podem vir em segundos, milissegundos ou nanossegundos."""
    ts = float(ts or 0)
    while ts > 1e11:
        ts /= 1000
    return ts


def texto_da_mensagem(mensagem: dict) -> str:
    conteudo = mensagem.get("content", "")
    if isinstance(conteudo, list):
        return "\n".join(p.get("text", "") for p in conteudo if p.get("type") == "text")
    return str(conteudo or "")


def temas_de(texto: str) -> list[str]:
    """Temas citados no texto. Palavras com símbolos (Γ, λ) são procuradas no texto original."""
    normal = sem_acento(texto)
    achados = []
    for tema, palavras in TEMAS.items():
        for p in palavras:
            if p.isascii():
                if re.search(rf"(?<![a-z0-9]){re.escape(p)}(?![a-z0-9])", normal):
                    break
            elif p in texto:
                break
        else:
            continue
        achados.append(tema)
    return achados


@dataclass
class Aluno:
    id: str
    nome: str
    email: str
    perguntas: list[tuple[float, str]] = field(default_factory=list)
    conversas: set = field(default_factory=set)
    modos: Counter = field(default_factory=Counter)
    temas: Counter = field(default_factory=Counter)
    pedidos_de_resposta: int = 0
    curtidas: int = 0
    descurtidas: int = 0
    ultima_atividade: float = 0


def analisar(usuarios: list[dict], chats: list[dict], dias: int, agora: float | None = None) -> dict:
    """Estatísticas das conversas dos alunos (role "user") nos últimos ``dias``."""
    agora = agora or time.time()
    desde = agora - dias * 86400
    alunos = {
        u["id"]: Aluno(u["id"], u.get("name") or u.get("email", "?"), u.get("email", ""))
        for u in usuarios
        if u.get("role") == "user"
    }
    ruins: list[dict] = []
    for chat in chats:
        aluno = alunos.get(chat.get("user_id"))
        if aluno is None:
            continue
        mensagens = (chat.get("chat") or {}).get("history", {}).get("messages", {}) or {}
        for msg in sorted(mensagens.values(), key=lambda m: segundos(m.get("timestamp"))):
            ts = segundos(msg.get("timestamp"))
            if ts < desde:
                continue
            texto = texto_da_mensagem(msg)
            if msg.get("role") == "user":
                if texto.startswith("### Task:"):
                    continue
                aluno.perguntas.append((ts, texto))
                aluno.conversas.add(chat.get("id"))
                aluno.temas.update(temas_de(texto))
                if any(p in sem_acento(texto) for p in PEDIDOS_DE_RESPOSTA):
                    aluno.pedidos_de_resposta += 1
                aluno.ultima_atividade = max(aluno.ultima_atividade, ts)
            elif msg.get("role") == "assistant":
                aluno.modos[NOMES_DOS_MODOS.get(msg.get("model"), msg.get("model") or "?")] += 1
                nota = (msg.get("annotation") or {}).get("rating")
                if nota == 1:
                    aluno.curtidas += 1
                elif nota == -1:
                    aluno.descurtidas += 1
                    pai = mensagens.get(msg.get("parentId"), {})
                    ruins.append({"pergunta": texto_da_mensagem(pai), "resposta": texto})
    ativos = [a for a in alunos.values() if a.perguntas]
    temas = Counter()
    modos = Counter()
    for a in ativos:
        temas.update(a.temas)
        modos.update(a.modos)
    return {
        "dias": dias,
        "alunos": alunos,
        "ativos": sorted(ativos, key=lambda a: len(a.perguntas), reverse=True),
        "inativos": sorted((a for a in alunos.values() if not a.perguntas), key=lambda a: a.nome.lower()),
        "temas": temas,
        "modos": modos,
        "ruins": ruins,
    }


BRASILIA = timezone(timedelta(hours=-3))


def data(ts: float) -> str:
    return datetime.fromtimestamp(ts, BRASILIA).strftime("%d/%m %H:%M") if ts else "-"


def relatorio_da_turma(analise: dict) -> str:
    ativos, dias = analise["ativos"], analise["dias"]
    perguntas = sum(len(a.perguntas) for a in ativos)
    curt = sum(a.curtidas for a in ativos)
    desc = sum(a.descurtidas for a in ativos)
    periodo = "todo o período" if dias >= 3650 else f"últimos {dias} dias"
    linhas = [
        f"## Relatório da turma ({periodo})",
        "",
        f"- **Alunos ativos:** {len(ativos)} de {len(analise['alunos'])} cadastrados",
        f"- **Perguntas feitas:** {perguntas}",
        f"- **Avaliações das respostas:** {curt} 👍 · {desc} 👎",
        "",
    ]
    if analise["temas"]:
        linhas += ["### Temas mais perguntados", "", "| Tema | Perguntas |", "| --- | --- |"]
        linhas += [f"| {t} | {n} |" for t, n in analise["temas"].most_common()]
        linhas.append("")
    if analise["modos"]:
        linhas += ["### Uso dos modos", "", "| Modo | Respostas |", "| --- | --- |"]
        linhas += [f"| {m} | {n} |" for m, n in analise["modos"].most_common()]
        linhas.append("")
    if ativos:
        linhas += [
            "### Por aluno",
            "",
            "| Aluno | Perguntas | Conversas | Temas principais | Pediu a resposta pronta | 👍 / 👎 | Última atividade |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for a in ativos:
            temas = ", ".join(t for t, _ in a.temas.most_common(3)) or "-"
            linhas.append(
                f"| {a.nome} | {len(a.perguntas)} | {len(a.conversas)} | {temas} | {a.pedidos_de_resposta} | "
                f"{a.curtidas} / {a.descurtidas} | {data(a.ultima_atividade)} |"
            )
        linhas.append("")
    if analise["inativos"]:
        linhas += [f"**Sem atividade no período:** {', '.join(a.nome for a in analise['inativos'])}", ""]
    return "\n".join(linhas)


def relatorio_do_aluno(aluno: Aluno, dias: int) -> str:
    periodo = "todo o período" if dias >= 3650 else f"últimos {dias} dias"
    linhas = [
        f"## Relatório de {aluno.nome} ({periodo})",
        "",
        f"- **E-mail:** {aluno.email}",
        f"- **Perguntas:** {len(aluno.perguntas)} em {len(aluno.conversas)} conversas",
        f"- **Pediu a resposta pronta:** {aluno.pedidos_de_resposta} vezes",
        f"- **Avaliações:** {aluno.curtidas} 👍 · {aluno.descurtidas} 👎",
        f"- **Última atividade:** {data(aluno.ultima_atividade)}",
        f"- **Temas:** {', '.join(f'{t} ({n})' for t, n in aluno.temas.most_common()) or '-'}",
        f"- **Modos usados:** {', '.join(f'{m} ({n})' for m, n in aluno.modos.most_common()) or '-'}",
        "",
    ]
    if aluno.perguntas:
        linhas += ["### Últimas perguntas", ""]
        for ts, texto in aluno.perguntas[-15:]:
            linhas.append(f"- *{data(ts)}* — {texto[:200].replace(chr(10), ' ')}")
        linhas.append("")
    return "\n".join(linhas)


def achar_aluno(pedido: str, alunos: dict[str, Aluno]) -> Aluno | None:
    """O aluno cujo nome completo, primeiro nome ou e-mail aparece no pedido."""
    pedido_n = sem_acento(pedido)
    candidatos = []
    for a in alunos.values():
        nome = sem_acento(a.nome)
        email = a.email.lower()
        if nome and nome in pedido_n:
            candidatos.append((3, a))
        elif email and email in pedido.lower():
            candidatos.append((3, a))
        elif nome.split() and re.search(rf"\b{re.escape(nome.split()[0])}\b", pedido_n):
            candidatos.append((1, a))
    if not candidatos:
        return None
    candidatos.sort(key=lambda c: c[0], reverse=True)
    melhores = [a for nota, a in candidatos if nota == candidatos[0][0]]
    return melhores[0] if len(melhores) == 1 else None


def material_para_resumo(analise: dict, limite: int = 150) -> str:
    perguntas = sorted((p for a in analise["ativos"] for p in a.perguntas), key=lambda p: p[0])[-limite:]
    partes = ["## Perguntas dos alunos", *[f"- {texto[:300].replace(chr(10), ' ')}" for _, texto in perguntas]]
    if analise["ruins"]:
        partes += ["", "## Respostas que os alunos marcaram com 👎"]
        for r in analise["ruins"][-20:]:
            partes.append(f"- Pergunta: {r['pergunta'][:200]} | Resposta: {r['resposta'][:300]}".replace("\n", " "))
    return "\n".join(partes)


class FonteOpenWebUI:
    """Lê usuários e conversas pela API do Open WebUI, com a conta de administrador."""

    def __init__(self, url: str, email: str, senha: str):
        self.url, self.email, self.senha = url.rstrip("/"), email, senha

    async def dados(self) -> tuple[list[dict], list[dict]]:
        async with httpx.AsyncClient(base_url=self.url, timeout=120) as cliente:
            login = await cliente.post("/api/v1/auths/signin", json={"email": self.email, "password": self.senha})
            login.raise_for_status()
            cabecalho = {"Authorization": f"Bearer {login.json()['token']}"}
            usuarios = await cliente.get("/api/v1/users/all", headers=cabecalho)
            usuarios.raise_for_status()
            chats = await cliente.get("/api/v1/chats/all/db", headers=cabecalho)
            chats.raise_for_status()
            return usuarios.json()["users"], chats.json()


class PainelProfessor:
    def __init__(self, fonte, llm: BaseChatModel | None):
        self.fonte, self.llm = fonte, llm

    async def _resumo(self, instrucoes: str, material: str) -> str:
        if self.llm is None or not material.strip():
            return ""
        try:
            resposta = await self.llm.ainvoke([SystemMessage(instrucoes), HumanMessage(material)])
            return str(resposta.content).strip()
        except Exception as erro:  # noqa: BLE001 - o relatório sai mesmo sem o resumo
            return f"_Não consegui gerar o resumo com a IA agora ({type(erro).__name__})._"

    async def responder(self, pedido: str) -> str:
        try:
            usuarios, chats = await self.fonte.dados()
        except Exception as erro:  # noqa: BLE001
            return (
                "⚠️ Não consegui ler as conversas no Open WebUI "
                f"({type(erro).__name__}). Confira WEBUI_ADMIN_EMAIL e WEBUI_ADMIN_PASSWORD no .env."
            )
        dias = periodo_em_dias(pedido, padrao=7)
        analise = analisar(usuarios, chats, dias)
        aluno = None if "turma" in pedido.lower() else achar_aluno(pedido, analise["alunos"])

        if aluno is not None:
            texto = relatorio_do_aluno(aluno, dias)
            if aluno.perguntas:
                perguntas = "\n".join(f"- {t[:300]}" for _, t in aluno.perguntas[-80:])
                resumo = await self._resumo(INSTRUCOES_ALUNO, perguntas)
                if resumo:
                    texto += "\n### Análise\n\n" + resumo + "\n"
            return texto + RODAPE

        texto = relatorio_da_turma(analise)
        if analise["ativos"]:
            resumo = await self._resumo(INSTRUCOES_RESUMO, material_para_resumo(analise))
            if resumo:
                texto += "\n## Análise das dificuldades\n\n" + resumo + "\n"
        else:
            texto += "\nNenhuma pergunta de aluno no período.\n"
        return texto + RODAPE


RODAPE = (
    "\n---\n*Estatísticas calculadas a partir das conversas; a análise é gerada pela IA e pode errar. "
    "Peça outro período (\"últimos 30 dias\", \"semestre\") ou um aluno (\"relatório do aluno Fulano\").*"
)
