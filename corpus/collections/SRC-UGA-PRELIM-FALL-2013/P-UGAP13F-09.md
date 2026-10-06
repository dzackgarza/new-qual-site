---
schema: qual/card@1
id: P-UGAP13F-09
kind: problem
title: Construct a linear map on $\mathbb R^3$ with a prescribed one-dimensional kernel
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give an example, with proof, of a linear map from $\mathbb R^3$ to some vector space whose kernel is exactly the subspace spanned by $(1,2,3)$.
:::

::: {.solution}
Define
\[
\boxed{
T:\mathbb R^3\to\mathbb R^2,
\qquad
T(x,y,z)
=
(2x-y,,3x-z).
}
\]

<1>1. The map $T$ is linear.

::: {.proof}
It is given by the matrix
\[
\begin{pmatrix}
2&-1&0\\
3&0&-1
\end{pmatrix}.
\]
Hence for
\[
u,v\in\mathbb R^3
\]
and
\[
a,b\in\mathbb R,
\]
\[
T(au+bv)
=
aT(u)+bT(v).
\]
:::

<1>2. The vector
\[
(1,2,3)
\]
lies in the kernel of $T$.

::: {.proof}
Compute
\[
T(1,2,3)
=
(2-2,,3-3)
=
(0,0).
\]
Therefore
\[
\operatorname{span}\{(1,2,3)\}
\subseteq
\ker T.
\]
:::

<1>3. If
\[
(x,y,z)\in\ker T,
\]
then
\[
y=2x
\qquad\text{and}\qquad
z=3x.
\]

::: {.proof}
The condition
\[
T(x,y,z)=(0,0)
\]
is exactly the system
\[
2x-y=0,
\qquad
3x-z=0.
\]
Solving gives the two displayed equations.
:::

<1>4. Hence every vector in the kernel has the form
\[
(x,y,z)
=
x(1,2,3).
\]

::: {.proof}
Substitute the equations from step <1>3:
\[
(x,y,z)
=
(x,2x,3x)
=
x(1,2,3).
\]
Therefore
\[
\ker T
\subseteq
\operatorname{span}\{(1,2,3)\}.
\]
:::

<1>5. Thus
\[
\boxed{
\ker T
=
\operatorname{span}\{(1,2,3)\}.
}
\]

::: {.proof}
Combine the two inclusions from steps <1>2 and <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 verifies that the displayed linear map has exactly the prescribed
kernel.
:::
:::
