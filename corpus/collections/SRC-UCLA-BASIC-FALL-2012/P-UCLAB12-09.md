---
schema: qual/card@1
id: P-UCLAB12-09
kind: problem
title: Least-squares minimizers form a coset of $\ker A$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let A be an m by n real matrix with $m \geq n$ Let $b \in \mathbb { R } ^ { m }$ . Let M be the set of vectors $x \in \mathbb { R } ^ { n }$ which minimize $| A x - b |$ Show that $M = x _ { 0 } + N$ where N is the kernel of A, and $x _ { 0 }$ is any element of M.
:::

::: {.solution}
Let
\[
N=\ker A
\]
and fix
\[
x_0\in M.
\]

<1>1. If $z\in N$, then
\[
x_0+z\in M.
\]

::: {.proof}
Since
\[
Az=0,
\]
one has
\[
A(x_0+z)-b
=
Ax_0-b.
\]
Therefore
\[
\|A(x_0+z)-b\|
=
\|Ax_0-b\|.
\]
Because $x_0$ is a minimizer, $x_0+z$ attains the same minimum value and belongs to $M$.
:::

<1>2. Hence
\[
x_0+N\subseteq M.
\]

::: {.proof}
Every element of $x_0+N$ has the form $x_0+z$ with $z\in N$, so step <1>1 applies.
:::

<1>3. If $x\in M$, then
\[
Ax=Ax_0.
\]

::: {.proof}
Both $Ax$ and $Ax_0$ lie in the subspace
\[
\operatorname{image}A\subseteq\mathbb R^m
\]
and both minimize the distance to $b$.
The nearest point in a linear subspace of Euclidean space is unique.

Indeed, if two distinct points $u,v$ in the subspace both had minimal distance $d$ to $b$, then their midpoint would also lie in the subspace, and the parallelogram identity would give
\[
\left\|b-\frac{u+v}{2}\right\|^2
=
d^2-\frac14\|u-v\|^2
<
d^2,
\]
contradicting minimality.
Thus
\[
Ax=Ax_0.
\]
:::

<1>4. If $x\in M$, then
\[
x-x_0\in N.
\]

::: {.proof}
By step <1>3,
\[
A(x-x_0)
=
Ax-Ax_0
=0.
\]
Hence
\[
x-x_0\in\ker A=N.
\]
:::

<1>5. Therefore
\[
M\subseteq x_0+N.
\]

::: {.proof}
If $x\in M$, step <1>4 gives
\[
x=x_0+(x-x_0)
\]
with $x-x_0\in N$.
:::

<1>6. Consequently
\[
\boxed{M=x_0+\ker A}.
\]

::: {.proof}
Combine the inclusions from steps <1>2 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required description of the set of minimizers.
:::
:::
