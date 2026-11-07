---
fonte: "Material do professor: Matrizes de Redes e Dispositivos de RF"
pagina: "https://app.in-foton.org/eletromagnetismo/matrizes-dispositivos-rf.html"
---

# Matrizes de Redes e Dispositivos de Radiofrequência

Módulo [MOD-MAT], bloco compartilhado entre Eletromagnetismo e Engenharia de RF: matrizes [ABCD] ↔ [S].

Da formulação analítica das ondas de potência de Kurokawa e parâmetros $[S]$, divisores de Wilkinson com análise de modos par e ímpar à síntese planar de filtros de micro-ondas via Richards e Kuroda.

## Por que matrizes de espalhamento [S] em radiofrequência e micro-ondas

Em frequências de rádio e micro-ondas, onde as dimensões físicas dos circuitos tornam-se da ordem do comprimento de onda ($\ell \sim \lambda$), os conceitos clássicos de circuitos lumped (tensões e correntes totais de Kirchhoff) perdem o significado físico direto devido a fenômenos de propagação e reflexão de ondas.

### Limitações da medição das matrizes [Z] e [Y] em altas frequências (circuito aberto e curto-circuito)

Além disso, a medição das matrizes de impedância $[Z]$ ou admitância $[Y]$ exigiria a aplicação de circuitos abertos ou curtos-circuitos perfeitos nas portas. Em altas frequências, tais condições apresentam severas limitações práticas:

- **Radiação e efeitos parasitas:** um condutor em aberto atua como uma antena irradiando energia, enquanto um curto-circuito real possui indutância de fiação mensurável.
- **Instabilidade de circuitos ativos:** transistores e amplificadores de RF frequentemente oscilam quando terminados em curto ou aberto.
- **Impossibilidade em guias de onda:** em guias de ondas ocos ou substratos de circuito integrado, não há condutores isolados para definir tensão terminal unívoca.

### Ondas de potência incidentes e refletidas de Kurokawa: rede de N portas

A solução elegante consagrada por **K. Kurokawa (1965)** é descrever as redes de RF por meio de **ondas de potência normalizadas incidentes ($a_n$) e refletidas ($b_n$)**, medidas com terminações casadas na impedância característica de referência $Z_{0n}$ (geralmente $50\,\Omega$).

*Figura 1: Representação de uma rede de micro-ondas de $N$ portas alimentada por linhas de transmissão com ondas de potência incidentes $a_n$ e emergentes $b_n$. O desenho mostra um bloco (a rede) com N linhas de acesso, cada uma com um plano de referência $t_1, t_2, \ldots, t_N$; em cada porta, setas vermelhas entrando indicam a onda incidente ($\dot V_n^+, \dot I_n^+$) e setas azuis saindo indicam a onda emergente ($\dot V_n^-, -\dot I_n^-$).*

### Definição analítica das ondas de potência de Kurokawa e potência na porta

$$a_n = \frac{V_n + Z_{0n} I_n}{2\sqrt{Z_{0n}}}, \qquad b_n = \frac{V_n - Z_{0n} I_n}{2\sqrt{Z_{0n}}}$$

A potência média líquida transmitida para o interior da rede através da porta $n$ é expressa de forma desacoplada por:

$$P_n = \frac{1}{2} \text{Re}\{ V_n I_n^* \} = \frac{1}{2} |a_n|^2 - \frac{1}{2} |b_n|^2$$

### Matriz de espalhamento [S]: definição b = [S] a e parâmetros S_ij

A matriz de espalhamento $[S]$ mapeia o vetor de ondas incidentes no vetor de ondas refletidas através da relação linear matricial:

$$\mathbf{b} = [S] \, \mathbf{a} \implies \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_N \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} & \cdots & S_{1N} \\ S_{21} & S_{22} & \cdots & S_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ S_{N1} & S_{N2} & \cdots & S_{NN} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_N \end{bmatrix}$$

### Propriedade de reciprocidade: matriz [S] simétrica

Se a rede for composta exclusivamente por materiais isotrópicos e lineares (sem plasma magnetizado ou ferritas com campo magnético externo polarizante), a matriz de espalhamento é estritamente **simétrica**:

$$[S] = [S]^T \iff S_{ij} = S_{ji}$$

