---
tags: [eletromagnetismo2, ufes, prova, formulas]
---
# EM2 LT - Fórmulas
← [[Eletromagnetismo 2]] · [[EM2 LT - Exercícios|Exercícios]] · [[EM2 LT - Revisão|Revisão]]

Capítulo 11, **Linhas de Transmissão** (Elementos de Eletromagnetismo, Sadiku). Os números entre parênteses, como (11.34), são as equações do livro. Notação do livro: $\operatorname{tgh}=\tanh$, $\operatorname{tg}=\tan$, $\operatorname{cotg}=\cot$, $\operatorname{sen}=\sin$.

Convenção: **$\ell$** é o comprimento da linha e **$\ell'$** é a distância medida **a partir da carga**, em direção ao gerador.

## Consulta rápida
As 12 que mais caem. O resto está nas seções abaixo.

| O que | Fórmula |
|---|---|
| Constante de propagação | $\gamma=\alpha+j\beta=\sqrt{(R+j\omega L)(G+j\omega C)}$ |
| Impedância característica | $Z_0=\sqrt{\dfrac{R+j\omega L}{G+j\omega C}}$ |
| Sem perdas | $Z_0=\sqrt{L/C}$, $\;u=1/\sqrt{LC}$, $\;\beta=\omega\sqrt{LC}$ |
| Sem distorção | $\dfrac RL=\dfrac GC$, $\;\alpha=\sqrt{RG}$, $\;Z_0=\sqrt{L/C}=\sqrt{R/G}$ |
| Coeficiente de reflexão na carga | $\Gamma_C=\dfrac{Z_C-Z_0}{Z_C+Z_0}$ |
| Ao longo da linha (sem perdas) | $\Gamma(\ell')=\Gamma_C\,e^{-j2\beta\ell'}$ |
| ROE | $s=\dfrac{1+\lvert\Gamma\rvert}{1-\lvert\Gamma\rvert}$, $\;\lvert\Gamma\rvert=\dfrac{s-1}{s+1}$ |
| Impedância de entrada (sem perdas) | $Z_{ent}=Z_0\dfrac{Z_C+jZ_0\tan\beta\ell}{Z_0+jZ_C\tan\beta\ell}$ |
| Curto / aberto | $Z_{cc}=jZ_0\tan\beta\ell$, $\;Z_{ca}=-jZ_0\cot\beta\ell$ |
| Transformador $\lambda/4$ | $Z_{ent}=Z_0^2/Z_C$, $\;Z_0'=\sqrt{Z_0Z_C}$ |
| Carta de Smith | $\Gamma=\dfrac{z-1}{z+1}$, $\;z=Z_C/Z_0$ |
| Transitório | $V_0=\dfrac{Z_0V_g}{Z_g+Z_0}$, $\;\Gamma_G=\dfrac{Z_g-Z_0}{Z_g+Z_0}$ |

