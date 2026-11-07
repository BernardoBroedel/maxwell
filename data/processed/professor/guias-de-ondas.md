---
fonte: "Material do professor: Guias de Ondas"
pagina: "https://app.in-foton.org/eletromagnetismo/guias-de-ondas.html"
---
# Guias de Ondas Metálicos e Propagação Confinada

Módulo [MOD-GUI] (Guias de Ondas e Modos de Propagação), bloco compartilhado de Eletromagnetismo, RF e Fotônica: modos TE/TM e fibras. Docente: Prof. Marcelo Eduardo Vieira Segatto, Departamento de Engenharia Elétrica (DEE), UFES; laboratórios LabTel e IN-Foton.

Da quantização e autofunções de Helmholtz ao guia retangular oco, modos TE/TM, frequências de corte, simulador interativo de campos em tempo real, técnicas de excitação por sondas e laços, e conexões fundamentais com a fotônica integrada.

## 1. O que é um modo de propagação em guias de ondas

Quando uma onda eletromagnética propaga-se no espaço livre ou em um meio dielétrico infinito homogêneo, ela tem total liberdade espacial transversal para se expandir como uma onda plana uniforme ou um feixe gaussiano. Entretanto, ao introduzirmos **fronteiras materiais** — sejam elas paredes condutoras metálicas ou descontinuidades dielétricas —, o campo eletromagnético é forçado a satisfazer rigorosamente as condições de contorno de Maxwell em cada ponto dessas superfícies limítrofes.

### Definição físico-matemática de modo de propagação (autofunção de Helmholtz)

Um **modo de propagação** é uma *autofunção* do operador diferencial de Helmholtz espacial que satisfaz as condições de contorno da estrutura guiante. Fisicamente, um modo corresponde a uma configuração transversal de campos $\vec{E}_t(x,y)$ e $\vec{H}_t(x,y)$ cuja **forma geométrica permanece perfeitamente invariante** à medida que a energia se desloca ao longo da coordenada longitudinal de propagação ($z$), alterando-se unicamente em amplitude e fase temporal:

$$\vec{E}(x,y,z,t) = \text{Re}\left\{ \vec{e}(x,y) \, e^{-\gamma z} \, e^{j\omega t} \right\}, \qquad \vec{H}(x,y,z,t) = \text{Re}\left\{ \vec{h}(x,y) \, e^{-\gamma z} \, e^{j\omega t} \right\}$$

onde $\gamma = \alpha + j\beta$ é a constante de propagação complexa do modo específico.

### 1.1 Interpretação ondulatória: ondas planas em zigue-zague, quantização e interferência construtiva

A visualização clássica de um modo guiado é dada pela superposição de duas ou mais ondas planas uniformes que se propagam em zigue-zague, rebatendo nas paredes laterais da estrutura com um ângulo de incidência $\theta$ em relação à normal da parede (reflexão total e interferência construtiva em zigue-zague).

**Interferência Construtiva Transversal (Quantização):** Para que a onda guiada sobreviva ao longo de múltiplos rebates sem sofrer cancelamento destrutivo, a defasagem total sofrida por uma frente de onda ao atravessar o guia de um lado ao outro, refletir nas paredes e retornar à mesma posição deve ser um múltiplo inteiro de $2\pi$ radianos ($360^\circ$). Essa condição impõe a **quantização discreta** do número de onda transversal $k_x = \frac{m\pi}{a}$ e $k_y = \frac{n\pi}{b}$, onde os inteiros $(m, n)$ rotulam a ordem do modo.

### Condição de corte e regime evanescente abaixo da frequência de corte

**Condição de Corte ($\theta \to 0$):** À medida que a frequência de operação diminui, o vetor de onda no meio $k = \omega\sqrt{\mu\varepsilon}$ reduz-se. Para manter a defasagem transversal quantizada, as ondas planas precisam incidir cada vez mais perpendicularmente às paredes condutoras. Na *frequência de corte* ($f = f_c$), o ângulo de propagação longitudinal anula-se ($\beta = 0$): a onda simplesmente rebate de um lado para o outro em vaivém, sem qualquer deslocamento de energia ao longo de $z$.

**Regime Evanescente ($f < f_c$):** Abaixo da frequência de corte, o comprimento de onda no meio excede a largura permitida para fechar o ciclo de interferência construtiva. O número de onda longitudinal torna-se puramente imaginário ($\beta \to -j\alpha$), resultando em um decaimento espacial exponencial $e^{-\alpha z}$ sem transporte de potência real líquida. O guia atua como um *filtro passa-altas distribuído*.

### 1.2 Velocidade de fase e velocidade de grupo no guia: por que vp > c não viola a relatividade

Uma das aparentes contradições conceituais encontradas por estudantes em guias de ondas reside na velocidade de fase da crista da onda dentro do guia. Relação fundamental entre velocidade de fase ($v_p$) e de grupo ($v_g$):

$$v_p = \frac{\omega}{\beta} = \frac{v}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}} > v, \qquad v_g = \frac{d\omega}{d\beta} = v \sqrt{1 - \left(\frac{f_c}{f}\right)^2} < v$$

$$v_p \cdot v_g = v^2 = \frac{c^2}{\mu_r \varepsilon_r}$$

**Explicação Física:** A velocidade de fase $v_p$ representa a velocidade aparente com que um ponto de fase constante (por exemplo, a crista geométrica de cruzamento de duas frentes de onda em zigue-zague) desliza ao longo da parede do guia — semelhante ao ponto de corte de uma tesoura ao se fechar, que pode viajar a velocidades arbitrárias. *Nenhuma energia, matéria ou sinal de informação trafega em $v_p$*. A energia eletromagnética e a informação trafegam rigorosamente na **velocidade de grupo** $v_g$, a qual é estritamente subluminal ($v_g < c$).

### 1.3 Por que guias condutores ocos não suportam modos TEM

Um modo Transversal Eletromagnético (TEM) caracteriza-se por possuir simultaneamente $E_z = 0$ e $H_z = 0$. Substituindo essa condição nas equações rotacionais de Maxwell transversais, deduz-se que os campos no plano de corte transversal devem satisfazer às equações da eletrostática bidimensional:

$$\nabla_t \times \vec{E}_t = 0 \implies \vec{E}_t = -\nabla_t \Phi, \qquad \nabla_t \cdot \vec{E}_t = 0 \implies \nabla_t^2 \Phi = 0$$

Em um guia condutor oco simples (seja retangular, circular ou elíptico), toda a fronteira do contorno interno é formada por uma **única superfície metálica contínua e fechada**. Como um condutor perfeito em equilíbrio eletrodinâmico é uma equipotencial, temos $\Phi = V_0 = \text{constante}$ em toda a borda. Pelo *Teorema do Extremo da Equação de Laplace*, uma função harmônica sem fontes internas não pode apresentar máximos ou mínimos locais em seu domínio: ela deve ser estritamente constante em todo o volume interior:

$$\Phi(x,y) = V_0 \quad \forall (x,y) \in \text{interior} \implies \vec{E}_t = -\nabla_t \Phi = 0$$

**Conclusão Rigorosa:** Para que um modo TEM exista, são necessários no mínimo **dois condutores eletricamente isolados** mantidos em potenciais distintos (como ocorre em cabos coaxiais, linhas bifilares ou microfitas com plano de terra). Em um condutor tubular oco único, apenas modos com componentes longitudinais não nulas — **$\text{TE}$ ($H_z \neq 0$)** e **$\text{TM}$ ($E_z \neq 0$)** — são matematicamente e fisicamente admissíveis.

## 2. Guia retangular metálico oco: dedução rigorosa dos modos

Consideremos um tubo metálico condutor perfeito (PEC) estendendo-se ao longo do eixo $z$, com seção reta retangular de largura interna $a$ (ao longo do eixo $x$) e altura interna $b$ (ao longo do eixo $y$), preenchido por um meio isotrópico homogêneo de parâmetros $(\varepsilon, \mu)$. Por convenção de engenharia, orientamos o guia de modo que $a > b$.

### 2.1 Decomposição transversal: campos transversais em função de Ez e Hz (equações rotacionais)