### Propriedade de redes sem perdas: matriz [S] unitária (unitariedade)

Para uma rede passiva sem perdas dissipativas (conservação integral de energia eletromagnética), a matriz de espalhamento é **unitária**:

$$[S]^\dagger [S] = [I] \implies \sum_{k=1}^N |S_{ki}|^2 = 1 \quad \text{e} \quad \sum_{k=1}^N S_{ki} S_{kj}^* = 0 \quad (i \neq j)$$

## Matrizes de parâmetros de redes de 2 portas ([Z], [Y], [ABCD]) e associações de quadripolos

A representação de quadripolos em micro-ondas permite a análise de módulos cascateados, filtros em seções periódicas e elementos em série/paralelo através de diferentes conjuntos de matrizes equivalentes.

### Associação em série de quadripolos: soma das matrizes de impedância [Z]

*Figura: associação série de quadripolos. Dois blocos (Dispositivo 1 e Dispositivo 2) com as portas ligadas em série, de modo que a mesma corrente $\dot I_1$ entra na porta de entrada e a mesma corrente $\dot I_2$ na porta de saída; tensões $\dot V_1$ e $\dot V_2$ indicadas nos terminais externos.*

$$[Z_{\text{eq}}] = [Z_A] + [Z_B]$$

Correntes de entrada e saída são idênticas em ambas as redes ($I_{1A} = I_{1B}$ e $I_{2A} = I_{2B}$).

### Associação em paralelo de quadripolos: soma das matrizes de admitância [Y]

*Figura: associação paralelo de quadripolos. Dois blocos (Dispositivo 1 e Dispositivo 2) com as portas de entrada ligadas em paralelo e as portas de saída ligadas em paralelo, compartilhando as tensões $\dot V_1$ e $\dot V_2$; correntes externas $\dot I_1$ e $\dot I_2$ indicadas.*

$$[Y_{\text{eq}}] = [Y_A] + [Y_B]$$

Tensões de entrada e saída são comuns aos dois blocos ($V_{1A} = V_{1B}$ e $V_{2A} = V_{2B}$).

### Associação em cascata de quadripolos: produto das matrizes de transmissão [ABCD]

*Figura: associação em cascata. Blocos Dispositivo 1, Dispositivo 2, ..., Dispositivo N ligados em sequência, a saída de um alimentando a entrada do seguinte; $\dot V_1$ e $\dot I_1$ na entrada e $\dot V_2$ e $\dot I_2$ na saída (no desenho, a seta de $\dot I_2$ aponta para dentro da rede).*

$$[ABCD_{\text{eq}}] = [ABCD_A] \cdot [ABCD_B]$$

A saída do bloco A alimenta a entrada do bloco B. Notação com $I_2$ saindo da rede.

### Conversão da matriz de transmissão [ABCD] para a matriz de espalhamento [S]

Conversão $[ABCD] \to [S]$ (com $Z_0$ idêntico em ambas as portas):

$$\Delta_s = A + \frac{B}{Z_0} + C Z_0 + D$$

$$S_{11} = \frac{A + B/Z_0 - C Z_0 - D}{\Delta_s}, \quad S_{12} = \frac{2(AD - BC)}{\Delta_s}$$

$$S_{21} = \frac{2}{\Delta_s}, \quad S_{22} = \frac{-A + B/Z_0 - C Z_0 + D}{\Delta_s}$$

### Conversão da matriz de espalhamento [S] para a matriz de transmissão [ABCD]

Conversão $[S] \to [ABCD]$:

$$A = \frac{(1 + S_{11})(1 - S_{22}) + S_{12} S_{21}}{2 S_{21}}$$

$$B = Z_0 \frac{(1 + S_{11})(1 + S_{22}) - S_{12} S_{21}}{2 S_{21}}$$

$$C = \frac{1}{Z_0} \frac{(1 - S_{11})(1 - S_{22}) - S_{12} S_{21}}{2 S_{21}}$$

$$D = \frac{(1 - S_{11})(1 + S_{22}) + S_{12} S_{21}}{2 S_{21}}$$

### Calculadora e conversor de redes de RF: matrizes [ABCD] e [S] (simulação interativa)

