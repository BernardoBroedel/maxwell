# Guia técnico

Detalhes para quem vai mexer no código. A visão geral do projeto está no [README](../README.md).

## Arquitetura

```
Aluno ──► Open WebUI ──► backend (FastAPI + LangGraph) ──► LLM (Groq ou Qwen local via Ollama)
                              │
                              ├─ modos especialistas (um prompt por modo)
                              ├─ RAG: busca no livro e nas notas da disciplina
                              └─ ferramentas de cálculo (Γ, ROE, Z_in...)
```

- **Open WebUI**: interface de chat (login, histórico, LaTeX).
- **backend**: expõe cada modo como um modelo numa API compatível com OpenAI. A cada mensagem, busca trechos do material, monta o prompt do modo e deixa o LLM chamar as ferramentas de cálculo.
- **LLM**: qualquer API compatível com OpenAI. Padrão: Groq. Alternativa: Qwen local via Ollama. Veja [OPCOES_LLM.md](OPCOES_LLM.md).

## Modos

| Modelo | Id |
|---|---|
| Maxwell | `maxwell-tutor` (padrão) |
| Maxwell · Revisão | `maxwell-revisao` |
| Maxwell · Cartões Anki | `maxwell-anki` |
| Maxwell · Exercícios | `maxwell-exercicios` |
| Maxwell · Plano de estudo | `maxwell-estudo` |

Os modos dividem o material, as ferramentas e as regras comuns ([`prompts/base.md`](../src/maxwell/prompts/base.md)); cada um tem o próprio prompt.

Para criar um modo novo:

1. Acrescente uma entrada em [`src/maxwell/modos.py`](../src/maxwell/modos.py).
2. Escreva o prompt em `src/maxwell/prompts/`.
3. Reconstrua o backend: `docker compose up -d --build backend`.
4. Rode o script `configurar` para criar o cartão no Open WebUI.

## RAG

O material fica em `data/processed/`. Só as notas são versionadas; o livro (PDF em `data/raw/` e Markdown em `data/processed/cap11/`) fica fora do git, por direitos autorais. Todo `.md` dessa pasta e das subpastas é carregado quando o backend inicia:

- `data/processed/cap11/`: capítulo 11 do livro (Sadiku) convertido em Markdown (fora do git);
- `data/processed/notas_lt/`: notas de estudo do Obsidian (Fórmulas, Exercícios e Revisão).

Os arquivos são divididos por títulos e indexados com BM25 (busca por palavras-chave, em Python puro, sem modelo de embeddings). A cada mensagem, até 2 trechos vão para o prompt (o limite por minuto do Groq gratuito não comporta mais). As soluções das notas entram marcadas como gabarito, para o modelo conferir as respostas do aluno sem entregá-las. Sem a pasta, o tutor roda sem RAG.

### Como adicionar material

1. **Converta para Markdown (`.md`).** O RAG não lê PDF. Dá para converter com um assistente de IA, um conversor de PDF ou copiando o texto à mão.
2. **Organize com títulos** `#`, `##` e `###`. Cada seção vira um trecho de busca, então títulos claros ("Exemplo 11.3", "Carta de Smith") melhoram muito os resultados. Seções longas são divididas sozinhas.
3. **Salve em uma subpasta de `data/processed/`**, uma por fonte (ex.: `data/processed/notas_go/`).
4. **Reinicie o backend:** `docker compose restart backend`.
5. **Confira no log** se o material entrou: `docker compose logs backend | grep RAG` mostra quantos trechos foram carregados.

Dicas de formato:

- **Nome da fonte:** por padrão é o nome do arquivo. Para um livro, coloque no topo do arquivo:

  ```markdown
  ---
  fonte: "Sadiku, Elementos de Eletromagnetismo"
  capitulo: 11
  ---
  ```

- **Notas do Obsidian funcionam direto:** links `[[...]]`, callouts e checkboxes são limpos automaticamente. Seções "Sumário" e "Como usar" são ignoradas.
- **Gabaritos:** respostas dentro de um callout `> [!success]` entram marcadas como gabarito, e o Maxwell as usa para conferir o aluno sem entregá-las.
- **Fórmulas** em LaTeX (`$...$`) funcionam normalmente.

**Direitos autorais:** material próprio (notas, listas da equipe) pode ser versionado. Material de terceiros (livros, apostilas) deve ir para uma pasta incluída no `.gitignore`, como `data/processed/cap11/`.

## Restart ou rebuild?

| O que mudou | Comando |
|---|---|
| Código ou prompts (`src/`) | `docker compose up -d --build backend` |
| `.env` | `docker compose up -d backend` (recria o container; `restart` mantém os valores antigos) |
| Material em `data/processed/` | `docker compose restart backend` |
| Novo modo em `modos.py` | rebuild do backend e depois o script `configurar` |

## Configuração do Open WebUI

