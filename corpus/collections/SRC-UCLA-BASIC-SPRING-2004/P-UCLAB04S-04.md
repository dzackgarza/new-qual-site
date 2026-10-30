---
schema: qual/card@1
id: P-UCLAB04S-04
kind: problem
title: Infinite compact subsets of the rational numbers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Are there infinite compact subsets of $\QQ$?
Prove your assertion.
:::

::: {.solution}

Yes.

::: pf

::: {.pf-step #s1-1}

Define
$$
K=
\left\{
0
\right\}
\cup
\left\{
\frac1n:n\in\NN
\right\}.
$$
Then
$$
K\subseteq\QQ
$$
and $K$ is infinite.


::: pf-proof

Every number
$$
0,\frac11,\frac12,\frac13,\ldots
$$
is rational.
The numbers
$$
\frac1n
$$
are pairwise distinct, so $K$ contains infinitely many points.

:::

:::

::: {.pf-step #s1-2}

The set $K$ is bounded.


::: pf-proof

Every point of $K$ lies in the interval
$$
[0,1].
$$

:::

:::

::: {.pf-step #s1-3}

The set $K$ is closed in $\RR$.


::: pf-proof

Let
$$
x\in\RR\setminus K.
$$
If
$$
x<0
\quad\text{or}\quad
x>1,
$$
there is clearly an open interval around $x$ disjoint from $K$.

Suppose
$$
0<x<1
$$
and
$$
x\notin K.
$$
Choose $N$ so large that
$$
\frac1N<\frac{x}{2}.
$$
Then all points
$$
\frac1n
$$
with
$$
n\ge N
$$
lie in
$$
\left(0,\frac{x}{2}\right),
$$
and hence are at distance at least $x/2$ from $x$.

The remaining set
$$
\left\{
\frac11,\ldots,\frac1{N-1}
\right\}
$$
is finite and does not contain $x$.
Therefore
$$
d
=
\min_{1\le n<N}
\abs{
x-\frac1n
}
>
0.
$$
Taking
$$
r
<
\min\left\{
\frac{x}{2},
\frac d2
\right\}
$$
gives an open interval
$$
(x-r,x+r)
$$
that misses every point of $K$.
Thus
$$
\RR\setminus K
$$
is open, so $K$ is closed.

:::

:::

::: {.pf-step #s1-4}

The set $K$ is compact in $\RR$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, $K$ is closed and bounded.
The Heine--Borel theorem therefore implies that $K$ is compact.

:::

:::

::: {.pf-step #s1-5}

Therefore there exist infinite compact subsets of $\QQ$.


::: pf-proof

The set $K$ from step [](#s1-1){.pf-ref} is an infinite subset of $\QQ$, and step [](#s1-4){.pf-ref} proves that it is compact.
Hence
$$
\boxed{
\left\{
0
\right\}
\cup
\left\{
\frac1n:n\in\NN
\right\}
}
$$
is an explicit example.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers the question affirmatively.

:::

:::

:::
