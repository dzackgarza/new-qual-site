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
Are there infinite compact subsets of $\mathbb Q$?
Prove your assertion.
:::

::: {.solution}
Yes.

<1>1. Define
\[
K=
\left\{
0
\right\}
\cup
\left\{
\frac1n:n\in\mathbb N
\right\}.
\]
Then
\[
K\subseteq\mathbb Q
\]
and $K$ is infinite.

::: {.proof}
Every number
\[
0,\frac11,\frac12,\frac13,\ldots
\]
is rational.
The numbers
\[
\frac1n
\]
are pairwise distinct, so $K$ contains infinitely many points.
:::

<1>2. The set $K$ is bounded.

::: {.proof}
Every point of $K$ lies in the interval
\[
[0,1].
\]
:::

<1>3. The set $K$ is closed in $\mathbb R$.

::: {.proof}
Let
\[
x\in\mathbb R\setminus K.
\]
If
\[
x<0
\quad\text{or}\quad
x>1,
\]
there is clearly an open interval around $x$ disjoint from $K$.

Suppose
\[
0<x<1
\]
and
\[
x\notin K.
\]
Choose $N$ so large that
\[
\frac1N<\frac{x}{2}.
\]
Then all points
\[
\frac1n
\]
with
\[
n\ge N
\]
lie in
\[
\left(0,\frac{x}{2}\right),
\]
and hence are at distance at least $x/2$ from $x$.

The remaining set
\[
\left\{
\frac11,\ldots,\frac1{N-1}
\right\}
\]
is finite and does not contain $x$.
Therefore
\[
d
=
\min_{1\le n<N}
\left|
x-\frac1n
\right|
>
0.
\]
Taking
\[
r
<
\min\left\{
\frac{x}{2},
\frac d2
\right\}
\]
gives an open interval
\[
(x-r,x+r)
\]
that misses every point of $K$.
Thus
\[
\mathbb R\setminus K
\]
is open, so $K$ is closed.
:::

<1>4. The set $K$ is compact in $\mathbb R$.

::: {.proof}
By steps <1>2--<1>3, $K$ is closed and bounded.
The Heine--Borel theorem therefore implies that $K$ is compact.
:::

<1>5. Therefore there exist infinite compact subsets of $\mathbb Q$.

::: {.proof}
The set $K$ from step <1>1 is an infinite subset of $\mathbb Q$, and step <1>4 proves that it is compact.
Hence
\[
\boxed{
\left\{
0
\right\}
\cup
\left\{
\frac1n:n\in\mathbb N
\right\}
}
\]
is an explicit example.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers the question affirmatively.
:::
:::
