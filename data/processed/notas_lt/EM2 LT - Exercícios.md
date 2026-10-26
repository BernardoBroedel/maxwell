---
tags: [eletromagnetismo2, ufes, prova, exercicios]
---
# EM2 LT - Exercícios
← [[Eletromagnetismo 2]] · [[EM2 LT - Fórmulas|Fórmulas]] · [[EM2 LT - Revisão|Revisão]]

Capítulo 11, **Linhas de Transmissão**. Os exercícios são do próprio capítulo: exemplos resolvidos, exercícios práticos e problemas do fim do capítulo.

## Como usar
1. Leia o enunciado e **tente sozinho** antes de abrir a resposta (cada resposta fica dobrada).
2. Marque o checkbox quando resolver sem consultar.
3. Se errar, anote o motivo na linha de baixo e volte na [[EM2 LT - Revisão#Armadilhas mais comuns|lista de armadilhas]].

> [!info] De onde vêm as respostas
> - **(livro)**: resposta ou valor impresso no capítulo. Os valores lidos em carta de Smith são aproximados (±2%).
> - **(calculado)**: os problemas do fim do capítulo **não têm gabarito** no trecho que recebi. Essas respostas são **cálculos meus**, conferidos numericamente, e não o gabarito do livro. Compare com o do seu professor.
> - Onde o livro tem erro de impressão ou arredondamento, está marcado com ⚠️.

## Sumário
1. [[#Exemplos resolvidos do capítulo]]
2. [[#Problemas: parâmetros e propagação]]
3. [[#Problemas: reflexão, ROE e impedância de entrada]]
4. [[#Problemas: medidas na linha e linha fendida]]
5. [[#Problemas: casamento de impedâncias]]
6. [[#Problemas: transitórios]]
7. [[#Problemas: microfita]]
8. [[#Demonstrações]]
9. [[#Simulado sugerido]]

---

## Exemplos resolvidos do capítulo
Cada exemplo tem o enunciado, o caminho de solução e os valores. Os **Exercícios Práticos (EP)** vêm logo depois, para treinar a mesma ideia.

### Exemplo 11.1
- [ ] Resolvi sozinho

Linha **no ar**, $Z_0=70\ \Omega$, $\beta=3$ rad/m a 100 MHz. Calcule $L$ e $C$ por metro.

> [!success]- Solução
> Linha no ar ⇒ sem perdas: $Z_0=\sqrt{L/C}$ e $\beta=\omega\sqrt{LC}$. Dividindo: $\dfrac{Z_0}{\beta}=\dfrac{1}{\omega C}$.
> $$C=\frac{\beta}{\omega Z_0}=\frac{3}{2\pi\cdot10^8\cdot70}=68{,}2\ \text{pF/m},\qquad L=Z_0^2C=334{,}2\ \text{nH/m}$$

**EP 11.1**: 500 MHz, $Z_0=80\ \Omega$, $\alpha=0{,}04$ Np/m, $\beta=1{,}5$ rad/m. Ache $R$, $L$, $G$, $C$.

> [!success]- Resposta (livro)
> $R=3{,}2\ \Omega$/m, $L=38{,}2$ nH/m, $G=5\times10^{-4}$ S/m, $C=5{,}97$ pF/m.
> Caminho (usa $Z_0$ real, ou seja, linha sem distorção): $R=\alpha Z_0$, $G=\alpha/Z_0$, $u=\omega/\beta$, $L=Z_0/u$, $C=1/(uZ_0)$.

### Exemplo 11.2
- [ ] Resolvi sozinho

Linha **sem distorção**, $Z_0=60\ \Omega$, $\alpha=20$ mNp/m, $u=0{,}6c$. Ache $R$, $L$, $G$, $C$ e $\lambda$ em 100 MHz.

> [!success]- Solução
> $R=\alpha Z_0=1{,}2\ \Omega$/m; $L=Z_0/u=333$ nH/m; $G=\alpha^2/R=333\ \mu$S/m; $C=1/(uZ_0)=92{,}59$ pF/m; $\lambda=u/f=1{,}8$ m.

**EP 11.2**: linha telefônica com $R=30\ \Omega$/km, $L=100$ mH/km, $G=0$, $C=20\ \mu$F/km, a 1 kHz. Ache $Z_0$, $\gamma$ e $u$.

> [!success]- Resposta (livro)
> $Z_0=70{,}75\angle-1{,}367^\circ\ \Omega$; $\gamma=2{,}121\times10^{-4}+j8{,}888\times10^{-3}$ /m; $u=7{,}069\times10^{5}$ m/s.

### Exemplo 11.3
- [ ] Resolvi sozinho

Linha com $\omega=10^6$ rad/s, $\alpha=8$ dB/m, $\beta=1$ rad/m, $Z_0=60+j40\ \Omega$, comprimento 2 m. Fonte $10\angle0^\circ$ V, $Z_g=40\ \Omega$, carga $20+j50\ \Omega$. Ache (a) $Z_{ent}$, (b) a corrente na entrada, (c) a corrente no meio da linha.

> [!success]- Solução
> $\alpha=8/8{,}686=0{,}921$ Np/m; $\gamma\ell=2(0{,}921+j1)=1{,}84+j2$. Use $\tanh\gamma\ell=1{,}033-j0{,}03929$ em (11.33):
> (a) $Z_{ent}=60{,}25+j38{,}79\ \Omega$.
> (b) $I_0=\dfrac{10}{Z_{ent}+Z_g}=93{,}03\angle-21{,}15^\circ$ mA.
> (c) $V_0=Z_{ent}I_0=6{,}667\angle11{,}62^\circ$ V; $V_0^+=\tfrac12(V_0+Z_0I_0)=6{,}687\angle12{,}08^\circ$ V; $V_0^-=\tfrac12(V_0-Z_0I_0)$. Em $z=\ell/2$ use $I=\dfrac{V_0^+}{Z_0}e^{-\gamma z}-\dfrac{V_0^-}{Z_0}e^{\gamma z}$, **com $\beta z=1$ rad $=57{,}3^\circ$**: $I(\ell/2)\approx35\angle281^\circ$ mA.
>
> ⚠️ O livro imprime $V_0^-=0{,}0518\angle260^\circ$ V e $I(\ell/2)=35{,}10\angle281^\circ$ mA. Recalculando saiu $V_0^-\approx0{,}0575\angle260{,}5^\circ$ V e $I(\ell/2)\approx34{,}9\angle-79{,}1^\circ$ mA (o mesmo ângulo, $281^\circ$). É diferença de arredondamento, e o roteiro é o mesmo.

**EP 11.3**: linha de 40 m, $V_g=15\angle0^\circ$ V rms, $Z_0=30+j60\ \Omega$, $V_L=5\angle-48^\circ$ V rms, **casada** com a carga. Ache (a) $Z_{ent}$, (b) $I_{ent}$ e $V_{ent}$, (c) $\gamma$.

> [!success]- Resposta (livro)
> (a) $30+j60\ \Omega$ (casada ⇒ $Z_{ent}=Z_0$). (b) $0{,}112\angle-63{,}43^\circ$ A e $7{,}5\angle0^\circ$ V rms. (c) $\gamma=0{,}0101+j0{,}2094$ /m.
>
> Caminho de (c): casada ⇒ $V_L=V_{ent}e^{-\gamma\ell}$. Módulo: $e^{-\alpha\ell}=5/7{,}5\Rightarrow\alpha=\ln1{,}5/40=0{,}0101$. Fase: $\beta\ell=48^\circ$ ⇒ $\beta=0{,}02094$ rad/m.
> ⚠️ O livro imprime $\beta=0{,}2094$. Isso parece **erro de impressão** (faltou um zero): $48^\circ/40$ m $=0{,}8378$ rad $/40=0{,}02094$ rad/m (tomando $n=0$).

### Exemplo 11.4
- [ ] Resolvi sozinho

Linha sem perdas de 30 m, $Z_0=50\ \Omega$, 2 MHz, $u=0{,}6c$, carga $60+j40\ \Omega$. Ache (a) $\Gamma$, (b) $s$, (c) $Z_{ent}$.

> [!success]- Solução
> (a) $\Gamma=\dfrac{10+j40}{110+j40}=0{,}3523\angle56^\circ$. (b) $s=\dfrac{1+0{,}3523}{1-0{,}3523}=2{,}088$.
> (c) $\beta\ell=\dfrac{\omega\ell}{u}=120^\circ$ ⇒ $Z_{ent}=23{,}97+j1{,}35\ \Omega=24{,}01\angle3{,}22^\circ$.
> **Carta de Smith**: $z_C=1{,}2+j0{,}8$; $\lambda=u/f=90$ m, $\ell=\lambda/3$ ⇒ $240^\circ$ **horário** (escala de $720^\circ$ por $\lambda$) ⇒ $z_{ent}=0{,}47+j0{,}035$ ⇒ $Z_{ent}\approx23{,}5+j1{,}75\ \Omega$ (livro, aproximado).

**EP 11.4**: lossless, $Z_0=70\ \Omega$, $s=1{,}6$, $\theta_\Gamma=300^\circ$, $\ell=0{,}6\lambda$. Ache (a) $\Gamma$, $Z_C$, $Z_{ent}$; (b) a distância do primeiro mínimo de tensão à carga.

> [!success]- Resposta (livro)
> (a) $\Gamma=0{,}228\angle300^\circ$, $Z_C=80{,}5-j33{,}6\ \Omega$, $Z_{ent}=47{,}6-j17{,}5\ \Omega$. (b) $\lambda/6$.
> Caminho de (b): $\ell'_{mín}=\dfrac{\theta_\Gamma+180^\circ}{720^\circ}\lambda=\dfrac{300^\circ-360^\circ+180^\circ}{720^\circ}\lambda=\dfrac{120^\circ}{720^\circ}\lambda$.

### Exemplo 11.5
- [ ] Resolvi sozinho

Carga $100+j150\ \Omega$ em linha sem perdas de 75 Ω. Ache (a) $\Gamma$; (b) $s$; (c) a admitância da carga $Y_L$; (d) $Z_{ent}$ a $0{,}4\lambda$ da carga; (e) a localização de $V_{máx}$ e $V_{mín}$ se a linha tem $0{,}6\lambda$; (f) $Z_{ent}$ no gerador.

> [!success]- Solução
> (a) $\Gamma=0{,}659\angle40^\circ$. (b) $s=4{,}865$ (carta: 4,82).
> (c) $Y_C=\dfrac{1}{100+j150}=3{,}07-j4{,}62$ mS (carta: $y_C=0{,}228-j0{,}35$, $3{,}04-j4{,}67$ mS).
> (d) $0{,}4\lambda\to288^\circ$ horário ⇒ $Z_{ent}=21{,}9+j47{,}6\ \Omega$ (carta: $22{,}5+j47{,}25$).
> (e) $0{,}6\lambda=432^\circ$ = 1 volta + $72^\circ$. Primeiro $V_{máx}$ em $\dfrac{40^\circ}{720^\circ}\lambda=0{,}055\lambda$; segundo em $0{,}555\lambda$; único $V_{mín}$ em $0{,}055\lambda+\lambda/4=0{,}3055\lambda$.
> (f) $Z_{ent}\approx135-j165\ \Omega$ (carta: $z=1{,}8-j2{,}2$; exato $133{,}6-j165{,}7$).

**EP 11.5**: $Z_0=60\ \Omega$, carga $60+j60\ \Omega$. (a) $\Gamma$ e $s$; se $Z_{ent}=120-j60\ \Omega$, qual a distância (em $\lambda$) entre gerador e carga? **Sem carta.** (b) Refaça com a carta; ache $Z_{máx}$, $Z_{mín}$ e a distância ao primeiro $V_{máx}$.

> [!success]- Resposta (livro)
> (a) $\Gamma=0{,}4472\angle63{,}43^\circ$, $s=2{,}618$, distância $\dfrac\lambda8(1+4n)$, $n=0,1,2,\dots$
> (b) pela carta: $\Gamma\approx0{,}4457\angle62^\circ$, $s\approx2{,}612$, $Z_{máx}=157{,}1\ \Omega$, $Z_{mín}=22{,}92\ \Omega$, primeiro $V_{máx}$ em $\approx0{,}0861\lambda$.
> (calculado) O valor exato do primeiro $V_{máx}$ é $63{,}43^\circ/720^\circ=0{,}0881\lambda$; a diferença é erro de leitura da carta.

### Exemplo 11.6 (linha fendida)
- [ ] Resolvi sozinho

Linha fendida no ar, carga desconhecida, $s=2$. Mínimos de tensão em 11 cm, 19 cm, ... Com **curto** os mínimos passam a 16 cm, 24 cm, ... $Z_0=50\ \Omega$. Ache $\lambda$, $f$ e $Z_C$.

> [!success]- Solução
> $\lambda/2=19-11=8$ cm ⇒ $\lambda=16$ cm; $f=c/\lambda=1{,}875$ GHz.
> O plano da carga fica num dos mínimos com curto (24 cm). $\ell=24-19=5$ cm $=0{,}3125\lambda$ ⇒ $225^\circ$ **anti-horário** (em direção à carga) a partir do $V_{mín}$ sobre o círculo $s=2$ ⇒ $z_C=1{,}4+j0{,}75$ ⇒ $Z_C=70+j37{,}5\ \Omega$ (livro; exato $69{,}5+j36{,}8\ \Omega$).

**EP 11.6**: linha fendida de 50 Ω. Com carga, $s=1{,}8$ e $V_{máx}$ em 23 cm, 33,5 cm, ...; com curto, $s=\infty$ e $V_{máx}$ em 25 cm, 37,5 cm, ... Ache $Z_C$.

> [!success]- Resposta
> (livro) $Z_C=32{,}5-j17{,}5\ \Omega$.
> ⚠️ O enunciado imprime "33,5 cm", mas o curto dá $\lambda/2=37{,}5-25=12{,}5$ cm, então o certo é provavelmente **35,5 cm** ($35{,}5-23=12{,}5$). Assim $\lambda=25$ cm.
> (calculado) Com $\lambda=25$ cm, o máximo da carga está 2 cm antes do máximo do curto; como o curto tem mínimo no plano da carga, $\ell'=2+\lambda/4=8{,}25$ cm do plano da carga, e $z_C=\dfrac{s-j\tan\beta\ell'}{1-js\tan\beta\ell'}=0{,}66-j0{,}35$ ⇒ $Z_C\approx33{,}1-j17{,}4\ \Omega$. Bate com o livro, a menos da precisão da carta.

### Exemplo 11.7 (toco único)
- [ ] Resolvi sozinho

Antena de $40+j30\ \Omega$ para linha sem perdas de 100 Ω com **toco curto-circuitado**. Ache (a) a admitância necessária do toco, (b) a distância do toco à antena, (c) o comprimento do toco, (d) a ROE em cada parte do sistema.

> [!success]- Solução
> $z_C=0{,}4+j0{,}3$; $y_C=1/z_C=1{,}6-j1{,}2$. O círculo $s$ corta $g=1$ em dois pontos, A e B:
> | | $\ell$ (carga→toco) | $y_s$ | $d$ do toco |
> |---|---|---|---|
> | **A** (livro) | $0{,}36\lambda$ | $-j1{,}04$ ($-j10{,}4$ mS) | $0{,}1222\lambda$ |
> | **B** (livro) | $0{,}032\lambda$ | $+j1{,}04$ ($+j10{,}4$ mS) | $0{,}3778\lambda$ |
>
> Note: $d_A+d_B=0{,}5\lambda$ ✔️. O toco curto usa $d$ medido a partir de $P_{cc}$.
> (d) $s\approx2{,}7$ entre o toco e a carga; $s=1$ do toco para o gerador; $s=\infty$ no toco.
>
> (calculado, exato) $s=2{,}763$; A: $\ell=0{,}3601\lambda$, $y_s=-j1{,}0607$ ($-j10{,}6$ mS), $d=0{,}1203\lambda$; B: $\ell=0{,}0325\lambda$, $y_s=+j1{,}0607$, $d=0{,}3797\lambda$. Os valores do livro são de leitura de carta.

**EP 11.7**: linha de 75 Ω, carga $100-j80\ \Omega$, toco curto. Ache comprimento do toco, distância à carga e admitância.

> [!success]- Resposta (livro)
> $\ell_A=0{,}093\lambda$, $\ell_B=0{,}272\lambda$ (distâncias à carga), $d_A=0{,}126\lambda$, $d_B=0{,}374\lambda$ (comprimentos de toco), $\pm j12{,}67$ mS.
> (calculado, exato) $\ell=0{,}0941\lambda$ e $0{,}2724\lambda$; toco $0{,}1276\lambda$ e $0{,}3724\lambda$; $12{,}9$ mS.

### Exemplo 11.8 (transitório, degrau)
- [ ] Resolvi sozinho

Bateria de 12 V com 100 Ω, linha de 50 Ω, $u=10^8$ m/s, 100 m, carga 200 Ω. Chave fecha em $t=0$. Ache a tensão e a corrente nas duas extremidades.

> [!success]- Solução
> $t_1=\ell/u=1\ \mu$s; $V_0=\dfrac{50}{150}(12)=4$ V; $I_0=V_0/Z_0=80$ mA; $\Gamma_G=\dfrac13$, $\Gamma_C=\dfrac35$.
> | $t$ | $V(\ell,t)$ (carga) | $V(0,t)$ (gerador) |
> |---|---|---|
> | $<1\ \mu$s | 0 | 4 V |
> | $1\ \mu$s | $4+2{,}4=6{,}4$ | |
> | $2\ \mu$s | | $4+2{,}4+0{,}8=7{,}2$ |
> | $3\ \mu$s | $6{,}4+0{,}8+0{,}48=7{,}68$ | |
> | $4\ \mu$s | | $7{,}84$ |
> | $5\ \mu$s | $7{,}936$ | |
> | $6\ \mu$s | | $7{,}968$ |
> | $\infty$ | $V_\infty=\dfrac{200}{300}12=8$ V | 8 V |
>
> Correntes: $I(0,t)=80,\ 48,\ 41{,}6,\ 40{,}32,\dots\to40$ mA; $I(\ell,t)=V(\ell,t)/Z_C=0,\ 32,\ 38{,}4,\ 39{,}68,\dots\to40$ mA. $I_\infty=\dfrac{12}{300}=40$ mA.
> Reflexão da **corrente**: $-\Gamma_G=-\tfrac13$ e $-\Gamma_C=-\tfrac35$.

**EP 11.8**: repita para a linha (a) em **curto**, (b) em **aberto**.

> [!success]- Resposta (livro, Figuras 11.33 e 11.34, valores lidos)
> **(a) curto** ($\Gamma_C=-1$): $V(\ell,t)=0$ sempre; $V(0,t)=4$ V (até 2 µs), $-4/3$ V (2–4 µs), $4/9$ V (4–6 µs), $\dots\to0$. $I(\ell,t)$: 0, depois $160$ mA (1–3 µs), $106{,}67$ mA (3–5 µs), $124{,}45$ mA (5–7 µs)... $I(0,t)$: $80$, $133{,}33$ (2–4 µs), $115{,}5$ mA (4–6 µs)...
> **(b) aberto** ($\Gamma_C=+1$): $I(\ell,t)=0$ sempre; $V(\ell,t)$: 0 até 1 µs, $8$ V (1–3), $10{,}67$ V (3–5), $11{,}55$ V (5–7) $\dots\to12$ V. $V(0,t)$: $4$ V (0–2 µs), $9{,}333$ V (2–4), $11{,}11$ V (4–6) $\dots\to12$ V. $I(0,t)$: $80$ mA, $80/3$ (2–4 µs), $80/9$ (4–6 µs) $\dots\to0$.
> Regra de conferência: o regime permanente de um aberto é $V_\infty=V_g=12$ V ($I_\infty=0$); o de um curto é $V_\infty=0$, $I_\infty=V_g/Z_g=120$ mA.

### Exemplo 11.9 (pulso de largura finita)
- [ ] Resolvi sozinho

Linha de 75 Ω, 60 m, carga 100 Ω, $Z_g=25\ \Omega$, $u=0{,}1c$. Pulso retangular de **5 µs** e **4 V**. Trace $I(0,t)$ e $I(\ell,t)$ para $0<t<15\ \mu$s.

> [!success]- Solução
> $\Gamma_G=-\tfrac12$, $\Gamma_C=\tfrac17$; $V_0=\dfrac{75}{100}4=3$ V; $I_0=\dfrac{4}{100}=40$ mA; $t_1=\dfrac{60}{3\times10^7}=2\ \mu$s. Como $2t_1=4\ \mu\text{s}<5\ \mu$s, **há superposição**.
> Corrente no gerador: $I(0,t)=40$ mA (0–4 µs); em 4 µs chega o refletido, $-\Gamma_C I_0=-5{,}714$ mA, que reflete de novo ($-\Gamma_G$) em $-2{,}857$ mA: $40-5{,}714-2{,}857=31{,}43$ mA (4–5 µs); com o pulso já acabado, $-8{,}571$ mA (5–8 µs); e assim por diante.
> Carga: $V(\ell,t)=0$ até 2 µs; $3+0{,}4286=3{,}429$ V (2–6 µs); $3{,}185$ V (6–7 µs); depois ≈ $-0{,}245$ V (7–10 µs), $-0{,}227$ V (10–11 µs), $+0{,}0176$ V (11–15 µs). $I(\ell,t)=V(\ell,t)/Z_C$ com $Z_C=100\ \Omega$: $34{,}3$ mA, $31{,}9$ mA, ...
> ⚠️ O livro escreve "$I=V/Z_0$"; o $Z_0$ ali é na verdade o **$Z_C=100$ Ω** (os números usam 100).

**EP 11.9**: repita com pulso **triangular** (0 a 10 V em 2 µs, depois zero; Fig. 11.36).

> [!success]- Resposta (livro)
> $(I_0)_{máx}=100$ mA ($=10/(25+75)$). Formas de onda na Fig. 11.37: $I(0,t)$ sobe até 100 mA em 2 µs, volta a pequenos valores negativos ($\approx-21{,}4$ mA em 6 µs); $I(\ell,t)$ chega a $85{,}71$ mA em 4 µs.

### Exemplo 11.10 (microfita)
- [ ] Resolvi sozinho

Microfita com quartzo fundido ($\varepsilon_r=3{,}8$), $w/h=4{,}5$. Ache (a) $\varepsilon_{ef}$, (b) $Z_0$, (c) $\lambda$ em 10 GHz.

> [!success]- Solução
> (a) $\varepsilon_{ef}=\dfrac{4{,}8}{2}+\dfrac{2{,}8}{2}\left(1+\dfrac{12}{4{,}5}\right)^{-1/2}=3{,}131$.
> (b) $w/h\ge1$: $Z_0=\dfrac{120\pi}{\sqrt{3{,}131}\,[4{,}5+1{,}393+0{,}667\ln(4{,}5+1{,}444)]}=\mathbf{30{,}08\ \Omega}$.
> (c) $\lambda=\dfrac{c}{f\sqrt{\varepsilon_{ef}}}=16{,}9$ mm.
> ⚠️ O livro imprime $Z_0=9{,}576\ \Omega$. **É erro de impressão/cálculo**: a mesma fórmula dá $30{,}08\ \Omega$ (recalculado). Os itens (a) e (c) estão certos.

**EP 11.10**: repita para $w/h=0{,}8$.

> [!success]- Resposta (livro, confere)
> (a) $\varepsilon_{ef}=2{,}75$; (b) $Z_0=84{,}03\ \Omega$ (usa a forma de $w/h\le1$, com $\ln(8h/w+w/4h)$); (c) $\lambda=18{,}09$ mm.

### Exemplo 11.11 (perdas na microfita)
- [ ] Resolvi sozinho

Microfita a 10 GHz: $h=1$ mm, $w=0{,}8$ mm, $\varepsilon_r=6{,}6$, $\tan\theta=10^{-4}$, $\sigma_c=5{,}8\times10^7$ S/m. Ache $\alpha_c$ e $\alpha_d$.

> [!success]- Solução (calculado, corrigido) e valores do livro
> | | Livro | Correto (recalculado) |
> |---|---|---|
> | $\varepsilon_{ef}$ | 4,3 | **4,5** |
> | $Z_0$ | 67,17 Ω | **65,69 Ω** |
> | $R_s$ | $2{,}609\times10^{-2}$ ("Ω/m²", na verdade Ω) | $0{,}02609\ \Omega$ |
> | $\alpha_c$ | 4,217 dB/m | **4,31 dB/m** |
> | $\lambda$ | 14,47 mm | **14,14 mm** |
> | $\alpha_d$ | 0,1706 dB/m | **0,177 dB/m** |
>
> ⚠️ O livro usa $(\varepsilon_r+1)/2=7{,}2/2$, mas $6{,}6+1=7{,}6$: o termo certo dá $\varepsilon_{ef}=3{,}8+\dfrac{5{,}6}{2}\cdot\dfrac14=4{,}5$. O erro se propaga para $Z_0$, $\alpha_c$ e $\alpha_d$. Os valores do livro estão **ligeiramente fora**; a diferença é pequena (~2%–4%).
> Caminho: $\varepsilon_{ef}\to Z_0$ (11.71, $w/h\le1$) $\to R_s=\sqrt{\pi f\mu_0/\sigma_c}\to\alpha_c=8{,}686R_s/(wZ_0)\to\lambda=c/(f\sqrt{\varepsilon_{ef}})\to\alpha_d=27{,}3\dfrac{(\varepsilon_{ef}-1)\varepsilon_r}{(\varepsilon_r-1)\varepsilon_{ef}}\dfrac{\tan\theta}{\lambda}$.

**EP 11.11**: atenuação por perdas ôhmicas a 20 GHz, condutores de cobre, $w=2{,}5$ mm, substrato de alumina, $Z_0=50\ \Omega$.

> [!success]- Resposta (livro, verificada)
> $\alpha_c=2{,}564$ dB/m (com $R_s=0{,}0369\ \Omega$ a 20 GHz).

---

## Problemas: parâmetros e propagação

### Problema 11.1
- [ ] Resolvi sozinho

Linha **planar no ar**, $w=30$ cm, $d=1{,}2$ cm, $t=3$ mm, placas com $\sigma_c=7\times10^7$ S/m. Calcule $R$, $L$, $C$, $G$ em 500 MHz.

> [!success]- Resposta (calculado)
> $\delta=2{,}69\ \mu$m, $R=\dfrac{2}{w\delta\sigma_c}=0{,}0354\ \Omega$/m, $L=\mu_0d/w=50{,}27$ nH/m, $C=\varepsilon_0w/d=221{,}35$ pF/m, $G=0$. $Z_0=\sqrt{L/C}=15{,}07\ \Omega$.

### Problema 11.2
- [ ] Resolvi sozinho

Fios de cobre de um diodo: 16 mm de comprimento, raio 0,3 mm, separação de 2 mm (Fig. 11.42). Ache a capacitância entre os fios e a resistência CA em 10 MHz.

> [!success]- Resposta (calculado, tratando como linha bifilar com $d=2$ mm entre centros)
> $C=\dfrac{\pi\varepsilon_0\ell}{\cosh^{-1}(d/2a)}=0{,}2375$ pF ($\cosh^{-1}(3{,}33)=1{,}874$); $\delta_{Cu}=20{,}9\ \mu$m, $R=\dfrac{\ell}{\pi a\delta\sigma_c}=0{,}014\ \Omega$.

### Problema 11.4
- [ ] Resolvi sozinho

Linha planar sem perdas de 78 Ω saiu fora do alvo. Que fração da largura da fita deve ser adicionada ou removida para ter $Z_0=75\ \Omega$?

> [!success]- Resposta (calculado)
> $Z_0=\sqrt{L/C}=\dfrac{d}{w}\sqrt{\mu/\varepsilon}\propto1/w$ ⇒ $w'=w\cdot\dfrac{78}{75}=1{,}04w$: **aumentar a largura em 4%**.

### Problema 11.5
- [ ] Resolvi sozinho

Linha telefônica: $R=40\ \Omega$/m, $G=400\ \mu$S/m, $L=0{,}2\ \mu$H/m, $C=0{,}5$ nF/m. Em 10 MHz: (a) $Z_0$ e $u$; (b) a quantos metros a tensão cai 30 dB?

> [!success]- Resposta (calculado)
> (a) $Z_0=29{,}59-j21{,}43\ \Omega$, $\gamma=0{,}685+j0{,}921$ /m, $u=\omega/\beta=6{,}82\times10^7$ m/s.
> (b) $30\ \text{dB}=3{,}454$ Np ⇒ $d=3{,}454/0{,}685=5{,}04$ m.

### Problema 11.6
- [ ] Resolvi sozinho

Linha **sem distorção**, 120 MHz, $R=20\ \Omega$/m, $L=0{,}3\ \mu$H/m, $C=63$ pF/m. (a) $\gamma$, $u$, $Z_0$; (b) distância para a amplitude cair a 20%; (c) distância para 45° de defasagem.

> [!success]- Resposta (calculado)
> $G=RC/L=4{,}2$ mS/m. (a) $\alpha=\sqrt{RG}=0{,}2898$ Np/m, $\beta=\omega\sqrt{LC}=3{,}278$ rad/m, $\gamma=0{,}2898+j3{,}278$, $u=2{,}3\times10^8$ m/s, $Z_0=\sqrt{L/C}=69{,}0\ \Omega$.
> (b) $e^{-\alpha d}=0{,}2\Rightarrow d=\ln5/0{,}2898=5{,}55$ m. (c) $d=\dfrac{\pi/4}{\beta}=0{,}2396$ m.

### Problema 11.8
- [ ] Resolvi sozinho

Par trançado ≈ linha bifilar de fios de cobre com $0{,}12$ cm de diâmetro e $0{,}32$ cm entre centros, dielétrico $\varepsilon=3{,}5\varepsilon_0$. Ache $L$, $C$ e $Z_0$.

> [!success]- Resposta (calculado)
> $a=0{,}6$ mm, $d/2a=2{,}667$, $\cosh^{-1}=1{,}637$. $L=\dfrac\mu\pi\cosh^{-1}=654{,}7$ nH/m, $C=\dfrac{\pi\varepsilon}{\cosh^{-1}}=59{,}48$ pF/m, $Z_0=104{,}9\ \Omega$.

### Problema 11.9
- [ ] Resolvi sozinho

Linha sem perdas com $V(z,t)=V_0\operatorname{sen}(\omega t-\beta z)$. Ache a onda de corrente.

> [!success]- Resposta (calculado)
> Só há onda incidente: $I(z,t)=\dfrac{V_0}{Z_0}\operatorname{sen}(\omega t-\beta z)$ (em fase com a tensão).

### Problema 11.10
- [ ] Resolvi sozinho

Linha **sem distorção**: $V(\ell')=120e^{0{,}0025\ell'}\cos(10^8t+2\ell')+60e^{-0{,}0025\ell'}\cos(10^8t-2\ell')$, com $\ell'$ medido a partir da carga. $Z_C=300\ \Omega$. Ache (a) $\alpha$, $\beta$, $u$; (b) $Z_0$ e $I(\ell')$.

> [!success]- Resposta (calculado)
> (a) $\alpha=0{,}0025$ Np/m, $\beta=2$ rad/m, $u=\omega/\beta=5\times10^7$ m/s.
> (b) $\Gamma=\dfrac{60}{120}=0{,}5=\dfrac{300-Z_0}{300+Z_0}\Rightarrow Z_0=100\ \Omega$. A corrente é $V/Z_0$ para a onda incidente e $-V/Z_0$ para a refletida:
> $I(\ell')=1{,}2e^{0{,}0025\ell'}\cos(10^8t+2\ell')-0{,}6e^{-0{,}0025\ell'}\cos(10^8t-2\ell')$ A.

### Problema 11.12
- [ ] Resolvi sozinho

Coaxial de 5,6 m: $R=6{,}5\ \Omega$/m, $L=3{,}4\ \mu$H/m, $G=8{,}4$ mS/m, $C=21{,}5$ pF/m, 2 MHz. Ache $Z_0$ e o tempo de propagação entre os extremos.

> [!success]- Resposta (calculado)
> $Z_0=55{,}13+j45{,}86\ \Omega$, $\gamma=0{,}4507+j0{,}4001$ /m, $u=3{,}14\times10^7$ m/s, atraso $=\ell/u=178{,}3$ ns.

### Problema 11.13
- [ ] Resolvi sozinho

Linha sem perdas, 4,5 GHz, $L=2{,}4\ \mu$H/m, $Z_0=85\ \Omega$. Ache $\beta$ e $u$.

> [!success]- Resposta (calculado)
> $C=L/Z_0^2=332{,}2$ pF/m; $\beta=\omega\sqrt{LC}=798{,}3$ rad/m; $u=\omega/\beta=3{,}54\times10^7$ m/s.

---

## Problemas: reflexão, ROE e impedância de entrada

### Problema 11.14
- [ ] Resolvi sozinho

Coaxial de 50 Ω alimenta um dipolo de $75+j20\ \Omega$. Ache $\Gamma$ e $s$.

> [!success]- Resposta (calculado)
> $\Gamma=\dfrac{25+j20}{125+j20}=0{,}2529\angle29{,}57^\circ$, $s=\dfrac{1+0{,}2529}{1-0{,}2529}=1{,}677$.

### Problema 11.16
- [ ] Resolvi sozinho

Impedância de entrada do coaxial curto-circuitado (Fig. 11.44), $Z_0=65+j38\ \Omega$, $\gamma=0{,}7+j2{,}5$ /m, $\ell=0{,}8$ m.

> [!success]- Resposta (calculado)
> Com perdas: $Z_{cc}=Z_0\tanh\gamma\ell$, $\gamma\ell=0{,}56+j2$ ⇒ $Z_{cc}=113{,}0+j2{,}73\ \Omega$.

### Problema 11.17
- [ ] Resolvi sozinho

Linha sem perdas (Fig. 11.45): $Z_0=50\ \Omega$, comprimento $\lambda/6$, carga 120 Ω. (a) $\Gamma$ e $s$; (b) $Z_{ent}$ no gerador.

> [!success]- Resposta (calculado)
> (a) $\Gamma=\dfrac{70}{170}=0{,}4118$, $s=2{,}4$. (b) $\beta\ell=60^\circ$, $Z_{ent}=26{,}26-j22{,}55\ \Omega$.

### Problema 11.18
- [ ] Resolvi sozinho

Linha de **$\lambda/4$** sem perdas, 100 Ω, terminada em $Z_C=210\ \Omega$. A tensão na recepção é 80 V. Qual a tensão na emissão?

> [!success]- Resposta (calculado)
> $I_C=80/210=0{,}381$ A. Em $\lambda/4$: $\lvert V_{ent}\rvert=Z_0\lvert I_C\rvert=100\cdot0{,}381=38{,}1$ V.

### Problema 11.19
- [ ] Resolvi sozinho

Linha sem perdas de 500 Ω com $V_C=10e^{j25^\circ}$ V e $Z_C=50e^{j30^\circ}\ \Omega$. Ache a corrente a $\lambda/8$ da carga.

> [!success]- Resposta (calculado)
> $I_C=V_C/Z_C=0{,}2\angle-5^\circ$ A; $V(\lambda/8)=V_C\cos45^\circ+jZ_0I_C\operatorname{sen}45^\circ=74{,}5\angle80{,}3^\circ$ V; $I(\lambda/8)=I_C\cos45^\circ+j\dfrac{V_C}{Z_0}\operatorname{sen}45^\circ=\mathbf{0{,}1349\angle0{,}21^\circ\ A}$.
> (Fórmulas gerais da linha sem perdas, partindo da carga: $V=V_C\cos\beta\ell'+jZ_0I_C\operatorname{sen}\beta\ell'$, $I=I_C\cos\beta\ell'+j\dfrac{V_C}{Z_0}\operatorname{sen}\beta\ell'$.)

### Problema 11.20
- [ ] Resolvi sozinho

Linha sem perdas de 60 Ω, gerador $V_g=10\angle0^\circ$ V rms e $Z_g=50-j40\ \Omega$, carga $j40\ \Omega$, comprimento 100 m, $\beta=0{,}25$ rad/m. Ache $Z_{ent}$ e $V$: (a) na emissão, (b) na recepção, (c) a 4 m da carga, (d) a 3 m do gerador.

> [!success]- Resposta (calculado)
> $\beta\ell=25$ rad (reduza módulo $2\pi$ ou use $25\cdot57{,}3^\circ$). $Z_{ent}=j29{,}37\ \Omega$. (a) $V_{ent}=5{,}746\angle102^\circ$ V rms; (b) $V_C=7{,}249\angle102^\circ$ V rms; (c) $V(4\text{ m})=13{,}07\angle102^\circ$ V rms; (d) $V(3\text{ m do gerador})=3{,}796\angle-78^\circ$ V rms.

### Problema 11.21
- [ ] Resolvi sozinho

Linha sem perdas de 75 Ω, carga 120 Ω, comprimento $1{,}25\lambda$, fonte de 100 V rms com impedância interna 50 Ω. Ache (a) $Z_{ent}$, (b) a amplitude da tensão na carga.

> [!success]- Resposta (calculado)
> (a) $1{,}25\lambda=\lambda+\lambda/4$ ⇒ $Z_{ent}=Z_0^2/Z_C=46{,}875\ \Omega$. (b) $V_{ent}=\dfrac{46{,}875}{96{,}875}100=48{,}39$ V rms; a potência na entrada ($V_{ent}^2/Z_{ent}\approx50$ W) vai toda à carga: $\lvert V_C\rvert=\sqrt{50\cdot120}=77{,}4$ V rms ($109{,}5$ V de pico).

### Problema 11.22
- [ ] Resolvi sozinho

Três linhas em cascata (Fig. 11.46): $5\lambda/8$ com $Z_0=50\ \Omega$ (A–B), $3\lambda/4$ com $100\ \Omega$ (B–C), $\lambda/2$ com $75\ \Omega$ (C–D), carga $Z_C=60-j35\ \Omega$. Ache $Z_{ent}$.

> [!success]- Resposta (calculado)
> Do fim ao início: $\lambda/2$ repete ⇒ $60-j35$ em C. $3\lambda/4\equiv\lambda/4$: $Z_B=100^2/(60-j35)=124{,}4+j72{,}5\ \Omega$. $5\lambda/8\equiv\lambda/8$ ($\tan45^\circ=1$): $Z_{ent}=38{,}93-j57{,}06\ \Omega$.

### Problema 11.24
- [ ] Resolvi sozinho

Linha sem perdas de 50 Ω, 4,2 m, 300 MHz, $u=0{,}8c$. A impedância no **centro da linha** é $80-j60\ \Omega$. Ache $Z_{ent}$ no gerador e o coeficiente de reflexão na carga.

> [!success]- Resposta (calculado)
> $\lambda=0{,}8$ m; do centro ao gerador há $2{,}1$ m $=2{,}625\lambda$. $Z_{ger}=21{,}62-j20{,}27\ \Omega$. Do centro à carga: $\Gamma(\text{centro})\to\Gamma_C=\Gamma e^{+j2\beta\cdot2{,}1}$, $\Gamma_C=0{,}4685\angle51{,}34^\circ$.

### Problema 11.25
- [ ] Resolvi sozinho

Linha de 60 Ω no ar, 20 MHz, 10 m. $Z_{ent}=90+j150\ \Omega$. Ache $Z_C$, $\Gamma$ e $s$.

> [!success]- Resposta (calculado)
> $\lambda=15$ m, $\ell=0{,}667\lambda$. $Z_C=10{,}24+j13{,}64\ \Omega$, $\Gamma=0{,}7211\angle153{,}7^\circ$, $s=6{,}17$.

### Problema 11.26
- [ ] Resolvi sozinho

Linha de 75 Ω com carga $120+j80\ \Omega$. (a) $\Gamma$ e $s$; (b) a que distâncias da carga a impedância é puramente resistiva?

> [!success]- Resposta (calculado)
> (a) $\Gamma=0{,}4355\angle38{,}34^\circ$, $s=2{,}543$. (b) resistiva nos $V_{máx}$ e $V_{mín}$: $\ell'=0{,}0532\lambda$ ($Z_{máx}=sZ_0=190{,}7\ \Omega$) e $0{,}3032\lambda$ ($Z_{mín}=29{,}5\ \Omega$), mais múltiplos de $\lambda/2$.
> Caminho: $\ell'_{máx}=\dfrac{\theta_\Gamma}{720^\circ}\lambda=\dfrac{38{,}34}{720}\lambda$.

### Problema 11.27
- [ ] Resolvi sozinho

Linha de 75 Ω de comprimento $5\lambda/8$. Ache $Z_{ent}$ para (a) $Z_C=j45\ \Omega$; (b) $Z_C=25-j65\ \Omega$.

> [!success]- Resposta (calculado)
> $5\lambda/8\equiv\lambda/8$ ($\beta\ell=225^\circ$, $\tan=1$). (a) $Z_{ent}=j300\ \Omega$. (b) $Z_{ent}=13{,}91+j2{,}87\ \Omega$.

### Problema 11.28
- [ ] Resolvi sozinho

Impedância de entrada **normalizada** a $\lambda/8$ da carga se: (a) $z_C=2+j$; (b) $y_C=0{,}2-j0{,}5$; (c) $\Gamma_C=0{,}3+j0{,}4$.

> [!success]- Resposta (calculado)
> A $\lambda/8$: $\Gamma\to\Gamma e^{-j90^\circ}$ (gire $90^\circ$ **horário**). (a) $1-j1$. (b) $z_C=1/y_C=0{,}69+j1{,}72\Rightarrow1{,}379-j2{,}448$. (c) $\Gamma'=0{,}4-j0{,}3\Rightarrow1{,}667-j1{,}333$.

### Problema 11.29
- [ ] Resolvi sozinho

Carga com admitância $Y_C=(0{,}6+j0{,}8)/Z_0$. Impedância normalizada a $\lambda/6$ da carga.

> [!success]- Resposta (calculado)
> $z_C=1/(0{,}6+j0{,}8)=0{,}6-j0{,}8$; $\beta\ell=60^\circ$ ⇒ $z=0{,}3544+j0{,}2363$.

### Problema 11.30
- [ ] Resolvi sozinho

Linha de 80 Ω, 12 MHz, $u=0{,}8c$, terminada em $Z_C$ desconhecida. A **22 m da carga** a impedância de entrada é $100-j120\ \Omega$. (a) $\Gamma_C$, $Z_{ent,máx}$, $Z_{ent,mín}$; (b) $Z_C$, $s$ e a impedância a 28 m da carga; (c) quantos $Z_{máx}$ e $Z_{mín}$ há entre a carga e esse ponto?

> [!success]- Resposta (calculado)
> $\lambda=20$ m. (a) $\Gamma_C=0{,}5624\angle25{,}15^\circ$; $s=3{,}57$; $Z_{máx}=285{,}6\ \Omega$; $Z_{mín}=22{,}4\ \Omega$. (b) $Z_C=183{,}4+j128{,}3\ \Omega$; $Z_{ent}(28\text{ m})=37{,}56+j61{,}3\ \Omega$. (c) Em 22 m $(=1{,}1\lambda)$: 3 máximos e 2 mínimos.

---

## Problemas: medidas na linha e linha fendida

### Problema 11.31
- [ ] Resolvi sozinho

Antena em linha sem perdas de 150 Ω, $s=2{,}6$. Máximos de tensão separados por 120 cm; o último máximo está a 40 cm da antena. $u=c$. Ache (a) $f$, (b) $Z_C$ da antena, (c) $\Gamma$.

> [!success]- Resposta (calculado)
> (a) $\lambda/2=120$ cm ⇒ $\lambda=240$ cm, $f=125$ MHz. (c) $\lvert\Gamma\rvert=1{,}6/3{,}6=0{,}4444$; $V_{máx}$ a $40$ cm $=\lambda/6=120^\circ$ no círculo ⇒ $\theta_\Gamma=120^\circ$, $\Gamma=0{,}4444\angle120^\circ$. (b) $Z_C=73{,}3+j70{,}3\ \Omega$.

### Problema 11.32
- [ ] Resolvi sozinho

Linha de 100 Ω, $s=8$, primeiro máximo de tensão a $0{,}3\lambda$ da carga. Ache $Z_C$ e $\Gamma$.

> [!success]- Resposta (calculado)
> $\lvert\Gamma\rvert=7/9=0{,}7778$; $\theta_\Gamma=720^\circ\cdot0{,}3=216^\circ$ ($=-144^\circ$). $\Gamma=0{,}7778\angle216^\circ$; $Z_C=13{,}8-j31{,}93\ \Omega$.

### Problema 11.33
- [ ] Resolvi sozinho

Linha de 50 Ω, $s=2{,}4$, um **máximo** de tensão a $\lambda/8$ da carga. (a) $Z_C$; (b) distância do primeiro mínimo à carga.

> [!success]- Resposta (calculado)
> $\lvert\Gamma\rvert=0{,}4118$; $V_{máx}$ a $\lambda/8$ ⇒ $\theta_\Gamma=90^\circ$. (a) $\Gamma=0{,}4118\angle90^\circ$, $Z_C=35{,}5+j35{,}2\ \Omega$. (b) mínimo a $\lambda/8+\lambda/4=0{,}375\lambda$.

### Problema 11.34
- [ ] Resolvi sozinho

Linha de 75 Ω com carga desconhecida. A $0{,}2\lambda$ da carga, $V_s=2+j$ V e a corrente é 10 mA. Ache $Z_C$ e $s$.

> [!success]- Resposta (calculado)
> $Z_{ent}=V/I=200+j100\ \Omega$ (módulo da corrente, referência de fase igual). $\Gamma$ no ponto $=0{,}547\angle18{,}7^\circ$; levando $0{,}2\lambda$ (=$144^\circ$) de volta à carga: $\Gamma_C=0{,}547\angle162{,}7^\circ$, $s=3{,}416$, $Z_C=22{,}42+j10{,}43\ \Omega$.

### Problema 11.43
- [ ] Resolvi sozinho

Linha de 60 Ω com carga $Z_C$. A onda estacionária de tensão está na Fig. 11.52: máximo de 4 V a 15 cm da carga e mínimo de 1 V a 5 cm (outros mínimos em 25 e 45 cm). Ache $s$, $\Gamma$ e $Z_C$.

> [!success]- Resposta (calculado)
> $s=4/1=4$; $\lambda/2=20$ cm ⇒ $\lambda=40$ cm; $\lvert\Gamma\rvert=0{,}6$. $V_{mín}$ a $5$ cm $=\lambda/8$: $\dfrac{\theta_\Gamma+180^\circ}{720^\circ}\lambda=\dfrac\lambda8\Rightarrow\theta_\Gamma=-90^\circ$. $\Gamma=0{,}6\angle-90^\circ$, $Z_C=28{,}24-j52{,}94\ \Omega$.

### Problema 11.44
- [ ] Resolvi sozinho

Linha fendida de 50 Ω. Com carga, $s=3{,}2$ e $V_{mín}$ consecutivos em 12 cm e 32 cm (valores maiores para o lado da carga). Com curto, $V_{mín}$ em 21 cm. Ache $f$ e $Z_C$.

> [!success]- Resposta (calculado)
> $\lambda/2=20$ cm ⇒ $\lambda=40$ cm, $f=750$ MHz. O $V_{mín}$ da carga (12 cm) está $21-12=9$ cm do plano da carga, em direção ao gerador: $\ell'=9$ cm $=0{,}225\lambda$. $Z_C=130{,}5-j58{,}2\ \Omega$.

### Problema 11.45
- [ ] Resolvi sozinho

Linha fendida de 50 Ω no ar. Mínimos adjacentes a 14 cm e 22,5 cm da carga com a carga desconhecida; $V_{máx}=0{,}95$ V e $V_{mín}=0{,}45$ V. Com um curto, os mínimos se deslocam 3,2 cm **em direção à carga**. Ache $s$, $f$, $\Gamma$ e $Z_C$.

> [!success]- Resposta (calculado)
> $s=0{,}95/0{,}45=2{,}111$; $\lambda/2=8{,}5$ cm ⇒ $\lambda=17$ cm, $f=1{,}765$ GHz. $\ell'=3{,}2$ cm $=0{,}188\lambda$ ⇒ $\theta_\Gamma=2\beta\ell'-180^\circ=-44{,}5^\circ$. $\Gamma=0{,}357\angle-44{,}5^\circ$; $Z_C=70{,}6-j40{,}5\ \Omega$.

---

## Problemas: casamento de impedâncias

### Problema 11.35
- [ ] Resolvi sozinho

Dois transformadores de $\lambda/4$ em cascata ligam 50 Ω a 75 Ω (Fig. 11.48). (a) $Z_{01}$ se $Z_{02}=30\ \Omega$ e não há onda refletida à esquerda de A. (b) Se o melhor resultado é $\left(\dfrac{Z_0}{Z_{01}}\right)^2=\dfrac{Z_{01}}{Z_{02}}=\left(\dfrac{Z_{02}}{Z_C}\right)^2$, ache $Z_{01}$ e $Z_{02}$.

> [!success]- Resposta (calculado)
> (a) Casado: $Z_0=\dfrac{Z_{01}^2Z_C}{Z_{02}^2}$ ⇒ $Z_{01}=Z_{02}\sqrt{Z_0/Z_C}=24{,}49\ \Omega$.
> (b) Das duas igualdades: $Z_{01}=Z_0^{2/3}\cdots$; resolvendo, $Z_{01}=55{,}33\ \Omega$ e $Z_{02}=67{,}77\ \Omega$ (razões iguais: $Z_0/Z_{01}=Z_{01}/Z_{02}=Z_{02}/Z_C$ ao longo do sistema).

### Problema 11.36
- [ ] Resolvi sozinho

Duas antenas idênticas de 74 Ω, alimentadas por três linhas sem perdas de $\lambda/4$ e 50 Ω (Fig. 11.49). Impedância de entrada na fonte.

> [!success]- Resposta (calculado)
> Cada ramo: $50^2/74=33{,}78\ \Omega$. Em paralelo: $16{,}89\ \Omega$. Tronco ($\lambda/4$): $50^2/16{,}89=148\ \Omega$.

### Problema 11.37
- [ ] Resolvi sozinho

A linha anterior é ligada a fonte de 120 V com impedância interna 80 Ω. Potência média em cada antena.

> [!success]- Resposta (calculado)
> $V_{ent}=120\cdot\dfrac{148}{148+80}=77{,}9$ V; $P_{ent}=V^2/Z_{ent}=41$ W (linha sem perdas, tudo chega às antenas); **20,5 W por antena** (se 120 V for rms; se for de pico, $\approx10{,}25$ W).

### Problema 11.38
- [ ] Resolvi sozinho

Três linhas sem perdas de $\lambda/4$ (Fig. 11.50), $Z_0=50\ \Omega$: a linha 1 termina em 200 Ω, a linha 2 em **curto**, a linha 3 recebe as duas em paralelo. Ache $Z_{ent}$ na entrada de (a) linha 1, (b) linha 2, (c) linha 3.

> [!success]- Resposta (calculado)
> (a) $50^2/200=12{,}5\ \Omega$. (b) curto a $\lambda/4$ ⇒ $\infty$ (circuito aberto). (c) Em paralelo: $12{,}5\parallel\infty=12{,}5$; $Z_{ent3}=50^2/12{,}5=200\ \Omega$.

### Problema 11.39
- [ ] Resolvi sozinho

Seção de linha sem perdas em **paralelo** com a principal (Fig. 11.51): $\ell_1=\lambda/4$ (da carga ao ponto), $\ell_2=\lambda/8$ (toco), $\ell_3=7\lambda/8$ (do ponto ao gerador). $Z_0=100\ \Omega$, $Z_C=200+j150\ \Omega$. Ache $y_{ent1}$, $y_{ent2}$, $y_{ent3}$ para toco em curto e para toco em aberto.

> [!success]- Resposta (calculado, normalizadas a $Y_0=10$ mS)
> $y_{ent1}=2+j1{,}5$ (λ/4 inverte: $y=z_C$). $y_{ent2}=-j1$ (curto) ou $+j1$ (aberto). $y_{ent3}=0{,}64+j0{,}52$ (curto) ou $0{,}246+j0{,}569$ (aberto), depois de somar $y_{ent1}+y_{ent2}$ e girar $7\lambda/8\equiv3\lambda/8$ (horário).

### Problema 11.40
- [ ] Resolvi sozinho

Casar uma linha de 50 Ω a uma carga $60-j50\ \Omega$ com **toco de 50 Ω**. Comprimento do toco e distância à carga.

> [!success]- Resposta (calculado)
> $y_C=0{,}4918+j0{,}4098$. Duas soluções: $d=0{,}0843\lambda$ da carga com toco de $0{,}1307\lambda$; ou $d=0{,}265\lambda$ com toco de $0{,}3693\lambda$ (toco curto-circuitado).

### Problema 11.41
- [ ] Resolvi sozinho

Toco de $0{,}12\lambda$ casa uma linha de 60 Ω a uma carga; o toco está a $0{,}3\lambda$ da carga. (a) $Z_C$; (b) comprimento do toco alternativo e sua distância; (c) ROE entre o toco e a carga.

> [!success]- Resposta (calculado)
> Toco curto de $0{,}12\lambda$ dá $y_s=-j\cot(43{,}2^\circ)=-j1{,}0649$ (sinal $-$): ponto A. (a) $Z_C=34{,}6+j41{,}34\ \Omega$. (b) toco $0{,}38\lambda$ ($d_A+d_B=\lambda/2$) a $0{,}4721\lambda$ da carga. (c) $s=2{,}773$.

### Problema 11.42
- [ ] Resolvi sozinho

Linha sem perdas com $s=4{,}2$ e **primeiro máximo a $\lambda/4$ da carga**. Onde colocar um toco curto-circuitado e qual o seu comprimento?

> [!success]- Resposta (calculado)
> $V_{máx}$ a $\lambda/4$ ⇒ $V_{mín}$ na carga ⇒ $z_C=1/s=1/4{,}2$. Duas soluções: $d=0{,}0723\lambda$ com toco de $0{,}4093\lambda$; ou $d=0{,}4277\lambda$ com toco de $0{,}0907\lambda$.

---

## Problemas: transitórios

### Problema 11.47
- [ ] Resolvi sozinho

Linha sem perdas de 60 Ω, gerador de pulsos de 40 Ω, 6 m, carga 100 Ω, pulso retangular de 5 µs e 20 V, $u=3\times10^8$ m/s. Ache $V(0,t)$ e $I(\ell,t)$ para $0\le t\le10\ \mu$s.

> [!success]- Resposta (calculado)
> $\Gamma_G=-0{,}2$, $\Gamma_C=0{,}25$, $V_0=\dfrac{60}{100}20=12$ V, $t_1=0{,}02\ \mu$s (muito menor que o pulso: quase tudo se sobrepõe, e o regime é praticamente o permanente). $V_\infty=\dfrac{100}{140}20=14{,}286$ V, $I_\infty=142{,}9$ mA. $V(0,t)\approx14{,}29$ V e $I(\ell,t)=V(\ell,t)/100\approx142{,}9$ mA até 5 µs; depois cai a ≈0 em poucas dezenas de ns.

### Problema 11.48
- [ ] Resolvi sozinho

Chave da Fig. 11.53 fecha em $t=0$: fonte de 27 V, $2Z_0$ em série, linha de $Z_0=50\ \Omega$, carga $0{,}5Z_0$, $\ell/u=2\ \mu$s. Trace a tensão e a corrente à direita da chave para $0<t<6\ell/u$.

> [!success]- Resposta (calculado)
> $\Gamma_G=\dfrac{2-1}{2+1}=\dfrac13$, $\Gamma_C=\dfrac{0{,}5-1}{1{,}5}=-\dfrac13$; $V_0=\dfrac{Z_0}{3Z_0}27=9$ V, $I_0=180$ mA. $V(0,t)$: **9 V** (0–4 µs), **5 V** (4–8 µs), **5,444 V** (8–12 µs); $V_\infty=\dfrac{0{,}5}{2{,}5}27=5{,}4$ V. A corrente é $I(0,t)=\dfrac{27-V(0,t)}{2Z_0}$: $180$, $220$, $215{,}6$ mA (…$\to216$ mA).

### Problema 11.49
- [ ] Resolvi sozinho

Sistema da Fig. 11.54: 100 V, $Z_g=50\ \Omega$, linha 75 Ω, $u=2\times10^8$ m/s, 200 m, carga 100 Ω. Trace $V(\ell,t)$ e $I(\ell,t)$ para $0<t<5\ \mu$s.

> [!success]- Resposta (calculado)
> $t_1=1\ \mu$s; $\Gamma_G=-0{,}2$, $\Gamma_C=\tfrac17$, $V_0=\dfrac{75}{125}100=60$ V. $V(\ell,t)$: **0** para $t<1\ \mu$s; **68,57 V** (1–3 µs); **66,61 V** (3–5 µs); $\to66{,}67$ V. $I(\ell,t)=V/100$: 0; 685,7 mA; 666,1 mA…

### Problema 11.50
- [ ] Resolvi sozinho

Fig. 11.55: $Z_g=25\ \Omega$, $Z_0=50\ \Omega$, $Z_C=150\ \Omega$, $\ell=150$ m, $u=c$. O pulso de dois retângulos (+15 V por 1 µs, depois −15 V por 1 µs, Fig. 11.56) entra em $t=0$. (a) Diagramas de saltos de tensão e corrente; (b) $V(0,t)$, $V(\ell,t)$, $I(0,t)$, $I(\ell,t)$ para $0<t<8\ \mu$s.

> [!success]- Resposta (calculado)
> $\Gamma_G=-\tfrac13$, $\Gamma_C=0{,}5$; $V_0=10$ V (primeiro pulso; $-10$ V no segundo); $t_1=0{,}5\ \mu$s. Os pulsos têm 1 µs ($=2t_1$), então **cada pulso acaba antes de o eco voltar para o mesmo ponto** em quase todo instante; some o que se sobrepõe.
> $V(0,t)$ por intervalos de 0,5 µs: $10,\ 10,\ -6{,}667,\ -6{,}667,\ -3{,}889,\ -3{,}889,\ 0{,}648,\ 0{,}648,\dots$
> $V(\ell,t)$: $0,\ 15,\ 15,\ -17{,}5,\ -17{,}5,\ 2{,}917,\ 2{,}917,\ -0{,}486,\dots$
> Correntes: $I(0,t)=[V_g(t)-V(0,t)]/Z_g$; $I(\ell,t)=V(\ell,t)/150$.

---

## Problemas: microfita

### Problema 11.51
- [ ] Resolvi sozinho

Microfita com 1 cm de espessura e 1,5 cm de largura, fita de bronze ($\sigma_c=1{,}1\times10^7$ S/m), substrato com $\varepsilon_r=2{,}2$ e $\tan\theta=0{,}002$, a 2,5 GHz. Ache (a) $Z_0$ e $\varepsilon_{ef}$; (b) $\alpha_c$ e $\alpha_d$; (c) a distância para a onda diminuir 20 dB.

> [!success]- Resposta (calculado)
> $w/h=1{,}5\ge1$. (a) $\varepsilon_{ef}=1{,}8$; $Z_0=77{,}77\ \Omega$. (b) $\alpha_c=0{,}223$ dB/m; $\alpha_d=0{,}497$ dB/m; $\alpha=0{,}72$ dB/m. (c) $d=20/0{,}72=27{,}8$ m.

### Problema 11.52
- [ ] Resolvi sozinho

Microfita de 50 Ω com defasagem de 45° em 8 GHz; substrato $h=8$ mm, $\varepsilon_r=4{,}6$. Ache (a) a largura da fita, (b) o comprimento da linha.

> [!success]- Resposta (calculado)
> (a) (11.72): $w/h=1{,}849\ (<2)\Rightarrow w=14{,}79$ mm. (b) $\varepsilon_{ef}=3{,}458$, $\lambda=\dfrac{c}{f\sqrt{\varepsilon_{ef}}}=20{,}17$ mm; $45^\circ=\lambda/8\Rightarrow\ell=2{,}52$ mm.

### Problema 11.53
- [ ] Resolvi sozinho

Alumina ($\varepsilon=9{,}6\varepsilon_0$), $h=2$ mm. A fita pode ter de 0,4 mm a 8 mm. Faixa de $Z_0$?

> [!success]- Resposta (calculado)
> $w=0{,}4$ mm ⇒ $w/h=0{,}2$, $\varepsilon_{ef}=5{,}85$, $Z_0=91{,}5\ \Omega$. $w=8$ mm ⇒ $w/h=4$, $\varepsilon_{ef}=7{,}45$, $Z_0=21{,}2\ \Omega$. Faixa: **21,2 Ω a 91,5 Ω** (fita mais larga ⇒ $Z_0$ menor).

### Problema 11.54
- [ ] Resolvi sozinho

Projete uma microfita de 75 Ω em duroide ($\varepsilon_r=2{,}3$), $h=1{,}2$ mm. Largura da fita e velocidade de fase.

> [!success]- Resposta (calculado)
> $w/h=1{,}539\Rightarrow w=1{,}847$ mm; $\varepsilon_{ef}=1{,}869$; $u=c/\sqrt{\varepsilon_{ef}}=2{,}19\times10^8$ m/s $=0{,}731c$.

---

## Demonstrações
Os problemas com asterisco pedem prova. Roteiro das provas:

### Problema 11.3
- [ ] Resolvi sozinho

Mostrar que (11.4) e (11.6) valem com os circuitos equivalentes **Π** e **T** (Fig. 11.43).

> [!success]- Roteiro
> Aplique KVL e KCL ao circuito de $\Delta z$, com $V(z+\Delta z)=V+\dfrac{\partial V}{\partial z}\Delta z$ e idem para $I$. No Π, as admitâncias $\tfrac{G}{2}\Delta z+\tfrac{C}{2}\Delta z\,\partial_t$ de cada lado dão termos de $\Delta z^2$. No T, o mesmo com as impedâncias em série $\tfrac R2\Delta z$ e $\tfrac L2\Delta z\,\partial_t$. Divida por $\Delta z$ e faça $\Delta z\to0$: **os termos de ordem $\Delta z^2$ somem** e sobram exatamente $-\partial V/\partial z=RI+L\,\partial I/\partial t$ e $-\partial I/\partial z=GV+C\,\partial V/\partial t$.

### Problema 11.7
- [ ] Resolvi sozinho

Para linha bifilar sem perdas: (a) $u=c=1/\sqrt{LC}$; (b) $Z_0=\dfrac{120}{\sqrt{\varepsilon_r}}\cosh^{-1}\dfrac{d}{2a}$. O resultado de (a) vale para outras linhas sem perdas?

> [!success]- Roteiro
> (a) $LC=\dfrac\mu\pi\cosh^{-1}\cdot\dfrac{\pi\varepsilon}{\cosh^{-1}}=\mu\varepsilon$, logo $u=1/\sqrt{\mu\varepsilon}=c$ no ar. (b) $Z_0=\sqrt{L/C}=\dfrac1\pi\sqrt{\dfrac\mu\varepsilon}\cosh^{-1}=\dfrac{\eta}{\pi}\cosh^{-1}=\dfrac{120\pi/\sqrt{\varepsilon_r}}{\pi}\cosh^{-1}$. Sim: **$LC=\mu\varepsilon$ vale para qualquer linha sem perdas** (TEM) em meio homogêneo, então $u=1/\sqrt{\mu\varepsilon}$.

### Problema 11.11
- [ ] Resolvi sozinho

(a) Mostrar $\tau_C=\dfrac{V_C}{V_0^+}=1+\Gamma_C=\dfrac{2Z_C}{Z_C+Z_0}$. (b) $\tau_C$ para: (i) $Z_C=nZ_0$; (ii) aberto; (iii) curto; (iv) casada.

> [!success]- Roteiro e resposta
> (a) Na carga $V_C=V_0^++V_0^-=V_0^+(1+\Gamma_C)$ e $1+\Gamma_C=\dfrac{2Z_C}{Z_C+Z_0}$. (b) (i) $\dfrac{2n}{n+1}$; (ii) $2$; (iii) $0$; (iv) $1$.

### Problema 11.15
- [ ] Resolvi sozinho

Linha com perdas: $Z_{cc}=Z_0\tanh\gamma\ell$ e $Z_{ca}=Z_0\coth\gamma\ell$. Confirmar (11.37) e (11.39).

> [!success]- Roteiro
> Em (11.33) faça $Z_C=0$ (dá $Z_0\tanh\gamma\ell$) e $Z_C\to\infty$ (dá $Z_0/\tanh\gamma\ell$). Para (11.37): $\Gamma(z)=\dfrac{V_0^-e^{\gamma z}}{V_0^+e^{-\gamma z}}$ com $z=\ell-\ell'$ e $\Gamma_C=\dfrac{V_0^-e^{\gamma\ell}}{V_0^+e^{-\gamma\ell}}$ ⇒ $\Gamma=\Gamma_Ce^{-2\gamma\ell'}$. Para (11.39): nos máximos de $\lvert V\rvert$ a corrente é mínima: $Z_{máx}=\dfrac{V_{máx}}{I_{mín}}=\dfrac{(1+\lvert\Gamma\rvert)V^+}{(1-\lvert\Gamma\rvert)V^+/Z_0}=sZ_0$, e analogamente $Z_{mín}=Z_0/s$.

### Problema 11.23
- [ ] Resolvi sozinho

Mostrar que a matriz $ABCD$ de uma linha com perdas é $\begin{bmatrix}\cosh\gamma\ell&Z_0\sinh\gamma\ell\\\frac{1}{Z_0}\sinh\gamma\ell&\cosh\gamma\ell\end{bmatrix}$.

> [!success]- Roteiro
> Escreva $V(z)=V^+e^{-\gamma z}+V^-e^{\gamma z}$ e $I(z)=(V^+e^{-\gamma z}-V^-e^{\gamma z})/Z_0$. Em $z=0$ ($V_1,I_1$) e $z=\ell$ ($V_2$ e $I_2$ entrando, ou seja, $-I_2$ sai). Elimine $V^\pm$: $V_1=V_2\cosh\gamma\ell+Z_0(-I_2)\sinh\gamma\ell$ e $I_1=\dfrac{V_2}{Z_0}\sinh\gamma\ell+(-I_2)\cosh\gamma\ell$ (com a convenção de sentido do problema). Isso dá $A=D=\cosh\gamma\ell$, $B=Z_0\sinh\gamma\ell$, $C=\sinh\gamma\ell/Z_0$.

### Problema 11.46
- [ ] Resolvi sozinho

Para $V_g$ contínua ligada em $t=0$, mostrar $V_\infty=\dfrac{V_gZ_C}{Z_g+Z_C}$ e $I_\infty=\dfrac{V_g}{Z_g+Z_C}$.

> [!success]- Roteiro
> Série das reflexões: $V_\infty=V_0\dfrac{1+\Gamma_C}{1-\Gamma_G\Gamma_C}$. Com $V_0=\dfrac{Z_0V_g}{Z_g+Z_0}$, $1+\Gamma_C=\dfrac{2Z_C}{Z_C+Z_0}$ e $1-\Gamma_G\Gamma_C=\dfrac{2Z_0(Z_g+Z_C)}{(Z_g+Z_0)(Z_C+Z_0)}$, tudo se simplifica em $V_\infty=\dfrac{V_gZ_C}{Z_g+Z_C}$. Ou, mais rápido: em regime permanente de CC, a linha é só fio, o circuito é $V_g$–$Z_g$–$Z_C$.
> O enunciado impresso diz "$t\ll\ell/u$", mas o sentido é $t\gg\ell/u$ (tempo longo).

---

## Simulado sugerido
Estilo de prova, **90 minutos**, sem consultar as respostas. *(Seleção minha, não é do livro.)*

| # | Problema | Assunto | Tempo |
|---|---|---|---|
| 1 | [[#Problema 11.6]] | sem distorção ($\gamma$, $u$, $Z_0$) | 8 min |
| 2 | [[#Problema 11.17]] | $\Gamma$, $s$, $Z_{ent}$ | 8 min |
| 3 | [[#Problema 11.30]] | $Z_{ent}$, $Z_{máx}$, $Z_C$ | 15 min |
| 4 | [[#Problema 11.33]] | ROE e $V_{máx}$ | 8 min |
| 5 | [[#Problema 11.36]] | transformador $\lambda/4$ | 8 min |
| 6 | [[#Problema 11.40]] | toco (Smith) | 15 min |
| 7 | [[#Problema 11.45]] | linha fendida | 12 min |
| 8 | [[#Problema 11.48]] | transitório | 12 min |
| 9 | [[#Problema 11.52]] | microfita | 8 min |

**Depois**: marque o que errou e volte na seção correspondente de [[EM2 LT - Fórmulas]]. Se errou por **sinal ou sentido de giro na carta**, releia a [[EM2 LT - Revisão#Armadilhas mais comuns|lista de armadilhas]].
