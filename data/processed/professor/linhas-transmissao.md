---
fonte: "Material do professor: Linhas de Transmissão"
pagina: "https://app.in-foton.org/eletromagnetismo/linhas-transmissao.html"
---

# Teoria de Linhas de Transmissão e Linhas Impressas (Microstrip)

Módulo [MOD-LT], bloco compartilhado entre Eletromagnetismo e Engenharia de RF (teoria e laboratórios). Docente: Prof. Marcelo Eduardo Vieira Segatto (DEE/UFES, LabTel, IN-Foton).

Do modelo infinitesimal de parâmetros distribuídos e equações dos telegrafistas às formulações de Wheeler/Pozar em circuitos planares e transformação conforme na Carta de Smith.

## Introdução: limite dos circuitos concentrados e propagação de ondas guiadas

A transição entre as leis de Kirchhoff e a propagação espaço-temporal de ondas guiadas.

Na análise clássica de circuitos elétricos concentrados (Leis de Kirchhoff para nós e malhas), assume-se implicitamente que as dimensões físicas dos componentes e das trilhas de interconexão são desprezíveis perante o comprimento de onda do sinal ($\ell \ll \lambda$), o que equivale a admitir velocidade de propagação infinita e tempo de trânsito nulo.

### Colapso da hipótese de parâmetros concentrados: critério de comprimento elétrico e tempo de subida

Conforme a frequência operacional se eleva para a faixa de radiofrequência (RF) e micro-ondas, ou quando lidamos com pulsos digitais de subida ultra-rápida ($t_r$ na escala de picossegundos), o comprimento elétrico da conexão atinge o regime crítico no qual os efeitos de propagação não podem mais ser ignorados:

$$\ell \gtrsim 0{,}01 \lambda \quad \Longleftrightarrow \quad t_d = \frac{\ell}{v_p} \gtrsim 0{,}1 \, t_r$$

Significado físico das variáveis:

- **$\ell$** (ou $l$): comprimento físico total da linha de transmissão ou da trilha condutora de interconexão $[\text{m}]$.
- **$\lambda$**: comprimento de onda da perturbação guiada no dielétrico ($\lambda = v_p / f$) $[\text{m}]$.
- **$v_p$**: velocidade de propagação de fase da onda eletromagnética no meio isolante ($v_p = c / \sqrt{\varepsilon_r}$) $[\text{m/s}]$.
- **$t_d$**: tempo de atraso de propagação (*time delay* ou tempo de trânsito ao longo da linha, dado por $t_d = \ell / v_p$) $[\text{s}]$.
- **$t_r$**: tempo de subida do pulso (*rise time*, usualmente medido no intervalo de $10\%$ a $90\%$ da transição de borda) $[\text{s}]$.

### Reflexões, overshoot, ringing e integridade de sinal: por que usar o modelo distribuído

Quando o tempo de trânsito $t_d$ atinge $10\%$ do tempo de subida $t_r$ ($t_d \gtrsim 0{,}1 \, t_r$), as reflexões originadas nas descontinuidades de impedância retornam antes que a transição lógica seja concluída, provocando sobretensão (*overshoot*), oscilações parasitas (*ringing*) e degradação da integridade de sinal.

Nessas condições, a tensão e a corrente deixam de ser grandezas puramente temporais e tornam-se **ondas espaço-temporais acopladas** $v(z,t)$ e $i(z,t)$, exigindo o modelo circuital distribuído formulado pioneiramente por **Oliver Heaviside**.

## Modelo circuital distribuído e equações dos telegrafistas

Dedução infinitesimal por malhas e nós no domínio do tempo e representação harmônica fasorial.

### Parâmetros primários distribuídos R, L, G e C por unidade de comprimento

Uma linha de transmissão uniforme de dois condutores é modelada como uma cascata de células infinitesimais de comprimento $\Delta z$, caracterizadas por quatro parâmetros primários distribuídos por unidade de comprimento:

- **$R$ [$\Omega/\text{m}$]**: resistência série distribuída decorrente da condutividade finita dos condutores e efeito pelicular.
- **$L$ [$\text{H}/\text{m}$]**: indutância série devida à autoindutância dos condutores e armazenamento de energia magnética.
- **$G$ [$\text{S}/\text{m}$]**: condutância paralelo associada às perdas dielétricas e correntes de fuga pelo meio isolante.
- **$C$ [$\text{F}/\text{m}$]**: capacitância paralelo entre os condutores associada à densidade de energia eletrostática confinada.

*Figura 4.1: Modelo circuital distribuído infinitesimal de comprimento $\Delta z$ e convenção de sinais para aplicação da Lei das Malhas e Lei dos Nós. O desenho mostra, no condutor superior, $R\Delta z$ e $L\Delta z$ em série; depois deles, $G\Delta z$ e $C\Delta z$ em paralelo entre os condutores. À esquerda, a tensão $v(z,t)$ e a corrente $i(z,t)$ entrando; à direita, a corrente $i(z+\Delta z,t)$ saindo e a tensão $v(z+\Delta z,t)$; a célula tem comprimento $\Delta z$.*

### Dedução das equações dos telegrafistas no domínio do tempo (LKT e LKC)

Aplicando a Lei de Kirchhoff das Tensões (LKT) na malha fechada:

$$v(z,t) - R \Delta z \, i(z,t) - L \Delta z \frac{\partial i(z,t)}{\partial t} - v(z + \Delta z, t) = 0$$

Dividindo por $\Delta z$ e tomando o limite infinitesimal $\Delta z \to 0$:

$$\boxed{\frac{\partial v(z,t)}{\partial z} = -R\, i(z,t) - L \frac{\partial i(z,t)}{\partial t}}$$

Aplicando a Lei de Kirchhoff das Correntes (LKC) no nó superior:

$$i(z,t) - G \Delta z \, v(z + \Delta z, t) - C \Delta z \frac{\partial v(z + \Delta z, t)}{\partial t} - i(z + \Delta z, t) = 0$$

$$\boxed{\frac{\partial i(z,t)}{\partial z} = -G\, v(z,t) - C \frac{\partial v(z,t)}{\partial t}}$$

### Equações fasoriais, equação de onda de Helmholtz, constante de propagação γ e impedância característica Z_0

Em regime harmônico permanente senoidal ($e^{j\omega t}$), adotando a notação fasorial canônica com ponto superior ($\dot{V}, \dot{I}$):

$$\frac{d\dot{V}(z)}{dz} = -(R + j\omega L)\dot{I}(z) = -Z'\dot{I}(z)$$

$$\frac{d\dot{I}(z)}{dz} = -(G + j\omega C)\dot{V}(z) = -Y'\dot{V}(z)$$

Derivando novamente em relação à coordenada espacial $z$, obtêm-se as **Equações de Onda Fasoriais (Helmholtz)** desacopladas:

$$\frac{d^2\dot{V}(z)}{dz^2} - \gamma^2 \dot{V}(z) = 0 \qquad \text{e} \qquad \frac{d^2\dot{I}(z)}{dz^2} - \gamma^2 \dot{I}(z) = 0$$

onde a constante de propagação complexa $\gamma$ e a impedância característica de onda $Z_0$ são definidas por:

$$\gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)}, \qquad Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \quad [\Omega]$$

## Linha sem perdas e condição de distorção nula de Heaviside

Aproximação de alta frequência e a célebre proporção analítica para propagação não-dispersiva.

### Linha sem perdas: α = 0, β = ω√(LC), Z_0 = √(L/C) e velocidade de fase

No regime de altas frequências ($\omega L \gg R$ e $\omega C \gg G$), as perdas ôhmicas e condutivas tornam-se desprezíveis perante as reatâncias distribuídas ($R = 0, G = 0$), caracterizando a **linha sem perdas**:

$$\alpha = 0, \qquad \beta = \omega\sqrt{LC}, \qquad Z_0 = \sqrt{\frac{L}{C}} \in \mathbb{R}^+, \qquad v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{LC}} = \frac{c}{\sqrt{\mu_r \epsilon_r}}$$

### Condição de Heaviside RC = LG: linha sem distorção e dispersão nula

Em 1887, Heaviside demonstrou que se uma linha real com perdas satisfizer a proporção $R/L = G/C \iff RC = LG$, a constante de atenuação torna-se **rigorosamente independente da frequência**:

$$\alpha = \sqrt{RG}, \qquad \beta = \omega\sqrt{LC}, \qquad v_p = \frac{1}{\sqrt{LC}} = \text{constante}$$

Isso assegura que todas as componentes harmônicas de um sinal de banda larga propaguem-se com a mesma velocidade de fase, garantindo **dispersão nula** e permitindo telecomunicações transoceânicas de longa distância sem deformação morfológica dos pulsos.

## Reflexão, descasamento, onda estacionária e transformação de impedância

Padrões de interferência estacionária, TOE/VSWR, perda de retorno e impedância de entrada.

### Coeficiente de reflexão de tensão na carga Γ_L

Quando uma linha é terminada por uma impedância de carga arbitrária $Z_L \neq Z_0$, uma onda refletida surge na descontinuidade. O coeficiente de reflexão complexo de tensão na carga é:

$$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_L| e^{j\theta_L}$$

### Taxa de onda estacionária (TOE / VSWR / ROE)

$$\text{TOE} = \frac{|\dot{V}|_{\max}}{|\dot{V}|_{\min}} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|}$$

Correspondente à consagrada sigla em inglês **VSWR** (*Voltage Standing Wave Ratio*, ou SWR). Varia de $\text{TOE} = 1$ (linha perfeitamente casada) até $\text{TOE} \to \infty$ (curto-circuito ou circuito aberto).

### Perda de retorno (Return Loss) em dB

$$RL = -20 \log_{10}|\Gamma_L| \quad [\text{dB}]$$

Mede a fração da potência incidente que retorna à fonte. O critério industrial padrão de RF exige $RL \ge 14\text{ dB} \iff \text{TOE} \le 1{,}5$.

### Impedância de entrada Z_in(ℓ) da linha e convenção de coordenadas z e ℓ = −z

A impedância de entrada vista olhando-se para a linha a uma distância $\ell$ da terminação é deduzida combinando as ondas progressivas e regressivas:

$$\boxed{Z_{\text{in}}(\ell) = Z_0 \frac{Z_L + j Z_0 \tan(\beta \ell)}{Z_0 + j Z_L \tan(\beta \ell)}}$$

*Figura 4.2: Convenção canônica de coordenadas espaciais em regime permanente: eixo $z$ com origem no gerador ($z \in [-d, 0]$) e eixo $\ell = -z$ com origem na carga ($Z_L$ em $\ell = 0$). O desenho mostra o gerador $\dot{V}_g$ com impedância $Z_g$ à esquerda, a linha sem perdas ($Z_0, \beta$, com $\beta = \omega/v_p = \omega\sqrt{LC}$ e $Z_0 = \sqrt{L/C}$) de comprimento $d$ e a carga $Z_L$ à direita. A onda progressiva (incidente) é $V^+(z) = V_0^+ e^{-j\beta z} = V_0^+ e^{+j\beta\ell}$ e a onda regressiva (refletida) é $V^-(z) = V_0^- e^{+j\beta z} = V_0^- e^{-j\beta\ell}$. No desenho, o eixo $z$ aparece rotulado "Origem na Carga", com $z = -d$ no gerador e $z = 0$ na carga; o eixo $\ell = -z$ vai de $\ell = 0$ (carga) a $\ell = d$ (gerador).*

