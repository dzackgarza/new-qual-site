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

Let
\[
N=\ker A
\]
and fix
\[
x_0\in M.
\]

::: pf

::: pf-step

If $z\in N$, then
\[
x_0+z\in M.
\]


::: pf-proof

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

:::

::: pf-step

Hence
\[
x_0+N\subseteq M.
\]


::: pf-proof

Every element of $x_0+N$ has the form $x_0+z$ with $z\in N$, so step <1>1 applies.

:::

:::

::: pf-step

If $x\in M$, then
\[
Ax=Ax_0.
\]


::: pf-proof

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

:::

::: pf-step

If $x\in M$, then
\[
x-x_0\in N.
\]


::: pf-proof

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

:::

::: pf-step

Therefore
\[
M\subseteq x_0+N.
\]


::: pf-proof

If $x\in M$, step <1>4 gives
\[
x=x_0+(x-x_0)
\]
with $x-x_0\in N$.

:::

:::

::: pf-step

Consequently
\[
\boxed{M=x_0+\ker A}.
\]


::: pf-proof

Combine the inclusions from steps <1>2 and <1>5.

:::

:::

::: pf-qed

Step <1>6 is the required description of the set of minimizers.

:::

:::