## Sumário
1. [[#Parâmetros distribuídos]]
2. [[#Equações do telegrafista e propagação]]
3. [[#Linha sem perdas e sem distorção]]
4. [[#Impedância de entrada e coeficiente de reflexão]]
5. [[#Casos especiais]]
6. [[#Carta de Smith]]
7. [[#Casamento de impedâncias]]
8. [[#Linha fendida]]
9. [[#Transitórios]]
10. [[#Microfita]]
11. [[#Constantes e conversões]]

---

## Parâmetros distribuídos
$R$ ($\Omega$/m), $L$ (H/m), $G$ (S/m), $C$ (F/m): por unidade de comprimento. $R$ e $L$ são **em série**; $G$ e $C$ são **em paralelo**.

Profundidade de penetração (efeito pelicular):
$$\delta=\frac{1}{\sqrt{\pi f\mu\sigma_c}}$$

**Tabela 11.1**

| | Coaxial | Bifilar | Planar |
|---|---|---|---|
| $R$ | $\dfrac{1}{2\pi\delta\sigma_c}\left(\dfrac1a+\dfrac1b\right)$ | $\dfrac{1}{\pi a\delta\sigma_c}$ | $\dfrac{2}{w\delta\sigma_c}$ |
| $L$ | $\dfrac{\mu}{2\pi}\ln\dfrac ba$ | $\dfrac\mu\pi\cosh^{-1}\dfrac{d}{2a}$ | $\dfrac{\mu d}{w}$ |
| $G$ | $\dfrac{2\pi\sigma}{\ln(b/a)}$ | $\dfrac{\pi\sigma}{\cosh^{-1}(d/2a)}$ | $\dfrac{\sigma w}{d}$ |
| $C$ | $\dfrac{2\pi\varepsilon}{\ln(b/a)}$ | $\dfrac{\pi\varepsilon}{\cosh^{-1}(d/2a)}$ | $\dfrac{\varepsilon w}{d}$ |

- Coaxial: $a$ = raio interno, $b$ = raio externo. Bifilar: $a$ = raio dos fios, $d$ = distância entre centros. Planar: $w$ = largura, $d$ = separação.
- $\sigma_c$ é a condutividade **dos condutores** (entra em $R$); $\sigma$ e $\varepsilon$ são do **dielétrico** (entram em $G$ e $C$).
- Relações: $LC=\mu\varepsilon$ e $\dfrac GC=\dfrac\sigma\varepsilon$.
- O $L$ da tabela é o **externo**. O livro despreza o interno.
- $R$ depende da frequência (via $\delta$); $L$, $G$ e $C$ da tabela não.

## Equações do telegrafista e propagação
Domínio do tempo (11.4) e (11.6):
$$-\frac{\partial V}{\partial z}=RI+L\frac{\partial I}{\partial t}\qquad -\frac{\partial I}{\partial z}=GV+C\frac{\partial V}{\partial t}$$

Fasores (11.8) e (11.9):
$$-\frac{dV}{dz}=(R+j\omega L)I\qquad -\frac{dI}{dz}=(G+j\omega C)V$$

Equação de onda (11.10):
$$\frac{d^2V}{dz^2}-\gamma^2V=0,\qquad \gamma=\alpha+j\beta=\sqrt{(R+j\omega L)(G+j\omega C)}\quad(11.11)$$

Solução (11.15 a 11.17): onda **incidente** (+z) e **refletida** (−z):
$$V(z)=V_0^+e^{-\gamma z}+V_0^-e^{\gamma z},\qquad I(z)=\frac{V_0^+}{Z_0}e^{-\gamma z}-\frac{V_0^-}{Z_0}e^{\gamma z}$$

Impedância característica (11.18/11.19):
$$Z_0=\sqrt{\frac{R+j\omega L}{G+j\omega C}}=\frac{V_0^+}{I_0^+}=-\frac{V_0^-}{I_0^-}$$

No tempo:
$$V(z,t)=\lvert V_0^+\rvert e^{-\alpha z}\cos(\omega t-\beta z+\varphi^+)+\lvert V_0^-\rvert e^{\alpha z}\cos(\omega t+\beta z+\varphi^-)$$

| Grandeza | Fórmula |
|---|---|
| Comprimento de onda | $\lambda=\dfrac{2\pi}{\beta}$ |
| Velocidade de fase | $u=\dfrac{\omega}{\beta}=f\lambda$ |
| Atenuação | $1\ \text{Np}=8{,}686\ \text{dB}$ → $\alpha[\text{dB/m}]=8{,}686\,\alpha[\text{Np/m}]$ |
| Comprimento elétrico | $\beta\ell=\dfrac{2\pi\ell}{\lambda}$ (em rad); $\ell/\lambda\times360^\circ$ (em graus) |
| Tempo de trânsito | $t_1=\ell/u$ |

Relações úteis (inversas), de $Z_0$, $\alpha$ e $u$:
$$R=\alpha Z_0,\qquad G=\frac{\alpha^2}{R}=\frac{\alpha}{Z_0},\qquad L=\frac{Z_0}{u},\qquad C=\frac{1}{uZ_0}$$
(válidas para linha **sem distorção**, que é o caso do Exemplo 11.2.)

## Linha sem perdas e sem distorção
**Tabela 11.2**

| | Geral | Sem perdas ($R=G=0$) | Sem distorção ($R/L=G/C$) |
|---|---|---|---|
| $\gamma$ | $\sqrt{(R+j\omega L)(G+j\omega C)}$ | $j\omega\sqrt{LC}$ | $\alpha=\sqrt{RG}$ e $\beta=\omega\sqrt{LC}$ |
| $\alpha$ | $\mathrm{Re}(\gamma)$ | $0$ | $\sqrt{RG}$ |
| $\beta$ | $\mathrm{Im}(\gamma)$ | $\omega\sqrt{LC}$ | $\omega\sqrt{LC}$ |
| $Z_0$ | $\sqrt{\dfrac{R+j\omega L}{G+j\omega C}}$ | $\sqrt{L/C}$ | $\sqrt{L/C}=\sqrt{R/G}$ ($X_0=0$) |
| $u$ | $\omega/\beta$ | $1/\sqrt{LC}$ | $1/\sqrt{LC}$ |

- Sem distorção: $\dfrac RL=\dfrac GC\iff RC=GL$. $\alpha$ e $u$ **não dependem da frequência**, então o pulso não se deforma. Só atenua.
- Toda linha sem perdas é sem distorção. **A recíproca é falsa.**
- Altas frequências ($R\ll\omega L$, $G\ll\omega C$): a linha tende à sem perdas, $Z_0\approx\sqrt{L/C}$ e $\alpha\approx\dfrac R2\sqrt{\dfrac CL}+\dfrac G2\sqrt{\dfrac LC}$.

## Impedância de entrada e coeficiente de reflexão
Condições iniciais (11.27) e (11.28), com $V_0$ e $I_0$ em $z=0$ (entrada):
$$V_0^+=\tfrac12(V_0+Z_0I_0),\quad V_0^-=\tfrac12(V_0-Z_0I_0);\qquad V_0=\frac{Z_{ent}V_g}{Z_{ent}+Z_g},\quad I_0=\frac{V_g}{Z_{ent}+Z_g}$$

**Com perdas** (11.33):
$$Z_{ent}=Z_0\,\frac{Z_C+Z_0\tanh\gamma\ell}{Z_0+Z_C\tanh\gamma\ell}$$

**Sem perdas** (11.34):
$$Z_{ent}=Z_0\,\frac{Z_C+jZ_0\tan\beta\ell}{Z_0+jZ_C\tan\beta\ell}$$

**Coeficiente de reflexão** (tensão):
$$\Gamma_C=\frac{Z_C-Z_0}{Z_C+Z_0},\qquad \Gamma(\ell')=\Gamma_Ce^{-2\gamma\ell'}\ (11.37)$$
Sem perdas: $\Gamma(\ell')=\lvert\Gamma_C\rvert\,e^{j(\theta_\Gamma-2\beta\ell')}$. O módulo se mantém e a fase **diminui** ao se afastar da carga.
- Em qualquer ponto: $Z=Z_0\dfrac{1+\Gamma}{1-\Gamma}$.
- O coeficiente de reflexão da **corrente** é $-\Gamma$ (não o inverso).
- $\lvert\Gamma\rvert\le1$ para carga passiva. $\Gamma=-1$ curto, $\Gamma=+1$ aberto, $\Gamma=0$ casada.

**Onda estacionária**
$$s=\frac{1+\lvert\Gamma\rvert}{1-\lvert\Gamma\rvert}=\frac{V_{máx}}{V_{mín}}\ (11.38),\qquad 1\le s\le\infty$$
$$\lvert Z_{ent}\rvert_{máx}=sZ_0,\qquad \lvert Z_{ent}\rvert_{mín}=\frac{Z_0}{s}\ (11.39)$$
Nesses pontos a impedância é **puramente resistiva**.

**Posições de máximos e mínimos** (sem perdas, $\ell'\ge0$):
$$\ell'_{máx}=\frac{\theta_\Gamma+2n\pi}{2\beta},\qquad \ell'_{mín}=\frac{\theta_\Gamma+(2n+1)\pi}{2\beta}$$
- Máximos consecutivos: $\lambda/2$. Máximo a mínimo vizinho: $\lambda/4$.
- Se a carga tem $\theta_\Gamma=0$ (resistiva com $Z_C>Z_0$): há máximo **na própria carga**.
- Se $\theta_\Gamma=\pm\pi$ ($Z_C<Z_0$ resistiva): há mínimo **na carga**.

**Impedância de uma carga a partir de um mínimo** (usa-se no ensaio com linha fendida):
$$z_C=\frac{1-js\tan\beta\ell'_{mín}}{s-j\tan\beta\ell'_{mín}}$$

**Potência média** (11.40), linha sem perdas, valores de **pico** (por isso o $\tfrac12$; com valores rms, tire o $\tfrac12$):
$$P_{méd}=\frac{\lvert V_0^+\rvert^2}{2Z_0}\left(1-\lvert\Gamma\rvert^2\right)=P_i-P_r,\qquad P_i=\frac{\lvert V_0^+\rvert^2}{2Z_0},\quad P_r=\lvert\Gamma\rvert^2P_i$$
A potência é **constante ao longo da linha** (sem perdas) e máxima na carga quando $\Gamma=0$.

## Casos especiais
Linha sem perdas, comprimento $\ell$, $\beta\ell=2\pi\ell/\lambda$.

| Terminação | $Z_{ent}$ | $\Gamma$ | $s$ |
|---|---|---|---|
| **Curto** ($Z_C=0$) | $Z_{cc}=jZ_0\tan\beta\ell$ | $-1$ | $\infty$ |
| **Aberto** ($Z_C=\infty$) | $Z_{ca}=-jZ_0\cot\beta\ell$ | $+1$ | $\infty$ |
| **Casada** ($Z_C=Z_0$) | $Z_0$ | $0$ | $1$ |

$$Z_{cc}\,Z_{ca}=Z_0^2\ (11.43)\quad\Rightarrow\quad Z_0=\sqrt{Z_{cc}Z_{ca}}$$
(medir os dois e achar $Z_0$.)

**Curto-circuito** ($Z_{cc}=jZ_0\tan\beta\ell$):

| $\ell$ | $Z_{cc}$ | Comportamento |
|---|---|---|
| $0<\ell<\lambda/4$ | $+jX$ | indutivo |
| $\lambda/8$ | $+jZ_0$ | indutivo |
| $\lambda/4$ | $\infty$ (aberto) | "circuito aberto" |
| $\lambda/4<\ell<\lambda/2$ | $-jX$ | capacitivo |
| $3\lambda/8$ | $-jZ_0$ | capacitivo |
| $\lambda/2$ | $0$ | curto |

**Aberto**: o oposto. $\lambda/8\to-jZ_0$, $\lambda/4\to0$, $3\lambda/8\to+jZ_0$, $\lambda/2\to\infty$.

**Linhas especiais**
- $\ell=\lambda/2$ (ou múltiplo): $Z_{ent}=Z_C$. A linha é "transparente".
- $\ell=\lambda/4$ (ou $\lambda/4+n\lambda/2$): $Z_{ent}=\dfrac{Z_0^2}{Z_C}$ (11.56). Inverte a impedância.
- As condições se repetem a cada $\lambda/2$ ($Z_{ent}$, $\Gamma$, tensão e corrente em módulo).
- Carga indutiva vira capacitiva e vice-versa a cada $\lambda/4$.
- Cascata: calcule a **última seção primeiro** e use o resultado como carga da seção anterior.

## Carta de Smith
Impedância normalizada $z=Z/Z_0=r+jx$, e $y=1/z=g+jb$.
$$\Gamma=\frac{z-1}{z+1}\ (11.48),\qquad \Gamma=\Gamma_r+j\Gamma_i$$

**Círculos de resistência $r$ constante** (Tabela 11.3): centro $\left(\dfrac{r}{1+r},0\right)$, raio $\dfrac{1}{1+r}$.

**Círculos de reatância $x$ constante** (Tabela 11.4): centro $\left(1,\dfrac1x\right)$, raio $\dfrac1{\lvert x\rvert}$. $x>0$ (indutivo) fica no semiplano **superior**, $x<0$ (capacitivo) no **inferior**.

**Círculo de $s$ constante**: centro na origem, raio $\lvert\Gamma\rvert$. Cruza o eixo real positivo em $z=s$ (ponto $V_{máx}$) e o negativo em $z=1/s$ ($V_{mín}$).

**Pontos notáveis**

| Ponto | $z$ | $\Gamma$ | Posição |
|---|---|---|---|
| Centro | $1+j0$ | $0$ | casada |
| $P_{cc}$ | $0$ | $-1$ | esquerda do eixo real |
| $P_{ca}$ | $\infty$ | $+1$ | direita do eixo real |
| $V_{máx}$ | $s$ (real) | eixo $\Gamma_r$ positivo | |
| $V_{mín}$ | $1/s$ (real) | eixo $\Gamma_r$ negativo | a $\lambda/4$ do $V_{máx}$ |
| Topo / base da borda | $0\pm j1$ | $\pm90^\circ$ | indutivo em cima, capacitivo embaixo |

**Deslocamento**
- Uma volta completa = $\lambda/2$ (escala de $720^\circ$ para $\lambda$: $2\beta\ell'=720^\circ\,\ell'/\lambda$).
- **Sentido horário**: em direção ao **gerador**. **Anti-horário**: em direção à **carga**.
- $\lambda/4$ = meia volta ($180^\circ$): passa de $z$ para $1/z$, ou seja, **impedância ↔ admitância**.

**Receita 1: $Z_{ent}$ a partir de $Z_C$**
1. $z_C=Z_C/Z_0$. Marque na carta.
2. Trace o círculo $s$ (centro na origem, passando por $z_C$). Leia $s$ no eixo real à direita.
3. Gire **horário** $\ell/\lambda$ (use a escala "comprimentos de onda em direção ao gerador").
4. Leia $z_{ent}$ e desnormalize: $Z_{ent}=Z_0z_{ent}$.

**Receita 2: $Z_C$ a partir de $Z_{ent}$**: o mesmo, girando **anti-horário**.

**Receita 3: $Z_C$ a partir de $s$ e do primeiro $V_{mín}$** ($\ell'_{mín}$):
1. Círculo $s$; no eixo real **à esquerda** está $V_{mín}$ ($z=1/s$).
2. Gire **anti-horário** $\ell'_{mín}/\lambda$ (em direção à carga).
3. Leia $z_C$.

**Receita 4: $V_{máx}$ e $V_{mín}$ a partir de $Z_C$**: gire horário do ponto $z_C$ até o eixo real. Direita = $V_{máx}$, esquerda = $V_{mín}$. A distância girada, em $\lambda$, é a posição.

**Receita 5: admitância**: gire $180^\circ$ ($\lambda/4$) sobre o mesmo círculo $s$.

## Casamento de impedâncias
**Objetivo**: eliminar a onda refletida entre a fonte e o dispositivo de casamento. Depois do dispositivo, a linha **casada** tem $s=1$.

### Transformador de $\lambda/4$
Linha de comprimento $\lambda/4$ e impedância $Z_0'$ entre a linha ($Z_0$) e uma carga **real** $Z_C$:
$$Z_{ent}=\frac{Z_0'^2}{Z_C}\ (11.56),\qquad Z_0'=\sqrt{Z_0Z_C}\ (11.58)$$
- Casa só **na frequência de projeto** (banda estreita). Fora dela $\lambda/4$ deixa de valer.
- Carga complexa: coloque o transformador no ponto da linha onde a impedância é **real** ($V_{máx}$ com $sZ_0$ ou $V_{mín}$ com $Z_0/s$). *(Técnica padrão, não está no livro nesta forma.)*
- **Duas seções em cascata**: $Z_{ent}=\dfrac{Z_{01}^2}{Z_{02}^2/Z_C}$, e a condição de casamento é $Z_0=\dfrac{Z_{01}^2\,Z_C}{Z_{02}^2}$.

### Toco único em paralelo (curto-circuitado)
Idéia: num ponto da linha a **admitância é $y=1+jb$**; o toco acrescenta $y_s=-jb$ e a soma vira $y=1$ (casada).

**Receita (Smith)**
1. $z_C\to$ marque; gire $180^\circ$ para obter $y_C$ (ou use $y_C=1/z_C$ e marque direto).
2. Trace o círculo $s$.
3. Gire **horário** (em direção ao gerador) até cruzar o círculo $g=1$. Há **duas soluções**, A e B, em $y=1\pm jb$.
4. $\ell_A$, $\ell_B$ = distância da carga até cada cruzamento, em $\lambda$.
5. Susceptância do toco: $y_s=-jb$ em cada caso (sinal oposto).
6. Comprimento do toco curto-circuitado: parta de $P_{cc}$ (o ponto de **curto**, $y=\infty$; na carta usada como admitância ele fica à **direita**, como na Figura 11.24 do livro) e gire **horário** até $y_s$. A distância girada é $d$.

**Fórmula para o comprimento do toco** (curto, $Z_0$ igual ao da linha):
$$y_s=-j\cot\beta d\quad\Rightarrow\quad d=\frac{\lambda}{2\pi}\arctan\!\left(\frac{-1}{b_s}\right)\ \ (\text{somar }\lambda/2\text{ se negativo}),\quad b_s=\mathrm{Im}\,y_s$$
- $b_s<0$ (toco **indutivo**) → $d<\lambda/4$. $b_s>0$ (capacitivo) → $d>\lambda/4$.
- Uma solução A e outra B: $d_A+d_B=\lambda/2$.
- Admitância normalizada → real: $Y=y\,Y_0$, com $Y_0=1/Z_0$.
- **Toco aberto**: $y_s=+j\tan\beta d$. O comprimento difere em $\lambda/4$.
- Escolha em geral o **menor** comprimento total.

**ROE em cada parte do sistema** (Exemplo 11.7d):
- entre o toco e a carga: $s$ **da carga** (não muda);
- do toco para o gerador: $s=1$ (linha casada);
- no toco (curto-circuitado): $s=\infty$.

## Linha fendida
Linha com uma fenda e uma sonda móvel com detector: mede $V$ ao longo da linha.

**Mede-se**: $s=V_{máx}/V_{mín}$; $\lambda$ (dobro da distância entre dois mínimos consecutivos: $\lambda=2\,\Delta x_{mín}$); $f=u/\lambda$; e a posição do $V_{mín}$.

**Para achar $Z_C$**
1. Meça $s$ com a carga ligada.
2. Marque as posições dos $V_{mín}$ com a carga.
3. Troque a carga por um **curto**; marque as novas posições dos $V_{mín}$ (equivalem a múltiplos de $\lambda/2$ do plano da carga).
4. $\ell'$ = distância, **em direção ao gerador**, do $V_{mín}$ com o curto até o $V_{mín}$ com a carga (tome o valor entre $0$ e $\lambda/2$). Esse $\ell'$ é a distância do **$V_{mín}$ ao plano da carga**.
5. Na carta: círculo $s$, ponto $V_{mín}$ (esquerda, $z=1/s$), gire **anti-horário** $\ell'/\lambda$, leia $z_C$. Ou use a fórmula de $z_C$ da seção anterior.

**Em termos de leitura da régua** ($x$):
- régua que cresce **em direção à carga** (Fig. 11.21 do livro): $\ell'=x_{curto}-x_{carga}$ (módulo $\lambda/2$). Exemplo 11.6: mínimos em 19 cm (carga) e 24 cm (curto) dão $\ell'=5$ cm.
- régua que cresce **em direção ao gerador** (distâncias medidas "a partir da carga"): $\ell'=x_{carga}-x_{curto}$. Problema 11.45: 14 cm e 10,8 cm dão $\ell'=3{,}2$ cm.

O mesmo vale com **$V_{máx}$** (o Exercício Prático 11.6 dá posições de máximos): o deslocamento entre o máximo com a carga e o máximo com o curto é igual ao dos mínimos. Mas o curto tem **mínimo** no plano da carga, então o máximo do curto está $\lambda/4$ adiante: some $\lambda/4$ ao ler a posição do plano da carga.

## Transitórios
Linha sem perdas, com chave que fecha em $t=0$. Fonte $V_g$ com $Z_g$, linha $Z_0$ e $\ell$, carga $Z_C$.

| Grandeza | Fórmula |
|---|---|
| Onda inicial | $I_0=\dfrac{V_g}{Z_g+Z_0}$, $\;V_0=\dfrac{Z_0V_g}{Z_g+Z_0}$ |
| Tempo de trânsito | $t_1=\ell/u$ |
| Reflexão na carga | $\Gamma_C=\dfrac{Z_C-Z_0}{Z_C+Z_0}$ |
| Reflexão no gerador | $\Gamma_G=\dfrac{Z_g-Z_0}{Z_g+Z_0}$ |
| Na carga, 1ª chegada | $V(\ell,t_1)=(1+\Gamma_C)V_0$, $\;I(\ell,t_1)=(1-\Gamma_C)I_0$ |
| Regime permanente | $V_\infty=\dfrac{V_gZ_C}{Z_g+Z_C}$, $\;I_\infty=\dfrac{V_g}{Z_g+Z_C}$ |
| Transmissão | $\tau_C=1+\Gamma_C=\dfrac{2Z_C}{Z_C+Z_0}$ |

- **Corrente** reflete com $-\Gamma$. Em cada ponto, $I=V/Z_0$ para onda incidente e $I=-V/Z_0$ para refletida (e $I=V/Z_C$ **no extremo**, para a carga resistiva).
- $V_\infty=V_0\,\dfrac{1+\Gamma_C}{1-\Gamma_G\Gamma_C}$. Serve para conferir o diagrama.
- Casos: $Z_C=0$ ⇒ $\Gamma_C=-1$ ($V=0$ na carga); $Z_C=\infty$ ⇒ $\Gamma_C=+1$ ($V$ dobra: $\tau_C=2$); $Z_C=Z_0$ ⇒ $\Gamma_C=0$ (sem reflexão; $\tau_C=1$).

**Diagrama de saltos** (bounce diagram)
1. Eixo horizontal: posição ($0$ gerador a $\ell$ carga). Eixo vertical: tempo (para baixo).
2. Linhas inclinadas de inclinação $u$: cada uma é uma onda que chega à outra ponta após $t_1$.
3. Em cada ponta, a onda refletida = $\Gamma\times$ onda incidente.
4. **Tensão num ponto** em um instante = **soma** de todas as ondas que já passaram por ali. **Corrente** = soma com sinais conforme o sentido (ou aplique $I=\sum$ com reflexão $-\Gamma$).

**Pulso retangular de duração $T$**: as ondas existem só durante $T$. Some os pulsos que se **sobrepõem** em cada instante.

**Cada ponta do diagrama**: $V(0,t)$ na entrada muda a cada $2t_1$; $V(\ell,t)$ na carga muda a cada $2t_1$, com defasagem de $t_1$.

## Microfita
Fita condutora de largura $w$ sobre substrato de espessura $h$ e $\varepsilon_r$; plano de terra embaixo. O campo está parte no dielétrico, parte no ar, e por isso se usa a **permissividade efetiva**.

$$\varepsilon_{ef}=\frac{\varepsilon_r+1}{2}+\frac{\varepsilon_r-1}{2}\frac{1}{\sqrt{1+12h/w}}\quad(11.70),\qquad 1<\varepsilon_{ef}<\varepsilon_r$$

**Impedância característica** (11.71)

$$\frac wh\le1:\quad Z_0=\frac{60}{\sqrt{\varepsilon_{ef}}}\ln\!\left(\frac{8h}{w}+\frac{w}{4h}\right)$$
$$\frac wh\ge1:\quad Z_0=\frac{120\pi}{\sqrt{\varepsilon_{ef}}\,\left[\dfrac wh+1{,}393+0{,}667\ln\!\left(\dfrac wh+1{,}444\right)\right]}$$

> [!warning] Erro de impressão no livro
> A primeira expressão de (11.71) vem impressa com $w/h$ dentro do logaritmo. A forma correta é $\dfrac{w}{4h}$, e é a que o Exemplo 11.11 realmente usa.

**Projeto** (dado $Z_0$ e $\varepsilon_r$, achar $w/h$), (11.72):
$$A=\frac{Z_0}{60}\sqrt{\frac{\varepsilon_r+1}{2}}+\frac{\varepsilon_r-1}{\varepsilon_r+1}\left(0{,}23+\frac{0{,}11}{\varepsilon_r}\right),\qquad B=\frac{60\pi^2}{Z_0\sqrt{\varepsilon_r}}$$
$$\frac wh=\frac{8e^A}{e^{2A}-2}\quad(w/h<2)$$
$$\frac wh=\frac2\pi\left\{B-1-\ln(2B-1)+\frac{\varepsilon_r-1}{2\varepsilon_r}\left[\ln(B-1)+0{,}39-\frac{0{,}61}{\varepsilon_r}\right]\right\}\quad(w/h>2)$$
Use a primeira, confira se $w/h<2$; se não, use a segunda.

> [!warning] Erros de impressão no livro (eq. 11.72 e 11.74)
> - Em $A$, o livro imprime $\sqrt{(\varepsilon_r-1)/2}$. A forma correta (padrão da literatura) é $\sqrt{(\varepsilon_r+1)/2}$, e é a que reproduz o projeto de 50 Ω do Problema 11.52 ($w/h\approx1{,}85$ para $\varepsilon_r=4{,}6$). Com o sinal impresso sairia $\approx2{,}6$.
> - Em 11.74 o livro imprime $\beta=\omega\varepsilon_{ef}/c$ e $u=c/\varepsilon_{ef}$, sem a raiz. O correto é com $\sqrt{\varepsilon_{ef}}$, como acima ($\lambda=c/(f\sqrt{\varepsilon_{ef}})$ é o que os Exemplos 11.10 e 11.11 usam).
> - Em prova, **confira com o seu professor** qual forma ele quer. Em dúvida, use as corretas.

**Propagação**: $u=\dfrac{c}{\sqrt{\varepsilon_{ef}}}$, $\;\beta=\dfrac{\omega\sqrt{\varepsilon_{ef}}}{c}$, $\;\lambda=\dfrac{c}{f\sqrt{\varepsilon_{ef}}}$

**Perdas** (11.75 a 11.77)
$$\alpha_c=8{,}686\,\frac{R_s}{wZ_0}\ \text{dB/m},\qquad R_s=\frac1{\sigma_c\delta}=\sqrt{\frac{\pi f\mu_0}{\sigma_c}}\ (\Omega)$$
$$\alpha_d=27{,}3\,\frac{(\varepsilon_{ef}-1)\,\varepsilon_r}{(\varepsilon_r-1)\,\varepsilon_{ef}}\,\frac{\tan\theta}{\lambda}\ \text{dB/m},\qquad \alpha=\alpha_c+\alpha_d$$
- $\tan\theta$ é a **tangente de perdas** do substrato e $\lambda$ é o comprimento de onda **na linha**.
- $\alpha_c$ (condutor) cresce com $\sqrt f$. $\alpha_d$ (dielétrico) cresce com $f$.
- Distância para queda de $N$ dB: $d=N/\alpha$ (em dB/m).
- Deslocamento de fase de $\phi$ graus: $\ell=\dfrac{\phi}{360^\circ}\lambda$.

## Constantes e conversões
| | Valor |
|---|---|
| $c$ | $3\times10^8$ m/s |
| $\mu_0$ | $4\pi\times10^{-7}$ H/m |
| $\varepsilon_0$ | $\dfrac{10^{-9}}{36\pi}\approx8{,}854\times10^{-12}$ F/m |
| $\eta_0$ | $\approx120\pi\ \Omega$ |
| $1\ \text{Np}$ | $8{,}686$ dB |
| $\lambda=c/f$ no ar | $f=300$ MHz → 1 m; $f=1$ GHz → 30 cm |
| $\lambda$ na linha | $\lambda=u/f$, $\;u=c/\sqrt{\varepsilon_r}$ no dielétrico homogêneo |
| $dB$ → razão de tensão | $20\log_{10}(V_1/V_2)$ |

**Atalhos de cálculo**
- $\tan\beta\ell$ com $\ell=\lambda/8$: $1$. $\ell=\lambda/6$: $\sqrt3$. $\ell=\lambda/12$: $1/\sqrt3$.
- $\ell/\lambda\times360^\circ$ dá $\beta\ell$ em graus.
- Mais de $\lambda/2$: subtraia múltiplos de $\lambda/2$ antes de usar $\tan\beta\ell$.

Para a visão de conjunto, veja a [[EM2 LT - Revisão|Revisão]]. Para aplicar as fórmulas, veja os [[EM2 LT - Exercícios|Exercícios]].
