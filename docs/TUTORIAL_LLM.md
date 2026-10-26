# Tutorial: obtendo acesso a cada LLM gratuito

Passo a passo para cada opção de [OPCOES_LLM.md](OPCOES_LLM.md), da mais fácil para a mais difícil. As três primeiras só pedem criar uma chave. A última instala o modelo na máquina.

## Antes de começar: onde guardar as chaves

**Nunca cole a chave no chat nem em arquivo versionado.** Guarde todas no `.env`, que está no `.gitignore`, em variáveis separadas. O backend ignora variáveis que não conhece, então elas não atrapalham:

```env
GROQ_API_KEY=
GEMINI_API_KEY=
OPENROUTER_API_KEY=
```

Depois de testar, a opção escolhida é copiada para as variáveis `LLM_*`, que são as que o tutor realmente usa.

Os testes abaixo usam o PowerShell. Troque `COLE_A_CHAVE` pela sua chave.

---

## 1. Groq (fácil, cerca de 3 minutos)

1. Acesse **https://console.groq.com** e entre com Google ou GitHub. Não pede cartão.
2. No menu, abra **API Keys** e clique em **Create API Key**.
3. Dê um nome (ex.: `maxwell`) e confirme.
4. Copie a chave **na hora**, porque ela só aparece uma vez. Ela começa com `gsk_`.
5. Cole no `.env`, em `GROQ_API_KEY=`.

**Teste rápido:**

```powershell
$key = "COLE_A_CHAVE"
$body = '{"model":"qwen/qwen3.8-27b","messages":[{"role":"user","content":"Responda so: ok"}]}'
(Invoke-RestMethod -Uri "https://api.groq.com/openai/v1/chat/completions" -Method Post `
  -Headers @{Authorization = "Bearer $key"} -ContentType "application/json" -Body $body).choices[0].message.content
```

Se aparecer um texto com "ok", talvez precedido de um bloco `<think>...</think>`, está funcionando. Os limites da conta ficam em **Settings → Limits**.

**Configuração para o tutor:**

```env
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_API_KEY=<a mesma chave do GROQ_API_KEY>
LLM_MODEL=qwen/qwen3.8-27b
```

---

## 2. Gemini (fácil, cerca de 3 minutos)

1. Acesse **https://aistudio.google.com** e entre com uma conta Google. Se for conta institucional da UFES, o administrador pode ter bloqueado o AI Studio; nesse caso use uma conta pessoal.
2. Aceite os termos, se aparecerem.
3. Clique em **Get API key** e depois em **Create API key**. Se ele pedir um projeto do Google Cloud, deixe criar um novo.
4. Copie a chave. Ela costuma começar com `AIza`.
5. Cole no `.env`, em `GEMINI_API_KEY=`.

**Teste rápido**, que lista os modelos que a sua chave pode usar:

```powershell
$key = "COLE_A_CHAVE"
(Invoke-RestMethod -Uri "https://generativelanguage.googleapis.com/v1beta/openai/models" `
  -Headers @{Authorization = "Bearer $key"}).data.id
```

Escolha um modelo `gemini-...-flash` da lista para o `LLM_MODEL`. Os nomes mudam com frequência. Os limites gratuitos aparecem no AI Studio, em **Usage / Rate limits**.

**Configuração para o tutor:**

```env
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_API_KEY=<a mesma chave do GEMINI_API_KEY>
LLM_MODEL=<um gemini-...-flash da lista>
```

---

## 3. OpenRouter com modelos gratuitos (fácil, cerca de 5 minutos)

1. Acesse **https://openrouter.ai** e entre com Google ou GitHub.
2. Abra **https://openrouter.ai/keys** e clique em **Create Key**.
3. Dê um nome e, por segurança, defina o **credit limit** como `0`. Assim a chave nunca gasta dinheiro.
4. Copie a chave. Ela começa com `sk-or-v1-`.
5. Cole no `.env`, em `OPENROUTER_API_KEY=`.
6. Opcional: em **Settings → Privacy**, alguns modelos gratuitos só funcionam se você permitir que o provedor use os dados para treino. Se o teste der erro 404 falando de *data policy*, é isso.

**Teste rápido**, que lista os modelos gratuitos do Qwen:

```powershell
(Invoke-RestMethod -Uri "https://openrouter.ai/api/v1/models").data.id | Where-Object { $_ -like "*qwen*:free" }
```

Depois teste a chave com um dos modelos da lista:

```powershell
$key = "COLE_A_CHAVE"
$body = '{"model":"COLE_O_MODELO:free","messages":[{"role":"user","content":"Responda so: ok"}]}'
(Invoke-RestMethod -Uri "https://openrouter.ai/api/v1/chat/completions" -Method Post `
  -Headers @{Authorization = "Bearer $key"} -ContentType "application/json" -Body $body).choices[0].message.content
