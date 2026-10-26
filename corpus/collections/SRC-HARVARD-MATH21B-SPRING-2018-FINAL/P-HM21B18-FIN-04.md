---
schema: qual/card@1
id: P-HM21B18-FIN-04
kind: problem
title: Row reduction for a four-variable affine system and the orthogonal complement of its kernel
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Find all $(x,y,z,w)\in\mathbb R^4$ satisfying
\[
x+y+z+w=20,
\qquad
x-y+z-w=10,
\]
by row-reducing the augmented matrix. Then find two linearly independent vectors perpendicular to the kernel of the coefficient matrix.
:::

Let
\[
A=
\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1
\end{pmatrix}.
\]

::: pf

::: pf-step

The augmented matrix reduces to
\[
\left[
\begin{array}{cccc|c}
1&0&1&0&15\\
0&1&0&1&5
\end{array}
\right].
\]


::: pf-proof

Starting from
\[
\left[
\begin{array}{cccc|c}
1&1&1&1&20\\
1&-1&1&-1&10
\end{array}
\right],
\]
apply $R_2\leftarrow R_2-R_1$, then
$R_2\leftarrow-\frac12R_2$, and finally
$R_1\leftarrow R_1-R_2$. This gives
\[
\left[
\begin{array}{cccc|c}
1&0&1&0&15\\
0&1&0&1&5
\end{array}
\right].
\]

:::

:::

::: pf-step

All solutions are
\[
(x,y,z,w)
=(15,5,0,0)
+s(-1,0,1,0)
+t(0,-1,0,1),
\qquad s,t\in\mathbb R.
\]


::: pf-proof

Step <1>1 gives $x+z=15$ and $y+w=5$. Set $z=s$ and $w=t$.
Then $x=15-s$ and $y=5-t$, which is exactly the displayed
parametrization.

:::

:::

::: pf-step

The kernel of $A$ is
\[
\ker A
=\operatorname{span}\{(-1,0,1,0),(0,-1,0,1)\}.
\]


::: pf-proof

The homogeneous version of the reduced system in step <1>1 is
$x+z=0$ and $y+w=0$. Parametrizing it as in step <1>2 gives the displayed
basis.

:::

:::

::: pf-step

The vectors
\[
r_1=(1,1,1,1),
\qquad
r_2=(1,-1,1,-1)
\]
are linearly independent and perpendicular to $\ker A$.


::: pf-proof

They are the two rows of $A$, and they are not scalar multiples, so they
are linearly independent. For the basis vectors from step <1>3,
\[
\begin{aligned}
r_1\cdot(-1,0,1,0)&=0,&
r_1\cdot(0,-1,0,1)&=0,\\
r_2\cdot(-1,0,1,0)&=0,&
r_2\cdot(0,-1,0,1)&=0.
\end{aligned}
\]
Hence each $r_i$ is perpendicular to every vector in $\ker A$.

:::

:::

::: pf-step

Therefore the requested results are
\[
\boxed{
\begin{gathered}
(x,y,z,w)
=(15,5,0,0)+s(-1,0,1,0)+t(0,-1,0,1),\\
s,t\in\mathbb R,\\
(1,1,1,1),\ (1,-1,1,-1)\in(\ker A)^\perp
\text{ are linearly independent.}
\end{gathered}}
\]


::: pf-proof

The solution set is step <1>2, and step <1>4 supplies the two required
vectors.

:::

:::

::: pf-qed

Step <1>5 contains both requested outputs.

:::

:::