Assumindo dependência harmônica temporal $e^{j\omega t}$ e dependência longitudinal $e^{-j\beta z}$, as derivadas em relação a $z$ simplificam-se para $\frac{\partial}{\partial z} \to -j\beta$. Expandindo as equações de Maxwell $\nabla \times \vec{E} = -j\omega\mu \vec{H}$ e $\nabla \times \vec{H} = j\omega\varepsilon \vec{E}$ componente a componente, obtemos o conjunto fundamental que expressa as 4 componentes transversais exclusivamente em função das duas componentes axiais $E_z$ e $H_z$.

Equações fundamentais de acoplamento transversal:

$$E_x = \frac{-j}{k_c^2} \left( \beta \frac{\partial E_z}{\partial x} + \omega\mu \frac{\partial H_z}{\partial y} \right), \qquad E_y = \frac{j}{k_c^2} \left( -\beta \frac{\partial E_z}{\partial y} + \omega\mu \frac{\partial H_z}{\partial x} \right)$$

$$H_x = \frac{j}{k_c^2} \left( \omega\varepsilon \frac{\partial E_z}{\partial y} - \beta \frac{\partial H_z}{\partial x} \right), \qquad H_y = \frac{-j}{k_c^2} \left( \omega\varepsilon \frac{\partial E_z}{\partial x} + \beta \frac{\partial H_z}{\partial y} \right)$$

onde $k_c^2 = k^2 - \beta^2$ é o autovalor transversal e $k = \omega\sqrt{\mu\varepsilon}$ é o número de onda intrínseco do meio.

### 2.2 Modos TE_mn (transversais elétricos) no guia retangular: condições de contorno e solução para Hz

Nos modos $\text{TE}$, temos por definição $E_z = 0$ e $H_z \neq 0$. A componente axial $H_z$ deve satisfazer à Equação de Helmholtz escalar bidimensional:

$$\left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + k_c^2 \right) H_z(x,y) = 0$$

Aplicando o método de **Separação de Variáveis**, postulamos $H_z(x,y) = X(x) Y(y)$. As condições de contorno de condutor elétrico perfeito (PEC) exigem que o campo elétrico tangencial às paredes se anule:

$$E_y(0,y) = 0, \quad E_y(a,y) = 0 \implies \left. \frac{\partial H_z}{\partial x} \right|_{x=0} = 0, \quad \left. \frac{\partial H_z}{\partial x} \right|_{x=a} = 0$$

$$E_x(x,0) = 0, \quad E_x(x,b) = 0 \implies \left. \frac{\partial H_z}{\partial y} \right|_{y=0} = 0, \quad \left. \frac{\partial H_z}{\partial y} \right|_{y=b} = 0$$

A solução geral que satisfaz a essas condições com derivadas nulas nas fronteiras é composta puramente por cossenos:

$$H_z(x,y,z) = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}, \quad (m,n = 0, 1, 2, \dots; \; m+n \ge 1)$$

### Componentes de campo dos modos TE_mn no guia retangular (Ex, Ey, Hx, Hy)

Substituindo $H_z$ nas equações de acoplamento transversal com $E_z = 0$, obtemos as componentes dos campos do modo $\text{TE}_{mn}$:

$$E_x(x,y) = \frac{j\omega\mu}{k_c^2} \left(\frac{n\pi}{b}\right) H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

$$E_y(x,y) = -\frac{j\omega\mu}{k_c^2} \left(\frac{m\pi}{a}\right) H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

$$H_x(x,y) = \frac{j\beta}{k_c^2} \left(\frac{m\pi}{a}\right) H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

$$H_y(x,y) = \frac{j\beta}{k_c^2} \left(\frac{n\pi}{b}\right) H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

### 2.3 Modos TM_mn (transversais magnéticos) no guia retangular: não existem TM10 nem TM01

Nos modos $\text{TM}$, temos $H_z = 0$ e $E_z \neq 0$. Como a componente $E_z$ é estritamente tangencial às quatro paredes condutoras em $x=0, a$ e $y=0, b$, a condição PEC impõe que ela se anule diretamente em todas as fronteiras:

$$E_z(0,y) = E_z(a,y) = E_z(x,0) = E_z(x,b) = 0$$

Assim, a separação de variáveis conduz a uma solução expressa pelo produto de senos:

$$E_z(x,y,z) = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}, \quad (m \ge 1, \; n \ge 1)$$

**Atenção Crucial:** Se $m=0$ ou $n=0$, a função seno anula-se identicamente ($\sin(0) = 0$), tornando todos os campos nulos. Portanto, **não existem modos $\text{TM}_{10}$ ou $\text{TM}_{01}$ em guias retangulares**. O modo de mais baixa ordem na família transversal magnética é o **$\text{TM}_{11}$**.

### 2.4 Frequência de corte, comprimento de onda de corte, constante de fase e comprimento de onda no guia retangular

O número de onda de corte é dado pela relação trigonométrica espacial $k_{c,mn}^2 = k_x^2 + k_y^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$. A partir dele, determinam-se todos os parâmetros de propagação da estrutura.

Frequência e comprimento de onda de corte:

$$f_{c,mn} = \frac{c}{2\sqrt{\mu_r \varepsilon_r}} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

$$\lambda_{c,mn} = \frac{2}{\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}}$$

Constante de fase e comprimento de onda no guia:

$$\beta = k \sqrt{1 - \left(\frac{f_{c,mn}}{f}\right)^2}$$

$$\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1 - \left(\frac{f_{c,mn}}{f}\right)^2}} > \lambda$$

### Impedância de onda dos modos TE e TM (impedâncias modais)

A razão entre as componentes de campo transversal elétrico e magnético define a **impedância de onda do modo**:

$$\eta_{\text{TE}} = \frac{E_x}{H_y} = -\frac{E_y}{H_x} = \frac{\eta}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}} > \eta, \qquad \eta_{\text{TM}} = \frac{E_x}{H_y} = -\frac{E_y}{H_x} = \eta \sqrt{1 - \left(\frac{f_c}{f}\right)^2} < \eta$$

### 2.5 Modo dominante TE10 do guia retangular: corte e campos

Para a geometria padrão $a > b$, o modo com a menor frequência de corte de toda a estrutura é obtido escolhendo-se $m=1$ e $n=0$: trata-se do **modo dominante $\text{TE}_{10}$**.

Propriedades singulares do modo $\text{TE}_{10}$:

$$f_{c,10} = \frac{c}{2a\sqrt{\mu_r\varepsilon_r}}, \qquad \lambda_{c,10} = 2a$$

Como $n=0$, o campo elétrico possui **unicamente componente vertical** ($E_x = 0$, $E_z = 0$ e $E_y \neq 0$), sem nenhuma variação ao longo da coordenada vertical $y$:

$$E_y(x) = -E_0 \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}, \qquad H_x(x) = \frac{E_0}{\eta_{\text{TE}}} \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}$$

$$H_z(x) = -j \frac{E_0}{\eta} \left(\frac{f_{c,10}}{f}\right) \cos\left(\frac{\pi x}{a}\right) e^{-j\beta z}$$

### Operação monomodo do guia retangular: projeto padrão a = 2b e faixa de uma oitava

**Projeto Monomodo Padrão ($a \approx 2b$):** Na engenharia de micro-ondas, escolhe-se deliberadamente a altura igual à metade da largura ($b = a/2$). Com essa proporção, as frequências de corte dos modos superiores imediatos tornam-se:

$$f_{c,20} = \frac{c}{2\sqrt{\mu_r\varepsilon_r}}\left(\frac{2}{a}\right) = 2 f_{c,10}, \qquad f_{c,01} = \frac{c}{2\sqrt{\mu_r\varepsilon_r}}\left(\frac{1}{b}\right) = \frac{c}{2\sqrt{\mu_r\varepsilon_r}}\left(\frac{2}{a}\right) = 2 f_{c,10}$$

Isso estabelece uma **faixa de passagem estritamente monomodo de uma oitava completa ($f_{c,10} < f < 2 f_{c,10}$)**, evitando dispersão intermodal e distorção de fase em pulsos de radar ou sinais digitais de micro-ondas.

## 3. Simulador interativo de modos no guia retangular metálico (padrões WR da EIA)

A página traz um laboratório virtual (DEE/UFES) em que o aluno ajusta a largura $a$, a altura $b$, a frequência $f$, a permissividade $\varepsilon_r$ e a permeabilidade $\mu_r$ do guia, escolhe um modo numa tabela de modos TE e TM (com corte $f_c$, estado propagante ou evanescente, $\beta$ e $\lambda_g$) e vê a distribuição transversal do campo $\vec{E}_t$, do campo $\vec{H}_t$ ou da densidade de potência $S_z$. Para o modo ativo, o simulador mostra frequência de corte, constante de fase $\beta$, comprimento de onda no guia $\lambda_g$, velocidades de fase e de grupo, impedância de onda e atenuação reativa $\alpha$.

