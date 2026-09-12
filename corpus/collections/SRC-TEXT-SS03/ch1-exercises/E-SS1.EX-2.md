---
schema: qual/card@1
id: E-SS1.EX-2
kind: problem
title: Euclidean and Hermitian inner products on $\mathbb C$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: exercise
Let $\langle\cdot,\cdot\rangle$ denote the usual inner product on $\mathbb R^2$:
\[
\langle (x_1,y_1),(x_2,y_2)\rangle=x_1x_2+y_1y_2.
\]
On $\mathbb C$, define the Hermitian inner product by
\[
(z,w)=z\overline w.
\]
Show that
\[
\langle z,w\rangle
=\frac12\bigl[(z,w)+(w,z)\bigr]
=\operatorname{Re}(z,w),
\]
where $z=x+iy\in\mathbb C$ is identified with $(x,y)\in\mathbb R^2$.
:::

::: {.solution}
<1>1. Write
\[
z=x_1+iy_1,
\qquad
w=x_2+iy_2.
\]
Then
\[
(z,w)=z\overline w
=(x_1x_2+y_1y_2)+i(y_1x_2-x_1y_2).
\]
::: {.proof}
Expand
\[
(x_1+iy_1)(x_2-iy_2)
=x_1x_2+y_1y_2+i(y_1x_2-x_1y_2).
\]
:::

<1>2. Therefore
\[
\operatorname{Re}(z,w)=x_1x_2+y_1y_2=\langle z,w\rangle.
\]
::: {.proof}
The real part of the expression in <1>1 is $x_1x_2+y_1y_2$, which is the Euclidean inner product under the usual identification $\mathbb C\cong\mathbb R^2$.
:::

<1>3. One has
\[
(w,z)=\overline{(z,w)}.
\]
::: {.proof}
Indeed,
\[
(w,z)=w\overline z=\overline{z\overline w}=\overline{(z,w)}.
\]
:::

<1>4. Hence
\[
\frac12\bigl[(z,w)+(w,z)\bigr]=\operatorname{Re}(z,w).
\]
::: {.proof}
By <1>3, the left-hand side is
\[
\frac12\bigl((z,w)+\overline{(z,w)}\bigr),
\]
which is the real part of $(z,w)$.
:::

<1>5. Combining the preceding identities gives
\[
\langle z,w\rangle
=\frac12\bigl[(z,w)+(w,z)\bigr]
=\operatorname{Re}(z,w).
\]
::: {.proof}
Use <1>2 and <1>4.
:::
:::