```bash
docker compose --profile setup run --rm configurar
```

O script ([`scripts/configurar_openwebui.py`](../scripts/configurar_openwebui.py)) aplica os cartões dos modos, o avatar, as descrições, as sugestões, o idioma pt-BR, o cadastro com aprovação e as permissões dos alunos. Usa as credenciais de admin do `.env` e pode rodar de novo sempre que algo mudar. Os arquivos da marca estão em [`branding/`](../branding/).

- **A primeira conta criada vira admin.** Com `WEBUI_ADMIN_EMAIL` e `WEBUI_ADMIN_PASSWORD` no `.env`, o admin é criado automaticamente.
- Logo após criar o admin, o Open WebUI **desliga sozinho os novos cadastros**, e isso fica salvo no banco (a variável `ENABLE_SIGNUP` deixa de valer). O script religa. À mão: *Painel Admin → Configurações → Autenticação*, ligue **Habilitar novos cadastros** com **Função padrão do usuário** = `pending`. Os cadastros ficam pendentes até o admin aprovar em *Painel Admin → Usuários*.
- O Open WebUI só lê `OPENAI_API_BASE_URL`/`OPENAI_API_KEY` na **primeira** inicialização. Essa é a conexão do Open WebUI com o backend, não com o LLM: trocar o LLM no `.env` não mexe nela. Para mudá-la, use *Painel Admin → Configurações → Conexões* ou `docker compose down -v` (apaga usuários e conversas).

## LLM

### Groq

- O plano gratuito tem cerca de **8 mil tokens por minuto**. Cada pergunta usa de 2 a 4 mil, então perguntas em sequência rápida ficam lentas: o backend espera o limite liberar e tenta de novo. Cada pessoa da equipe deve usar a própria chave.
- O catálogo do Groq muda com o tempo (o `qwen/qwen3-32b` já saiu, por exemplo). Para conferir os modelos da sua conta:

  ```bash
  curl -s https://api.groq.com/openai/v1/models -H "Authorization: Bearer SUA_CHAVE" | grep -o '"id":"[^"]*"'
  ```

### Ollama (local)

Instale o [Ollama](https://ollama.com/download) direto no sistema, baixe um modelo que caiba na VRAM (`ollama pull qwen3:4b` para 6 GB) e use no `.env`:

```env
LLM_BASE_URL=http://host.docker.internal:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=qwen3:4b
```

Em Linux, há também o perfil `local` do compose, que sobe o Ollama num container (`docker compose --profile local up -d`, com `LLM_BASE_URL=http://ollama:11434/v1`). Passo a passo completo em [TUTORIAL_LLM.md](TUTORIAL_LLM.md).

### Requisitos para modelo local

Valores aproximados, para modelos quantizados (Q4):

| Uso | Mínimo recomendado |
|---|---|
| Testes individuais | GPU NVIDIA com 6 GB de VRAM (modelos de ~4B) e 16 GB de RAM |
| Demonstração com boa qualidade | GPU com 8 a 12 GB de VRAM (modelos de 7B a 14B) |
| Turma usando ao mesmo tempo | GPU com 24 GB ou mais |
| Ajuste fino (LoRA/QLoRA) | GPU NVIDIA com 16 a 24 GB de VRAM e um conjunto de exemplos de conversas |

Só com processador, modelos pequenos rodam, mas o contexto do RAG leva dezenas de segundos para ser processado antes de cada resposta. Ajuste fino sem GPU é inviável na prática.

## Desenvolvimento

O projeto usa [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pytest
uv run uvicorn maxwell.api:create_app --factory --reload   # backend em http://localhost:8000
```

Sem Python instalado, rode os testes em container:

```bash
docker run --rm -v "$PWD:/app" -w /app -e UV_PROJECT_ENVIRONMENT=/tmp/venv \
  ghcr.io/astral-sh/uv:python3.12-bookworm-slim uv run pytest
```

## Estrutura

```
src/maxwell/
  api.py          # endpoints compatíveis com OpenAI (/v1/models, /v1/chat/completions), um grafo por modo
  modos.py        # lista dos modos especialistas (id, nome, prompt, descrição, sugestões)
  graph.py        # grafo LangGraph: material (RAG) → tutor ⇄ ferramentas
  material.py     # RAG: divide o Markdown em trechos e busca com BM25
  linhas.py       # física de linhas de transmissão (Γ, ROE, Z_in...), sem dependências
  tools.py        # ferramentas que o tutor chama (envolvem linhas.py, entrada em texto)
  llm.py          # cliente do LLM e carregamento dos prompts
  config.py       # configurações lidas do .env
  prompts/        # base.md (regras comuns) + um arquivo por modo
tests/
docs/
data/raw/         # PDFs da disciplina (fora do git, por direitos autorais)
data/processed/   # material do RAG em Markdown (cap11/, o livro, fica fora do git)
```
