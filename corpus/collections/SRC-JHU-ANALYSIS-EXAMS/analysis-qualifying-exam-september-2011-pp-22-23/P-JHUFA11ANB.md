---
schema: qual/card@1
id: P-JHUFA11ANB
kind: problem
title: A harmonic function on the plane bounded below is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared September 2011 problem 2 on PDF page 22; replaced the truncated conclusion title without changing the lower-bound hypothesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked an explicit globally defined harmonic conjugate, both Cauchy–Riemann equations, and the nonzero exponential factor needed to deduce constancy."
---

::: {.problem}
2. Let $h : \mathbb { C } \to \mathbb { R }$ be a harmonic function such that h is bounded below.
   Prove that h is constant.
:::

::: {.solution}
<1>1. Construct an entire function whose real part is $h$.

::: {.proof}
Write $z=x+iy$, regard $h$ as a function of $(x,y)$, and
define on all of $\mathbb R^2$
$$
v(x,y)=-\int_0^x h_y(t,0)\,dt+
\int_0^y h_x(x,s)\,ds.
$$
The first and second derivatives used here are continuous,
and $h_{xx}+h_{yy}=0$, since $h$ is harmonic.
Differentiation under these finite integrals gives
$$
v_y(x,y)=h_x(x,y),
$$
and
$$
\begin{aligned}
v_x(x,y)
&=-h_y(x,0)+\int_0^y h_{xx}(x,s)\,ds\\
&=-h_y(x,0)-\int_0^y h_{yy}(x,s)\,ds
=-h_y(x,y).
\end{aligned}
$$
Thus $H=h+iv$ has continuous first partial derivatives
and satisfies the Cauchy–Riemann equations on the plane.
It is entire and has real part $h$ [@SS03].
:::

<1>2. The lower bound makes an entire exponential bounded.

::: {.proof}
Choose $m\in\mathbb R$ with $h(z)\geq m$ everywhere.
Then $E(z)=e^{-H(z)}$ is entire and satisfies
$$
|E(z)|=e^{-\operatorname{Re}H(z)}=e^{-h(z)}\leq e^{-m}.
$$
Liouville's theorem makes $E$ constant [@SS03]. Since
an exponential never vanishes, differentiation of this
constant function yields
$0=E'=-H'e^{-H}$ and hence $H'=0$ everywhere.
An entire function with zero derivative is constant on
the connected plane, so $h=\operatorname{Re}H$ is constant.
:::
:::
