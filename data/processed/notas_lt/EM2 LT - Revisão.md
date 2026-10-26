---
tags: [eletromagnetismo2, ufes, prova, revisao, consulta]
---
# EM2 LT - Revisão
← [[Eletromagnetismo 2]] · [[EM2 LT - Fórmulas|Fórmulas]] · [[EM2 LT - Exercícios|Exercícios]]

Revisão do capítulo 11, **Linhas de Transmissão**. Use esta nota na véspera: leia o resumo, responda às perguntas sem olhar, passe pelo checklist e releia as armadilhas.

> [!info] Origem do conteúdo
> O resumo, as perguntas e as armadilhas foram escritos por mim a partir do capítulo. **As perguntas não são as do fim do capítulo do livro.** Confira com o material do seu professor.

## Consulta rápida
| Preciso de... | Fórmula | Onde |
|---|---|---|
| $Z_0$ sem perdas | $\sqrt{L/C}$ | [[EM2 LT - Fórmulas#Linha sem perdas e sem distorção]] |
| $\Gamma$ na carga | $\dfrac{Z_C-Z_0}{Z_C+Z_0}$ | [[EM2 LT - Fórmulas#Impedância de entrada e coeficiente de reflexão]] |
| ROE | $s=\dfrac{1+\lvert\Gamma\rvert}{1-\lvert\Gamma\rvert}$ | idem |
| $Z_{ent}$ sem perdas | $Z_0\dfrac{Z_C+jZ_0\tan\beta\ell}{Z_0+jZ_C\tan\beta\ell}$ | idem |
| $\lambda/4$ | $Z_{ent}=Z_0^2/Z_C$ | [[EM2 LT - Fórmulas#Casamento de impedâncias]] |
| Carta de Smith | gire $720^\circ$ por $\lambda$, horário = para o gerador | [[EM2 LT - Fórmulas#Carta de Smith]] |
| Transitório | $\Gamma_G$, $\Gamma_C$, $V_0=\dfrac{Z_0V_g}{Z_g+Z_0}$ | [[EM2 LT - Fórmulas#Transitórios]] |
| Microfita | $\varepsilon_{ef}$, $Z_0$ | [[EM2 LT - Fórmulas#Microfita]] |

## Sumário
1. [[#Resumo em uma página]]
2. [[#Casos especiais de carga]]
3. [[#Receitas de prova]]
4. [[#Perguntas de revisão]]
5. [[#Checklist de estudo]]
6. [[#Armadilhas mais comuns]]
7. [[#Erros de impressão no livro]]

---

## Resumo em uma página
**Ideia central.** Quando o comprimento da linha é comparável ao comprimento de onda, tensão e corrente variam ao longo dela. A linha é modelada por **parâmetros distribuídos** $R$, $L$, $G$, $C$ (por metro). As **equações do telegrafista** dão ondas que viajam nos dois sentidos:
$$V(z)=V_0^+e^{-\gamma z}+V_0^-e^{+\gamma z},\qquad I(z)=\frac{V_0^+}{Z_0}e^{-\gamma z}-\frac{V_0^-}{Z_0}e^{+\gamma z}$$

**Propagação.**
- $\gamma=\alpha+j\beta=\sqrt{(R+j\omega L)(G+j\omega C)}$ e $Z_0=\sqrt{\dfrac{R+j\omega L}{G+j\omega C}}$.
- **Sem perdas** ($R=G=0$): $\alpha=0$, $\beta=\omega\sqrt{LC}$, $Z_0=\sqrt{L/C}$ real, $u=1/\sqrt{LC}=1/\sqrt{\mu\varepsilon}$.
- **Sem distorção** ($R/L=G/C$): $Z_0$ real, $\alpha=\sqrt{RG}$, e a velocidade não depende da frequência.
- 1 Np $=8{,}686$ dB.

**Reflexão.**
- $\Gamma_C=\dfrac{Z_C-Z_0}{Z_C+Z_0}$; ao longo da linha $\Gamma(\ell')=\Gamma_Ce^{-2\gamma\ell'}$ (sem perdas: só **gira** $-2\beta\ell'$, módulo constante).
- $s=\dfrac{1+\lvert\Gamma\rvert}{1-\lvert\Gamma\rvert}$; $Z_{máx}=sZ_0$ nos máximos de tensão, $Z_{mín}=Z_0/s$ nos mínimos. Máximos e mínimos de tensão ficam **$\lambda/4$** afastados; dois máximos consecutivos, $\lambda/2$.
- A **corrente** reflete com sinal trocado ($-\Gamma$): onde $\lvert V\rvert$ é máx, $\lvert I\rvert$ é mín.
- Potência média: $P=P_i-P_r=P_i(1-\lvert\Gamma\rvert^2)$.

**Impedância de entrada.** $Z_{ent}=Z_0\dfrac{Z_C+Z_0\tanh\gamma\ell}{Z_0+Z_C\tanh\gamma\ell}$. Sem perdas, troque $\tanh\gamma\ell$ por $j\tan\beta\ell$. Propriedades: repete a cada $\lambda/2$; inverte em $\lambda/4$.

**Casamento.** Objetivo: $\Gamma=0$ ($s=1$) para que toda a potência vá à carga.
- **Transformador $\lambda/4$**: $Z_{01}=\sqrt{Z_0Z_C}$ (carga **real**).
- **Toco (stub)** em paralelo: use a carta como **carta de admitâncias**; ande até o círculo $g=1$ e cancele a susceptância com o toco.

**Transitórios.** Um degrau de $V_g$ viaja com $V_0^+=\dfrac{Z_0V_g}{Z_g+Z_0}$; reflexões sucessivas no gerador ($\Gamma_G$) e na carga ($\Gamma_C$) levam a $V_\infty=\dfrac{Z_C}{Z_g+Z_C}V_g$.

**Microfita.** Dielétrico não homogêneo ⇒ usa-se a **permissividade efetiva** $\varepsilon_{ef}$, com $\varepsilon_{ef}<\varepsilon_r$; $u=c/\sqrt{\varepsilon_{ef}}$. Perdas: $\alpha=\alpha_c+\alpha_d$.

## Casos especiais de carga
| Carga $Z_C$ | $\Gamma_C$ | $s$ | Onda | $Z_{ent}$ |
|---|---|---|---|---|
| **Casada** $Z_0$ | $0$ | $1$ | só incidente (progressiva) | $Z_0$ para qualquer $\ell$ |
| **Curto** $0$ | $-1$ | $\infty$ | estacionária pura; mínimo (zero) de $V$ na carga | $jZ_0\tan\beta\ell$ |
| **Aberto** $\infty$ | $+1$ | $\infty$ | estacionária pura; máximo de $V$ na carga | $-jZ_0\cot\beta\ell$ |
| **Reativa** pura $jX$ | $\lvert\Gamma\rvert=1$ | $\infty$ | estacionária pura; nenhuma potência absorvida | $jX'$ |
| **Real** $R_L>Z_0$ | $>0$, real | $R_L/Z_0$ | máximo de $V$ na carga | — |
| **Real** $R_L<Z_0$ | $<0$, real | $Z_0/R_L$ | mínimo de $V$ na carga | — |

Mais três casos que caem em prova:
- $\ell=\lambda/2$: $Z_{ent}=Z_C$.
- $\ell=\lambda/4$: $Z_{ent}=Z_0^2/Z_C$ (curto vira aberto e vice-versa).
- $Z_{cc}\cdot Z_{ca}=Z_0^2$, logo $Z_0=\sqrt{Z_{cc}Z_{ca}}$ (e $\tanh^2\gamma\ell=Z_{cc}/Z_{ca}$).

## Receitas de prova
Ordem de ataque para os tipos de questão mais comuns. Os detalhes estão em [[EM2 LT - Fórmulas]].

1. **"Dados $L$, $C$, $\omega$..., achar $Z_0$, $\beta$, $u$."** Sem perdas: $Z_0=\sqrt{L/C}$, $\beta=\omega\sqrt{LC}$, $u=\omega/\beta$. Com perdas, vá direto a $\gamma$ e $Z_0$ complexos.
2. **"Achar $Z_{ent}$."** (i) $\beta\ell$ em graus; (ii) reduza módulo $180^\circ$ no $\tan$; (iii) fórmula. Cheque os atalhos $\lambda/4$ e $\lambda/2$ antes de calcular.
3. **"Achar $V_{máx}$, $V_{mín}$ e suas posições."** $\lvert\Gamma\rvert\to s$. O primeiro $V_{máx}$ fica em $\ell'=\dfrac{\theta_\Gamma}{720^\circ}\lambda$ (se $\theta_\Gamma\ge0$); o primeiro $V_{mín}$, $\lambda/4$ depois (ou antes).
4. **"Linha fendida."** $\lambda$ vem de dois mínimos consecutivos ($\lambda/2$); $s$ vem de $V_{máx}/V_{mín}$; o deslocamento com o curto dá a posição da carga. Use a regra do sentido (para o gerador/para a carga) de [[EM2 LT - Fórmulas#Linha fendida]].
5. **"Casar com toco."** $y_C=1/z_C$ → círculo $s$ → intersecção com $g=1$ (duas soluções) → $y_s=-jb$ → comprimento do toco medido a partir de $P_{cc}$. Confira $d_A+d_B=\lambda/2$.
6. **"Transitório."** Calcule $\Gamma_G$, $\Gamma_C$, $V_0^+$, $t_1=\ell/u$. Monte o diagrama de saltos e some os degraus por intervalo. Confira o limite $V_\infty$.
7. **"Microfita."** Defina se $w/h\le1$ ou $\ge1$ antes de escolher a fórmula de $Z_0$. Projeto: calcule $A$ ou $B$ e escolha pela comparação com $w/h=2$.

## Perguntas de revisão
Responda de cabeça e abra a resposta para conferir. Todas são minhas.

### 1. Por que precisamos do modelo de linha de transmissão?
> [!success]- Resposta
> Porque, quando $\ell$ é comparável a $\lambda$ (em geral $\ell>\lambda/10$), tensão e corrente variam apreciavelmente ao longo do condutor; o modelo de circuito de parâmetros concentrados deixa de valer. A linha passa a ser tratada como infinitos elementos $R\Delta z$, $L\Delta z$, $G\Delta z$, $C\Delta z$.

### 2. O que significam $\alpha$ e $\beta$? Quais as unidades?
> [!success]- Resposta
> $\alpha$ (Np/m) é a atenuação; $\beta$ (rad/m) é a constante de fase, com $\beta=2\pi/\lambda$ e $u=\omega/\beta$. O sinal cai como $e^{-\alpha z}$ e a fase gira $-\beta z$.

### 3. Quando $Z_0$ é real?
> [!success]- Resposta
> Em linha **sem perdas** ($R=G=0$) e em linha **sem distorção** ($R/L=G/C$). Em geral é complexo.

### 4. O que acontece com $\lvert\Gamma\rvert$ ao longo de uma linha **sem perdas**? E com perdas?
> [!success]- Resposta
> Sem perdas, $\lvert\Gamma\rvert$ é constante (só a fase gira). Com perdas, $\lvert\Gamma(\ell')\rvert=\lvert\Gamma_C\rvert e^{-2\alpha\ell'}$ decai em direção ao gerador, e a espiral na carta converge para o centro.

### 5. Uma linha tem $s=1$. O que se pode dizer da carga?
> [!success]- Resposta
> $\Gamma=0$, então a carga é casada, $Z_C=Z_0$; há só onda incidente, $\lvert V\rvert$ é constante e toda a potência é absorvida.

### 6. Dois pontos da linha distam $\lambda/2$. Como se relacionam as impedâncias?
> [!success]- Resposta
> São **iguais**. A $\lambda/4$ valem $Z_{ent}=Z_0^2/Z_C$.

### 7. Linha de 50 Ω, curto-circuitada, com $\ell=\lambda/4$. Qual a impedância de entrada? E a $\lambda/8$?
> [!success]- Resposta
> $\lambda/4$: aberto ($\infty$). $\lambda/8$: $Z=jZ_0\tan45^\circ=j50\ \Omega$ (indutor). Entre 0 e $\lambda/4$, curto é **indutivo**; entre $\lambda/4$ e $\lambda/2$, é **capacitivo**.

### 8. Onde estão os mínimos de tensão de uma linha em curto?
> [!success]- Resposta
> Na carga e a cada $\lambda/2$ (zeros de $\lvert V\rvert$). Os máximos ficam em $\lambda/4$, $3\lambda/4$, ...

### 9. Se $Z_C$ é real e maior que $Z_0$, o que há na carga: máximo ou mínimo de tensão?
> [!success]- Resposta
> **Máximo**: $\Gamma>0$ e $\theta_\Gamma=0$, então $V_{máx}$ cai na carga, com $s=Z_C/Z_0$.

### 10. Na carta de Smith, o que representam: o centro, a borda, o semicírculo superior, o eixo real?
> [!success]- Resposta
> Centro: $z=1$ ($\Gamma=0$, casado). Borda: $\lvert\Gamma\rvert=1$ ($r=0$, só reatância). Metade superior: reatância **indutiva** ($x>0$); inferior: capacitiva. Eixo real: $x=0$, onde ficam $r_{máx}=s$ (direita) e $r_{mín}=1/s$ (esquerda).

### 11. Como converter impedância em admitância na carta?
> [!success]- Resposta
> Gire $180^\circ$ ($\lambda/4$) sobre o círculo $s$ (ponto diametralmente oposto). Em carta de admitâncias, $P_{cc}$ passa a ser o ponto à direita.

### 12. Quantas soluções de toco único existem? O que as distingue?
> [!success]- Resposta
> Duas (A e B): o círculo $s$ corta $g=1$ em dois pontos conjugados, com $y_s=\mp jb$. A soma das distâncias dos tocos curtos é $\lambda/2$; uma é indutiva e a outra capacitiva. Normalmente escolhe-se a de menor distância/comprimento.

### 13. Por que o transformador $\lambda/4$ só vale em uma banda estreita?
> [!success]- Resposta
> Porque $\ell=\lambda/4$ vale em uma só frequência; ao se afastar dela, $\beta\ell\neq90^\circ$ e a transformação deixa de ser exata. Para largura de banda maior usam-se várias seções em cascata.

### 14. Qual a condição para o transformador $\lambda/4$ casar uma carga complexa?
> [!success]- Resposta
> Só casa carga **real**. Para carga complexa é preciso primeiro anulá-la com um trecho de linha até um $V_{máx}$ ou $V_{mín}$ (onde $Z$ é real $= sZ_0$ ou $Z_0/s$), ou com um toco.

### 15. Num transitório, para que servem $\Gamma_G$ e $\Gamma_C$?
> [!success]- Resposta
> São os fatores de reflexão nas duas extremidades: $\Gamma_G=\dfrac{Z_g-Z_0}{Z_g+Z_0}$ e $\Gamma_C=\dfrac{Z_C-Z_0}{Z_C+Z_0}$. A cada ida e volta o degrau é multiplicado por $\Gamma_G\Gamma_C$; a soma geométrica leva a $V_\infty$. Para a **corrente**, os sinais trocam.

### 16. Linha com $Z_g=Z_0$: o que acontece no transitório?
> [!success]- Resposta
> $\Gamma_G=0$: a onda refletida na carga é absorvida no gerador, e o regime permanente chega após **uma ida e volta** ($2\ell/u$).

### 17. Por que a microfita tem $\varepsilon_{ef}<\varepsilon_r$?
> [!success]- Resposta
> Parte do campo está no ar acima da fita e parte no substrato; a onda se propaga em meio não homogêneo, e o modo é **quase-TEM**. Usa-se um dielétrico homogêneo equivalente com $\varepsilon_{ef}$ entre 1 e $\varepsilon_r$.

### 18. Em microfita, o que acontece com $Z_0$ se aumentamos $w$?
> [!success]- Resposta
> $Z_0$ **diminui** (mais capacitância); e $\varepsilon_{ef}$ aumenta, aproximando-se de $\varepsilon_r$.

## Checklist de estudo
Marque quando souber fazer **sem consultar**.

**Teoria**
- [ ] Deduzir as equações do telegrafista a partir do circuito de $\Delta z$
- [ ] Obter $\gamma$ e $Z_0$ e dizer quando são reais
- [ ] Reconhecer linha sem perdas e sem distorção e as condições
- [ ] Explicar $\Gamma$, $s$, $Z_{máx}$, $Z_{mín}$
- [ ] Explicar por que o sinal da corrente refletida é trocado

**Cálculo**
- [ ] $Z_{ent}$ com e sem perdas
- [ ] $\Gamma$, $s$ e posições de $V_{máx}$/$V_{mín}$
- [ ] Casos curto, aberto, casado, $\lambda/4$, $\lambda/2$
- [ ] Linhas em cascata e em paralelo (reduzir do fim para o início)
- [ ] Potência refletida e transmitida

**Carta de Smith**
- [ ] Marcar $z$ e ler $\Gamma$ e $s$
- [ ] Girar por distância ($720^\circ/\lambda$) nos dois sentidos
- [ ] Converter $z\leftrightarrow y$
- [ ] Linha fendida com a carta
- [ ] Toco único (as duas soluções)

**Casamento**
- [ ] Transformador $\lambda/4$ e em cascata
- [ ] Toco curto-circuitado e aberto

**Transitórios**
- [ ] $V_0^+$, $\Gamma_G$, $\Gamma_C$, diagrama de saltos
- [ ] Pulso de largura finita (superposição)
- [ ] $V_\infty$ e $I_\infty$

**Microfita**
- [ ] $\varepsilon_{ef}$ e $Z_0$ (os dois ramos de $w/h$)
- [ ] Projeto: $w/h$ a partir de $Z_0$
- [ ] $\alpha_c$, $\alpha_d$ e comprimento de onda guiado

## Armadilhas mais comuns
1. **Sentido de giro na carta.** Para o **gerador** = horário; para a **carga** = anti-horário. Trocar o sentido é o erro mais comum.
2. **$720^\circ$ vs $360^\circ$.** Na escala de comprimentos de onda, uma volta completa na carta é $\lambda/2$, ou seja, $720^\circ$ por $\lambda$. Gira-se $2\beta\ell$, não $\beta\ell$.
3. **Graus x radianos** no $\tan\beta\ell$. Confira a calculadora.
4. **$\tan$ de $\beta\ell\ge90^\circ$.** Reduza módulo $180^\circ$; em $90^\circ$ o $\tan$ não existe: use o atalho $\lambda/4$.
5. **Normalizar.** Divida por $Z_0$ antes de entrar na carta e **multiplique de volta** ao sair.
6. **Admitância na carta.** Ao trabalhar com $y$, o curto está à **direita** ($P_{cc}$) e o aberto à esquerda. O toco curto mede-se a partir de $P_{cc}$.
7. **ROE.** $s\ge1$ sempre. Se der menor que 1, inverteu $\Gamma$.
8. **Corrente refletida.** O coeficiente é $-\Gamma$, não $\Gamma$.
9. **$\lambda$ na linha.** $\lambda=u/f$, com $u=c/\sqrt{\varepsilon_r}$. Não use o $\lambda$ do ar numa linha com dielétrico.
10. **Linha fendida.** Reduza a distância ao plano da carga **pelo lado certo** (a escala da régua cresce para a carga ou para o gerador?). Veja a regra em [[EM2 LT - Fórmulas#Linha fendida]].
11. **Transitório com pulso curto.** Se $2t_1<$ duração do pulso, as reflexões **se sobrepõem**; some os degraus.
12. **$\Gamma_G$ e $\Gamma_C$.** $\Gamma_G=\dfrac{Z_g-Z_0}{Z_g+Z_0}$ usa a impedância do **gerador**; $\Gamma_C$ usa a da **carga**. Não troque.
13. **Microfita.** Cheque se $w/h\le1$ ou $\ge1$ antes de escolher a fórmula, e use $\sqrt{\varepsilon_{ef}}$ no $\beta$ e no $\lambda$.
14. **Unidades de atenuação.** 1 Np/m $=8{,}686$ dB/m.
15. **Arredondar cedo.** Mantenha 4 casas até o fim; erros de carta (±2%) já são suficientes.

## Erros de impressão no livro
Se o seu resultado difere do livro, confira esta lista **antes** de duvidar de si.

| Onde | O livro imprime | Provável correto |
|---|---|---|
| Eq. 11.71 (microfita, $w/h\le1$) | argumento do $\ln$ | $\dfrac{8h}{w}+\dfrac{w}{4h}$ |
| Eq. 11.72 (projeto, $A$) | $\sqrt{(\varepsilon_r-1)/2}$ | $\sqrt{(\varepsilon_r+1)/2}$ |
| Eq. 11.74 | $\beta=\omega/c$ sem a raiz | $\beta=\omega\sqrt{\varepsilon_{ef}}/c$ |
| Exemplo 11.10 | $Z_0=9{,}576\ \Omega$ | $30{,}08\ \Omega$ |
| Exemplo 11.11 | $\varepsilon_r+1=7{,}2$ | $7{,}6$ (afeta $\varepsilon_{ef}$, $Z_0$, $\alpha$) |
| Exemplo 11.9 | "$I=V/Z_0$" | usar $Z_C=100\ \Omega$ |
| EP 11.3 | $\beta=0{,}2094$ | $0{,}02094$ |
| EP 11.6 | "33,5 cm" | provavelmente $35{,}5$ cm |
| Revisão 11.6(i) | "D, B" | ver o seu exemplar |
| Revisão 11.1 | rótulo "(d)" repetido | numeração |

> [!tip] Como usar
> Se em prova o professor cobrar a fórmula **do livro** (com o erro), siga o que ele passou em aula. As fórmulas corretas estão em [[EM2 LT - Fórmulas#Microfita]].
