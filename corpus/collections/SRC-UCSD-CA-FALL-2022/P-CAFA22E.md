---
schema: qual/card@1
id: P-CAFA22E
kind: problem
title: "Harmonic function on punctured plane and its Laurent decomposition"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G = \CC \setminus \{0\}$, and let $h : G \to \RR$ be harmonic.

(i) Show that $g = h_x - ih_y$ is a holomorphic function in $G$, and that its residue at $0$ is a real number.

(ii) Show that there exist a constant $c$ and a holomorphic function $f : G \to \CC$ such that
$$
h(z) = c\log\abs{z} + \operatorname{Re} f(z) \quad \forall z \in G.
$$
:::

::: {.solution}

The argument is the card's own, by the conjugate differential of a harmonic function and the vanishing of its periods; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $G=\CC\setminus\{0\}$ and let $h:G\to\RR$ be harmonic.

::: pf

::: {.pf-step #holomorphic}
$g=h_{x}-ih_{y}$ is holomorphic on $G$.

::: pf-proof
Write $g=u+iv$ with $u=h_{x}$ and $v=-h_{y}$, both of class $C^{1}$ because $h$ is harmonic, hence of class $C^{2}$. The Cauchy--Riemann equations hold: $u_{x}=h_{xx}=-h_{yy}=v_{y}$ because $h_{xx}+h_{yy}=0$, and $u_{y}=h_{xy}=h_{yx}=-v_{x}$ because the mixed partials agree. A $C^{1}$ function satisfying the Cauchy--Riemann equations on an open set is holomorphic there.
:::

:::

::: {.pf-step #residue-real}
For $0<r$ the integral $\int_{\abs{z}=r}g(z)\,dz$ is purely imaginary, so $\operatorname{Res}_{0}g=\frac{1}{2\pi i}\int_{\abs{z}=r}g(z)\,dz$ is real.

::: pf-proof
Parametrise the positively oriented circle by $z=re^{it}$, so $dz=(-\sin t+i\cos t)r\,dt$. Then
$$
g(z)\,dz=(h_{x}-ih_{y})\big(-\sin t+i\cos t\big)r\,dt,
$$
whose real part is $r\big(-h_{x}\sin t+h_{y}\cos t\big)=r\frac{d}{dt}h(re^{it})$, the derivative of $t\mapsto h(re^{it})$. Hence
$$
\operatorname{Re}\int_{\abs{z}=r}g\,dz=\int_{0}^{2\pi}\frac{d}{dt}h(re^{it})\,dt=h(re^{2\pi i})-h(re^{0})=0,
$$
so the integral is purely imaginary and division by $2\pi i$ gives a real number. The residue is independent of $r$ because $g$ is holomorphic on the annulus between any two such circles. Write $c$ for this real number.
:::

:::

::: {.pf-step #primitive}
$g-c/z$ has a holomorphic primitive on $G$.

::: pf-proof
$g-c/z$ is holomorphic on $G$: both terms are, $1/z$ being holomorphic on $\CC\setminus\{0\}$. For a closed curve $\gamma$ in $G$ with winding number $n(\gamma,0)$ about $0$, the residue theorem applied to $g$, whose only singularity in $\CC$ is the isolated point $0$, gives $\frac{1}{2\pi i}\int_{\gamma}g=n(\gamma,0)\operatorname{Res}_{0}g=n(\gamma,0)c$, while $\frac{1}{2\pi i}\int_{\gamma}\frac{dz}{z}=n(\gamma,0)$. Hence $\int_{\gamma}\big(g-\tfrac{c}{z}\big)=2\pi i\,n(\gamma,0)c-c\cdot2\pi i\,n(\gamma,0)=0$, so all periods of $g-c/z$ vanish. A holomorphic function on a domain whose integral over every closed curve vanishes has a primitive $F$ there, by the construction of the primitive from a fixed base point, which is well defined because the integral is path independent.
:::

:::

::: {.pf-step #decomposition}
$h-c\log\abs{z}-\operatorname{Re}F$ is constant on $G$.

::: pf-proof
Write $\varphi=h-c\log\abs{z}-\operatorname{Re}F$, a real-valued $C^{1}$ function. The Wirtinger derivative of $\operatorname{Re}F$ is $\tfrac12 F'$, and $\log\abs{z}=\tfrac12\log(z\bar z)$ has $\partial_{z}$-derivative $\tfrac{1}{2z}$. Hence
$$
2\,\frac{\partial\varphi}{\partial z}=g-\frac{c}{z}-F'=0
$$
by step [](#primitive){.pf-ref}, since $g=h_{x}-ih_{y}=2h_{z}$ is the definition of $g$ read in Wirtinger derivatives. A real-valued $C^{1}$ function with vanishing $\partial_{z}$ is constant: its partial derivatives are $\varphi_{x}=\varphi_{z}+\varphi_{\bar z}$ and $\varphi_{y}=i(\varphi_{z}-\varphi_{\bar z})$, and for real-valued $\varphi$ one has $\varphi_{\bar z}=\overline{\varphi_{z}}=0$, so both partial derivatives vanish on the connected set $G$ and $\varphi$ is constant.
:::

:::

::: {.pf-step #answer}
There are $c\in\RR$ and $f$ holomorphic on $G$ with $h(z)=c\log\abs{z}+\operatorname{Re}f(z)$ for all $z\in G$.

::: pf-proof
Let $c$ be the real residue of step [](#residue-real){.pf-ref}, let $F$ be the primitive of step [](#primitive){.pf-ref} and let $k$ be the constant of step [](#decomposition){.pf-ref}, so that $h=c\log\abs{z}+\operatorname{Re}F+k$. Put $f=F+k$, which is holomorphic on $G$; then $\operatorname{Re}f=\operatorname{Re}F+k$ and
$$
\boxed{h(z)=c\log\abs{z}+\operatorname{Re}f(z)}
$$
for every $z\in G$.
:::

:::

:::
:::
