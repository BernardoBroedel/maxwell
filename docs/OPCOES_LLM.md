# Opções de LLM gratuitas

Levantamento de 2026-10-26 das formas de rodar o LLM do tutor **sem custo**: por API gratuita ou localmente.

> Os limites dos planos gratuitos mudam com frequência, e a maior parte dos números abaixo vem de blogs, não da documentação oficial. Confira no painel de cada serviço ao criar a conta.

## Contexto

- O backend aceita qualquer API compatível com OpenAI. Trocar de LLM é só mudar `LLM_BASE_URL`, `LLM_MODEL` e `LLM_API_KEY` no `.env` e recriar o backend com `docker compose up -d backend` (um `restart` não relê o `.env`).
- O tutor usa **chamada de ferramentas** (Γ, ROE, Z_in em `src/maxwell/tools.py`), e modelos pequenos erram bastante nisso.
- Quando o tutor usa uma ferramenta, uma pergunta do aluno vira **2 ou mais requisições**. Cada requisição envia o prompt e as ferramentas (cerca de 1,5 mil tokens) mais o histórico da conversa.
- **Máquina de desenvolvimento:** RTX 3050 Laptop com 6 GB de VRAM (cerca de 1,1 GB já ocupados pelo sistema), 32 GB de RAM e Core 7 240H.
- A chave do OpenRouter no `.env` era um placeholder (HTTP 401). A opção paga ficou de fora por enquanto.

## API gratuita

### 1. Groq (recomendada)

- **Modelo:** `qwen/qwen3.8-27b`. O `qwen/qwen3-32b` não está mais disponível no Groq; este é o Qwen que a conta lista hoje, e ele faz chamada de ferramentas corretamente (testado em 2026-10-26).
- **Limites do plano gratuito:** cerca de 30 a 60 requisições por minuto, 1.000 por dia e **6.000 tokens por minuto**.
- **A favor:** é muito rápida, aceita chamada de ferramentas e não pede cartão.
- **Contra:** o limite de tokens por minuto é o gargalo. Dá umas 3 ou 4 requisições por minuto com conversa curta. Serve para uma demo com uma pessoa usando; não serve para a turma toda ao mesmo tempo.

Configuração esperada no `.env`:

```env
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_API_KEY=<chave criada em console.groq.com>
LLM_MODEL=qwen/qwen3.8-27b
```

### 2. Gemini Flash (Google AI Studio)

- **Limites do plano gratuito:** variam muito entre as fontes. Uns falam em 15 por minuto e 1.500 por dia; relatos de abril de 2026 falam em 5 a 10 por minuto e só 20 a 100 por dia.
- **A favor:** o modelo é bom e aceita chamada de ferramentas.
- **Contra:** os limites estão incertos e foram reduzidos recentemente, e há relatos de cota que não reinicia. Também deixa de ser Qwen, o que foge da proposta do projeto.

### 3. OpenRouter com modelos `:free`

- **Limites do plano gratuito:** 20 por minuto, mas só **50 por dia** sem comprar crédito (1.000 por dia depois de comprar US$ 10).
- **Contra:** 50 requisições dão umas 20 ou 30 perguntas no dia todo. Os modelos gratuitos também ficam lentos ou saem do ar sem aviso nos horários de pico. Descartada para demonstrações.

## Local

### 4. Ollama nativo no Windows com Qwen3

Instalar o Ollama direto no Windows, em vez de usar o perfil `local` do compose, evita ter que passar a GPU para o Docker. O backend, no container, acessa o Ollama por `http://host.docker.internal:11434/v1`.

| Modelo | Cabe nos 6 GB? | Velocidade esperada | Qualidade para o tutor |
|---|---|---|---|
| Qwen3 **4B** (Q4, ~2,5 GB) | Sim, inteiro na GPU | Rápida | Razoável no português, erra mais nas ferramentas |
| Qwen3 **8B** (Q4, ~5 GB) | No limite, parte vai para a CPU | Média, um pouco lenta | Boa |
| Qwen3 **14B** | Não, a maior parte roda na CPU | Lenta demais | Boa, mas inviável nessa máquina |

- **A favor:** custo zero, sem limite de uso e sem internet.
- **Contra:** responde mais devagar e erra mais. Será preciso desligar o "modo de pensar" do Qwen3 para reduzir a espera.
- As velocidades da tabela são estimativas e precisam ser medidas.

Configuração esperada no `.env`:

```env
LLM_BASE_URL=http://host.docker.internal:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=qwen3:4b
```

## Recomendação

**Groq como principal e Ollama local como reserva.** Os dois são gratuitos, os dois rodam Qwen e trocar entre eles é só editar 3 linhas do `.env`.

## Fontes

- [Groq: limites gratuitos (grizzlypeaksoftware)](https://www.grizzlypeaksoftware.com/articles/p/groq-api-free-tier-limits-in-2026-what-you-actually-get-uwysd6mb)
- [Groq: qwen3-32b gratuito (freellm)](https://freellm.net/models/groq/qwen-qwen3-32b)
- [Groq: preços em 2026 (eesel)](https://eesel.ai/blog/groq-pricing)
- [Gemini: mudanças de abril de 2026 (agentdeals)](https://agentdeals.dev/gemini-api-pricing-changes)
- [Gemini: limites do plano gratuito (tinkerllm)](https://tinkerllm.com/blog/gemini-api-free-tier-limits-rate-quotas/)
- [Gemini: relato de cota que não reinicia (fórum do Google)](https://discuss.ai.google.dev/t/limits-on-gemini-api-free-tier-not-resetting/135026)
- [OpenRouter: comparação de APIs gratuitas](https://openrouter.ai/blog/tutorials/free-llm-apis-compared/)
- [OpenRouter: limites do plano gratuito (truefoundry)](https://www.truefoundry.com/pt/blog/openrouter-rate-limits-your-free-tier-depends-on-what-youve-already-paid)
