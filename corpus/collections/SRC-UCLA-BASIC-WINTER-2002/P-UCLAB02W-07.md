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
Suppose $F:\RR^2\to\RR^2$ is differentiable everywhere, its derivative matrix is continuous everywhere, and its Jacobian determinant is everywhere nonzero.
Assume also that
$$
\norm{F(x,y)}\geq1
\quad\text{whenever}\quad
\norm{(x,y)}=1,
$$
and that
$$
F(0,0)=(0,0).
$$
Prove that
$$
F\bigl(\{(x,y):x^2+y^2<1\}\bigr)
\supseteq
\{(x,y):x^2+y^2<1\}.
$$

Hint: if $U=\{(x,y):x^2+y^2<1\}$, prove that $F(U)\cap U$ is open and closed in $U$.
:::

::: {.solution}

Let
$$
U=\{p\in\RR^2:\norm{p}<1\}
$$
and define
$$
Y=F(U)\cap U.
$$

::: pf

::: {.pf-step #s1-1}

The set $Y$ is nonempty.


::: pf-proof

By hypothesis,
$$
F(0,0)=(0,0).
$$
Since
$$
(0,0)\in U,
$$
one has
$$
(0,0)\in F(U)\cap U=Y.
$$

:::

:::

::: {.pf-step #s1-2}

The set $F(U)$ is open in $\RR^2$.


::: pf-proof

Fix
$$
p\in U.
$$
The derivative
$$
DF(p)
$$
has nonzero determinant by hypothesis, hence is invertible.
The inverse function theorem therefore gives an open neighborhood
$$
N_p\subseteq U
$$
such that
$$
F(N_p)
$$
is open in $\RR^2$.
Since
$$
F(U)
=
\bigcup_{p\in U}F(N_p),
$$
the set $F(U)$ is open.

:::

:::

::: {.pf-step #s1-3}

The set $Y$ is open in the subspace $U$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $F(U)$ is open in $\RR^2$.
Therefore
$$
Y=F(U)\cap U
$$
is open in the subspace topology on $U$.

:::

:::

::: {.pf-step #s1-4}

Let $(y_n)$ be a sequence in $Y$ converging to a point
$$
y\in U.
$$
For each $n$, choose
$$
x_n\in U
$$
such that
$$
F(x_n)=y_n.
$$


::: pf-proof

Every $y_n$ belongs to $F(U)$ by definition of $Y$, so such an $x_n$ exists.

:::

:::

::: {.pf-step #s1-5}

The sequence $(x_n)$ has a convergent subsequence
$$
x_{n_k}\to x
$$
with
$$
x\in\overline U.
$$


::: pf-proof

The closed unit disk
$$
\overline U
=
\{p\in\RR^2:\norm{p}\le1\}
$$
is compact.
Every $x_n$ belongs to $U\subseteq\overline U$.
Hence Bolzano--Weierstrass gives a convergent subsequence with limit in $\overline U$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
F(x)=y.
$$


::: pf-proof

The map $F$ is continuous because its derivative matrix is continuous.
Therefore
$$
F(x)
=
F\!\left(\lim_{k\to\infty}x_{n_k}\right)
=
\lim_{k\to\infty}F(x_{n_k})
=
\lim_{k\to\infty}y_{n_k}
=
y.
$$

:::

:::

::: {.pf-step #s1-7}

The limit point $x$ lies in $U$, not on $\partial U$.


::: pf-proof

Suppose
$$
\norm{x}=1.
$$
Then the boundary hypothesis gives
$$
\norm{F(x)}\ge1.
$$
By step [](#s1-6){.pf-ref},
$$
F(x)=y.
$$
But
$$
y\in U,
$$
so
$$
\norm{y}<1,
$$
a contradiction.
Thus
$$
\norm{x}<1,
$$
so $x\in U$.

:::

:::

::: {.pf-step #s1-8}

The set $Y$ is closed in $U$.


::: pf-proof

Let
$$
y_n\in Y
$$
converge to
$$
y\in U.
$$
Steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} produce
$$
x\in U
$$
such that
$$
F(x)=y.
$$
Hence
$$
y\in F(U)\cap U=Y.
$$
Thus $Y$ contains every limit in $U$ of sequences from $Y$, so it is closed in the metric space $U$.

:::

:::

::: {.pf-step #s1-9}

One has
$$
Y=U.
$$


::: pf-proof

The open unit disk $U$ is connected.
By steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-8){.pf-ref}, the subset $Y\subseteq U$ is nonempty and both open and closed in $U$.
Connectedness therefore forces
$$
Y=U.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{F(U)\supseteq U}.
$$


::: pf-proof

Since
$$
Y=F(U)\cap U,
$$
step [](#s1-9){.pf-ref} gives
$$
F(U)\cap U=U.
$$
This is equivalent to
$$
U\subseteq F(U).
$$

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