### Método matricial 2×2 para as amplitudes V_0^+ e V_0^- com gerador real (DEE/UFES)

Em problemas práticos com gerador real ($\dot{V}_g, Z_g$), a determinação rigorosa das amplitudes das ondas progressiva ($V_0^+$) e regressiva ($V_0^-$) é formulada no DEE/UFES através de um **sistema linear algébrico $2 \times 2$** que conecta a teoria de linhas de transmissão diretamente à Álgebra Linear:

$$\begin{bmatrix} \Gamma_L & -1 \\ e^{j\beta d} & e^{-j\beta d} \end{bmatrix} \begin{bmatrix} V_0^+ \\ V_0^- \end{bmatrix} = \begin{bmatrix} 0 \\ \dot{V}(-d) \end{bmatrix}$$

onde $\dot{V}(-d) = \dot{V}_g \frac{Z_{\text{in}}(-d)}{Z_g + Z_{\text{in}}(-d)}$. Essa modelagem viabiliza a solução computacional analítica imediata via Python (`numpy.linalg.solve`), obtendo-se instantaneamente $v(z,t)$ e $i(z,t)$ ao longo de toda a extensão da linha.

### Simulação em Python: distribuição de |V(z)| e |I(z)| na linha de 50 Ω com quatro cargas

Problema canônico (50 Ω). Para ilustrar a formulação matricial e o surgimento do padrão de onda estacionária, consideramos uma linha de transmissão sem perdas de $Z_0 = 50\,\Omega$ alimentada por gerador com $\dot{V}_g = 1{,}0\,\text{V}$ e $Z_g = 50\,\Omega$ em frequência de $f = 300\,\text{MHz}$ ($\lambda = 1{,}0\,\text{m}$) e comprimento físico de $d = 2{,}0\,\text{m} = 2\lambda$. Analisam-se as quatro condições de terminação canônicas.

*Figura 4.3: Simulação numérica em Python da distribuição espacial de $|V(z)|$ [V] e $10\cdot|I(z)|$ [A] ao longo da linha de $50\,\Omega$ para: (a) Carga Casada ($Z_L = 50\,\Omega$), (b) Carga Descasada ($Z_L = 200\,\Omega$), (c) Curto-Circuito ($Z_L = 0\,\Omega$) e (d) Circuito Aberto ($Z_L \to \infty$). Quatro gráficos com eixo horizontal $z$ de $-2$ m a $0$ m. (a) $|V| = 0{,}5$ e $10|I| = 0{,}1$ constantes. (b) $|V|$ oscila entre $0{,}2$ e $0{,}8$ (máximos em $z = 0, -0{,}5, -1{,}0, \ldots$) e $10|I|$ entre $0{,}04$ e $0{,}16$, em oposição. (c) $|V|$ oscila entre $0$ (nós em $z = 0, -0{,}5, \ldots$) e $1{,}0$; $10|I|$ entre $0$ e $0{,}2$ (máximo em $z = 0$). (d) Como o curto, mas deslocado: $|V| = 1{,}0$ e $|I| = 0$ em $z = 0$.*

### Carga casada (50 Ω) e carga descasada (200 Ω): TOE e padrão de onda estacionária

**1. Carga casada ($Z_L = 50\,\Omega$), $\Gamma_L = 0$.** Como $Z_L = Z_0$, o coeficiente de reflexão na carga é nulo ($\Gamma_L = 0$) e $\text{TOE} = 1{,}0$. Não há onda refletida ($V_0^- = 0$). As amplitudes de tensão ($0{,}5\,\text{V}$) e corrente ($10\,\text{mA}$) são rigorosamente constantes ao longo de toda a extensão da linha.

*Figura: simulação da linha casada de 50 Ω (mesmo gráfico do painel (a) da Figura 4.3).*

**2. Descasada ($Z_L = 200\,\Omega$), $\Gamma_L = +0{,}60$.** Reflexão parcial com $\text{TOE} = 4{,}0$. Na carga ($z=0$), a tensão atinge o máximo $|V|_{\max} = 0{,}8\,\text{V}$ e a corrente atinge o mínimo relativo $10|I| = 0{,}04$. O padrão estacionário oscila com período espacial de $\lambda/2 = 0{,}5\,\text{m}$.

*Figura: simulação da carga de 200 Ω (mesmo gráfico do painel (b) da Figura 4.3).*

### Curto-circuito e circuito aberto: nós e ventres de tensão e corrente na onda estacionária

**3. Curto-circuito ($Z_L = 0\,\Omega$), $\Gamma_L = -1$.** Reflexão total e onda puramente estacionária ($\text{TOE} \to \infty$). Na carga ($z=0$), ocorre nó de tensão ($|V(0)| = 0$) e ventre de corrente ($10|I(0)| = 0{,}20$). Nós de tensão repetem-se a cada $\lambda/2 = 0{,}5\,\text{m}$. Potência ativa média transmitida à carga é zero.

*Figura: simulação do curto-circuito (mesmo gráfico do painel (c) da Figura 4.3).*

