---
schema: qual/card@1
id: P-UCLAB10S-12
kind: problem
title: Uniform bounds and pointwise convergence for nonnegative functions with $\int_0^1 f_n\to0$
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 12. Let $(f_n)$ be a sequence of nonnegative continuous functions on $[0,1]$ such that
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=0.
$$
Determine, with proof, whether each assertion must hold:

(a) There is a constant $B$ such that $f_n(x)\le B$ for every $x\in[0,1]$ and every $n$.

(b) There is a point $x_0\in[0,1]$ such that
$$
\lim_{n\to\infty}f_n(x_0)=0.
$$
:::

::: {.solution}

Both assertions are false.

::: pf

::: {.pf-step #s1-1}

For part (a), define
$$
g_n(x)
=
\begin{cases}
n^3x,
&0\le x\le n^{-2},\\[1mm]
n^3(2n^{-2}-x),
&n^{-2}\le x\le2n^{-2},\\[1mm]
0,
&2n^{-2}\le x\le1.
\end{cases}
$$
Then
$$
\int_0^1g_n(x)\,dx=\frac1n\to0,
$$
but
$$
\max_{x\in[0,1]}g_n(x)=n.
$$


::: pf-proof

The graph is a triangle of base
$$
2n^{-2}
$$
and height
$$
n^3n^{-2}=n.
$$
Thus its area is
$$
\frac12\cdot2n^{-2}\cdot n
=
\frac1n.
$$
The maximum value is the height $n$.
Therefore no constant $B$ can bound all the functions simultaneously.

:::

:::

::: {.pf-step #s1-2}

Consequently assertion (a) is false.


::: pf-proof

The sequence $(g_n)$ from step [](#s1-1){.pf-ref} consists of continuous nonnegative functions with integrals tending to $0$, but
$$
\sup_{n,x}g_n(x)=\infty.
$$
Hence the asserted uniform bound need not exist.

:::

:::

::: {.pf-step #s1-3}

For part (b), for each positive integer $m$ and each
$$
j=0,1,\ldots,m-1,
$$
choose a continuous function
$$
h_{m,j}:[0,1]\to[0,1]
$$
such that
$$
h_{m,j}(x)=1
$$
for
$$
x\in
\left[
\frac jm,\frac{j+1}{m}
\right]
$$
and
$$
h_{m,j}(x)=0
$$
outside
$$
\left(
\frac{j-1}{m},
\frac{j+2}{m}
\right)\cap[0,1].
$$


::: pf-proof

Such a function may be chosen piecewise linear:
take value $1$ on the closed cell
$$
\left[
\frac jm,\frac{j+1}{m}
\right],
$$
taper linearly to $0$ across each adjacent interval of length $1/m$ when present, and set it equal to $0$ elsewhere.
This gives a continuous function with values in $[0,1]$.

:::

:::

::: {.pf-step #s1-4}

Each function in step [](#s1-3){.pf-ref} satisfies
$$
\int_0^1h_{m,j}(x)\,dx
\le
\frac3m.
$$


::: pf-proof

The function takes values in $[0,1]$ and is supported in an interval of length at most
$$
\frac3m.
$$
Therefore its integral is at most the support length.

:::

:::

::: {.pf-step #s1-5}

Enumerate the functions block by block:
first all functions with $m=1$, then all with $m=2$, then all with $m=3$, and so on.
Call the resulting sequence
$$
(f_n).
$$
Then
$$
\int_0^1f_n(x)\,dx\to0.
$$


::: pf-proof

If $f_n$ belongs to the block indexed by $m$, step [](#s1-4){.pf-ref} gives
$$
\int_0^1f_n(x)\,dx
\le
\frac3m.
$$
As $n\to\infty$, the block index $m\to\infty$.
Hence
$$
\frac3m\to0,
$$
and the squeeze theorem gives
$$
\int_0^1f_n\to0.
$$

:::

:::

::: {.pf-step #s1-6}

Fix
$$
x\in[0,1].
$$
For every $m$, there exists
$$
j\in\{0,\ldots,m-1\}
$$
such that
$$
x\in
\left[
\frac jm,\frac{j+1}{m}
\right].
$$


::: pf-proof

The $m$ intervals
$$
\left[
\frac jm,\frac{j+1}{m}
\right],
\qquad
j=0,\ldots,m-1,
$$
cover $[0,1]$.

:::

:::

::: {.pf-step #s1-7}

For every $x\in[0,1]$, there are infinitely many indices $n$ for which
$$
f_n(x)=1.
$$


::: pf-proof

Fix $x$.
For each block $m$, choose a cell containing $x$ as in step [](#s1-6){.pf-ref}.
The corresponding function $h_{m,j}$ equals $1$ on that entire cell by step [](#s1-3){.pf-ref}.
Thus each block contributes at least one term of the enumerated sequence with value $1$ at $x$.
Since there are infinitely many blocks, this happens infinitely often.

:::

:::

::: {.pf-step #s1-8}

There is no point
$$
x_0\in[0,1]
$$
such that
$$
f_n(x_0)\to0.
$$


::: pf-proof

For every fixed $x_0$, step [](#s1-7){.pf-ref} gives infinitely many indices $n$ with
$$
f_n(x_0)=1.
$$
A sequence having infinitely many terms equal to $1$ cannot converge to $0$.
Thus no such $x_0$ exists.

:::

:::

::: {.pf-step #s1-9}

Consequently assertion (b) is false.


::: pf-proof

The sequence from step [](#s1-5){.pf-ref} consists of nonnegative continuous functions whose integrals tend to $0$, while step [](#s1-8){.pf-ref} shows that no point has pointwise limit $0$ along the full sequence.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} disproves assertion (a), and step [](#s1-9){.pf-ref} disproves assertion (b).

:::

:::

:::