A página traz uma calculadora interativa de quadripolos em RF: seleciona-se uma topologia de rede de 2 portas (linha de transmissão TEM com impedância $Z_{01}$ e comprimento elétrico $\theta$, impedância em série $Z_s = R + jX$ ou admitância em derivação/paralelo $Y_p = G + jB$) e a impedância de referência do sistema $Z_0$, obtendo simultaneamente a matriz de transmissão em cascata $[ABCD]$ e a matriz de espalhamento $[S]$ normalizada para $Z_0$, além de métricas de RF (perda de inserção, perda de retorno e potência).

## Dispositivos passivos de micro-ondas: junções T, divisores e acopladores

### Teorema fundamental das redes de três portas: sem perdas, recíproca e casada

**É matematicamente impossível construir uma rede passiva de 3 portas que seja simultaneamente sem perdas dissipativas, perfeitamente recíproca e casada em todas as três portas.**

Demonstração: Se a rede é casada ($S_{ii} = 0$) e recíproca ($S_{ij} = S_{ji}$), a imposição da condição unitária $[S]^\dagger [S] = [I]$ produz um sistema de equações sem solução não nula simultânea para todas as linhas e colunas.

### Divisor de potência de Wilkinson (1960): resistor de isolamento R = 2Z_0

Publicado por **Ernest J. Wilkinson** no artigo clássico *"An N-Way Hybrid Power Divider"*, este dispositivo supera a restrição do teorema das 3 portas introduzindo um **resistor de isolamento interno de $R = 2 Z_0$**.

Quando o sinal entra pela **Porta 1**, divide-se em partes iguais em amplitude e fase nos dois braços de $\lambda/4$ de impedância $Z_{01} = \sqrt{2} Z_0$. Os nós das portas 2 e 3 encontram-se rigorosamente no mesmo potencial ($V_2 = V_3$), de modo que **nenhuma corrente flui pelo resistor** (dissipação nula, operando sem perdas para a divisão de potência).

Quando sinais entram pelas portas 2 ou 3 (desbalanceamento ou reflexões da carga), o resistor absorve integralmente a energia da onda refletida no modo ímpar, garantindo **isolamento ideal ($S_{23} = S_{32} = 0$)** e casamento simultâneo em todas as portas.

*Figura 2: Topologia planar em microfita do Divisor de Wilkinson de $3\,\text{dB}$ com braços de quarto de onda e resistor de isolamento de $100\,\Omega$. O desenho mostra a linha de entrada $Z_0$ que se bifurca em dois braços curvos de impedância $\sqrt{2}Z_0$ e comprimento $\lambda/4$, o resistor $2Z_0$ ligado entre as extremidades dos braços e as duas linhas de saída $Z_0$, sobre o substrato.*

### Simulador do divisor de Wilkinson de 3 dB: síntese em microfita e curvas S11, S21, S23, S22

A página traz um projetista e simulador do divisor de Wilkinson de 3 dB (síntese microstrip e modos par/ímpar): define-se a frequência de projeto $f_0$, a impedância de referência $Z_0$ e o substrato planar (FR-4 com $\varepsilon_r = 4.4$ e $h = 1.6$ mm; Rogers RO4003C com $\varepsilon_r = 3.55$ e $h = 0.813$ mm; Rogers RT/duroid 5880 com $\varepsilon_r = 2.20$ e $h = 0.787$ mm; Alumina 96% com $\varepsilon_r = 9.80$ e $h = 0.635$ mm) para sintetizar a máscara física com dimensões de Wheeler/Pozar e simular as curvas de espalhamento ($S_{11}, S_{21}, S_{23}, S_{22}$) de 0.2 $f_0$ a 1.8 $f_0$.

Na configuração inicial (2.40 GHz, $Z_0 = 50\,\Omega$, FR-4), os parâmetros sintetizados mostrados são: trilhas $50\,\Omega$ ($w_0$) = 3.06 mm; braços $70.7\,\Omega$ ($w_1$) = 1.62 mm; comprimento $\lambda/4$ ($\ell$) = 16.9 mm; resistor de isolamento ($R=2Z_0$) = 100.0 Ω.