**4. Circuito aberto ($Z_L \to \infty$), $\Gamma_L = +1$.** Reflexão total dual ao curto-circuito ($\text{TOE} \to \infty$). Na terminação ($z=0$), a tensão tem ventre ($|V(0)| = 1{,}0\,\text{V}$) e a corrente é estritamente nula ($|I(0)| = 0$). O padrão é defasado espacialmente de $\lambda/4 = 0{,}25\,\text{m}$ em relação ao curto.

*Figura: simulação do circuito aberto (mesmo gráfico do painel (d) da Figura 4.3).*

### Código Python da simulação da linha de 50 Ω (algoritmo matricial do Prof. Segatto)

Parâmetros físicos da linha e do gerador:

```python
import numpy as np
import matplotlib.pyplot as plt
    # Parâmetros Físicos da Linha e Gerador
c    = 3.0e8              # Velocidade no vácuo [m/s]
f    = 3.0e8              # Frequência [Hz] (300 MHz)
lamb = c / f              # Comprimento de onda: 1.0 m
beta = 2 * np.pi / lamb   # Constante de fase: 2*pi rad/m
Z0   = 50.0               # Impedância característica [Ohm]
ZG   = 50.0               # Impedância do gerador [Ohm]
VG   = 1.0                # Amplitude da fonte [V]
l    = 2.0                # Comprimento da linha [m] (2*lambda)
    # Cargas canônicas: 50 Ohms (casada), 200 Ohms, Curto (0) e Aberto (inf)
ZL_list = [50.0, 200.0, 0.0, 1e12]
z = np.linspace(-l, 0.0, 1000)
```

Laço sobre as cargas, com a solução do sistema matricial 2×2:

```python
for ZL in ZL_list:
    GammaL = (ZL - Z0) / (ZL + Z0) if ZL < 1e11 else 1.0
    tl = np.tan(beta * l)
    Zent = -1j * Z0 / tl if ZL > 1e11 else Z0 * (ZL + 1j * Z0 * tl) / (Z0 + 1j * ZL * tl)
    Vent = (Zent / (ZG + Zent)) * VG
    # Solução do Sistema Linear Matricial 2x2:
    # [GammaL   -1      ] [V0+] = [  0  ]
    # [exp(j*b*l) exp(-j*b*l)] [V0-] = [Vent]
    V0plus  = Vent / (np.exp(1j * beta * l) + GammaL * np.exp(-1j * beta * l))
    V0minus = V0plus * GammaL
```

Continuação do corpo do laço (ondas de tensão e corrente e gráficos):

```python
    # Ondas de Tensão e Corrente ao longo de z
    V = V0plus * np.exp(-1j * beta * z) + V0minus * np.exp(1j * beta * z)
    I = (V0plus / Z0) * np.exp(-1j * beta * z) - (V0minus / Z0) * np.exp(1j * beta * z)
    plt.figure()
    plt.plot(z, np.abs(V), label='|V(z)| [V]')
    plt.plot(z, 10 * np.abs(I), label='10*|I(z)| [A]')
    plt.xlabel('z [m]')
    plt.ylabel('Amplitude')
    plt.title(f'Simulação Linha 50 Ohm - ZL = {ZL} Ohm')
    plt.legend()
    plt.grid(True)
    plt.show()
```

## Terminações canônicas em regime permanente: curto, aberto, λ/4 e λ/2

Curto-circuito, circuito aberto, transformador de quarto de onda e repetidor de meia onda.

### Linha terminada em curto-circuito: Z_in = jZ_0 tan(βℓ), Z_L = 0 e Γ_L = −1

*Figura: linha de impedância $Z_0$ e comprimento $l$ com a extremidade da carga em curto (os dois condutores ligados por um fio); $Z_{ent}$ é a impedância vista na entrada.*

$$Z_{\text{in}}^{\text{cc}} = j Z_0 \tan(\beta \ell)$$

- Para $0 < \ell < \lambda/4$: reatância indutiva ($X > 0$);
- Para $\lambda/4 < \ell < \lambda/2$: reatância capacitiva ($X < 0$);
- Para $\ell = \lambda/4$: antirressonância ($Z_{\text{in}} \to \infty$).

### Linha terminada em circuito aberto: Z_in = −jZ_0 cot(βℓ), Z_L → ∞ e Γ_L = +1

*Figura: linha de impedância $Z_0$ e comprimento $l$ com a extremidade da carga em aberto (condutores desconectados); $Z_{ent}$ é a impedância vista na entrada.*

$$Z_{\text{in}}^{\text{ca}} = -j Z_0 \cot(\beta \ell)$$

- Para $0 < \ell < \lambda/4$: reatância capacitiva ($X < 0$);
- Para $\lambda/4 < \ell < \lambda/2$: reatância indutiva ($X > 0$);
- Para $\ell = \lambda/4$: ressonância série ($Z_{\text{in}} = 0$).

### Transformador de quarto de onda (ℓ = λ/4): inversor de impedâncias e casamento

$$Z_{\text{in}}(\lambda/4) = \frac{Z_0^2}{Z_L}$$

Atua como inversor de impedâncias. Permite casar perfeitamente uma linha de impedância $Z_1$ com uma carga real $R_L$ escolhendo $Z_0 = \sqrt{Z_1 R_L}$.

### Repetidor de meia onda (ℓ = λ/2): Z_in = Z_L

$$Z_{\text{in}}(\lambda/2) = Z_L$$

Replica rigorosamente o valor exato da impedância de carga, independentemente do valor da impedância característica $Z_0$ da linha intermediária.

