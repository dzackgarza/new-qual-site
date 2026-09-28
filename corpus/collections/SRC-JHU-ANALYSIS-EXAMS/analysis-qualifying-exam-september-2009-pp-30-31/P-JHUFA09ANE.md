---
schema: qual/card@1
id: P-JHUFA09ANE
kind: problem
title: Complex differentiability at a point without local holomorphy
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann Equations
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the real polynomial and both true-or-false assertions with September 2009 problem 5 in the retained JHU extraction; replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Bounded the difference quotient in all complex directions and exhibited Cauchy–Riemann failure at real nonzero points in every neighborhood of zero."
---

::: {.problem}
5. Let

$$
f ( x + i y ) = x ^ { 3 } - 3 x y ^ { 2 } + i y ^ { 3 } .
$$

State whether each of the following is true or false and give proofs for your answers:

a) the complex derivative $f ^ { \prime } ( 0 )$ exists;

b) f is holomorphic in a neighborhood of 0.
:::

::: {.solution}
Part (a) is true, with $f'(0)=0$. Part (b) is false.

<1>1. The difference quotient tends to zero at the origin.

::: {.proof}
For $z=x+iy$, one has $f(0)=0$ and $|x|,|y|\leq|z|$.
The triangle inequality gives
$$
|f(z)|\leq |x|^3+3|x||y|^2+|y|^3\leq5|z|^3.
$$
Thus for $z\ne0$,
$$
\left|\frac{f(z)-f(0)}z\right|\leq5|z|^2\longrightarrow0.
$$
This limit is independent of the direction of approach,
so the complex derivative exists and equals zero.
:::

<1>2. Every neighborhood contains a point where the complex derivative fails to exist.

::: {.proof}
Writing $f=u+iv$, its real partial derivatives are
$$
u_x=3x^2-3y^2,\qquad u_y=-6xy,\qquad
v_x=0,\qquad v_y=3y^2.
$$
Complex differentiability requires the Cauchy–Riemann
equations $u_x=v_y$ and $u_y=-v_x$ [@SS03].
At a point $(x,0)$ with $x\ne0$, the first equation
would read $3x^2=0$, which is false. Every neighborhood
of zero contains such a point. Therefore no neighborhood
of zero is a domain on which $f$ is holomorphic, proving (b).
:::
:::
