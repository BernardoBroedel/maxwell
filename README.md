# Maxwell

> [!CAUTION]
> **O Maxwell pode errar. Não confie 100% nas respostas.**
> Ele é uma ferramenta de apoio ao estudo e não substitui o professor, o livro ou as aulas. Sempre confira fórmulas, valores e resoluções com o material da disciplina.

Assistente de estudo com IA para a disciplina de **Eletromagnetismo II** da UFES.

Em vez de entregar a resposta pronta, o Maxwell guia o aluno com perguntas e dicas, como um monitor. Foco atual: **Linhas de Transmissão**.

## O que ele faz

| Modo | Para quê |
|---|---|
| **Maxwell** | Tirar dúvidas, com dicas passo a passo |
| **Revisão** | Treinar para a prova com perguntas rápidas |
| **Cartões Anki** | Gerar cartões de memorização para o [Anki](#cartões-anki) |
| **Exercícios** | Resolver exercícios junto com o aluno, depois que ele tenta |
| **Plano de estudo** | Montar um roteiro de estudo até a prova |

![Exemplo de conversa com o Maxwell](docs/img/conversa.png)

## Como funciona

```
Aluno ──► Chat no navegador ──► Maxwell ──► Modelo de IA
                                   │
                                   ├─ consulta o livro e as notas da disciplina
                                   ├─ segue regras de ensino (não entrega a resposta pronta)
                                   └─ usa uma calculadora própria para as contas
```

O modelo de IA pode ser um serviço gratuito na internet (Groq) ou rodar no próprio computador.

## Cartões Anki

O [Anki](https://apps.ankiweb.net) é um aplicativo gratuito de **cartões de memorização** (flashcards): pergunta na frente, resposta no verso. Você lê a pergunta, tenta lembrar, vira o cartão e diz se acertou.

O diferencial é a **repetição espaçada**: o Anki decide quando cada cartão volta. O que você erra aparece de novo logo; o que você acerta volta em alguns dias, depois em semanas. Assim o aluno estuda mais o que ainda não sabe, em poucos minutos por dia. Funciona muito bem para fórmulas, definições e casos limite.

O modo **Cartões Anki** do Maxwell gera esses cartões a partir do material da disciplina, prontos para importar.

| Plataforma | Aplicativo |
|---|---|
| Windows, Mac e Linux | [Anki](https://apps.ankiweb.net) (gratuito) |
| Android | AnkiDroid (gratuito, na Play Store) |
| iPhone | AnkiMobile (pago) ou [AnkiWeb](https://ankiweb.net) no navegador (gratuito) |

**Como usar:**

1. No Maxwell, escolha o modo **Cartões Anki** e peça os cartões de um tema (ex.: *"Gera 10 cartões sobre carta de Smith"*).
2. Copie o bloco de texto da resposta (ícone de copiar, no canto do bloco), cole no Bloco de Notas e salve como `cartoes.txt`.
3. No Anki, vá em **Arquivo → Importar**, escolha o arquivo e o baralho de destino (ex.: "EM2 - Linhas de Transmissão") e clique em **Importar**.
4. Para estudar, clique no baralho e em **Estudar agora**. As fórmulas aparecem formatadas.

Para usar também no celular, crie uma conta gratuita no AnkiWeb, importe no computador uma vez e sincronize.

**Dicas:** peça poucos cartões por tema (de 8 a 15), confira os cartões antes de estudar (o Maxwell pode errar) e estude um pouco todo dia. A repetição espaçada funciona com constância, não com maratona na véspera.

## Como rodar

Você vai precisar de:

- **Docker Desktop**, o programa que roda o Maxwell. Se você não tem, siga o [tutorial oficial de instalação](https://docs.docker.com/get-started/get-docker/).
- **Uma chave gratuita do Groq**, o serviço de IA que recomendamos para testar. Veja [como obter a chave](docs/TUTORIAL_LLM.md).

Depois:

1. Copie o arquivo `.env.example` para `.env` e preencha:
   - `LLM_API_KEY`: a chave do Groq;
   - `WEBUI_SECRET_KEY`: qualquer texto longo e aleatório (funciona como uma senha interna);
   - `WEBUI_ADMIN_EMAIL` e `WEBUI_ADMIN_PASSWORD`: o e-mail e a senha do administrador.
2. Abra um terminal na pasta do projeto e rode:

   ```bash
   docker compose up -d --build
   docker compose --profile setup run --rm configurar
   ```

3. Acesse **http://localhost:3000** e entre com o e-mail e a senha do administrador. O [guia do administrador](docs/GUIA_ADMIN.md) mostra, com imagens, o que dá para fazer: aprovar alunos, ver as avaliações, ligar e desligar modos.

> As notas de estudo da disciplina já vêm no repositório. O livro não vem, por direitos autorais: peça os arquivos à equipe.

## Rodar a IA no próprio computador

É possível, mas precisa de placa de vídeo NVIDIA:

| Uso | Placa de vídeo |
|---|---|
| Testar | 6 GB |
| Apresentar com boa qualidade | 8 a 12 GB |
| Turma inteira usando | 24 GB ou mais |

Sem placa de vídeo, funciona, mas fica lento demais para uso real. Treinar um modelo próprio não é necessário por enquanto: o Maxwell se especializa pelas regras de ensino e pelo material da disciplina.

## Como contribuir

**Não precisa saber programar.** O que mais ajuda agora é apontar erros de conteúdo e sugerir melhorias. Para isso, abra uma **issue**: um pedido registrado aqui no GitHub, que a equipe acompanha e responde.

**Como abrir uma issue:**

1. Crie uma conta gratuita no [GitHub](https://github.com/signup), se ainda não tiver.
2. Acesse **[Nova issue](https://github.com/BernardoBroedel/maxwell/issues/new/choose)**.
3. Escolha o formulário:
   - **Erro de conteúdo:** o Maxwell errou uma fórmula, um valor ou uma explicação.
   - **Sugestão:** ideia de melhoria, novo conteúdo, novo modo ou envio de material.
4. Preencha os campos e clique em **Create** (ou **Submit new issue**). Para anexar um print, arraste a imagem para o campo de texto.

**Ao relatar um erro, ajuda informar:** o modo usado, a pergunta, o que o Maxwell respondeu, o que seria o certo e, se possível, onde conferir (livro, página, equação).

**Quer enviar material?** Notas, resumos e listas resolvidas podem ser anexados numa issue de Sugestão, em `.md`, `.docx` ou PDF. A equipe converte e inclui no Maxwell. Envie só material seu ou da turma: livros e apostilas têm direitos autorais.

Não tem conta no GitHub? Fale direto com a equipe.

Para quem programa: veja o [guia técnico](docs/DESENVOLVIMENTO.md) e envie um *pull request*.

## Documentação

- [Guia do aluno](docs/GUIA_ALUNO.md)
- [Guia do administrador](docs/GUIA_ADMIN.md)
- [Como obter a chave ou rodar a IA localmente](docs/TUTORIAL_LLM.md)
- [Comparação das opções de IA](docs/OPCOES_LLM.md)
- [Como adicionar material ao Maxwell](docs/DESENVOLVIMENTO.md#como-adicionar-material)
- [Pesquisa sobre IA no estudo](docs/PESQUISA_IA_ESTUDO.md)
- [Guia técnico](docs/DESENVOLVIMENTO.md)

## Licença

Código sob a [licença MIT](LICENSE). O material da disciplina pertence aos respectivos autores.