## Linhas impressas e microfita (microstrip): estrutura planar e modo quase-TEM

Estrutura planar quase-TEM, campos de borda e formulações canônicas de Wheeler e Pozar.

A linha de microfita é a estrutura planar mais ubíqua da engenharia de RF e circuitos integrados de micro-ondas (MICs/MMICs). Consiste em uma fita condutora de largura $w$ depositada sobre a face superior de um substrato dielétrico de espessura $h$ e permissividade relativa $\epsilon_r$, cuja face oposta é integralmente metalizada, atuando como plano de terra.

### Modo quase-TEM, campos de borda (fringing) e permissividade efetiva da microfita

Como a estrutura é estratificada entre o ar superior ($\epsilon_0$) e o dielétrico inferior ($\epsilon_r \epsilon_0$), a velocidade de propagação nos dois meios difere, impossibilitando a existência de um modo TEM puro. Para substratos eletricamente finos ($h \ll \lambda$), a propagação ocorre como um **modo Quase-TEM (Quasi-TEM)** caracterizado por uma **permissividade dielétrica efetiva $\epsilon_{\text{eff}}$** ($1 < \epsilon_{\text{eff}} < \epsilon_r$).

*Figura 4.3: (a) Vista tridimensional explodida da linha de microfita com trilha condutora superior, dielétrico e plano de terra; (b) Distribuição transversal das linhas de campo elétrico e magnético em modo Quase-TEM com campos de borda (fringing).*

### Expressões canônicas de Wheeler, Hammerstad e Pozar para microfita

Modelos quase-estáticos fechados de alta precisão (erro relativo menor que 1% em relação a simulações de onda completa) para projeto e verificação de linhas planares de microfita.

### Microfita (análise): permissividade efetiva ε_eff e impedância característica Z_0 a partir de w, h e ε_r

Fórmulas de análise: $(w, h, \epsilon_r) \longrightarrow (\epsilon_{\text{eff}}, Z_0)$. A partir da geometria física da placa (largura $w$ e espessura do substrato $h$) e da permissividade do dielétrico ($\epsilon_r$), calcula-se a permissividade efetiva de fase e a impedância característica.

1. Permissividade dielétrica efetiva ($\epsilon_{\text{eff}}$):

$$\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2}\frac{1}{\sqrt{1 + 12\dfrac{h}{w}}}$$

2. Impedância característica ($Z_0$) calculada conforme a razão de aspecto $w/h$:

$$Z_0 = \begin{cases}
\dfrac{60}{\sqrt{\epsilon_{\text{eff}}}}\ln\left( \dfrac{8h}{w} + \dfrac{w}{4h} \right), & \text{para } \dfrac{w}{h} \le 1 \\[1.2em]
\dfrac{120\pi}{\sqrt{\epsilon_{\text{eff}}}\left[ \dfrac{w}{h} + 1{,}393 + 0{,}667\ln\left( \dfrac{w}{h} + 1{,}444 \right) \right]}, & \text{para } \dfrac{w}{h} > 1
\end{cases}$$

### Microfita (síntese de Wheeler/Pozar): razão w/h para linhas estreitas, Ramo 1 e coeficiente A

Fórmulas de síntese de Wheeler/Pozar: $(Z_0, h, \epsilon_r) \longrightarrow (w/h, w)$. No projeto de circuitos de RF, a especificação requer uma impedância nominal (geralmente $50\,\Omega$). A formulação de síntese determina a razão de aspecto necessária $w/h$ através de dois ramos analíticos complementares.

Ramo 1: linhas estreitas ($w/h \le 2$ ou $Z_0 \sqrt{\epsilon_r} \gtrsim 44\,\Omega$):

$$\frac{w}{h} = \frac{8e^A}{e^{2A} - 2}$$

onde o coeficiente adimensional $A$ é definido por:

$$A = \frac{Z_0}{60}\sqrt{\frac{\epsilon_r + 1}{2}} + \frac{\epsilon_r - 1}{\epsilon_r + 1}\left(0{,}23 + \frac{0{,}11}{\epsilon_r}\right)$$

### Microfita (síntese): linhas largas, Ramo 2, coeficiente B e regra de decisão A > 1,52

Ramo 2: linhas largas ($w/h > 2$ ou $Z_0 \sqrt{\epsilon_r} \lesssim 44\,\Omega$):

$$\frac{w}{h} = \frac{2}{\pi}\left[ B - 1 - \ln(2B - 1) + \frac{\epsilon_r - 1}{2\epsilon_r}\left\{ \ln(B - 1) + 0{,}39 - \frac{0{,}61}{\epsilon_r} \right\} \right]$$

onde o coeficiente adimensional $B$ é dado por:

$$B = \frac{377\pi}{2 Z_0 \sqrt{\epsilon_r}} = \frac{60\pi^2}{Z_0 \sqrt{\epsilon_r}}$$

**Regra prática de decisão:** calcula-se inicialmente o valor de $A$. Se $A > 1{,}52$, a linha satisfaz $w/h \le 2$ (Ramo 1). Se $A \le 1{,}52$, calcula-se $B$ e utiliza-se a formulação do Ramo 2.

### Exemplo numérico: projeto de microfita de 50 Ω em substrato FR-4 (largura da trilha w)

**Especificação de engenharia:** projetar uma linha casada de $Z_0 = 50\,\Omega$ sobre substrato comercial padrão FR-4 ($\epsilon_r = 4{,}4$, espessura $h = 1{,}6\text{ mm}$, $\tan\delta = 0{,}02$).

