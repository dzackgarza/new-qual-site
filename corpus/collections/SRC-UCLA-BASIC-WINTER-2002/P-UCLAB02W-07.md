---
schema: qual/card@1
id: P-UCLAB02W-07
kind: problem
title: A nonsingular planar map covering the open unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Suppose $F:\mathbb R^2\to\mathbb R^2$ is differentiable everywhere, its derivative matrix is continuous everywhere, and its Jacobian determinant is everywhere nonzero.
Assume also that
\[
\|F(x,y)\|\geq1
\quad\text{whenever}\quad
\|(x,y)\|=1,
\]
and that
\[
F(0,0)=(0,0).
\]
Prove that
\[
F\bigl(\{(x,y):x^2+y^2<1\}\bigr)
\supseteq
\{(x,y):x^2+y^2<1\}.
\]

Hint: if $U=\{(x,y):x^2+y^2<1\}$, prove that $F(U)\cap U$ is open and closed in $U$.
:::

Let
\[
U=\{p\in\mathbb R^2:\|p\|<1\}
\]
and define
\[
Y=F(U)\cap U.
\]

::: pf

::: pf-step

The set $Y$ is nonempty.


::: pf-proof

By hypothesis,
\[
F(0,0)=(0,0).
\]
Since
\[
(0,0)\in U,
\]
one has
\[
(0,0)\in F(U)\cap U=Y.
\]

:::

:::

::: pf-step

The set $F(U)$ is open in $\mathbb R^2$.


::: pf-proof

Fix
\[
p\in U.
\]
The derivative
\[
DF(p)
\]
has nonzero determinant by hypothesis, hence is invertible.
The inverse function theorem therefore gives an open neighborhood
\[
N_p\subseteq U
\]
such that
\[
F(N_p)
\]
is open in $\mathbb R^2$.
Since
\[
F(U)
=
\bigcup_{p\in U}F(N_p),
\]
the set $F(U)$ is open.

:::

:::

::: pf-step

The set $Y$ is open in the subspace $U$.


::: pf-proof

By step <1>2, $F(U)$ is open in $\mathbb R^2$.
Therefore
\[
Y=F(U)\cap U
\]
is open in the subspace topology on $U$.

:::

:::

::: pf-step

Let $(y_n)$ be a sequence in $Y$ converging to a point
\[
y\in U.
\]
For each $n$, choose
\[
x_n\in U
\]
such that
\[
F(x_n)=y_n.
\]


::: pf-proof

Every $y_n$ belongs to $F(U)$ by definition of $Y$, so such an $x_n$ exists.

:::

:::

::: pf-step

The sequence $(x_n)$ has a convergent subsequence
\[
x_{n_k}\to x
\]
with
\[
x\in\overline U.
\]


::: pf-proof

The closed unit disk
\[
\overline U
=
\{p\in\mathbb R^2:\|p\|\le1\}
\]
is compact.
Every $x_n$ belongs to $U\subseteq\overline U$.
Hence Bolzano--Weierstrass gives a convergent subsequence with limit in $\overline U$.

:::

:::

::: pf-step

One has
\[
F(x)=y.
\]


::: pf-proof

The map $F$ is continuous because its derivative matrix is continuous.
Therefore
\[
F(x)
=
F\!\left(\lim_{k\to\infty}x_{n_k}\right)
=
\lim_{k\to\infty}F(x_{n_k})
=
\lim_{k\to\infty}y_{n_k}
=
y.
\]

:::

:::

::: pf-step

The limit point $x$ lies in $U$, not on $\partial U$.


::: pf-proof

Suppose
\[
\|x\|=1.
\]
Then the boundary hypothesis gives
\[
\|F(x)\|\ge1.
\]
By step <1>6,
\[
F(x)=y.
\]
But
\[
y\in U,
\]
so
\[
\|y\|<1,
\]
a contradiction.
Thus
\[
\|x\|<1,
\]
so $x\in U$.

:::

:::

::: pf-step

The set $Y$ is closed in $U$.


::: pf-proof

Let
\[
y_n\in Y
\]
converge to
\[
y\in U.
\]
Steps <1>4--<1>7 produce
\[
x\in U
\]
such that
\[
F(x)=y.
\]
Hence
\[
y\in F(U)\cap U=Y.
\]
Thus $Y$ contains every limit in $U$ of sequences from $Y$, so it is closed in the metric space $U$.

:::

:::

::: pf-step

One has
\[
Y=U.
\]


::: pf-proof

The open unit disk $U$ is connected.
By steps <1>1, <1>3, and <1>8, the subset $Y\subseteq U$ is nonempty and both open and closed in $U$.
Connectedness therefore forces
\[
Y=U.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{F(U)\supseteq U}.
\]


::: pf-proof

Since
\[
Y=F(U)\cap U,
\]
step <1>9 gives
\[
F(U)\cap U=U.
\]
This is equivalent to
\[
U\subseteq F(U).
\]

:::

:::

::: pf-qed

Step <1>10 is the required conclusion.

:::

:::