Presets de guias retangulares padronizados (padrão industrial EIA) disponíveis no simulador:

| Guia | Banda | Faixa de operação | $a$ | $b$ |
|---|---|---|---|---|
| WR-90 | Banda X | 8.2 - 12.4 GHz | 22.86 mm | 10.16 mm |
| WR-62 | Banda Ku | 12.4 - 18.0 GHz | 15.80 mm | 7.90 mm |
| WR-28 | Banda Ka / 5G mmWave | 26.5 - 40.0 GHz | 7.11 mm | 3.56 mm |
| WR-284 | Banda S / Radares | 2.6 - 3.95 GHz | 72.14 mm | 34.04 mm |
| WR-12 | Banda E / W | 60 - 90 GHz | 3.10 mm | 1.55 mm |

Valores exibidos na configuração inicial (WR-90, $f = 10$ GHz, $\varepsilon_r = \mu_r = 1$, modo $\text{TE}_{10}$, propagante): frequência de corte $f_c = 6.557$ GHz; constante de fase $\beta = 158.5$ rad/m; comprimento no guia $\lambda_g = 39.63$ mm; velocidade de fase $v_p = 3.96 \times 10^8$ m/s; velocidade de grupo $v_g = 2.27 \times 10^8$ m/s; impedância de onda $\eta = 498.4\ \Omega$; atenuação reativa $\alpha = 0$ dB/cm.

## 4. Como excitar modos no guia retangular metálico

Para transferir energia de uma linha de transmissão convencional (como um cabo coaxial de $50\,\Omega$ conectado a um gerador de RF ou amplificador) para o interior de um guia de ondas metálico oco, é necessário utilizar uma estrutura de acoplamento transicional. Os métodos físicos baseiam-se no **Teorema da Reciprocidade de Lorentz** e no casamento com os perfis espaciais dos campos $\vec{E}$ ou $\vec{H}$ do modo desejado.

### 4.1 Sonda de campo elétrico (E-probe) para o modo TE10 e curto-circuito a λg/4 (backshort)

Consiste na extensão do condutor central de um conector coaxial (SMA ou tipo N) penetrando no interior do guia paralelamente às linhas de campo elétrico. A corrente no pino atua como uma fonte filamentar de corrente $\vec{J}$, excitando o campo $\vec{E}$.

Posicionamento para o modo $\text{TE}_{10}$ dominante:

- **Localização transversal:** No centro exato da parede larga superior ($x = a/2$), onde $E_y$ atinge seu valor máximo global.
- **Fundo de curto-circuito (Backshort):** A sonda é posicionada a uma distância rigorosa de **$\lambda_g / 4$** de uma tampa metálica de curto-circuito. A onda emitida para trás percorre $\lambda_g/4$, reflete no curto sofrendo defasagem de $180^\circ$ ($-1$) e percorre mais $\lambda_g/4$ de volta à sonda ($180^\circ$ adicionais). O atraso total de ida e volta é $360^\circ$ ($2\pi$), fazendo com que a onda refletida se some *perfeitamente em fase* com a onda emitida para frente.
- **Profundidade de inserção ($d$):** Ajusta o nível de acoplamento para casar os $50\,\Omega$ do coaxial com a alta impedância de onda $\eta_{\text{TE}} \approx 400 - 500\,\Omega$.

### 4.2 Laço de campo magnético (H-loop) para excitar o guia retangular

O pino central do coaxial é dobrado e soldado diretamente na parede condutora do guia, formando uma espira fechada. Pela Lei de Faraday-Lenz, a corrente de RF na espira cria um fluxo magnético alternado $\Phi_B$ que se acopla diretamente às linhas fechadas de $\vec{H}$.

Orientação e montagem:

- O plano do laço deve ser orientado *estritamente perpendicular* às linhas de indução magnética $\vec{H}$ do modo para interceptar o fluxo máximo.
- **Parede terminal de curto:** Excelente posição, pois na parede condutora de término o campo elétrico é forçado a zero ($\vec{E} = 0$), enquanto as correntes superficiais e o campo magnético transversal tangencial são máximos.
- **Parede lateral estreita ($x=0$ ou $x=a$):** Posição ideal para acoplar à componente longitudinal $H_z$, que atinge sua amplitude máxima justamente sobre essas paredes.

### 4.3 Acoplamento por fendas e íris (antenas de guia fendado, slotted waveguide arrays)

Utiliza pequenas aberturas perfuradas na parede comum entre dois guias adjacentes ou na face externa para radiação no espaço livre (antenas de fenda).

Princípio das correntes interrompidas:

- Nas paredes condutoras fluem correntes superficiais $\vec{J}_s = \hat{n} \times \vec{H}$.
- Uma fenda que corta transversalmente as linhas de $\vec{J}_s$ obriga a corrente a contornar a abertura, acumulando cargas nas bordas e excitando uma diferença de potencial que radia energia.
- Base de projeto dos famosos **arranjos de antenas em guias fendados** (*slotted waveguide arrays*), amplamente utilizados em radares navais, meteorológicos e de controle de tráfego aéreo.

### Excitação seletiva de modos de ordem superior no guia retangular (TE20 e TM11)

Em certas aplicações de telecomunicações, cavidades ressonantes ou sensores industriais, deseja-se excitar exclusivamente um modo de ordem superior — como o **$\text{TE}_{20}$** ou o **$\text{TM}_{11}$** — suprimindo energicamente o modo fundamental $\text{TE}_{10}$. Como realizar essa seletividade?

- **Alimentação Diferencial em Contrafase ($180^\circ$) para $\text{TE}_{20}$:** O modo $\text{TE}_{20}$ possui dois lóbulos de campo elétrico vertical com polaridades opostas: positivo em $0 < x < a/2$ e negativo em $a/2 < x < a$. Ao inserirmos duas sondas em $x = a/4$ e $x = 3a/4$ alimentadas por um divisor híbrido de $180^\circ$ (em oposição de fase), a simetria ímpar casa perfeitamente com o $\text{TE}_{20}$ e cancela totalmente o $\text{TE}_{10}$ (que requer alimentação em fase simétrica).
- **Sonda Inclinada ou Acoplador Direcional para Modos $\text{TM}_{11}$:** Modos TM exigem componentes axiais $E_z \neq 0$. Uma sonda longitudinal introduzida paralelamente ao eixo $z$ ou inclinada a $45^\circ$ acopla eficientemente o componente elétrico longitudinal inexistente na família TE.

## 5. Guia circular metálico oco: dedução rigorosa com funções de Bessel

Quando a seção transversal do condutor metálico transita da geometria retangular para o cilindro circular de raio $a$, a simetria rotacional impõe a transição das funções trigonométricas cartesianas para as **Funções Especiais de Bessel**. Esta geometria é a base de alimentadores de antenas refletoras, cornetas cônicas, polarizadores circulares, transições para cabos coaxiais e juntas rotativas de radar.

### 5.1 Equação de Helmholtz em coordenadas cilíndricas e decomposição transversal do guia circular

Adotando o sistema de coordenadas cilíndricas $(r, \phi, z)$, onde o eixo $z$ coincide com o eixo longitudinal de propagação do guia e $r \le a$ delimita o meio dielétrico interno ($\mu, \varepsilon$), as equações de onda de Helmholtz para as componentes axiais $E_z$ e $H_z$ assumem a forma:

$$\nabla_t^2 \psi(r, \phi) + k_c^2 \psi(r, \phi) = 0 \implies \left[ \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2}{\partial \phi^2} + k_c^2 \right] \psi(r, \phi) = 0$$

onde $\psi$ representa $E_z$ (para modos TM) ou $H_z$ (para modos TE), e $k_c^2 = k^2 - \beta^2 = \omega^2\mu\varepsilon - \beta^2$ é o número de onda de corte. A partir das equações de Maxwell rotacionais $\nabla \times \vec{E} = -j\omega\mu\vec{H}$ e $\nabla \times \vec{H} = j\omega\varepsilon\vec{E}$, as componentes transversais no plano $(r, \phi)$ são expressas estritamente em função das derivadas espaciais das componentes axiais:

$$E_r = \frac{-j}{k_c^2}\left( \beta \frac{\partial E_z}{\partial r} + \frac{\omega\mu}{r}\frac{\partial H_z}{\partial \phi} \right), \qquad E_\phi = \frac{-j}{k_c^2}\left( \frac{\beta}{r}\frac{\partial E_z}{\partial \phi} - \omega\mu\frac{\partial H_z}{\partial r} \right)$$

$$H_r = \frac{j}{k_c^2}\left( -\frac{\omega\varepsilon}{r}\frac{\partial E_z}{\partial \phi} - \beta\frac{\partial H_z}{\partial r} \right), \qquad H_\phi = \frac{-j}{k_c^2}\left( \omega\varepsilon \frac{\partial E_z}{\partial r} + \frac{\beta}{r}\frac{\partial H_z}{\partial \phi} \right)$$

### 5.2 Separação de variáveis e equação diferencial de Bessel no guia circular

Propomos a solução por separação de variáveis na forma de produto $\psi(r, \phi) = R(r)\Phi(\phi)$. Substituindo no operador diferencial e multiplicando por $r^2 / (R\Phi)$:

$$\frac{r^2}{R}\frac{d^2 R}{dr^2} + \frac{r}{R}\frac{dR}{dr} + k_c^2 r^2 = -\frac{1}{\Phi}\frac{d^2 \Phi}{d\phi^2} = n^2$$

Como o primeiro membro depende unicamente da variável radial $r$ e o segundo membro depende unicamente da coordenada azimutal $\phi$, ambos devem ser rigorosamente iguais a uma constante de separação real $n^2$.

**1. Equação Azimutal e Periodicidade Física:**

$$\frac{d^2 \Phi}{d\phi^2} + n^2 \Phi = 0 \implies \Phi(\phi) = A \cos(n\phi) + B \sin(n\phi)$$

O espaço azimutal é circularmente fechado sobre si mesmo. Para que os campos eletromagnéticos sejam univocamente definidos em qualquer ponto físico do espaço, exige-se que $\Phi(\phi + 2\pi) = \Phi(\phi)$. Esta condição de continuidade cíclica impõe categoricamente que **$n$ seja um número inteiro**:

$$n \in \{0, 1, 2, 3, \dots\}$$

**2. Equação Radial de Bessel:** Substituindo a constante de separação $n^2$, a equação radial assume a clássica **Equação Diferencial de Bessel de ordem $n$**:

$$r^2 \frac{d^2 R}{dr^2} + r \frac{dR}{dr} + (k_c^2 r^2 - n^2)R = 0$$

A solução geral desta equação de segunda ordem é dada por uma combinação linear das *Funções de Bessel de primeira espécie* $J_n(k_c r)$ e das *Funções de Bessel de segunda espécie (ou funções de Neumann)* $Y_n(k_c r)$:

$$R(r) = C J_n(k_c r) + D Y_n(k_c r)$$

### Condição de campo finito no eixo (r = 0): descarte da função de Neumann Yn

**3. Condição de Campo Finito no Eixo ($r = 0$):** Ao analisarmos o comportamento assintótico para pequenos argumentos ($x \to 0$), constata-se que:

$$J_n(x) \sim \frac{x^n}{2^n n!} \quad (\text{finito}), \qquad Y_n(x) \sim \begin{cases} \frac{2}{\pi}\ln(x) \to -\infty, & n = 0 \\ -\frac{(n-1)!}{\pi}\left(\frac{2}{x}\right)^n \to -\infty, & n \ge 1 \end{cases}$$

Como o interior do guia de ondas circular é oco e contém meio dielétrico contínuo sem filamentos de carga ou correntes no eixo geométrico $r=0$, a densidade de energia armazenada deve ser fisicamente finita. Consequentemente, **o coeficiente $D$ deve anular-se estritamente ($D = 0$)**. A solução radial reduz-se a:

$$R(r) = C J_n(k_c r)$$

### 5.3 Condições de contorno na parede metálica (r = a): frequência de corte dos modos TM_nm e TE_nm do guia circular

Na parede condutora cilíndrica $r = a$, as condições de contorno de Condutor Elétrico Perfeito (PEC) exigem que as componentes tangenciais do campo elétrico ($E_z$ e $E_\phi$) sejam nulas.

**Modos $\text{TM}_{nm}$ ($H_z = 0, E_z \neq 0$):** A componente axial tangencial deve anular-se na casca condutora:

$$E_z(a, \phi) = 0 \implies J_n(k_c a) = 0$$

Seja $p_{nm}$ o **$m$-ésimo zero positivo** da função de Bessel $J_n(x)$. O número de onda de corte é quantizado por:

$$k_{c,nm}^{\text{TM}} = \frac{p_{nm}}{a}, \qquad f_{c,nm}^{\text{TM}} = \frac{c p_{nm}}{2\pi a \sqrt{\mu_r \varepsilon_r}}$$

**Modos $\text{TE}_{nm}$ ($E_z = 0, H_z \neq 0$):** A componente azimutal tangencial $E_\phi$ deve anular-se na parede $r=a$:

$$E_\phi(a, \phi) \propto \left.\frac{\partial H_z}{\partial r}\right|_{r=a} = 0 \implies J'_n(k_c a) = 0$$

Seja $p'_{nm}$ o **$m$-ésimo zero positivo da derivada** $J'_n(x) = \frac{d J_n(x)}{dx}$. O número de onda de corte é:

$$k_{c,nm}^{\text{TE}} = \frac{p'_{nm}}{a}, \qquad f_{c,nm}^{\text{TE}} = \frac{c p'_{nm}}{2\pi a \sqrt{\mu_r \varepsilon_r}}$$

### Tabela de zeros das funções de Bessel e derivadas (p'nm e pnm): ordem dos modos do guia circular

