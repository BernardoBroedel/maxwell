"""Transcreve páginas de um livro escaneado para Markdown com LaTeX, usando o modelo de visão do Ollama.

O texto embutido nos PDFs escaneados destrói as equações. Aqui cada página vira imagem e
o modelo (qwen3.8, que lê imagens) escreve o Markdown. Cada página fica salva à parte, então
dá para interromper e continuar: páginas já transcritas são puladas.

Uso, no supermicro (na pasta do projeto):
    sudo docker compose run --rm -v ./data:/app/dados -v ./scripts:/app/scripts backend \\
        uv run --no-sync --with pymupdf python scripts/transcrever_livro.py \\
        --pdf dados/raw/LIVRO.pdf --capitulo 11 --titulo "Linhas de Transmissão" --paginas 426-486

    Teste rápido antes: --paginas 445-446 --so-paginas  (não monta o capítulo)

Saída: dados/raw/transcricao/pNNNN.md (uma por página) e dados/processed/sadiku/capNN.md
(o capítulo montado, com o cabeçalho que o RAG usa para citar a fonte).
"""

import argparse
import asyncio
import base64
import os
from pathlib import Path

import httpx

PROMPT = """Transcreva esta página de um livro de Eletromagnetismo para Markdown, fielmente e em português.

- Copie o texto exatamente como está. Não resuma, não explique, não corrija e não acrescente nada.
- Títulos de seção viram cabeçalhos: "## 11.3 TÍTULO DA SEÇÃO"; subseções com "###".
- TODA expressão matemática em LaTeX: $...$ no meio do texto e $$...$$ para equações em destaque.
  Se a equação tem número, coloque-o com \\tag: $$\\Gamma = \\frac{Z_L - Z_0}{Z_L + Z_0} \\tag{11.37}$$
- Vetores unitários como \\mathbf{a}_x; letras gregas com o comando certo (\\Gamma, \\gamma, \\beta, \\lambda...).
- Tabelas viram tabelas Markdown.
- Figuras: não descreva o desenho. Escreva só a legenda: [Figura 11.11: Círculos r típicos...].
- Exemplos, exercícios práticos e problemas: mantenha o enunciado e a solução, com o título em negrito
  (ex.: **EXEMPLO 11.3**, **Solução:**, **EXERCÍCIO PRÁTICO 11.3**, **Resposta:**).
- Ignore o cabeçalho com o nome do capítulo e o número da página.
- Se um trecho estiver ilegível, escreva [ilegível].

Responda apenas com o Markdown da página."""


def intervalo(texto: str) -> list[int]:
    paginas = []
    for parte in texto.split(","):
        inicio, _, fim = parte.partition("-")
        paginas += list(range(int(inicio), int(fim or inicio) + 1))
    return paginas


def imagem_da_pagina(pdf, numero: int, dpi: int) -> str:
    pagina = pdf[numero - 1]  # o PyMuPDF conta a partir de 0
    png = pagina.get_pixmap(dpi=dpi).tobytes("png")
    return base64.b64encode(png).decode()


async def transcrever(cliente: httpx.AsyncClient, url: str, modelo: str, imagem_b64: str) -> str:
    corpo = {
        "model": modelo,
        "temperature": 0,
        "reasoning_effort": "none",
        "max_tokens": 6000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{imagem_b64}"}},
                ],
            }
        ],
    }
    resposta = await cliente.post(f"{url}/chat/completions", json=corpo, timeout=900)
    resposta.raise_for_status()
    texto = resposta.json()["choices"][0]["message"]["content"].strip()
    # Às vezes o modelo embrulha tudo num bloco ```markdown
    if texto.startswith("```"):
        texto = texto.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return texto


async def main() -> None:
    import fitz  # PyMuPDF, instalado na hora pelo "uv run --with pymupdf"

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--paginas", required=True, help='ex.: "426-486" ou "445,447-450"')
    parser.add_argument("--capitulo", type=int, help="número do capítulo, para montar dados/processed/sadiku/capNN.md")
    parser.add_argument("--titulo", default="", help="título do capítulo")
    parser.add_argument("--fonte", default="Sadiku, Elementos de Eletromagnetismo (3ª ed.)")
    parser.add_argument("--saida", default="dados/processed/sadiku")
    parser.add_argument("--cache", default="dados/raw/transcricao")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--paralelo", type=int, default=2)
    parser.add_argument("--so-paginas", action="store_true", help="só transcreve, sem montar o capítulo")
    parser.add_argument("--refazer", action="store_true", help="transcreve de novo páginas já feitas")
    args = parser.parse_args()

    url = os.environ.get("LLM_BASE_URL", "http://host.docker.internal:11434/v1").rstrip("/")
    modelo = os.environ.get("LLM_MODEL", "qwen3.8")
    pdf = fitz.open(args.pdf)
    paginas = intervalo(args.paginas)
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    semaforo = asyncio.Semaphore(args.paralelo)
    feitas = 0

    async def uma(cliente: httpx.AsyncClient, numero: int) -> None:
        nonlocal feitas
        destino = cache / f"p{numero:04d}.md"
        if destino.exists() and not args.refazer:
            feitas += 1
            return
        async with semaforo:
            try:
                texto = await transcrever(cliente, url, modelo, imagem_da_pagina(pdf, numero, args.dpi))
                destino.write_text(texto + "\n", encoding="utf-8")
                situacao = "ok"
            except Exception as erro:  # noqa: BLE001 - segue com as outras páginas
                situacao = f"ERRO {type(erro).__name__}: {erro}"[:200]
        feitas += 1
        print(f"[{feitas}/{len(paginas)}] página {numero}: {situacao}", flush=True)

    async with httpx.AsyncClient() as cliente:
        await asyncio.gather(*(uma(cliente, n) for n in paginas))

    faltando = [n for n in paginas if not (cache / f"p{n:04d}.md").exists()]
    if faltando:
        print(f"\nFaltaram {len(faltando)} páginas: {faltando}. Rode de novo para tentar só essas.")
    if args.so_paginas or args.capitulo is None:
        return
    partes = [
        "---",
        f'fonte: "{args.fonte}"',
        f"capitulo: {args.capitulo}",
        "---",
        "",
        f"# Capítulo {args.capitulo}: {args.titulo}".rstrip(": "),
        "",
    ]
    for n in paginas:
        arquivo = cache / f"p{n:04d}.md"
        if arquivo.exists():
            partes += [f"<!-- p. {n} -->", arquivo.read_text(encoding="utf-8").strip(), ""]
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    destino = saida / f"cap{args.capitulo:02d}.md"
    destino.write_text("\n".join(partes), encoding="utf-8")
    print(f"\nCapítulo montado em {destino} ({len(paginas) - len(faltando)} páginas).")


if __name__ == "__main__":
    asyncio.run(main())
