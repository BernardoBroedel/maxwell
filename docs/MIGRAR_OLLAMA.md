# Migrar para a IA local (Ollama) e testar o ensino

Roteiro da primeira fase do cronograma (até 10/11): trocar a API do Groq por um modelo rodando no próprio PC e medir, com o mesmo banco de perguntas, se o tutor continua ensinando bem.

## 1. Ver quanto de memória de vídeo o PC tem

No PowerShell:

```powershell
nvidia-smi
```

Olhe a coluna de memória (ex.: `8192MiB`). Ela define o modelo:

| Memória de vídeo | Modelo para começar | Observação |
|---|---|---|
| 6 GB | `qwen3:4b` | Funciona, mas erra mais na chamada de ferramentas |
| 8 GB | `qwen3:8b` | Bom ponto de partida |
| 12 a 16 GB | `qwen3:14b` | Melhor qualidade que cabe numa placa comum |
| 24 GB ou mais | `qwen3:30b-a3b` ou `qwen3:32b` | Para a turma toda |

Antes de baixar, confira em https://ollama.com/library se há uma versão mais nova do Qwen com a etiqueta **tools**. O tutor depende de chamada de ferramentas.

## 2. Instalar e configurar o Ollama

1. Baixe e instale em https://ollama.com/download (Windows).
2. Aumente o contexto. O padrão do Ollama é pequeno, e o prompt + ferramentas + material + histórico passam disso. Sem isso, o modelo "esquece" as regras no meio da conversa:

   ```powershell
   setx OLLAMA_CONTEXT_LENGTH 8192
   ```

   Feche o Ollama pela bandeja (Quit) e abra de novo para valer.
3. Baixe o modelo e teste:

   ```powershell
   ollama pull qwen3:8b
   ollama run qwen3:8b "Responda só: ok"
   ollama ps
   ```

   Em `ollama ps`, a coluna PROCESSOR deve mostrar **100% GPU**. Se aparecer CPU, o modelo não coube na placa: use um menor.

## 3. Medir antes de trocar (avaliação)

O script `scripts/avaliar.py` conversa com o Maxwell usando o banco de perguntas `avaliacao/perguntas.json` e mede:

- **vazamento:** o tutor deu o resultado final antes da tentativa do aluno, mesmo com insistência;
- **ferramenta:** chamou a calculadora certa;
- **tamanho:** respostas curtas, como mandam os prompts;
- **tempo:** segundos por resposta;
- **`<think>`:** o modelo mostrou o raciocínio interno na resposta.

Instale o `uv` uma vez (`pip install uv`) e, na pasta do projeto:

```powershell
uv sync
# Linha de base: Groq (usa o .env atual). A pausa evita o limite por minuto.
uv run python scripts/avaliar.py --rotulo groq --pausa 20
# Modelo local
uv run python scripts/avaliar.py --rotulo qwen3-8b --base-url http://localhost:11434/v1 --modelo qwen3:8b --chave ollama
```

Cada rodada gera um relatório em `avaliacao/resultados/` com a tabela de casos e todas as respostas. Compare os dois e **leia as respostas**: o script pega vazamento de número e falta de ferramenta, mas a qualidade da explicação só se vê lendo.

Para rodar um caso só: `--so tutor-gamma-insistente`.

## 4. Trocar o Maxwell para o modelo local

No `.env`:

```env
LLM_BASE_URL=http://host.docker.internal:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=qwen3:8b
```

E recrie o backend (um `restart` não relê o `.env`):

```powershell
docker compose up -d backend
```

`host.docker.internal` é como o container enxerga o PC. O `docker-compose.yml` já tem `extra_hosts` para isso funcionar também no Linux do PC do professor.

## 5. Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Resposta muito lenta, `ollama ps` mostra CPU | Modelo maior que a memória de vídeo | Modelo menor |
| Aparece `<think>...</think>` ou demora antes de começar a responder | O Qwen3 "pensa" antes de responder | Teste acrescentar `/no_think` no fim do `base.md` e compare na avaliação |
| Não chama as ferramentas ou inventa números | Modelo pequeno demais | Suba um tamanho; reforce no prompt "use as ferramentas" |
| Esquece o modo socrático no meio da conversa | Contexto curto | Confira `OLLAMA_CONTEXT_LENGTH` (passo 2) |
| Backend não conecta no Ollama | URL errada dentro do Docker | Use `host.docker.internal`, não `localhost`, no `.env` |

## 6. Ciclo de melhoria do método de ensino

1. Rode a avaliação.
2. Leia o relatório e anote os casos que falharam e as respostas ruins.
3. Mude **uma coisa** no prompt (`src/maxwell/prompts/`).
4. Rode de novo com outro rótulo e compare.

Acrescente casos novos em `avaliacao/perguntas.json` sempre que achar um comportamento ruim usando o site. Assim ele não volta.
