"""Avalia o Maxwell com um banco de perguntas fixo, para comparar modelos (Groq x Ollama).

Para cada caso de avaliacao/perguntas.json, conversa com o modo indicado turno a
turno e mede:
- vazamento: a resposta contém um valor proibido (ex.: o resultado final antes da tentativa);
- ferramenta: o modelo chamou a ferramenta de cálculo esperada;
- tamanho: número de palavras (a regra é ser breve);
- tempo: segundos por resposta;
- <think>: o modelo deixou o raciocínio interno aparecer na resposta (comum no Qwen local).

Uso (na raiz do projeto):
    uv run python scripts/avaliar.py --rotulo groq
    uv run python scripts/avaliar.py --rotulo qwen3-8b --base-url http://localhost:11434/v1 --modelo qwen3:8b --chave ollama
    uv run python scripts/avaliar.py --rotulo teste --so tutor-gamma-insistente

Sem --base-url/--modelo/--chave, usa o que está no .env. Os resultados vão para
avaliacao/resultados/ (um .md para ler e um .json com as respostas completas).
"""

import argparse
import asyncio
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage

from maxwell.config import Settings
from maxwell.graph import build_tutor_graph
from maxwell.llm import build_llm, load_prompt
from maxwell.material import Busca, carregar
from maxwell.modos import MODOS

RAIZ = Path(__file__).resolve().parent.parent
PERGUNTAS = RAIZ / "avaliacao" / "perguntas.json"
SAIDA = RAIZ / "avaliacao" / "resultados"


def normalizar(texto: str) -> str:
    """Minúsculas, sem espaços, vírgula decimal vira ponto e o menos unicode vira hífen."""
    return re.sub(r"\s+", "", texto.lower()).replace(",", ".").replace("−", "-")


def contem(resposta: str, trecho: str) -> bool:
    return normalizar(trecho) in normalizar(resposta)


async def rodar_caso(caso: dict, grafos: dict, pausa: float) -> dict:
    grafo = grafos[caso["modo"]]
    historico = []
    turnos = []
    ferramentas_usadas: list[str] = []
    for turno in caso["turnos"]:
        historico.append(HumanMessage(turno["aluno"]))
        inicio = time.perf_counter()
        try:
            estado = await grafo.ainvoke({"messages": list(historico)})
            erro = None
        except Exception as e:  # noqa: BLE001 - o erro vira resultado da avaliação
            estado, erro = None, f"{type(e).__name__}: {e}"
        segundos = time.perf_counter() - inicio

        if estado is None:
            resposta, chamadas = "", []
        else:
            novas = estado["messages"][len(historico):]
            chamadas = [c["name"] for m in novas if isinstance(m, AIMessage) for c in (m.tool_calls or [])]
            resposta = str(estado["messages"][-1].content)
        ferramentas_usadas += chamadas
        historico.append(AIMessage(resposta))

        vazou = [p for p in turno.get("proibido", []) if contem(resposta, p)]
        faltou_todos = [p for p in turno.get("deve_conter_todos", []) if not contem(resposta, p)]
        algum = turno.get("deve_conter_algum", [])
        faltou_algum = bool(algum) and not any(contem(resposta, p) for p in algum)
        palavras = len(resposta.split())
        longo = "max_palavras" in turno and palavras > turno["max_palavras"]
        problemas = []
        if erro:
            problemas.append(f"erro: {erro}")
        if vazou:
            problemas.append("vazou " + ", ".join(vazou))
        if faltou_todos:
            problemas.append("faltou " + ", ".join(faltou_todos))
        if faltou_algum:
            problemas.append("faltou um de " + ", ".join(algum))
        if longo:
            problemas.append(f"longo ({palavras} > {turno['max_palavras']} palavras)")
        if "<think>" in resposta:
            problemas.append("<think> na resposta")
        turnos.append(
            {
                "aluno": turno["aluno"],
                "resposta": resposta,
                "ferramentas": chamadas,
                "segundos": round(segundos, 1),
                "palavras": palavras,
                "problemas": problemas,
            }
        )
        if pausa:
            await asyncio.sleep(pausa)

    esperada = caso.get("ferramenta_esperada")
    sem_ferramenta = bool(esperada) and esperada not in ferramentas_usadas
    problemas = [p for t in turnos for p in t["problemas"]]
    if sem_ferramenta:
        problemas.append(f"não chamou {esperada}")
    return {
        "id": caso["id"],
        "modo": caso["modo"],
        "descricao": caso.get("descricao", ""),
        "passou": not problemas,
        "problemas": problemas,
        "turnos": turnos,
    }