> [!success]- Solução
> 1. **Cálculo do coeficiente $A$:**
> 
> $$A = \frac{50}{60}\sqrt{\frac{4{,}4 + 1}{2}} + \frac{4{,}4 - 1}{4{,}4 + 1}\left(0{,}23 + \frac{0{,}11}{4{,}4}\right) \approx 1{,}369 + 0{,}161 = \mathbf{1{,}530}$$
> 
> 2. **Aplicação do Ramo 1 ($A = 1{,}530 > 1{,}52 \implies w/h \le 2$):**
> 
> $$\frac{w}{h} = \frac{8e^{1{,}530}}{e^{3{,}060} - 2} = \frac{8 \times 4{,}618}{21{,}328 - 2} \approx \mathbf{1{,}912} \quad (\le 2 \implies \text{válido})$$
> 
> 3. **Largura física da trilha ($w$):**
> 
> $$w = 1{,}912 \times h = 1{,}912 \times 1{,}6\text{ mm} \approx \mathbf{3{,}06\text{ mm}}$$
> 
> 4. **Permissividade efetiva e velocidade de fase:**
> 
> $$\epsilon_{\text{eff}} \approx \mathbf{3{,}33}, \quad v_p = \frac{c}{\sqrt{\epsilon_{\text{eff}}}} = \frac{3 \times 10^8}{\sqrt{3{,}33}} \approx \mathbf{1{,}64 \times 10^8\text{ m/s}} \quad (54{,}8\% \text{ de } c)$$

### Laboratório virtual 1: calculadora e projetista de microfita (síntese e análise)

Simulação interativa (modelos de Wheeler & Pozar) que alterna entre **Projeto (Síntese: $Z_0 \to w$)** e **Verificação (Análise: $w \to Z_0$)**, desenhando o corte transversal da microfita com os campos elétricos confinados no dielétrico e os arcos de campos de borda (*fringing fields*) no ar. Os resultados exibidos são $w$, $w/h$, $Z_0$, $\epsilon_{\text{eff}}$, velocidade de fase $v_p$ e retardo; com os valores iniciais (FR-4, $50\,\Omega$) mostra $w = 3{,}059$ mm, $w/h = 1{,}912$, $\epsilon_{\text{eff}} = 3{,}330$, $v_p = 1{,}64 \times 10^8$ m/s (54,8% de $c$), retardo de 6,09 ns/m e "Ramo 1".

Substratos pré-definidos na calculadora: FR-4 Standard ($\epsilon_r = 4{,}4$, $h = 1{,}6$ mm); Rogers RO4003C ($\epsilon_r = 3{,}55$, $h = 0{,}813$ mm); Rogers RT/duroid 5880 ($\epsilon_r = 2{,}20$, $h = 0{,}787$ mm); Alumina 96% ($\epsilon_r = 9{,}80$, $h = 0{,}635$ mm); ou personalizado. Faixas dos controles: $Z_0$ de 20 a 120 Ω, $w$ de 0,2 a 12 mm, $h$ de 0,2 a 3,5 mm e $\epsilon_r$ de 1,0 a 12,0.

## Carta de Smith: fundamentos matemáticos e aplicações

A transformação conforme bilinear de Phillip H. Smith, topologia no plano complexo e metodologia de casamento de impedâncias.

### História da Carta de Smith: Phillip H. Smith (1939) e Tosaku Mizuhashi (1937)

*Figura: retrato de Phillip H. Smith (1905–1987), Bell Labs & RCA.*

"Desde a época em que comecei a calcular linhas de transmissão com réguas de cálculo, procurei uma representação gráfica que eliminasse as tediosas repetições com funções hiperbólicas complexas." (Phillip H. Smith)

Desenvolvida em 1939 por **Phillip Hagar Smith** (e formulada de forma independente no Japão por Tosaku Mizuhashi em 1937), a **Carta de Smith** é o mais célebre ábaco gráfico da engenharia de RF e micro-ondas. Ela converte cálculos algébricos intrincados de ondas estacionárias e transformações de impedância em trajetórias geométricas diretas e intuitivas.

### Transformação conforme bilinear de Möbius: impedância normalizada z e coeficiente de reflexão Γ

Seja uma linha com impedância característica real $Z_0$ conectada a uma carga $Z_L = R_L + jX_L$. Definimos a **impedância normalizada** adimensional $z = Z_L / Z_0 = r + jx$. A relação biunívoca com o coeficiente de reflexão complexo $\Gamma = u + jv = |\Gamma|e^{j\theta}$ é expressa pela **transformação bilinear de Möbius**:

$$\Gamma = \frac{z - 1}{z + 1} \iff z = \frac{1 + \Gamma}{1 - \Gamma} = \frac{1 + (u+jv)}{1 - (u+jv)}$$

### Mapeamento conforme: retas r e x constantes viram círculos no plano Γ e |Γ| ≤ 1

Como a derivada complexa $\frac{d\Gamma}{dz} = \frac{2}{(z+1)^2} \neq 0$ para qualquer carga passiva ($r \ge 0$), essa função é holomorfa e constitui um **mapeamento conforme**: preserva rigorosamente a magnitude e o sentido dos ângulos entre curvas no plano complexo.

Por conseguinte, as famílias ortogonais de retas $r = \text{constante}$ e $x = \text{constante}$ no plano $z$ transformam-se em **círculos e arcos mutuamente ortogonais** no plano $\Gamma$. Além disso, todo o semiplano infinito $r \ge 0$ fica compactado dentro do **círculo unitário fechado $|\Gamma| \le 1$**.

### Dedução analítica das partes real r e imaginária x em função de u e v

