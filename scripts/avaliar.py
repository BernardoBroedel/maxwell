"""Avalia o Maxwell com um banco de casos de teste, para comparar modelos e configurações.

Para cada caso, conversa com o modo indicado turno a turno e mede:
- vazamento: a resposta contém um valor proibido (ex.: o resultado antes da tentativa);
- ferramenta: o modelo chamou a ferramenta de cálculo esperada;
- confirmação: quando o aluno acerta, o tutor confirma (deve_conter_algum);
- tamanho e tempo de cada resposta;
- <think>: o raciocínio interno apareceu na resposta.

Com --juiz, o próprio modelo (com raciocínio médio, ajustável) lê cada conversa e julga física,
entrega antecipada da resposta e didática, usando o gabarito do caso.

Uso (na raiz do projeto):
    uv run python scripts/avaliar.py --rotulo teste
    uv run python scripts/avaliar.py --rotulo noite --arquivo avaliacao/bateria.json --paralelo 4 --juiz
    uv run python scripts/avaliar.py --rotulo groq --pausa 20 --base-url ... --modelo ... --chave ...

Os resultados vão para avaliacao/resultados/: um .jsonl salvo caso a caso (não se perde
se a execução cair), um .json completo e um .md com o resumo por categoria e as falhas.
"""

import argparse
import asyncio
import json
import re
import sys
import time
from collections import defaultdict
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

JUIZ_PROMPT = """Você avalia as respostas de um tutor de IA de Eletromagnetismo II (Linhas de Transmissão) para alunos de graduação.

Regras que o tutor deve seguir:
- Física e matemática corretas.
- Nos modos tutor e exercícios: antes de o aluno tentar, não entregar resultado numérico nem contas intermediárias com os números do aluno; dar fórmulas, dicas e pedir a tentativa. Depois de uma tentativa real do aluno, pode corrigir e mostrar o valor certo.
- Quando o aluno acerta, confirmar com clareza; quando erra, dizer que não está certo e ajudar a achar o erro.
- Respostas curtas, em português, que façam o aluno pensar.
- Perguntas conceituais (sem um exercício com os números do aluno) podem ser respondidas direto, inclusive com valores simples dos casos-limite; isso não é "entregar cedo".

Modo do tutor: {modo}
O que o caso testa: {descricao}
Gabarito (calculado por ferramenta, confiável): {gabarito}

Conversa:
{conversa}

Responda APENAS com um objeto JSON, sem nenhum texto antes ou depois:
{{"fisica_correta": true ou false, "entregou_cedo": true ou false, "seguiu_o_modo": true ou false, "nota": número de 1 a 5, "comentario": "uma frase curta com o principal problema, ou ok"}}"""


def normalizar(texto: str) -> str:
    """Minúsculas, sem espaços, vírgula decimal vira ponto e o menos unicode vira hífen.

    Também tira a marcação do LaTeX que esconde números: "0{,}277" e "40\\,\\Omega".
    """
    t = re.sub(r"\s+", "", texto.lower())
    t = re.sub(r"\\[,;:!]", "", t).replace("{", "").replace("}", "")
    return t.replace(",", ".").replace("−", "-")


def contem(resposta: str, trecho: str) -> bool:
    return normalizar(trecho) in normalizar(resposta)


def cartoes_anki_quebrados(resposta: str) -> int:
    """Linhas de cartão, dentro do bloco de código, que não têm exatamente um ';' (quebram a importação)."""
    bloco = re.search(r"```[^\n]*\n(.*?)```", resposta, re.DOTALL)
    if not bloco:
        return 0
    linhas = [l for l in bloco.group(1).splitlines() if l.strip() and not l.startswith("#")]
    return sum(l.count(";") != 1 for l in linhas)


def ler_veredito(texto: str) -> dict:
    achado = re.search(r"\{.*\}", texto, re.DOTALL)
    try:
        return json.loads(achado.group(0)) if achado else {"erro": texto[:200]}
    except json.JSONDecodeError:
        return {"erro": texto[:200]}


def problemas_do_juiz(veredito: dict) -> list[str]:
    if "erro" in veredito:
        return []  # juiz não respondeu em JSON: não conta como falha do tutor
    problemas = []
    if veredito.get("fisica_correta") is False:
        problemas.append("juiz: física errada")
    if veredito.get("entregou_cedo") is True:
        problemas.append("juiz: entregou cedo")
    if veredito.get("seguiu_o_modo") is False:
        problemas.append("juiz: não seguiu o modo")
    nota = veredito.get("nota")
    if isinstance(nota, (int, float)) and nota <= 2:
        problemas.append(f"juiz: nota {nota}")
    return problemas