Hierarquia de corte dos modos do guia circular, com o zero de Bessel ($p'_{nm}$ ou $p_{nm}$) e a razão relativa $f_c / f_{c,\text{TE11}}$ (parte 1):

| Hierarquia de Corte | Modo | Tipo | Zero de Bessel ($p'_{nm}$ ou $p_{nm}$) | Razão Relativa ($f_c / f_{c,\text{TE11}}$) | Particularidade Física |
|---|---|---|---|---|---|
| 1º | $\text{TE}_{11}$ | TE | $p'_{11} \approx 1.8412$ | 1.000 | **Modo Fundamental / Dominante** (menor corte absoluto). |
| 2º | $\text{TM}_{01}$ | TM | $p_{01} \approx 2.4048$ | 1.306 | Simetria radial pura ($\partial/\partial\phi = 0$). Padrão para juntas rotativas. |
| 3º | $\text{TE}_{21}$ | TE | $p'_{21} \approx 3.0542$ | 1.659 | Distribuição quadrupolar (4 lóbulos transversais). |
| 4º (Par) | $\text{TE}_{01}$ | TE | $p'_{01} \approx 3.8317$ | 2.081 | **Degenerescência exata com $\text{TM}_{11}$**. Perdas ôhmicas decrescentes! |

Tabela de zeros de Bessel do guia circular (parte 2):

| Hierarquia de Corte | Modo | Tipo | Zero de Bessel ($p'_{nm}$ ou $p_{nm}$) | Razão Relativa ($f_c / f_{c,\text{TE11}}$) | Particularidade Física |
|---|---|---|---|---|---|
| 4º (Par) | $\text{TM}_{11}$ | TM | $p_{11} \approx 3.8317$ | 2.081 | Como $J'_0(x) = -J_1(x)$, seus zeros são matematicamente idênticos. |
| 5º | $\text{TE}_{31}$ | TE | $p'_{31} \approx 4.2012$ | 2.282 | Distribuição hexapolar (6 setores azimutais). |
| 6º | $\text{TM}_{21}$ | TM | $p_{21} \approx 5.1356$ | 2.789 | Modo TM de ordem superior. |
| 7º | $\text{TE}_{12}$ | TE | $p'_{12} \approx 5.3314$ | 2.896 | Segundo anel radial ($m=2$). |

### Degenerescência exata entre os modos TE01 e TM11 no guia circular

Das relações fundamentais de recorrência das funções de Bessel, tem-se a identidade analítica rigorosa:

$$J'_0(x) = \frac{d J_0(x)}{dx} = -J_1(x)$$

Portanto, o primeiro zero positivo da derivada da função de ordem zero ($p'_{01}$, que define a frequência de corte do modo $\text{TE}_{01}$) coincide com o primeiro zero positivo da própria função de ordem um ($p_{11}$, que define o corte do modo $\text{TM}_{11}$). Ambos ocorrem em $x = 3.831706\dots$, fazendo com que os dois modos possuam exatamente a mesma frequência de corte e velocidade de fase em qualquer guia circular oco.

### 5.4 Modo fundamental TE11 do guia circular: o cavalo de batalha monomodo e a degenerescência de polarização

Análise físico-tecnológica dos três modos notáveis do guia circular ($\text{TE}_{11}$, $\text{TM}_{01}$ e $\text{TE}_{01}$). **1. Modo Fundamental $\text{TE}_{11}$ · O Cavalo de Batalha Monomodo.**

Com o menor autovalor ($p'_{11} \approx 1.8412$), o $\text{TE}_{11}$ é o modo dominante no guia circular. Ele possui uma distribuição de campo elétrico dipolar muito semelhante à do modo $\text{TE}_{10}$ no guia retangular levemente curvado.

**Degenerescência de Polarização:** Como o cilindro possui simetria rotacional contínua, existem duas orientações ortogonais independentes ($\cos\phi$ e $\sin\phi$) que compartilham rigorosamente a mesma frequência de corte. Isto viabiliza a transmissão simultânea de duas polarizações ortogonais para duplicação de capacidade (polarização cruzada em satélites) e polarização circular. Contudo, qualquer leve deformação elíptica ou imperfeição mecânica quebra a simetria, dividindo os cortes e provocando rotação espúria do plano de polarização.

### Modo circular simétrico TM01 do guia circular: aplicação em juntas rotativas de radar

**2. Modo Circular Simétrico $\text{TM}_{01}$ · Aplicação em Juntas Rotativas de Radar.** O modo $\text{TM}_{01}$ possui $n = 0$, o que elimina qualquer variação com o ângulo azimutal ($\partial/\partial\phi = 0$). As linhas de campo elétrico são estritamente **radiais ($E_r$) e longitudinais ($E_z$)**, enquanto as linhas de campo magnético formam círculos concêntricos fechados perfeitos ($H_\phi$).

**Por que é essencial em radares móveis?** Antenas de radar militar, meteorológico e de controle de tráfego aéreo giram mecanicamente $360^\circ$ de forma ininterrupta. Se o sinal de micro-ondas atravessasse a junta mecânica em um modo não simétrico (como o $\text{TE}_{11}$), o giro da antena modularia a amplitude e a fase do feixe. Utilizando o modo $\text{TM}_{01}$, o guia de ondas pode girar livremente sobre seu eixo de rotação sem produzir absolutamente nenhuma alteração no sinal de transmissão (juntas rotativas coaxiais-guia circular).

### Modo TE01 do guia circular: atenuação ôhmica decrescente com a frequência (sistema WT4)

**3. Modo Circular $\text{TE}_{01}$ · O Fenômeno da Atenuação Decrescente com a Frequência.** O modo $\text{TE}_{01}$ possui simetria azimutal ($n=0$) e campo elétrico puramente circular ($E_\phi$), formando anéis fechados que não tocam a parede metálica. Nas paredes condutoras ($r = a$), a corrente superficial induzida pelas leis de fronteira é dada por:

$$\vec{J}_s = \hat{r} \times \vec{H} = \hat{r} \times (H_z \hat{z}) = -H_z \hat{\phi}$$

Como não existe componente azimutal de campo magnético na parede ($H_\phi = 0$), não há corrente superficial longitudinal $\vec{J}_z$. Conforme a frequência de operação $f$ aumenta muito acima do corte ($f \gg f_c$), o campo axial $H_z$ decai proporcionalmente a $(f_c/f)^2$. Esse decaimento quadrático supera a elevação da resistência pelicular $R_s \propto \sqrt{f}$, resultando em uma **atenuação ôhmica que decresce continuamente conforme a frequência sobe**:

$$\alpha_c^{\text{TE01}} \propto \frac{1}{\sqrt{f}} \quad (f \to \infty)$$

Esta propriedade espetacular e exclusiva motivou os Bell Telephone Laboratories na década de 1970 a desenvolverem o sistema experimental **WT4**: guias circulares helicoidais enterrados de 50 mm operando em ondas milimétricas ($40 - 110\text{ GHz}$) para transportar centenas de milhares de canais telefônicos com atenuações inferiores a $1\text{ dB/km}$, antes da consagração comercial das fibras ópticas de sílica dopada.

### 5.5 Como excitar modos no guia circular metálico (TE11, TM01 e TE01)

A injeção de sinais eletromagnéticos no guia circular requer transições que respeitem as condições de simetria vetorial de cada família modal.

**Excitação do Modo $\text{TE}_{11}$ — Sonda Coaxial Radial:** O pino central do conector coaxial é inserido radialmente através da parede lateral do guia no plano $x-y$.

- A sonda alinha-se perfeitamente com o campo elétrico central máximo do $\text{TE}_{11}$;
- A parede terminal de curto-circuito é posicionada a uma distância de $\lambda_g / 4$ da sonda para somar a reflexão em fase ($360^\circ$ construtiva);
- Inserir duas sondas ortogonais defasadas de $90^\circ$ excita diretamente polarização circular (direita ou esquerda).

**Excitação do Modo $\text{TM}_{01}$ — Sonda Axial no Eixo Central:** O condutor coaxial penetra longitudinalmente ao longo do eixo $r = 0$ através do centro da tampa metálica traseira.

- As correntes axiais que fluem pela sonda lançam linhas de campo elétrico radial perfeitamente simétricas ($\hat{r}$) em todas as direções;
- Como a sonda situa-se exatamente na linha neutra onde o $\text{TE}_{11}$ tem campo nulo para modos de ordem par, a pureza espectral do $\text{TM}_{01}$ atinge níveis excelentes.

### Excitação do modo TE01 no guia circular: laços magnéticos periféricos e transição de Marie

**Excitação do Modo $\text{TE}_{01}$ — Laços Magnéticos Periféricos ou Transição Marie:** O modo $\text{TE}_{01}$ possui campo magnético axial $H_z$ e correntes azimutais, sem campo elétrico radial.

- Utilizam-se 4 pequenos laços magnéticos distribuídos simetricamente na circunferência da parede de fundo, excitados todos em fase;
- Alternativamente, utiliza-se a *transição de Marie*, que deforma suavemente a seção retangular excitada em $\text{TE}_{10}$ para a seção circular enquanto torce gradualmente as linhas de campo elétrico em círculos concêntricos.

### Simulador analítico e visualizador 2D de modos do guia circular metálico

A página traz um laboratório computacional interativo em coordenadas cilíndricas $(r, \phi)$: o aluno escolhe o raio $a$, o dielétrico interno ($\varepsilon_r$, $\mu_r$) e a frequência de operação, vê a tabela de modos com raiz ($p'_{nm} / p_{nm}$), $f_c$, estado, $\beta$ ou $\alpha$, $\lambda_g$ e $\eta$, e visualiza na seção circular o campo $\vec{E}_t$, o campo $\vec{H}_t$ ou a potência $S_z$, inspecionando com o cursor $(r, \phi)$, $|\vec{E}_t|$, $|\vec{H}_t|$ e $S_z$.

Presets padronizados (diâmetro interno): tubo didático (Ø 20.00 mm, raio $a$ = 10.0 mm); WC-109 / adaptador WR-90 (Ø 27.69 mm, raio $a$ = 13.85 mm); WC-75 (Ø 19.05 mm, raio $a$ = 9.53 mm, banda X); WC-54 (Ø 13.72 mm, raio $a$ = 6.86 mm, banda Ku); WC-38 (Ø 9.70 mm, raio $a$ = 4.85 mm, banda K); WC-28 (Ø 7.14 mm, raio $a$ = 3.57 mm, banda Ka / 5G).

Valores exibidos na configuração inicial (tubo didático, $a = 10$ mm, $f = 12$ GHz, modo $\text{TE}_{11}$ fundamental/dominante): frequência de corte 8.79 GHz; $\beta$ = 171.2 rad/m; $\lambda_g$ = 36.7 mm; $v_p$ = 1.47 c; $v_g$ = 0.68 c; impedância de onda $\eta$ = 553.8 Ω.

## 6. Guia dielétrico planar (slab) e fotônica em silício (SOI)

Ao contrário dos guias metálicos fechados, onde o confinamento ocorre por reflexão em paredes condutoras perfeitas com correntes superficiais, os **guias dielétricos** confinam a radiação eletromagnética por **Reflexão Interna Total (TIR)** através de um salto de permissividade entre um meio central de alto índice de refração ($n_1$, núcleo) e meios circundantes de menor índice ($n_2$, casca). O guia planar estratificado (*slab waveguide*) é o modelo canônico fundamental para o projeto de circuitos integrados nanofotônicos em chips de silício.

### 6.1 Reflexão interna total e índice de refração efetivo (n_eff) do guia slab

Consideremos um guia dielétrico planar simétrico infinito no plano $y-z$, formado por um núcleo de espessura $2d$ (compreendido entre $-d \le x \le d$) de índice de refração $n_1 = \sqrt{\varepsilon_{r1}}$, imerso em um meio infinito de casca com índice $n_2 = \sqrt{\varepsilon_{r2}}$, com $n_1 > n_2$. Uma onda monocromática de comprimento de onda no vácuo $\lambda_0$ propaga-se ao longo do eixo longitudinal $z$ com dependência espacial $e^{-j\beta z}$.

O número de onda no vácuo é $k_0 = \omega/c = 2\pi/\lambda_0$. Definimos o **índice de refração efetivo do modo** como:

$$n_{\text{eff}} \equiv \frac{\beta}{k_0} = \frac{\lambda_0}{\lambda_g}$$

Para que o campo eletromagnético permaneça **estritamente guiado** sem irradiar potência para o infinito nas cascas transversais ($|x| \to \infty$), o ângulo de propagação dos raios parciais em zigue-zague deve exceder o ângulo crítico de Fresnel $\theta_c = \arcsin(n_2 / n_1)$. Isto impõe a condição universal fundamental:

$$n_2 < n_{\text{eff}} < n_1 \iff k_0 n_2 < \beta < k_0 n_1$$

### Campo oscilatório no núcleo e onda evanescente na casca do guia dielétrico

- **No Núcleo ($|x| \le d$):** Como $\beta < k_0 n_1$, o número de onda transversal é real: $\kappa_x = \sqrt{k_0^2 n_1^2 - \beta^2} = k_0 \sqrt{n_1^2 - n_{\text{eff}}^2}$. O campo possui comportamento *oscilatório estacionário* ($\cos(\kappa_x x)$ ou $\sin(\kappa_x x)$).
- **Na Casca ($|x| > d$):** Como $\beta > k_0 n_2$, o número de onda transversal torna-se puramente imaginário: $\gamma_x = \sqrt{\beta^2 - k_0^2 n_2^2} = k_0 \sqrt{n_{\text{eff}}^2 - n_2^2}$. O campo não propaga transversalmente, decaindo como uma *onda puramente evanescente* ($e^{-\gamma_x (|x| - d)}$).

### 6.2 Equações de dispersão (transcendentais) dos modos TE e TM do guia slab

Impondo as condições de fronteira de continuidade dos campos eletromagnéticos nas duas interfaces dielétricas $x = \pm d$, deduzem-se as relações que quantizam os valores permitidos para $n_{\text{eff}}$.

**Modos $\text{TE}$ ($E_y \neq 0, H_x, H_z$):** O campo elétrico é inteiramente tangencial às interfaces ($E_y$). A continuidade de $E_y$ e da componente magnética tangencial $H_z = \frac{j}{\omega\mu}\frac{\partial E_y}{\partial x}$ em $x = \pm d$ resulta nas célebres relações:

$$\kappa_x \tan(\kappa_x d) = \gamma_x \quad (\text{Modos Pares / Simétricos})$$

$$-\kappa_x \cot(\kappa_x d) = \gamma_x \quad (\text{Modos Ímpares / Anti-simétricos})$$

**Modos $\text{TM}$ ($H_y \neq 0, E_x, E_z$):** O campo magnético é tangencial ($H_y$). A continuidade de $H_y$ e de $E_z = -\frac{j}{\omega\varepsilon}\frac{\partial H_y}{\partial x}$ introduz o salto das permissividades dielétricas $(n_1/n_2)^2$:

$$\kappa_x \tan(\kappa_x d) = \left(\frac{n_1}{n_2}\right)^2 \gamma_x \quad (\text{Modos Pares})$$

$$-\kappa_x \cot(\kappa_x d) = \left(\frac{n_1}{n_2}\right)^2 \gamma_x \quad (\text{Modos Ímpares})$$

### Salto do campo elétrico normal nos modos TM e os guias de ranhura (slot waveguides)

Na interface $x = \pm d$, a lei de Gauss $\nabla \cdot \vec{D} = 0$ exige que o deslocamento elétrico normal seja contínuo: $D_{x1} = D_{x2} \implies \varepsilon_1 E_{x1} = \varepsilon_2 E_{x2}$. Em fotônica de silício, onde o núcleo é Silício ($n_1 \approx 3.47 \implies \varepsilon_1 \approx 12.04$) e a casca é Sílica ($n_2 \approx 1.44 \implies \varepsilon_2 \approx 2.07$), a razão de permissividades atinge $\varepsilon_1 / \varepsilon_2 \approx 5.81$.

Isto significa que **o campo elétrico perpendicular sofre um salto brutal de quase 6 vezes ao passar para o meio de menor índice** ($E_{x,\text{casca}} \approx 5.81 E_{x,\text{núcleo}}$). Em nanofotônica, exploramos essa física através dos *guias de ranhura* (*Slot Waveguides*), confinando luz em altíssima intensidade dentro de uma fenda de apenas $50\text{ nm}$ de ar ou dióxido de silício para sensores bioquímicos e modulação óptica não linear.

### 6.3 Parâmetros normalizados do guia slab: frequência normalizada V, índice efetivo normalizado b e confinamento Γ

Para universalizar a análise independente da escala nanométrica e do comprimento de onda utilizado, definem-se as variáveis normalizadas adimensionais:

$$u = \kappa_x d, \qquad w = \gamma_x d, \qquad V = \sqrt{u^2 + w^2} = k_0 d \sqrt{n_1^2 - n_2^2} = \frac{2\pi d}{\lambda_0}\sqrt{n_1^2 - n_2^2}$$

onde $V$ é a **frequência normalizada** da estrutura. O índice de refração efetivo normalizado $b \in [0, 1]$ e a fração de confinamento de potência no núcleo $\Gamma$ são expressos por:

$$b = \frac{n_{\text{eff}}^2 - n_2^2}{n_1^2 - n_2^2} = \frac{w^2}{V^2}, \qquad \Gamma \equiv \frac{\iint_{\text{núcleo}} S_z \, dx \, dy}{\iint_{\infty} S_z \, dx \, dy} = \frac{1 + \frac{\sin(2u)}{2u}}{1 + \frac{\sin(2u)}{2u} + \frac{\cos^2(u)}{w}}$$

### Por que o modo fundamental TE0 do guia slab não tem frequência de corte (condição monomodo V < π/2)

Na condição de corte de um modo dielétrico, o campo deixa de decair na casca e estende-se ao infinito ($\gamma_x \to 0 \implies w \to 0$). Para os modos pares TE, a relação $u \tan(u) = w$ com $w = 0$ fornece:

$$u \tan(u) = 0 \implies u = 0 \implies V_{\text{corte}} = 0$$

Isto demonstra que **o modo fundamental $\text{TE}_0$ no guia slab simétrico propaga-se para qualquer espessura $d > 0$ e qualquer comprimento de onda $\lambda_0$**, não possuindo corte físico! O primeiro modo superior ($\text{TE}_1$, ímpar) surge quando $-u \cot(u) = 0 \implies u = \pi/2 \implies V_c = \pi/2 \approx 1.5708$. Consequentemente, a **condição estritamente monomodo** para o guia dielétrico planar simétrico é:

$$V < \frac{\pi}{2} \iff 2d < \frac{\lambda_0}{2\sqrt{n_1^2 - n_2^2}}$$

## 7. Fibras ópticas cilíndricas e a aproximação de modos LP

A fibra óptica de sílica é a espinha dorsal de toda a transmissão de dados planetária. Estruturada como um guia dielétrico cilíndrico de núcleo de raio $a$ e casca de raio $b \approx 62.5\,\mu\text{m}$ (diâmetro total de $125\,\mu\text{m}$), a fibra opera sob uma física sutilmente distinta da fotônica de silício: o regime de **guia fracamente guiado**.

### 7.1 Abertura numérica (NA) da fibra óptica e a aproximação de guiamento fraco de Gloge (Δ ≪ 1)

Em uma fibra óptica de telecomunicações típica (como a Corning SMF-28), o núcleo de sílica pura é dopado com pequenas porcentagens de germânio ($\text{GeO}_2$) para elevar minimamente seu índice: $n_1 \approx 1.4492$ contra $n_2 \approx 1.4440$ da casca pura de $\text{SiO}_2$ em $\lambda_0 = 1550\text{ nm}$. O contraste relativo de índices $\Delta$ é minúsculo:

$$\Delta = \frac{n_1^2 - n_2^2}{2 n_1^2} \approx \frac{n_1 - n_2}{n_1} \approx \frac{0.0052}{1.4492} \approx 0.36\% \ll 1$$

A **Abertura Numérica ($\text{NA}$)**, que define o cone angular de aceitação de luz incidente no ar pelo topo da fibra ($\theta_{\text{acc}} = \arcsin(\text{NA})$), é dada por:

$$\text{NA} = \sqrt{n_1^2 - n_2^2} \approx n_1 \sqrt{2\Delta} \approx 1.4492 \sqrt{2 \times 0.0036} \approx 0.123$$

Como $\Delta \ll 1$, os campos axiais longitudinais $E_z$ e $H_z$ são ordens de grandeza menores do que os campos transversais ($E_z \sim \sqrt{2\Delta} \, E_t$). Demonstrou Allan Snyder e Dietrich Gloge que as soluções vetoriais híbridas exatas de Maxwell ($\text{HE}_{lm}, \text{EH}_{lm}, \text{TE}_{0m}, \text{TM}_{0m}$) degeneram em grupos com quase a mesma constante de fase, combinando-se em **Modos Linearmente Polarizados ($\text{LP}_{lm}$)**.

### 7.2 Modo fundamental LP01 da fibra e condição monomodo (V < 2,4048)

A frequência normalizada para o guia cilíndrico de núcleo de raio $a$ é expressa por:

$$V = \frac{2\pi a}{\lambda_0} \sqrt{n_1^2 - n_2^2} = \frac{2\pi a}{\lambda_0} \text{NA}$$

O modo fundamental da fibra é o **$\text{LP}_{01}$** (correspondente ao modo vetorial $\text{HE}_{11}$). No núcleo ($r \le a$), sua distribuição radial de campo é proporcional à função de Bessel de primeira espécie $J_0(u r/a)$; na casca ($r > a$), decai suavemente como uma função de Bessel modificada de segunda espécie $K_0(w r/a)$.

O primeiro modo superior a ser excitado é o $\text{LP}_{11}$ (formado pelos modos vetoriais $\text{TE}_{01}, \text{TM}_{01}$ e $\text{HE}_{21}$), cuja frequência de corte normalizada coincide rigorosamente com o **primeiro zero positivo da função de Bessel $J_0(x)$**:

$$V_c = p_{01} \approx 2.4048255$$

### Comprimento de onda de corte monomodo da fibra SMF-28 (bandas O e C)

Para garantir que uma fibra óptica opere de modo **estritamente monomodal**, eliminando a dispersão intermodal (que destruiria a taxa de transmissão em gigabits por segundo), exige-se:

$$V = \frac{2\pi a}{\lambda_0} \text{NA} < 2.4048 \iff \lambda_0 > \lambda_c = \frac{2\pi a}{2.4048}\text{NA}$$

Para a fibra padrão SMF-28 com raio de núcleo $a = 4.1\,\mu\text{m}$ e $\text{NA} \approx 0.123$, temos $\lambda_c \approx 1260\text{ nm}$. Isso assegura que tanto na **Banda O ($1310\text{ nm}$)** quanto na **Banda C ($1550\text{ nm}$)**, a fibra opere com pureza monomodal absoluta.

### 7.3 Diâmetro de campo modal (MFD) da fibra e a fórmula de Marcuse

Como uma fração significativa da potência do modo fundamental $\text{LP}_{01}$ trafega na casca como onda evanescente, a mancha luminosa é ligeiramente maior do que o diâmetro físico do núcleo. Define-se o **Diâmetro do Campo Modal (Mode Field Diameter - MFD)** como a largura na qual a intensidade óptica decai para $1/e^2$ ($\approx 13.5\%$) de seu valor de pico no centro.

Aproximando a distribuição modal por um feixe gaussiano equivalente de raio de cintura $w_0$ ($\text{MFD} = 2w_0$), utiliza-se a universalmente consagrada **Fórmula Empírica de Marcuse**:

$$\frac{w_0}{a} \approx 0.65 + \frac{1.619}{V^{3/2}} + \frac{2.879}{V^6} \quad (0.8 \le V \le 2.8)$$

Para a fibra SMF-28 operando em $\lambda_0 = 1550\text{ nm}$ ($V \approx 2.04$), a fórmula prediz $w_0 \approx 5.11\,\mu\text{m}$, resultando em um $\text{MFD} \approx 10.22\,\mu\text{m}$ (perfeitamente aderente à especificação comercial de catálogo da Corning: $10.4 \pm 0.5\,\mu\text{m}$).

### Simulador gráfico de modos LP em fibra óptica (solução em r = 0)

A página oferece um laboratório computacional com a solução numérica exata das equações de dispersão de Gloge sem descontinuidade em $r = 0$: o aluno alterna entre os modos $\text{LP}_{01}$, $\text{LP}_{11}$ e $\text{LP}_{21}$ e compara distribuições de campo vetorial $\vec{E}_t(x,y)$, intensidade luminosa $I(x,y)$ e o perfil de corte radial $1\text{D}$ (ver a seção 9).

## 8. Contraste tecnológico: fotônica em silício (SOI, alto contraste) vs fibra óptica (baixo contraste)

A magnitude da descontinuidade de índice de refração ($\Delta n$) molda radicalmente as dimensões, o confinamento físico, as perdas radiativas e as aplicações práticas dos guias dielétricos modernos.

Comparação entre fotônica integrada em silício (SOI) e fibra óptica monomodo (SMF-28): materiais e contraste de índice.

| Característica Físico-Óptica | Fotônica Integrada em Silício (SOI) | Fibra Óptica Monomodo (SMF-28) |
|---|---|---|
| Materiais do Núcleo / Casca | Silício cristalino ($n_1 \approx 3.476$) sobre Sílica ($n_2 \approx 1.444$) | Sílica dopada com germânio ($n_1 \approx 1.449$) sobre Sílica ($n_2 \approx 1.444$) |
| Contraste Absoluto de Índice ($\Delta n$) | $\Delta n \approx 2.032$ (ALTÍSSIMO CONTRASTE) | $\Delta n \approx 0.0052$ (BAIXÍSSIMO CONTRASTE) |
| Contraste Relativo ($\Delta$) | $\Delta \approx 41.3\%$ | $\Delta \approx 0.36\%$ |

### Dimensões, raio de curvatura, atenuação e aplicações: SOI vs fibra SMF-28

| Característica Físico-Óptica | Fotônica Integrada em Silício (SOI) | Fibra Óptica Monomodo (SMF-28) |
|---|---|---|
| Dimensão Típica do Núcleo | **$500\text{ nm} \times 220\text{ nm}$** (escala submicrométrica nanométrica) | **$8.2\,\mu\text{m}$ a $9.0\,\mu\text{m}$** (quase 20 vezes maior) |
| Raio Mínimo de Curvatura ($R_{\text{min}}$) | $3\,\mu\text{m}$ a $5\,\mu\text{m}$ (curvas ultracompactas em chip) | $20\text{ mm}$ a $30\text{ mm}$ (sob risco de radiação) |
| Atenuação Típica em $1550\text{ nm}$ | $1.0$ a $2.5\text{ dB/cm}$ (espalhamento em rugosidades litográficas) | $0.18\text{ dB/km}$ (transparência extrema) |
| Aplicação Predominante | Processamento óptico ultradenso em chips (PICs), transceivers de datacenters, IA óptica e sensores biológicos. | Transporte transcontinental de sinais em longa distância, enlaces metropolitanos e redes FTTH. |

### Por que em fotônica usamos comprimento de onda λ0 (nm) e em micro-ondas usamos frequência f (GHz)

Revisão epistemológica: ao transitar dos guias metálicos para os circuitos fotônicos e fibras, a grandeza independente padrão torna-se o **comprimento de onda no vácuo ($\lambda_0$)**. Reiteramos as razões fundamentais:

1. **Dispersão Material de Sellmeier:** O índice de refração $n(\lambda_0)$ do silício e da sílica é modelado diretamente por equações empíricas de física de estado sólido formuladas em comprimentos de onda ópticos;
2. **Escalares Litográficos em Chip:** O projeto de redes de difração de acoplamento (*grating couplers*), anéis microrressonantes e filtros MZI depende da dimensão física espacial $\Lambda = \lambda_0 / n_{\text{eff}}$;
3. **Instrumentação Laboratorial:** Espectrômetros ópticos (OSAs) utilizam grades de difração para separar fisicamente feixes segundo a lei da rede ($d\sin\theta = m\lambda_0$), medindo comprimentos de onda com resolução subnanométrica;
4. **Janelas ITU-T:** Toda a infraestrutura óptica é padronizada em comprimentos de onda: Banda O ($1260 - 1360\text{ nm}$) e Banda C ($1530 - 1565\text{ nm}$).

## 9. Simulador computacional de guias dielétricos: slab SOI e fibras monomodo SMF

Laboratório de óptica integrada parametrizado em comprimento de onda ($\lambda_0$ em nm). O aluno alterna entre o guia planar em fotônica de silício e a fibra óptica monomodo e calcula o índice efetivo $n_{\text{eff}}$, o confinamento óptico $\Gamma$, a penetração evanescente e o perfil modal.

### Simulador do guia slab dielétrico (fotônica em silício SOI): índice efetivo, confinamento e penetração evanescente

Parâmetros ajustáveis: espessura do núcleo $2d$ (nm), índices $n_1$ e $n_2$, comprimento de onda $\lambda_0$ (atalhos 1310 nm, banda O, e 1550 nm, banda C) e polarização TE (campo $E_y$) ou TM (campo $H_y$). Presets: fotônica em silício SOI strip (220 nm, $\Delta n \approx 2.03$); fotônica em silício larga (500 nm, baixa perda); nitreto de silício Si3N4 (800 nm, médio contraste); guia polimérico / vidro dopado (2.0 µm, baixo contraste).

A tabela de modos guiados mostra $n_{\text{eff}}$, $\beta$, confinamento $\Gamma$, penetração ($1/\gamma$) e estado de cada modo. O gráfico mostra a distribuição transversal do campo óptico $E(x)$ (onda estacionária no núcleo e cauda evanescente na casca) sobre o perfil de índice $n(x)$, com uma linha marcando $n_{\text{eff}}$.

Valores exibidos na configuração inicial (SOI, $2d = 220$ nm, $n_1 = 3.476$, $n_2 = 1.444$, $\lambda_0 = 1550$ nm): frequência normalizada $V = 1.408$; $n_{\text{eff}} = 2.8415$; confinamento $\Gamma = 81.0\%$; penetração $1/\gamma_x = 100.7$ nm; contraste $\Delta n = 2.032$ (alto); regime monomodo.

### Simulador de modos LP em fibra óptica: parâmetros U, W, V e tratamento exato da origem r = 0

Parâmetros ajustáveis: raio do núcleo $a$ (µm), índices $n_1$ e $n_2$, comprimento de onda $\lambda_0$ (atalhos 850, 1310 e 1550 nm), polarização linear $\hat{x}$ ($E_x$) ou $\hat{y}$ ($E_y$), grandeza exibida (intensidade $I \propto |\psi|^2$ ou amplitude $\psi(r,\phi)$) e orientação azimutal dos lóbulos ($\cos(\ell\phi)$ ou $\sin(\ell\phi)$). Presets: Corning SMF-28 (núcleo 8.2 µm, $\lambda$ = 1550 nm, monomodo $\text{LP}_{01}$); SMF-28 em 850 nm (poucos modos, $\text{LP}_{01}$ + $\text{LP}_{11}$); fibra de alto contraste (Hi-NA, núcleo 3.6 µm); fibra multimodo de datacenter (OM3/OM4 50/125 µm).

A tabela lista os modos LP guiados ($V_c < V$) com corte $V_c$, $n_{\text{eff}}$, $U$, $W$, confinamento $\Gamma$ e estado. O gráfico 2D mostra a seção da fibra (núcleo físico $r = a$, círculo do MFD para $\text{LP}_{01}$ e setas de polarização linear) e um perfil radial de $\psi(r)$ e da intensidade $|\psi|^2$ com a interface $r = a$ marcada.

**Tratamento exato da origem ($r = 0$):** Nos modos linearmente polarizados ($\text{LP}_{\ell m}$), o campo é formulado diretamente no referencial cartesiano ($\vec{E}_t = \psi \hat{x}$). No eixo $r = 0$: para $\ell = 0$ ($\text{LP}_{0m}$), o campo é estritamente isotrópico e finito: $\lim_{r\to 0} \psi = E_0 / J_0(U)$, com derivada nula $\left.\frac{\partial\psi}{\partial r}\right|_{r=0} = 0$; para $\ell \ge 1$ ($\text{LP}_{11}, \text{LP}_{21}, \dots$), $\lim_{r\to 0} J_\ell(U r/a) = 0$, resultando em um nó nulo identicamente contínuo, eliminando qualquer polo $1/r$ ou indeterminação angular em $\phi = \text{atan2}(0,0)$.

Valores exibidos na configuração inicial (SMF-28, $a = 4.1$ µm, $n_1 = 1.4492$, $n_2 = 1.4440$, $\lambda_0 = 1550$ nm): $V = 2.039$; $n_{\text{eff}} = 1.4462$; confinamento no núcleo $\Gamma = 75.1\%$; $U = 1.541$; $W = 1.335$; NA = 0.1227; corte monomodo $\lambda_c$ = 1313.9 nm; regime monomodo $\text{LP}_{01}$.

## 10. Matriz comparativa das quatro geometrias de guias: retangular, circular, slab dielétrico e fibra óptica

Quadro sinóptico consolidando os princípios físicos, as autofunções matemáticas e as fronteiras tecnológicas dos guias condutores metálicos e guias dielétricos estudados.

Geometria, mecanismo de confinamento e autofunções:

| Tipo de Guia | Geometria / Sistema | Mecanismo de Confinamento | Autofunções Matemáticas |
|---|---|---|---|
| Guia Retangular Metálico | Cartesiano $x-y$ ($a \times b$) | Reflexão PEC em paredes condutoras | $\cos(m\pi x/a)\cos(n\pi y/b)$ |
| Guia Circular Metálico | Cilíndrico Polar $r-\phi$ (raio $a$) | Reflexão PEC em tubo condutor | $J_n(k_c r)\cos(n\phi)$ (Bessel) |
| Guia Slab Dielétrico (SOI) | Cartesiano 1D $x$ (espessura $2d$) | Reflexão Interna Total (TIR) com salto $\Delta n \approx 2.03$ | $\cos(\kappa_x x)$ núcleo / $e^{-\gamma_x x}$ casca |
| Fibra Óptica Cilíndrica (SMF) | Cilíndrico 2D $r-\phi$ (raio $a$) | Reflexão Interna Total Fraca ($\Delta \ll 1, \Delta n \approx 0.005$) | $J_l(u r/a)$ núcleo / $K_l(w r/a)$ casca |

### Modo fundamental, existência de corte e grandeza primária de cada tipo de guia

| Tipo de Guia | Modo Fundamental | Existe Corte no Fundamental? | Grandeza Primária |
|---|---|---|---|
| Guia Retangular Metálico | $\text{TE}_{10}$ | SIM ($f_{c,10} = c / 2a$) | Frequência $f$ (GHz) |
| Guia Circular Metálico | $\text{TE}_{11}$ | SIM ($p'_{11} \approx 1.841$) | Frequência $f$ (GHz) |
| Guia Slab Dielétrico (SOI) | $\text{TE}_0$ | NÃO ($V_c = 0$, propaga sempre) | Comprimento $\lambda_0$ (nm) |
| Fibra Óptica Cilíndrica (SMF) | $\text{LP}_{01}$ ($\text{HE}_{11}$) | NÃO ($V_c = 0$, sem corte) | Comprimento $\lambda_0$ (nm) |
