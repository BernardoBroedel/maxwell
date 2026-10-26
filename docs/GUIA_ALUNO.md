# Guia do aluno

> [!CAUTION]
> **O Maxwell pode errar. Não confie 100% nas respostas.**
> Sempre confira fórmulas, valores e resoluções com o livro, as notas da disciplina e o professor.

O Maxwell é um monitor de estudo de Eletromagnetismo II. Ele **não entrega a resposta pronta**: faz perguntas e dá dicas para você chegar lá sozinho. É assim que o conteúdo fixa para a prova.

## 1. Criar a conta

1. Acesse o endereço do Maxwell informado pelo professor.
2. Clique em **Inscrever-se** e preencha nome, e-mail e senha.

![Cadastro](img/aluno-cadastro.png)

3. Aguarde a aprovação do professor ou do monitor. Depois de aprovado, clique em **Verificar Novamente**.

![Aguardando aprovação](img/aluno-pendente.png)

## 2. Escolher o modo

Clique no nome do modo, ao lado da caixa de texto, para trocar:

![Escolha do modo](img/modos.png)

| Modo | Use quando... |
|---|---|
| **Maxwell** | tiver uma dúvida de conceito ou travar num exercício |
| **Exercícios** | quiser resolver um exercício específico, passo a passo |
| **Revisão** | quiser se testar antes da prova |
| **Cartões Anki** | quiser memorizar fórmulas com cartões ([como funciona](#5-cartões-anki)) |
| **Plano de estudo** | precisar organizar o tempo até a prova |

## 3. Como perguntar bem

- **Mande o enunciado completo**, com valores e unidades.
- **Mostre o que você já tentou**, mesmo que esteja errado. Quanto mais você mostra, mais certeira é a ajuda.
- **Uma dúvida por mensagem.**
- **Responda às perguntas do Maxwell.** É assim que ele passa para a próxima dica.
- Impedâncias podem ser escritas como `75+j25`, `50∠30°`, `curto` ou `aberto`.

| ❌ Evite | ✅ Prefira |
|---|---|
| "Resolve o 11.16 pra mim." | "No 11.16 (coaxial em curto, Z0 = 65+j38 Ω, γ = 0,7+j2,5 /m, ℓ = 0,8 m), usei Zcc = Z0·tgh(γℓ), mas não sei calcular a tgh de um número complexo." |
| "Não entendi carta de Smith." | "Na carta de Smith, por que andar em direção ao gerador é no sentido horário?" |

## 4. O que esperar

- **Dicas antes da resposta.** Insistir não adianta: tente, e ele corrige o seu raciocínio. Nos modos **Revisão** e **Cartões Anki**, as respostas vêm diretas.
- **Contas conferidas.** Ele usa uma calculadora própria e consulta as notas da disciplina.
- **Ele pode errar.** Confira com o livro, as notas e o professor. O Maxwell é um apoio, não substitui a aula.
- **Foco atual:** Linhas de Transmissão.

## 5. Cartões Anki

### O que é o Anki

O [Anki](https://apps.ankiweb.net) é um aplicativo gratuito de **cartões de memorização** (flashcards). Cada cartão tem uma pergunta na frente e a resposta no verso. Você lê a pergunta, tenta lembrar a resposta, vira o cartão e diz se acertou.

O diferencial é a **repetição espaçada**: o Anki decide quando cada cartão volta. O que você erra aparece de novo logo; o que você acerta volta em alguns dias, depois em semanas. Assim você estuda mais o que ainda não sabe, em poucos minutos por dia. Funciona muito bem para fórmulas, definições e casos limite.

### Onde baixar

| Plataforma | Aplicativo |
|---|---|
| Windows, Mac e Linux | [Anki](https://apps.ankiweb.net) (gratuito) |
| Android | AnkiDroid (gratuito, na Play Store) |
| iPhone | AnkiMobile (pago) ou [AnkiWeb](https://ankiweb.net) no navegador (gratuito) |

Para usar no celular e no computador ao mesmo tempo, crie uma conta gratuita no AnkiWeb e sincronize.

### Como gerar os cartões no Maxwell

1. Escolha o modo **Cartões Anki**.
2. Peça os cartões de um tema. Por exemplo: *"Gera 10 cartões sobre carta de Smith"* ou *"Cartões com as fórmulas de impedância de entrada"*.
3. O Maxwell responde com um bloco de texto que começa com `#separator:Semicolon`. Esse bloco já está no formato que o Anki entende.

### Como importar no Anki (computador)

1. Clique no ícone de **copiar**, no canto do bloco de texto.
2. Abra o Bloco de Notas, cole e salve como `cartoes.txt`.
3. No Anki, vá em **Arquivo → Importar** e escolha o arquivo.
4. Confira o **baralho** de destino (crie um, como "EM2 - Linhas de Transmissão") e clique em **Importar**.

As fórmulas aparecem formatadas no Anki. Para estudar, clique no baralho e em **Estudar agora**. Se você usa só o celular, importe no computador uma vez e sincronize pelo AnkiWeb.

**Dicas:**

- Peça poucos cartões por tema (de 8 a 15) e importe aos poucos, conforme avança na matéria.
- Confira os cartões antes de estudar: o Maxwell pode errar.
- Estude um pouco todo dia. A repetição espaçada funciona com constância, não com maratona na véspera.

## 6. Avalie as respostas

Embaixo de cada resposta há 👍 e 👎. Avaliar ajuda a equipe a encontrar e corrigir os erros do Maxwell.

![Exemplo de conversa](img/conversa.png)

## 7. Se algo der errado

- **"⏳ Muitas perguntas ao mesmo tempo"**: o serviço de IA atingiu o limite de uso. Espere uns 30 segundos e mande de novo.
- **Resposta estranha:** clique em 🔄 (*Gerar novamente*) ou reformule a pergunta.
- **Esqueceu a senha:** fale com o professor ou o monitor.

## Boas práticas

- As conversas ficam salvas no servidor da disciplina: **não compartilhe dados pessoais**.
- Em provas e trabalhos avaliados, use o Maxwell só se o professor permitir.