```

Lembre do limite de **50 requisições por dia** sem crédito comprado. Não gaste tudo testando.

**Configuração para o tutor:**

```env
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_API_KEY=<a mesma chave do OPENROUTER_API_KEY>
LLM_MODEL=<modelo terminado em :free>
```

---

## 4. Ollama local (médio, cerca de 15 a 30 minutos, a maior parte é download)

Não precisa de chave, mas instala um programa e baixa alguns GB.

### Instalação

1. Baixe o instalador em **https://ollama.com/download/windows** e execute o `OllamaSetup.exe`.
2. Ao terminar, o Ollama fica rodando na bandeja do sistema, ao lado do relógio.
3. Abra um **novo** PowerShell e confira:

   ```powershell
   ollama --version
   ```

### Baixando os modelos

```powershell
ollama pull qwen3:4b    # ~2,5 GB, cabe inteiro na GPU
ollama pull qwen3:8b    # ~5 GB, no limite da VRAM
```

### Teste rápido

```powershell
ollama run qwen3:4b "Explique em uma frase o que é coeficiente de reflexão. /no_think"
```

O `/no_think` desliga o "modo de pensar" do Qwen3, que deixa as respostas bem mais lentas.

Em **outro** PowerShell, enquanto o modelo responde, confira se ele está na GPU:

```powershell
ollama ps
```

A coluna **PROCESSOR** deve mostrar `100% GPU` para o 4B. Para o 8B, algo como `30%/70% CPU/GPU` significa que parte foi para a CPU e vai ficar mais lento.

Teste também o endpoint compatível com OpenAI, que é o que o backend usa:

```powershell
$body = '{"model":"qwen3:4b","messages":[{"role":"user","content":"Responda so: ok /no_think"}]}'
(Invoke-RestMethod -Uri "http://localhost:11434/v1/chat/completions" -Method Post `
  -ContentType "application/json" -Body $body).choices[0].message.content
```

**Configuração para o tutor**, com o backend rodando no Docker:

```env
LLM_BASE_URL=http://host.docker.internal:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=qwen3:4b
```

Se o backend rodar fora do Docker (`uv run uvicorn ...`), use `http://localhost:11434/v1`.

### Se o container não conseguir falar com o Ollama

Por padrão o Ollama só escuta em `127.0.0.1`. Se o backend no Docker não conectar:

1. Feche o Ollama pela bandeja do sistema.
2. Defina a variável de ambiente do usuário `OLLAMA_HOST` como `0.0.0.0`: **Configurações → Sistema → Sobre → Configurações avançadas do sistema → Variáveis de Ambiente**.
3. Abra o Ollama de novo.

---

## Depois de pegar as chaves

Com as chaves no `.env`, é só pedir o teste. Faremos o seguinte:

1. testar cada chave direto na API;
2. subir o projeto (`docker compose up -d --build`) com a opção escolhida nas variáveis `LLM_*`;
3. fazer uma pergunta de linhas de transmissão que force o uso de ferramenta (ex.: calcular Γ) e medir o tempo de resposta.