Multiplicando o numerador e o denominador de $z = \frac{(1+u) + jv}{(1-u) - jv}$ pelo conjugado complexo do denominador $[(1-u) + jv]$:

$$r + jx = \frac{[(1+u) + jv][(1-u) + jv]}{(1-u)^2 + v^2} = \frac{(1 - u^2 - v^2) + j(2v)}{(1 - u)^2 + v^2}$$

$$\boxed{r = \frac{1 - u^2 - v^2}{(1 - u)^2 + v^2}} \qquad \text{e} \qquad \boxed{x = \frac{2v}{(1 - u)^2 + v^2}}$$

### Círculos de resistência r constante na Carta de Smith: centro e raio

$$\left( u - \frac{r}{1+r} \right)^2 + v^2 = \left( \frac{1}{1+r} \right)^2$$

- **Centro:** $\left(\frac{r}{1+r}, \, 0\right)$ sobre o eixo horizontal real;
- **Raio:** $R_r = \frac{1}{1+r}$;
- **Tangência universal:** todos os círculos tangenciam internamente o ponto $(1, 0)$ de circuito aberto ($r \to \infty$);
- Para $r = 0$, temos a circunferência unitária externa $|\Gamma| = 1$.

### Arcos de reatância x constante na Carta de Smith: centro, raio, indutivo e capacitivo

$$(u - 1)^2 + \left( v - \frac{1}{x} \right)^2 = \left( \frac{1}{x} \right)^2$$

- **Centro:** $\left(1, \, \frac{1}{x}\right)$ localizados sobre a reta vertical $u = 1$;
- **Raio:** $R_x = \frac{1}{|x|}$;
- **Semiplano superior ($x > 0$):** reatâncias indutivas ($+j\omega L$);
- **Semiplano inferior ($x < 0$):** reatâncias capacitivas ($-j/\omega C$);
- Para $x = 0$, degenera no próprio **eixo real central** ($v = 0$).

### Topologia e pontos notáveis da Carta de Smith: casamento, curto-circuito, circuito aberto e regiões indutiva e capacitiva

| Região / Ponto | Plano $\Gamma$ $(u, v)$ | Impedância $z$ | TOE / VSWR | Significado Físico em RF |
|---|---|---|---|---|
| Centro da Carta | $(0, 0)$ | $1 + j0$ | $1{,}00$ | **Casamento Perfeito:** $Z_L = Z_0$, sem nenhuma reflexão de potência ($\Gamma = 0$). |
| Extremo Esquerdo | $(-1, 0)$ | $0 + j0$ | $\infty$ | **Curto-Circuito:** Tensão nula, reflexão total com inversão de fase ($\Gamma = -1$). |
| Extremo Direito | $(+1, 0)$ | $\infty$ | $\infty$ | **Circuito Aberto:** Corrente nula, reflexão total em fase ($\Gamma = +1$). |

| Região / Ponto | Plano $\Gamma$ $(u, v)$ | Impedância $z$ | TOE / VSWR | Significado Físico em RF |
|---|---|---|---|---|
| Perímetro Unitário | $u^2 + v^2 = 1$ | $0 + jx$ | $\infty$ | **Fronteira Reativa Pura:** Resistência nula ($r = 0$), $100\%$ de reflexão de potência. |
| Semiplano Superior | $v > 0$ | $r + jx \ (x > 0)$ | $> 1$ | **Região Indutiva:** A tensão adianta-se em relação à corrente na carga ($x > 0$). |
| Semiplano Inferior | $v < 0$ | $r - jx \ (x < 0)$ | $> 1$ | **Região Capacitiva:** A corrente adianta-se em relação à tensão na carga ($x < 0$). |

*Figura 4.4: Mapeamento conforme bilinear entre o semiplano complexo de impedâncias $z = r + jx$ e o círculo unitário $|\Gamma| \le 1$ no plano de reflexão $\Gamma = u + jv$, gerando os círculos de resistência constante $r$ e arcos de reatância constante $x$ da Carta de Smith.*

### Coeficiente de reflexão ao longo da linha Γ(ℓ) e círculo de TOE constante (VSWR)

Em uma linha de transmissão sem perdas ($\alpha = 0$), o coeficiente de reflexão na posição $\ell$ (medida da carga em direção ao gerador) é dado por:

$$\Gamma(\ell) = \Gamma_L e^{-j 2\beta \ell} = |\Gamma_L| e^{j(\theta_L - 2\beta \ell)}$$

Como $|\Gamma(\ell)| = |\Gamma_L| = \text{constante}$, caminhar ao longo de uma linha sem perdas corresponde a percorrer uma **circunferência concêntrica à origem**. O valor numérico da TOE é lido diretamente no cruzamento com o eixo horizontal positivo ($u > 0$):

$$r_{\text{max}} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \text{TOE}$$

### Regra de rotação na Carta de Smith: sentido horário em direção ao gerador e período de λ/2

Conforme nos afastamos da carga em direção ao gerador ($\ell$ cresce), a fase varia por $-2\beta\ell$, gerando uma rotação no **sentido horário** (*Toward Generator*). Uma volta completa de $360^\circ$ ocorre para:

$$2\beta\ell = 2\pi \iff 2\left(\frac{2\pi}{\lambda}\right)\ell = 2\pi \iff \boxed{\ell = \frac{\lambda}{2}}$$

Uma volta inteira na Carta equivale a apenas meia onda na linha física.

### Carta de admitâncias (Y): conversão z ↔ y por rotação de 180° e círculo de condutância g = 1

