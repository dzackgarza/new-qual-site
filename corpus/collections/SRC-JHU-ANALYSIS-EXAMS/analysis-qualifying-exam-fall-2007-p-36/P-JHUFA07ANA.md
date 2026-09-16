---
schema: qual/card@1
id: P-JHUFA07ANA
kind: problem
title: "Complex analyticity of a real polynomial via the Cauchy-Riemann equations"
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
  note: "Visually checked every sign of Fall 2007 problem 1 on PDF page 36 and removed the trailing fragment of the next problem number."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Computed both Cauchy–Riemann equations, not just the one that holds identically, and distinguished differentiability on two lines from analyticity on an open set."
---

::: {.problem}
1) Is the function

$$
f ( x , y ) = x ^ { 3 } + 3 x y ^ { 2 } - 3 x ^ { 2 } y - 1 0 + i ( y ^ { 3 } + 3 x ^ { 2 } y - 3 y ^ { 2 } x + 5 )
$$

complex analytic? Prove that your answer is correct.
:::

::: solution
The function is not complex analytic on any nonempty open set.

<1>1. The Cauchy–Riemann equations hold only on two real lines.

::: proof
Write $f=u+iv$ with
$u=x^3+3xy^2-3x^2y-10$ and
$v=y^3+3x^2y-3xy^2+5$. Then
$$
u_x=3x^2+3y^2-6xy=v_y,\qquad
u_y=6xy-3x^2,\qquad v_x=6xy-3y^2.
$$
The remaining Cauchy–Riemann equation $u_y=-v_x$ is
equivalent to
$$
x^2-4xy+y^2=0,
\quad\text{or}\quad
\bigl(y-(2+\sqrt3)x\bigr)\bigl(y-(2-\sqrt3)x\bigr)=0.
$$
Thus the equations hold precisely on the union of these
two lines. As $u,v$ are polynomials, their real partial
derivatives are continuous; the Cauchy–Riemann criterion
therefore also shows complex differentiability at the
points of these lines [@SS03].
:::

<1>2. This pointwise differentiability cannot give analyticity on an open set.

::: proof
A holomorphic function must satisfy both Cauchy–Riemann
equations at every point of its open domain [@SS03].
The union of two lines contains no nonempty open disk:
in any disk one can fix a horizontal coordinate and
choose a vertical coordinate different from the at most
two values specified by the lines. Hence no nonempty
open set is contained in the differentiability locus.
In particular, at $(1,0)$ one has $u_y=-3$ but $-v_x=0$,
which alone rules out analyticity on the whole plane.
:::
:::