async def julgar(juiz, caso: dict, turnos: list[dict]) -> dict:
    conversa = "\n\n".join(f"ALUNO: {t['aluno']}\nTUTOR: {t['resposta']}" for t in turnos)
    prompt = JUIZ_PROMPT.format(
        modo=caso["modo"], descricao=caso.get("descricao", ""), gabarito=caso.get("gabarito", "não informado"),
        conversa=conversa,
    )
    try:
        resposta = await juiz.ainvoke([HumanMessage(prompt)])
        return ler_veredito(str(resposta.content))
    except Exception as e:  # noqa: BLE001
        return {"erro": f"{type(e).__name__}: {e}"[:200]}


async def rodar_caso(caso: dict, grafos: dict, pausa: float = 0, juiz=None) -> dict:
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
            problemas.append("não confirmou (faltou um de: " + ", ".join(algum) + ")")
        if longo:
            problemas.append(f"longo ({palavras} > {turno['max_palavras']} palavras)")
        if "<think>" in resposta:
            problemas.append("<think> na resposta")
        if caso["modo"] == "maxwell-anki" and (quebrados := cartoes_anki_quebrados(resposta)):
            problemas.append(f"anki: {quebrados} cartão(ões) com ';' a mais ou a menos")
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
    problemas = [p for t in turnos for p in t["problemas"]]
    if esperada and esperada not in ferramentas_usadas:
        problemas.append(f"não chamou {esperada}")
    resultado = {
        "id": caso["id"],
        "categoria": caso.get("categoria", caso["modo"]),
        "modo": caso["modo"],
        "descricao": caso.get("descricao", ""),
        "gabarito": caso.get("gabarito", ""),
        "turnos": turnos,
    }
    if juiz is not None:
        resultado["juiz"] = await julgar(juiz, caso, turnos)
        problemas += problemas_do_juiz(resultado["juiz"])
    resultado["problemas"] = problemas
    resultado["passou"] = not problemas
    return resultado


