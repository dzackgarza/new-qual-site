---
schema: qual/card@1
id: P-JHUSP05ANG
kind: problem
title: "Holomorphic bijection from the quadrant to the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the open first quadrant, unit disk and prescribed image of 1+i with Spring 2005 problem 7 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved both constituent maps are bijective, checked their image inequalities and denominators, and verified the normalization exactly."
---

::: {.problem}
Find a bijective holomorphic map $f$ from the quadrant

$$
Q = \{ x + iy \in \mathbb{C} : x > 0, \ y > 0 \}
$$

onto the unit disk $D = \{ z \in \mathbb{C} : |z| < 1 \}$ with $f(1+i) = 0$.
:::

::: solution
One such map is
$$
\boxed{f(z)=\frac{z^2-2i}{z^2+2i}.}
$$

<1>1. Squaring maps $Q$ biholomorphically onto the upper half-plane $H$.
::: proof
Every $z\in Q$ has a unique polar expression $re^{i\theta}$
with $r>0$ and $0<\theta<\pi/2$. Its square has argument
$2\theta\in(0,\pi)$, so lies in $H=\{v:\operatorname{Im}v>0\}$.
Conversely, for $v=\rho e^{i\alpha}\in H$ with
$0<\alpha<\pi$, the point $z=\sqrt\rho e^{i\alpha/2}$
is in $Q$ and squares to $v$. It is the only such point:
the other square root is $-z$, which is outside $Q$.
Thus squaring is a holomorphic bijection. Its derivative
$2z$ is nonzero on $Q$, so the inverse is holomorphic
by the local inverse function theorem [@SS03].
:::

<1>2. A fractional transformation supplies the target disk and prescribed zero.
::: proof
Set
$$
T(v)=\frac{v-2i}{v+2i},\qquad
S(w)=2i\frac{1+w}{1-w}.
$$
For $v\in H$, the denominator is nonzero and
$$
1-|T(v)|^2=\frac{8\operatorname{Im}v}{|v+2i|^2}>0.
$$
For $w\in D$, $1-w\ne0$ and
$$
\operatorname{Im}S(w)=2\frac{1-|w|^2}{|1-w|^2}>0.
$$
Substitution gives $T\circ S=\operatorname{id}_D$ and
$S\circ T=\operatorname{id}_H$. Hence $T:H\to D$ is
a holomorphic bijection. Composing it with step <1>1
gives the stated $f$, whose denominator cannot vanish
on $Q$. Finally $(1+i)^2=2i$, so $f(1+i)=T(2i)=0$.
:::
:::
