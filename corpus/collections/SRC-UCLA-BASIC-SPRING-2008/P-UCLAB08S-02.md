---
schema: qual/card@1
id: P-UCLAB08S-02
kind: problem
title: Pointwise convergence need not imply convergence of integrals
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $(f_n)$ be a sequence of continuous nonnegative functions on $[0,1]$ such that $f_n(x)\to0$ for every $x\in[0,1]$.
Prove or give a counterexample to the assertion
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=0.
$$
:::

::: {.solution}

The assertion is false.

::: pf

::: {.pf-step #s1-1}

For each integer
$$
n\ge2,
$$
define
$$
f_n(x)
=
\begin{cases}
n^2x,
&0\le x\le \frac1n,\\[2mm]
n^2\left(\frac2n-x\right),
&\frac1n\le x\le\frac2n,\\[2mm]
0,
&\frac2n\le x\le1.
\end{cases}
$$


::: pf-proof

The formulas agree at the break points:
$$
n^2\cdot\frac1n
=n
=
n^2\left(\frac2n-\frac1n\right),
$$
and
$$
n^2\left(\frac2n-\frac2n\right)=0.
$$
Hence each $f_n$ is continuous.
All three pieces are nonnegative, so
$$
f_n(x)\ge0
$$
on $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

For every fixed
$$
x\in[0,1],
$$
one has
$$
f_n(x)\to0.
$$


::: pf-proof

If
$$
x=0,
$$
then
$$
f_n(0)=0
$$
for every $n$.

Fix
$$
x>0.
$$
Since
$$
\frac2n\to0,
$$
there exists $N$ such that
$$
\frac2n<x
$$
for every
$$
n\ge N.
$$
Then
$$
x\ge\frac2n,
$$
so by the third branch of the definition,
$$
f_n(x)=0
$$
for every $n\ge N$.
Thus
$$
f_n(x)\to0.
$$

:::

:::

::: {.pf-step #s1-3}

For every $n\ge2$,
$$
\boxed{
\int_0^1 f_n(x)\,dx=1
}.
$$


::: pf-proof

The graph of $f_n$ is a triangle supported on
$$
\left[0,\frac2n\right],
$$
with base length
$$
\frac2n
$$
and height
$$
n.
$$
Hence its area is
$$
\frac12\cdot\frac2n\cdot n
=1.
$$
Therefore
$$
\int_0^1f_n(x)\,dx=1.
$$

:::

:::

::: {.pf-step #s1-4}

Consequently
$$
\lim_{n\to\infty}\int_0^1f_n(x)\,dx
=1
\ne
0.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the integral is identically $1$ for all $n$.
Thus its limit is $1$.

:::

:::

::: {.pf-step #s1-5}

Therefore pointwise convergence
$$
f_n(x)\to0
$$
of continuous nonnegative functions does not imply convergence of the integrals to $0$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} verify all hypotheses of the problem for this sequence, while step [](#s1-4){.pf-ref} contradicts the asserted conclusion.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required counterexample.

:::

:::

:::
