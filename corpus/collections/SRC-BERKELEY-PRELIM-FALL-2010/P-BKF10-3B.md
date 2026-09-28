---
schema: qual/card@1
id: P-BKF10-3B
kind: problem
title: Conformal map from the unit disk onto the sector $0<\arg z<\pi/4$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Cayley transform and its inverse, the upper-half-plane
    fourth-root branch, surjectivity onto the sector, and nonvanishing
    derivatives.
---

::: {.problem}
Give an example of a conformal map from the unit disk $\{z:\abs{z}<1\}$ onto the sector $\{z:0<\arg z<\pi/4\}$.
:::

::: {.solution}
Let
$$
D\coloneqq\{z\in\CC:\abs{z}<1\},
\qquad
H\coloneqq\{w\in\CC:\operatorname{Im}w>0\}.
$$
On $H$, let $\operatorname{Log}$ denote the holomorphic logarithm with
$0<\operatorname{Im}\operatorname{Log}w<\pi$.

<1>1. The Möbius transformation
$$
C(z)\coloneqq i\frac{1+z}{1-z}
$$
is a conformal bijection from $D$ onto $H$.

::: {.proof}
For $z\in D$,
$$
\operatorname{Im}C(z)
=\frac{1-\abs{z}^2}{\abs{1-z}^2}>0,
$$
so $C(D)\subseteq H$. Solving $w=C(z)$ for $z$ gives
$$
z=\frac{w-i}{w+i}.
$$
If $w=u+iv\in H$, then
$$
\abs{w-i}^2=u^2+(v-1)^2
<u^2+(v+1)^2=\abs{w+i}^2,
$$
so this inverse satisfies $\abs{z}<1$. Hence $C$ is bijective from
$D$ to $H$. Finally,
$$
C'(z)=\frac{2i}{(1-z)^2}\ne0
$$
on $D$, so the bijection is conformal.
:::

<1>2. The map
$$
R(w)\coloneqq\exp\left(\frac14\operatorname{Log}w\right)
$$
is a conformal bijection from $H$ onto
$$
S\coloneqq\{\zeta\in\CC:0<\arg\zeta<\pi/4\}.
$$

::: {.proof}
Write $w=re^{i\theta}$ with $r>0$ and $0<\theta<\pi$. Then
$$
R(w)=r^{1/4}e^{i\theta/4},
$$
so $0<\arg R(w)<\pi/4$ and therefore $R(H)\subseteq S$.

Conversely, if $\zeta=\rho e^{i\varphi}\in S$, then
$0<4\varphi<\pi$, so $\zeta^4\in H$, and the chosen logarithm gives
$$
R(\zeta^4)=\zeta.
$$
Thus $R$ is onto. The same polar representation shows that it is
injective. Moreover,
$$
R'(w)=\frac14\exp\left(-\frac34\operatorname{Log}w\right)\ne0,
$$
so $R$ is conformal.
:::

<1>3. The map
$$
\boxed{
\Phi(z)
=\exp\left(
\frac14\operatorname{Log}\left(i\frac{1+z}{1-z}\right)
\right)
}
$$
is a conformal bijection from the unit disk onto the required sector.

::: {.proof}
By step <1>1, $C$ is a conformal bijection from $D$ onto $H$.
By step <1>2, $R$ is a conformal bijection from $H$ onto $S$.
Therefore their composition $\Phi=R\circ C$ is a conformal bijection
from $D$ onto $S$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested example.
:::
:::
