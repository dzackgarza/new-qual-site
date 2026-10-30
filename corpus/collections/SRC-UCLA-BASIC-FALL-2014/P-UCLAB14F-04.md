---
schema: qual/card@1
id: P-UCLAB14F-04
kind: problem
title: A compactness theorem for bounded convex functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Let $f_n:[-2,2]\to[0,1]$ be a sequence of convex functions. Show that there is a subsequence which converges uniformly on $[-1,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f$ is convex on an interval and
$$
a<b<c,
$$
then the secant slopes satisfy
$$
\frac{f(b)-f(a)}{b-a}
\le
\frac{f(c)-f(a)}{c-a}
\le
\frac{f(c)-f(b)}{c-b}.
$$


::: pf-proof

Write
$$
b
=
\frac{c-b}{c-a}a
+
\frac{b-a}{c-a}c.
$$
Convexity gives
$$
f(b)
\le
\frac{c-b}{c-a}f(a)
+
\frac{b-a}{c-a}f(c).
$$
Rearranging yields
$$
\frac{f(b)-f(a)}{b-a}
\le
\frac{f(c)-f(a)}{c-a}.
$$
The second inequality follows by the same rearrangement, or equivalently by solving the same convexity inequality for the other secant slope.

:::

:::

::: {.pf-step #s1-2}

Let $f:[-2,2]\to[0,1]$ be convex.
If
$$
-1\le x<y\le1,
$$
then
$$
\frac{f(y)-f(x)}{y-x}\le1.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to
$$
x<y<2.
$$
Then
$$
\frac{f(y)-f(x)}{y-x}
\le
\frac{f(2)-f(y)}{2-y}.
$$
Because
$$
0\le f(y),f(2)\le1
$$
and
$$
2-y\ge1,
$$
one has
$$
\frac{f(2)-f(y)}{2-y}\le1.
$$

:::

:::

::: {.pf-step #s1-3}

Under the same hypotheses,
$$
\frac{f(y)-f(x)}{y-x}\ge-1.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to
$$
-2<x<y.
$$
Then
$$
\frac{f(x)-f(-2)}{x+2}
\le
\frac{f(y)-f(x)}{y-x}.
$$
Since
$$
f(x)-f(-2)\ge-1
$$
and
$$
x+2\ge1,
$$
the left side is at least $-1$.
Therefore the secant slope from $x$ to $y$ is at least $-1$.

:::

:::

::: {.pf-step #s1-4}

Every convex function
$$
f:[-2,2]\to[0,1]
$$
is $1$-Lipschitz on $[-1,1]$:
$$
\abs{f(y)-f(x)}\le\abs{y-x}
$$
for all $x,y\in[-1,1]$.


::: pf-proof

For $x<y$, steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give
$$
-1
\le
\frac{f(y)-f(x)}{y-x}
\le
1.
$$
Multiplying by $y-x>0$ gives
$$
\abs{f(y)-f(x)}\le y-x.
$$
The case $x>y$ follows by symmetry, and $x=y$ is trivial.

:::

:::

::: {.pf-step #s1-5}

The family
$$
\{f_n\restrict_{[-1,1]}:n\in\NN\}
$$
is uniformly bounded and equicontinuous.


::: pf-proof

Uniform boundedness follows from
$$
0\le f_n(x)\le1
$$
for all $n$ and $x$.

By step [](#s1-4){.pf-ref}, every $f_n$ is $1$-Lipschitz on $[-1,1]$.
Thus for every $\varepsilon>0$, choosing
$$
\delta=\varepsilon
$$
gives
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f_n(x)-f_n(y)}<\varepsilon
$$
simultaneously for all $n$.
Hence the family is equicontinuous.

:::

:::

::: {.pf-step #s1-6}

There is a subsequence $(f_{n_j})$ converging uniformly on $[-1,1]$.


::: pf-proof

The interval $[-1,1]$ is compact.
By step [](#s1-5){.pf-ref}, the restrictions of the functions form a uniformly bounded equicontinuous family in
$$
C([-1,1]).
$$
The Arzelà--Ascoli theorem therefore gives a uniformly convergent subsequence.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
