---
schema: qual/card@1
id: P-UCLAB07S-08
kind: problem
title: Differentiability of a pointwise limit under uniform derivative bounds
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Suppose $f_n\in C^2([0,1])$, $f_n(x)\to f(x)$ pointwise, and
\[
|f_n'(x)|\le1,\qquad |f_n''(x)|\le1
\]
for every $x\in[0,1]$ and $n\ge1$.
Prove that $f$ is continuously differentiable on $[0,1]$.
:::

::: pf

::: pf-step

The family of derivatives
\[
\{f_n':n\ge1\}
\]
is uniformly bounded on $[0,1]$.


::: pf-proof

This is exactly the hypothesis
\[
|f_n'(x)|\le1
\]
for every
\[
x\in[0,1]
\]
and every $n$.

:::

:::

::: pf-step

The family
\[
\{f_n':n\ge1\}
\]
is equicontinuous on $[0,1]$.


::: pf-proof

Fix
\[
x,y\in[0,1].
\]
By the mean value theorem applied to $f_n'$,
\[
|f_n'(x)-f_n'(y)|
\le
\sup_{t\in[0,1]}|f_n''(t)|\,|x-y|.
\]
The hypothesis gives
\[
|f_n''(t)|\le1,
\]
so
\[
|f_n'(x)-f_n'(y)|
\le
|x-y|
\]
for every $n$.
Thus every derivative is $1$-Lipschitz, with a common Lipschitz constant.
Hence the family is equicontinuous.

:::

:::

::: pf-step

There is a subsequence
\[
(f_{n_j}')
\]
that converges uniformly on $[0,1]$ to a continuous function
\[
g:[0,1]\to\mathbb R.
\]


::: pf-proof

By steps <1>1--<1>2, the family of derivatives is uniformly bounded and equicontinuous on the compact interval $[0,1]$.
The Arzelà--Ascoli theorem therefore yields a uniformly convergent subsequence.
Each $f_{n_j}'$ is continuous, so its uniform limit $g$ is continuous.

:::

:::

::: pf-step

One has
\[
f_{n_j}(0)\to f(0).
\]


::: pf-proof

The original sequence satisfies
\[
f_n(x)\to f(x)
\]
pointwise for every
\[
x\in[0,1].
\]
Taking
\[
x=0
\]
and passing to the subsequence gives the claim.

:::

:::

::: pf-step

For every $j$ and every
\[
x\in[0,1],
\]
one has
\[
f_{n_j}(x)
=
f_{n_j}(0)
+
\int_0^x f_{n_j}'(t)\,dt.
\]


::: pf-proof

Each
\[
f_{n_j}
\]
belongs to
\[
C^2([0,1]),
\]
hence is continuously differentiable.
The fundamental theorem of calculus gives the displayed identity.

:::

:::

::: pf-step

For every
\[
x\in[0,1],
\]
one has
\[
\int_0^x f_{n_j}'(t)\,dt
\longrightarrow
\int_0^x g(t)\,dt.
\]


::: pf-proof

Uniform convergence from step <1>3 gives
\[
\|f_{n_j}'-g\|_\infty\to0.
\]
Therefore
\[
\begin{aligned}
\left|
\int_0^x f_{n_j}'(t)\,dt
-
\int_0^x g(t)\,dt
\right|
&\le
\int_0^x
|f_{n_j}'(t)-g(t)|
\,dt\\
&\le
x\,
\|f_{n_j}'-g\|_\infty\\
&\le
\|f_{n_j}'-g\|_\infty
\longrightarrow0.
\end{aligned}
\]

:::

:::

::: pf-step

For every
\[
x\in[0,1],
\]
one has
\[
\boxed{
f(x)
=
f(0)
+
\int_0^x g(t)\,dt
}.
\]


::: pf-proof

Take the limit
\[
j\to\infty
\]
in the identity from step <1>5.
The left side converges to
\[
f(x)
\]
by pointwise convergence of the original sequence.
The first term on the right converges to
\[
f(0)
\]
by step <1>4.
The integral term converges by step <1>6.
Thus the displayed identity follows.

:::

:::

::: pf-step

The function $f$ is continuously differentiable and
\[
\boxed{f'(x)=g(x)}.
\]


::: pf-proof

The function $g$ is continuous by step <1>3.
By step <1>7,
\[
f(x)
=
f(0)
+
\int_0^x g(t)\,dt.
\]
The fundamental theorem of calculus therefore gives
\[
f'(x)=g(x)
\]
for every
\[
x\in[0,1].
\]
Since $g$ is continuous,
\[
f'
\]
is continuous.
Hence
\[
f\in C^1([0,1]).
\]

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
