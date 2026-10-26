---
schema: qual/card@1
id: P-UCLAB02S-03
kind: problem
title: Compact metric spaces are sequentially compact
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Suppose $X$ is a compact metric space, where compactness is understood in the open-cover sense.
Prove directly that every sequence
\[
(x_n)_{n\geq1},\qquad x_n\in X,
\]
has a convergent subsequence.

Do not merely quote a theorem asserting the result.
:::

Let
\[
(x_n)_{n\ge1}
\]
be an arbitrary sequence in $X$.

::: pf

::: pf-step

If some point $x\in X$ has the property that every neighborhood of $x$ contains infinitely many terms of the sequence, then $(x_n)$ has a subsequence converging to $x$.


::: pf-proof

For each positive integer $k$, the ball
\[
B\left(x,\frac1k\right)
\]
contains infinitely many terms of the sequence.
Choose indices inductively so that
\[
n_1<n_2<\cdots
\]
and
\[
x_{n_k}\in B\left(x,\frac1k\right).
\]
Then
\[
d(x_{n_k},x)<\frac1k,
\]
so
\[
x_{n_k}\to x.
\]

:::

:::

::: pf-step

Suppose, for contradiction, that $(x_n)$ has no convergent subsequence.
Then for every $x\in X$, there is an open neighborhood $U_x$ of $x$ containing only finitely many terms $x_n$.


::: pf-proof

If some $x\in X$ had every neighborhood containing infinitely many terms, step <1>1 would produce a convergent subsequence.
Thus for each $x$, at least one neighborhood contains only finitely many terms.

:::

:::

::: pf-step

The family
\[
\{U_x:x\in X\}
\]
is an open cover of $X$.


::: pf-proof

By construction,
\[
x\in U_x
\]
for each $x\in X$.
Thus every point is covered.

:::

:::

::: pf-step

By compactness, there are finitely many points
\[
x^{(1)},\ldots,x^{(m)}\in X
\]
such that
\[
X
=
U_{x^{(1)}}\cup\cdots\cup U_{x^{(m)}}.
\]


::: pf-proof

This is exactly the open-cover definition of compactness applied to the cover in step <1>3.

:::

:::

::: pf-step

The finite union in step <1>4 contains only finitely many terms of the sequence.


::: pf-proof

Each set
\[
U_{x^{(j)}}
\]
contains only finitely many terms $x_n$ by step <1>2.
The union of finitely many finite sets of indices is finite.
Hence only finitely many sequence terms lie in the union.

:::

:::

::: pf-step

Step <1>5 is impossible.


::: pf-proof

Every term
\[
x_n
\]
belongs to $X$.
By step <1>4,
\[
X
=
\bigcup_{j=1}^mU_{x^{(j)}}.
\]
Therefore every sequence term lies in the finite union.
But step <1>5 says only finitely many terms lie there.
This contradicts the existence of infinitely many indexed terms
\[
x_1,x_2,\ldots.
\]

:::

:::

::: pf-step

Therefore $(x_n)$ has a convergent subsequence.


::: pf-proof

The assumption in step <1>2 that no convergent subsequence exists leads to the contradiction in step <1>6.
Hence some convergent subsequence must exist.

:::

:::

::: pf-qed

Step <1>7 proves directly from open-cover compactness that every sequence in $X$ has a convergent subsequence.

:::

:::