Para circuitos em paralelo (como *stubs* em derivação), somam-se admitâncias normalizadas $y = Y / Y_0 = g + jb = 1/z$. Como $\Gamma_y = -\Gamma_z = \Gamma_z e^{\pm j180^\circ}$, converter $z \leftrightarrow y$ equivale a uma **rotação de $180^\circ$ ($\lambda/4$)** sobre o mesmo círculo de TOE. O círculo de **condutância $g = 1$** passa pelo centro e serve de órbita de captura para casamentos em derivação.

### Algoritmo de casamento de impedâncias por stub simples paralelo na Carta de Smith

1. **Plote a carga normalizada $z_L$:** trace o círculo de TOE concêntrico com raio $|\Gamma_L|$;
2. **Desloque-se pela linha principal ($d$):** gire no sentido horário (em direção ao gerador) até interceptar o círculo $g = 1$, onde a admitância é $y(d) = 1 + jb_1$;
3. **Anule a susceptância com o *stub* ($\ell_s$):** conecte em paralelo um trecho de linha em curto ou aberto com susceptância oposta:

$$b_{\text{stub}} = -b_1 \implies y_{\text{total}} = 1 + j0$$

4. **Conclusão:** a impedância resultante vista pelo transmissor é $Z_{\text{in}} = Z_0$ ($\text{TOE} = 1{,}00$).

### Exemplo de casamento por stub simples paralelo: carga z_L = 0,4 + j0,6 em Z_0 = 50 Ω

Exemplo ilustrado: casar a carga normalizada $z_L = 0{,}4 + j0{,}6$ (em $Z_0 = 50\,\Omega$) com um *stub* simples paralelo.

> [!success]- Solução
> $z_L = 0{,}4 + j0{,}6 \implies d_1 = 0{,}327\,\lambda$, $y(d_1) = 1 + j1{,}34$, cancelado por stub indutivo em curto de $\ell_s = 0{,}102\,\lambda$ (ou aberto de $0{,}352\,\lambda$).
> 
> *Figura 4.5: Trajetória de casamento de impedâncias por stub simples paralelo na Carta de Smith ($z_L = 0{,}4 + j0{,}6$ em $Z_0 = 50\,\Omega$). O desenho mostra o ponto $z_L = 0{,}4 + j0{,}6$ no semiplano indutivo ($x > 0$), o círculo de TOE constante ($|\Gamma| = 0{,}56$, em verde), a rotação $d_1 = 0{,}327\,\lambda$ ao longo desse círculo até o ponto $y(d_1) = 1 + j1{,}34$ sobre o círculo $g = 1$ (tracejado em vermelho), e o arco do stub indutivo $jb_s = -j1{,}34$ levando ao centro $z = 1$ ($y = 1$). Também aparecem o círculo $r = 1$, a segunda solução "Sol. 2 ($d_2$)" e os pontos de curto (esquerda) e aberto (direita).*

### Laboratório virtual 2: missões e desafios da Carta de Smith (simulação interativa)

Simulação interativa da Carta de Smith com três missões educacionais (Missão 1: transformador $\lambda/4$; Missão 2: reatância indutiva; Missão 3: stub único na carta de admitâncias $Y$) e um modo livre, em que se movem a resistência normalizada $r = R_L/Z_0$ e a reatância normalizada $x = X_L/Z_0$ (ou se clica na carta) e se leem $Z_L$, $\Gamma = |\Gamma|\angle\theta$, TOE/VSWR e perda de retorno em dB para $Z_0 = 50\,\Omega$. A carta mostra o círculo $|\Gamma| = 1$, o círculo de TOE constante e a trajetória da missão; o nível de casamento é classificado como severo ($\text{TOE} > 3$), moderado ($1{,}5$ a $3$), excelente ($\le 1{,}5$) ou ideal ($1{,}00$).

Primeiro passo da Missão 1 (transformador de quarto de onda): a carga real é $R_L = 200\,\Omega$. Normalizando em relação à linha principal ($Z_0 = 50\,\Omega$):

$$z_L = \frac{R_L}{Z_0} = \frac{200}{50} = 4{,}0$$

O ponto situa-se no eixo real direito com $\text{TOE} = 4{,}00$ (descasamento severo com $36\%$ de potência refletida, $|\Gamma| = 0{,}60$). Ao final, a missão é cumprida quando a carga fica perfeitamente casada com a linha ($Z_{\text{in}} = Z_0$, $\text{TOE} = 1{,}00$).

## Referências

- **POZAR, David M.** *Microwave Engineering*. 4th ed. Hoboken, NJ: John Wiley & Sons, 2012. (Capítulo 2: Transmission Line Theory; Capítulo 3: Transmission Lines and Waveguides; Capítulo 5: Impedance Matching and Tuning).
- **CHENG, David K.** *Field and Wave Electromagnetics*. 2nd ed. Reading, MA: Addison-Wesley, 1989. (Capítulo 9: Distributed TEM Waves and Transmission Lines).
- **BALANIS, Constantine A.** *Advanced Engineering Electromagnetics*. 2nd ed. Hoboken, NJ: John Wiley & Sons, 2012.
- **EDWARDS, Terry C.; STEER, Michael B.** *Foundations for Microstrip Circuit Design*. 4th ed. Chichester: John Wiley & Sons, 2016.
- **SMITH, Phillip H.** "Transmission Line Calculator." *Electronics*, v. 12, n. 1, p. 29–31, Jan. 1939.
- **HEAVISIDE, Oliver.** *Electromagnetic Theory*. London: The Electrician Printing and Publishing Co., 1893.