def relatorio(rotulo: str, modelo: str, resultados: list[dict]) -> str:
    aprovados = sum(r["passou"] for r in resultados)
    tempos = [t["segundos"] for r in resultados for t in r["turnos"]]
    palavras = [t["palavras"] for r in resultados for t in r["turnos"]]
    vazamentos = sum(any(p.startswith("vazou") for p in r["problemas"]) for r in resultados)
    linhas = [
        f"# Avaliação: {rotulo}",
        "",
        f"Modelo: `{modelo}` · {datetime.now():%d/%m/%Y %H:%M}",
        "",
        f"- **Casos aprovados:** {aprovados} de {len(resultados)}",
        f"- **Casos com vazamento de resposta:** {vazamentos}",
        f"- **Tempo médio por resposta:** {sum(tempos) / max(len(tempos), 1):.1f} s (máximo {max(tempos, default=0):.1f} s)",
        f"- **Tamanho médio da resposta:** {sum(palavras) / max(len(palavras), 1):.0f} palavras",
        "",
        "| Caso | Resultado | Problemas |",
        "| --- | --- | --- |",
    ]
    for r in resultados:
        linhas.append(f"| {r['id']} | {'ok' if r['passou'] else 'FALHOU'} | {'; '.join(r['problemas']) or '-'} |")
    linhas += ["", "## Respostas", ""]
    for r in resultados:
        linhas += [f"### {r['id']}", "", f"_{r['descricao']}_", ""]
        for t in r["turnos"]:
            ferramentas = ", ".join(t["ferramentas"]) or "nenhuma"
            linhas += [
                f"**Aluno:** {t['aluno']}",
                "",
                f"**Maxwell** ({t['segundos']} s, {t['palavras']} palavras, ferramentas: {ferramentas}):",
                "",
                t["resposta"],
                "",
            ]
    return "\n".join(linhas)


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rotulo", required=True, help="nome desta rodada, ex.: groq, qwen3-8b")
    parser.add_argument("--base-url", help="sobrescreve LLM_BASE_URL do .env")
    parser.add_argument("--modelo", help="sobrescreve LLM_MODEL do .env")
    parser.add_argument("--chave", help="sobrescreve LLM_API_KEY do .env")
    parser.add_argument("--so", nargs="*", help="roda só os casos com estes ids")
    parser.add_argument("--pausa", type=float, default=0, help="segundos entre turnos (use ~20 no Groq gratuito)")
    args = parser.parse_args()

    extras = {"llm_base_url": args.base_url, "llm_model": args.modelo, "llm_api_key": args.chave}
    settings = Settings(**{k: v for k, v in extras.items() if v})
    llm = build_llm(settings)
    material = RAIZ / settings.material_dir
    trechos = carregar(material) if material.is_dir() else []
    busca = Busca(trechos) if trechos else None
    grafos = {m.id: build_tutor_graph(llm, load_prompt(m.prompt), busca=busca) for m in MODOS}

    casos = json.loads(PERGUNTAS.read_text(encoding="utf-8"))
    if args.so:
        casos = [c for c in casos if c["id"] in args.so]
    print(f"Modelo {settings.llm_model} em {settings.llm_base_url} · {len(casos)} casos · RAG: {len(trechos)} trechos")

    resultados = []
    for caso in casos:
        r = await rodar_caso(caso, grafos, args.pausa)
        print(f"  {'ok    ' if r['passou'] else 'FALHOU'} {r['id']}  {'; '.join(r['problemas'])}")
        resultados.append(r)

    SAIDA.mkdir(parents=True, exist_ok=True)
    nome = f"{args.rotulo}_{datetime.now():%Y%m%d-%H%M}"
    (SAIDA / f"{nome}.json").write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    (SAIDA / f"{nome}.md").write_text(relatorio(args.rotulo, settings.llm_model, resultados), encoding="utf-8")
    aprovados = sum(r["passou"] for r in resultados)
    print(f"\n{aprovados} de {len(resultados)} casos aprovados. Relatório: avaliacao/resultados/{nome}.md")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