**Propriedades notáveis em $f_0$:** Casamento ideal em todas as portas ($S_{11} = S_{22} = S_{33} = 0$), isolamento perfeito entre as saídas ($S_{23} = -\infty\text{ dB}$) e divisão exata de potência de metade para cada ramo ($|S_{21}| = |S_{31}| = -3.01\text{ dB}$).

### Acopladores direcionais de 4 portas: branch-line (híbrida de 90°) e anel híbrido rat-race (híbrida de 180°)

Redes de quatro portas sem perdas e recíprocas podem ser perfeitamente casadas e fornecer acoplamento controlado de potência com defasamento em quadratura ($90^\circ$) ou contrafase ($180^\circ$):

- **Acoplador Branch-Line (Híbrida de $90^\circ$):** composto por quatro linhas de $\lambda/4$ formando um anel retangular. Divide a potência igualmente entre as portas através e acoplada com defasamento relativo fixo de $90^\circ$, isolando a quarta porta;
- **Híbrida em Anel Rat-Race (Híbrida de $180^\circ$):** anel circular de perímetro $1.5 \lambda$ (três seções de $\lambda/4$ e uma seção de $3\lambda/4$). Atua como somador e subtrator vetorial de sinais de RF.

*Figura 3: Híbrida planar em anel (Rat-Race) para processamento analógico de sinais de RF. O desenho mostra, em microfita, um anel retangular de quatro portas: porta 1 (Entrada), porta 2 (Saída), porta 3 (Isolada) e porta 4 (Saída), todas com linhas de acesso $Z_0$; os dois ramos horizontais do anel têm impedância $Z_0/\sqrt{2}$, os dois verticais $Z_0$, e cada ramo tem comprimento $\lambda/4$.*

## Síntese e projeto de filtros de micro-ondas

### Etapas da síntese de filtros: protótipo passa-baixas, transformação de Richards e identidades de Kuroda

A metodologia clássica de síntese de filtros de RF por parâmetros distribuídos segue uma sequência rigorosa de transformações conforme ilustrado no fluxograma:

1. **Especificação:** frequência de corte $\omega_c$, atenuação mínima na banda de rejeição, ondulação na banda de passagem;
2. **Filtro protótipo passa-baixas lumped:** cálculo dos coeficientes $g_k$ para resposta Maximamente Plana (Butterworth) ou Chebyshev;
3. **Transformação de Richards:** substituição dos elementos indutores e capacitores por stubs de linhas de transmissão através da variável complexa de Richards $S = j \Omega = j \tan(\beta \ell)$;
4. **Identidades de Kuroda:** conversão de stubs em série (difíceis de fabricar em microfita) em stubs em derivação conectados através de linhas intermediárias (linhas unitárias) com casamento de impedâncias.

*Figura 4: Etapas sistemáticas de síntese de filtros planares de micro-ondas. Fluxograma: Início → Especificação Técnica → Normalização → Aproximação (Butterworth, Chebyshev, Elíptico, Kaiser, ...) → Função de rede → Realização → De-normalização → Satisfeito? Se sim (S), Fim; se não (N), volta à Especificação Técnica.*

## Referências

- POZAR, David M. *Microwave Engineering*. 4th ed. Hoboken, NJ: John Wiley & Sons, 2012. (Capítulo 4: Microwave Network Analysis; Capítulo 7: Power Dividers and Directional Couplers; Capítulo 8: Microwave Filters).
- COLLIN, Robert E. *Foundations for Microwave Engineering*. 2nd ed. New York: IEEE Press / McGraw-Hill, 2001.
- KUROKAWA, Kaneyuki. "Power Waves and the Scattering Matrix." *IEEE Transactions on Microwave Theory and Techniques*, v. MTT-13, n. 2, p. 194–202, Mar. 1965.
- WILKINSON, Ernest J. "An N-Way Hybrid Power Divider." *IRE Transactions on Microwave Theory and Techniques*, v. MTT-8, n. 1, p. 116–118, Jan. 1960.
- KURODA, K. "Filter networks having specified elements." *Journal of the Institute of Electrical Communication Engineers of Japan*, v. 38, p. 280–286, 1955.
- RICHARDS, P. I. "Resistor-Transmission-Line Circuits." *Proceedings of the IRE*, v. 36, n. 2, p. 217–220, Feb. 1948.
