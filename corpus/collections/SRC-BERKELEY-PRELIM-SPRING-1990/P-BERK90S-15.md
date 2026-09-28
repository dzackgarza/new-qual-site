---
schema: qual/card@1
id: P-BERK90S-15
kind: problem
title: Conformal map of a semicircular disk onto the upper half-plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the center and radius of the semidisc, the positive imaginary part, and the bijective conformal mapping requirement with Problem 15 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Mapped the semidisc to the first quadrant by z/(1-z), verified the inverse algebraically, and squared to obtain the upper half-plane.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked the real and imaginary parts of the map and inverse, the unique square root in the first quadrant, surjectivity, and nonvanishing of the composite derivative on the open semidisc.
---

::: {.problem}
Find a one-to-one conformal map from
$$
\left\{z\in\CC:\Im z>0,
\ \abs{z-\frac12}<\frac12\right\}
$$
onto the upper half-plane.
:::

::: {.hint}
The map $z\mapsto z/(1-z)$ sends the diameter endpoints $0,1$
to $0,\infty$. Determine its image on the semidisc and then
apply a power map to double the angle.
:::

::: {.solution}
Let $D$ be the given semidisc, and put
$$
Q\coloneqq\{w\in\CC:\Re w>0,\ \Im w>0\},
\qquad
H\coloneqq\{\zeta\in\CC:\Im\zeta>0\}.
$$

<1>1. The map
$$
T\colon D\longrightarrow Q,\qquad T(z)\coloneqq\frac{z}{1-z},
$$
is a bijection with inverse $T^{-1}(w)=w/(1+w)$.

::: {.proof}
For $z=x+iy$, the inequality $\abs{z-1/2}<1/2$ is equivalent
to $\abs{z}^2<x$. Thus $D$ is described by
$y>0$ and $\abs{z}^2<x$, and $1\notin D$. Multiplication by
$1-\overline z$ gives
$$
\Re T(z)=\frac{x-\abs{z}^2}{\abs{1-z}^2}>0,
\qquad
\Im T(z)=\frac{y}{\abs{1-z}^2}>0.
$$
Hence $T(D)\subset Q$. Conversely, let $w=u+iv\in Q$ and
set $z=w/(1+w)$. Since $u>0$, the denominator is nonzero.
Direct calculation gives
$$
\Im z=\frac{v}{\abs{1+w}^2}>0,
\qquad
\Re z-\abs{z}^2=\frac{u}{\abs{1+w}^2}>0.
$$
Therefore $z\in D$. The identities
$$
T\left(\frac{w}{1+w}\right)=w,
\qquad
\frac{T(z)}{1+T(z)}=z
$$
show that the stated maps are inverse bijections.
:::

<1>2. The map $P\colon Q\to H$ defined by $P(w)=w^2$ is a
bijection.

::: {.proof}
Each $w\in Q$ has a unique polar representation
$w=re^{i\theta}$ with $r>0$ and $0<\theta<\pi/2$.
Then $w^2=r^2e^{2i\theta}\in H$. Conversely, each
$\zeta\in H$ has a unique polar representation
$\zeta=Re^{i\phi}$ with $R>0$ and $0<\phi<\pi$.
Its unique preimage in $Q$ is
$w=\sqrt{R}\,e^{i\phi/2}$, proving both surjectivity and
injectivity.
:::

<1>3. A one-to-one conformal map onto the upper half-plane is
$$
F\colon D\longrightarrow H,\qquad
F(z)=\boxed{\left(\frac{z}{1-z}\right)^2}.
$$

::: {.proof}
Steps <1>1 and <1>2 show that $F=P\circ T$ is a bijection.
It is holomorphic on $D$, since its only pole is at $1$,
and its derivative is
$$
F'(z)=\frac{2z}{(1-z)^3}.
$$
The points $0$ and $1$ are outside $D$, so $F'(z)\neq0$
throughout $D$. Thus $F$ is conformal.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 supplies the required bijective conformal map.
:::
:::