def resumo_por_categoria(resultados: list[dict]) -> list[str]:
    grupos = defaultdict(list)
    for r in resultados:
        grupos[r["categoria"]].append(r)
    linhas = [
        "| Categoria | Casos | Aprovados | Vazamentos | Física errada (juiz) | Entregou cedo (juiz) | Nota média (juiz) |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for categoria, rs in sorted(grupos.items()):
        aprovados = sum(r["passou"] for r in rs)
        vazamentos = sum(any(p.startswith("vazou") for p in r["problemas"]) for r in rs)
        fisica = sum("juiz: física errada" in r["problemas"] for r in rs)
        cedo = sum("juiz: entregou cedo" in r["problemas"] for r in rs)
        notas = [r["juiz"]["nota"] for r in rs if isinstance(r.get("juiz", {}).get("nota"), (int, float))]
        nota = f"{sum(notas) / len(notas):.1f}" if notas else "-"
        linhas.append(
            f"| {categoria} | {len(rs)} | {aprovados} ({100 * aprovados / len(rs):.0f}%) | {vazamentos} | {fisica} | {cedo} | {nota} |"
        )
    return linhas


def conversa_md(r: dict) -> list[str]:
    linhas = [f"### {r['id']}", "", f"_{r['descricao']}_", ""]
    if r.get("gabarito"):
        linhas += [f"Gabarito: {r['gabarito']}", ""]
    if r["problemas"]:
        linhas += [f"**Problemas:** {'; '.join(r['problemas'])}", ""]
    if "juiz" in r:
        linhas += [f"**Juiz:** `{json.dumps(r['juiz'], ensure_ascii=False)}`", ""]
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
    return linhas


def relatorio(rotulo: str, modelo: str, resultados: list[dict], todas: bool | None = None) -> str:
    aprovados = sum(r["passou"] for r in resultados)
    tempos = [t["segundos"] for r in resultados for t in r["turnos"]]
    palavras = [t["palavras"] for r in resultados for t in r["turnos"]]
    vazamentos = sum(any(p.startswith("vazou") for p in r["problemas"]) for r in resultados)
    julgados = [r for r in resultados if "juiz" in r and "erro" not in r["juiz"]]
    linhas = [
        f"# Avaliação: {rotulo}",
        "",
        f"Modelo: `{modelo}` · {datetime.now():%d/%m/%Y %H:%M}",
        "",
        f"- **Casos aprovados:** {aprovados} de {len(resultados)} ({100 * aprovados / max(len(resultados), 1):.0f}%)",
        f"- **Casos com vazamento de resposta:** {vazamentos}",
        f"- **Tempo médio por resposta:** {sum(tempos) / max(len(tempos), 1):.1f} s (máximo {max(tempos, default=0):.1f} s)",
        f"- **Tamanho médio da resposta:** {sum(palavras) / max(len(palavras), 1):.0f} palavras",
    ]
    if julgados:
        notas = [r["juiz"].get("nota") for r in julgados if isinstance(r["juiz"].get("nota"), (int, float))]
        linhas += [
            f"- **Julgados pelo juiz:** {len(julgados)} · física errada: "
            f"{sum(r['juiz'].get('fisica_correta') is False for r in julgados)} · entregou cedo: "
            f"{sum(r['juiz'].get('entregou_cedo') is True for r in julgados)} · nota média: "
            f"{sum(notas) / max(len(notas), 1):.2f}",
        ]
    linhas += ["", "## Por categoria", "", *resumo_por_categoria(resultados), ""]
    todas = len(resultados) <= 30 if todas is None else todas
    mostrar = resultados if todas else [r for r in resultados if not r["passou"]]
    linhas += ["## " + ("Respostas" if todas else f"Casos com problema ({len(mostrar)})"), ""]
    for r in mostrar:
        linhas += conversa_md(r)
    return "\n".join(linhas)


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rotulo", required=True, help="nome desta rodada, ex.: noite-low")
    parser.add_argument("--arquivo", default=str(PERGUNTAS), help="banco de casos (padrão: avaliacao/perguntas.json)")
    parser.add_argument("--base-url", help="sobrescreve LLM_BASE_URL do .env")
    parser.add_argument("--modelo", help="sobrescreve LLM_MODEL do .env")
    parser.add_argument("--chave", help="sobrescreve LLM_API_KEY do .env")
    parser.add_argument("--so", nargs="*", help="roda só os casos com estes ids")
    parser.add_argument("--limite", type=int, help="roda só os primeiros N casos (para testar a bateria)")
    parser.add_argument("--paralelo", type=int, default=1, help="casos ao mesmo tempo (use até OLLAMA_NUM_PARALLEL)")
    parser.add_argument("--juiz", action="store_true", help="o próprio modelo julga cada conversa")
    parser.add_argument("--juiz-raciocinio", default="medium", help="raciocínio do juiz: low, medium ou high")
    parser.add_argument("--pausa", type=float, default=0, help="segundos entre turnos (use ~20 no Groq gratuito)")
    parser.add_argument("--sem", nargs="*", default=[], help="subpastas de data/processed fora do RAG nesta rodada (ex.: notas_lt)")
    parser.add_argument("--todas", action="store_true", help="põe todas as conversas no .md, não só as falhas")
    args = parser.parse_args()

    extras = {"llm_base_url": args.base_url, "llm_model": args.modelo, "llm_api_key": args.chave}
    settings = Settings(**{k: v for k, v in extras.items() if v})
    llm = build_llm(settings)
    juiz = None
    if args.juiz:
        juiz = build_llm(settings.model_copy(update={"llm_reasoning_effort": args.juiz_raciocinio, "llm_temperature": 0.0}))
    material = RAIZ / settings.material_dir
    trechos = carregar(material, ignorar=args.sem) if material.is_dir() else []
    busca = Busca(trechos) if trechos else None
    grafos = {m.id: build_tutor_graph(llm, load_prompt(m.prompt), busca=busca) for m in MODOS}

    arquivo = Path(args.arquivo)
    casos = json.loads((arquivo if arquivo.is_absolute() else RAIZ / arquivo).read_text(encoding="utf-8"))
    if args.so:
        casos = [c for c in casos if c["id"] in args.so]
    if args.limite:
        casos = casos[: args.limite]
    print(
        f"Modelo {settings.llm_model} (raciocínio: {settings.llm_reasoning_effort or 'padrão'}) · {len(casos)} casos · "
        f"paralelo {args.paralelo} · juiz {'sim' if juiz else 'não'} · RAG: {len(trechos)} trechos"
        + (f" (sem {', '.join(args.sem)})" if args.sem else ""),
        flush=True,
    )

    SAIDA.mkdir(parents=True, exist_ok=True)
    nome = f"{args.rotulo}_{datetime.now():%Y%m%d-%H%M}"
    parcial = SAIDA / f"{nome}.jsonl"
    semaforo = asyncio.Semaphore(max(1, args.paralelo))
    resultados: list[dict] = []
    inicio = time.perf_counter()

    async def um(caso: dict) -> None:
        async with semaforo:
            r = await rodar_caso(caso, grafos, args.pausa, juiz)
        resultados.append(r)
        with parcial.open("a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        feitos, aprovados = len(resultados), sum(x["passou"] for x in resultados)
        minutos = (time.perf_counter() - inicio) / 60
        print(
            f"[{feitos}/{len(casos)} · {aprovados} ok · {minutos:.0f} min] "
            f"{'ok    ' if r['passou'] else 'FALHOU'} {r['id']}  {'; '.join(r['problemas'])}",
            flush=True,
        )

    await asyncio.gather(*(um(c) for c in casos))

    ordem = {c["id"]: i for i, c in enumerate(casos)}
    resultados.sort(key=lambda r: ordem[r["id"]])
    (SAIDA / f"{nome}.json").write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    (SAIDA / f"{nome}.md").write_text(
        relatorio(args.rotulo, settings.llm_model, resultados, True if args.todas else None), encoding="utf-8"
    )
    aprovados = sum(r["passou"] for r in resultados)
    print(f"\n{aprovados} de {len(resultados)} casos aprovados. Relatório: avaliacao/resultados/{nome}.md")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
