# Resultados dos testes automáticos

Como o Maxwell foi avaliado antes da entrega e o que os números mostram.

## Como o teste funciona

O script `scripts/avaliar.py` conversa com o Maxwell como se fosse um aluno, usando uma bateria gerada por `scripts/gerar_bateria.py`, e confere cada resposta de duas formas:

- **Regras automáticas:** vazamento do resultado antes da tentativa do aluno (inclusive escrito em LaTeX), uso da ferramenta de cálculo certa, formato dos cartões do Anki, tamanho da resposta.
- **Juiz:** o próprio modelo, com mais raciocínio, lê a conversa e o gabarito e avalia se a física está correta, se o tutor entregou a resposta cedo demais, se seguiu o modo e dá uma nota de 1 a 5.

Os gabaritos numéricos vêm das ferramentas de cálculo de linhas de transmissão (`src/maxwell/linhas.py`), não do modelo.

## Configuração do teste final (17 para 18/11/2026)

- **Modelo:** qwen3.8 (27B, quantizado Q4_K_M) rodando localmente no Ollama, no PC do laboratório, com raciocínio `low`.
- **Juiz:** o mesmo modelo, com raciocínio `medium` e temperatura 0.
- **Material no RAG:** Sadiku, *Elementos de Eletromagnetismo*, caps. 9 a 12 (transcritos página a página); material do professor (Linhas de Transmissão, Guias de Ondas, Matrizes e Dispositivos de RF); notas de estudo do cap. 11 (fórmulas, exercícios resolvidos e revisão).
- **Bateria:** 247 casos (328 mensagens de aluno), rodada duas vezes ao mesmo tempo: **com** e **sem** as notas de estudo do cap. 11, para decidir se elas ficam.

## Resultado

| | Com as notas (versão entregue) | Sem as notas |
| --- | --- | --- |
| Casos aprovados | **222 de 247 (90%)** | 216 de 247 (87%) |
| Vazamento do resultado | **0** | 0 |
| Física errada (juiz) | **1** | 5 |
| Entregou cedo (juiz) | 20 | 25 |
| Nota média (juiz, 1 a 5) | **4,67** | 4,64 |

### Por categoria (versão entregue)

| Categoria | Casos | Aprovados | Nota média |
| --- | --- | --- | --- |
| Conceitos de Maxwell, ondas, guias e RF (caps. 9, 10, 12) | 40 | 100% | 4,7 |
| Conceitos de linhas de transmissão | 40 | 98% | 4,8 |
| Confere resposta errada do aluno | 21 | 100% | 4,8 |
| Confere resposta certa do aluno | 21 | 90% | 5,0 |
| Exercícios: impedância de entrada | 24 | 96% | 4,9 |
| Exercícios: transformador λ/4 sem tentativa | 12 | 83% | 4,5 |
| Exercícios: aluno pede o valor e insiste | 15 | 80% | 4,3 |
| Tutor: aluno pede o valor e insiste | 30 | 53% | 4,0 |
| Cartões do Anki | 20 | 90% | 4,8 |
| Revisão (uma pergunta por vez) | 10 | 100% | 4,9 |
| Plano de estudo | 6 | 100% | 4,5 |
| Segurança (tentar extrair as instruções) | 8 | 100% | 5,0 |

### Evolução em relação à primeira bateria grande (noite de 13/11)

| | Primeira bateria | Teste final |
| --- | --- | --- |
| Casos aprovados | 79% (331 casos) | **90%** (247 casos) |
| Física errada (juiz) | 10 (3%) | **1 (0,4%)** |
| Entregou cedo (juiz) | 48 (15%) | **20 (8%)** |
| Nota média do juiz | 4,37 | **4,67** |
| Exercícios: aluno pede o valor | 36% | **80%** |

Entre as duas baterias foram ajustados os prompts (fórmulas de referência, sinais de reatância, regras contra entregar contas com os números do aluno, formato do Anki) e o material completo da disciplina entrou no RAG.

## Conclusões

- **As notas de estudo do cap. 11 ficam.** Com elas, os erros de física caíram de 5 para 1 e o transformador λ/4 subiu de 50% para 83%: os exercícios resolvidos e o gabarito ajudam o tutor a conferir sem errar.
- **O modelo local é suficiente.** Nenhum caso entregou o resultado final, a física saiu errada em 1 de 247 casos e o conteúdo novo (caps. 9, 10, 12 e RF) teve 100% de acerto.
- **Limitação conhecida:** quando o aluno insiste muito pelo valor, o tutor às vezes escreve a fórmula já com os números do aluno, como $\Gamma_L = \frac{45-100}{45+100}$, sem fazer a conta. O resultado não é revelado, mas o juiz conta isso como "entregou cedo". É o principal ponto a melhorar.
- O único erro de física foi num comentário extra: o tutor disse que andar da carga para o gerador gira a carta de Smith no sentido anti-horário (o correto é horário).

## Tempo de resposta

No teste, o PC atendia 4 conversas e o juiz ao mesmo tempo, e a resposta média levou cerca de 2,5 minutos. Com poucos alunos usando ao mesmo tempo, a resposta é bem mais rápida (o modelo gera cerca de 29 tokens por segundo). Neste projeto a prioridade foi responder certo, não responder rápido.
