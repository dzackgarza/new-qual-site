---
schema: qual/card@1
id: P-UCLAB13F-01
kind: problem
title: Infinite products and convergence of positive series
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $a_n>0$ and define
\[
P_n=\prod_{j=1}^n(1+a_j).
\]
Prove that $\lim_{n\to\infty}P_n$ exists and is a nonzero real number if and only if
\[
\sum_n a_n<\infty.
\]
:::

Since every $a_n>0$, one has
\[
P_n>0
\]
for every $n$.

::: pf

::: pf-step

For every $x\ge0$,
\[
\log(1+x)\le x.
\]


::: pf-proof

Define
\[
h(x)=x-\log(1+x).
\]
Then
\[
h(0)=0
\]
and
\[
h'(x)
=
1-\frac1{1+x}
=
\frac{x}{1+x}
\ge0.
\]
Thus $h(x)\ge0$ for $x\ge0$, which is the stated inequality.

:::

:::

::: pf-step

If
\[
\sum_{n=1}^{\infty}a_n<\infty,
\]
then
\[
\sum_{n=1}^{\infty}\log(1+a_n)
\]
converges.


::: pf-proof

By step <1>1,
\[
0<\log(1+a_n)\le a_n.
\]
The comparison test therefore gives convergence.

:::

:::

::: pf-step

If
\[
\sum_n a_n<\infty,
\]
then $P_n$ converges to a finite positive number.


::: pf-proof

By definition,
\[
\log P_n
=
\sum_{j=1}^n\log(1+a_j).
\]
By step <1>2, these partial sums converge to some finite real number $L$.
Continuity of the exponential gives
\[
P_n
=
\exp(\log P_n)
\longrightarrow
e^L.
\]
Since $e^L>0$, the limit is a nonzero real number.

:::

:::

::: pf-step

Conversely, suppose
\[
P_n\to P
\]
for some finite number $P>0$.
Then
\[
a_n\to0.
\]


::: pf-proof

For $n\ge2$,
\[
1+a_n
=
\frac{P_n}{P_{n-1}}.
\]
Since
\[
P_n\to P
\qquad\text{and}\qquad
P_{n-1}\to P>0,
\]
one has
\[
\frac{P_n}{P_{n-1}}\to1.
\]
Therefore
\[
a_n\to0.
\]

:::

:::

::: pf-step

For every $x\in[0,1]$,
\[
\log(1+x)\ge\frac{x}{2}.
\]


::: pf-proof

Define
\[
g(x)=\log(1+x)-\frac{x}{2}.
\]
Then
\[
g(0)=0
\]
and
\[
g'(x)
=
\frac1{1+x}-\frac12
=
\frac{1-x}{2(1+x)}
\ge0
\]
for $0\le x\le1$.
Thus $g(x)\ge0$ on $[0,1]$.

:::

:::

::: pf-step

Under the assumption in step <1>4,
\[
\sum_{n=1}^{\infty}\log(1+a_n)
\]
converges.


::: pf-proof

Since
\[
P_n\to P>0,
\]
continuity of $\log$ gives
\[
\log P_n\to\log P.
\]
But
\[
\log P_n
=
\sum_{j=1}^n\log(1+a_j).
\]
Thus the displayed series converges.

:::

:::

::: pf-step

Under the assumption in step <1>4,
\[
\sum_{n=1}^{\infty}a_n<\infty.
\]


::: pf-proof

By step <1>4, there exists $N$ such that
\[
0<a_n\le1
\]
for every $n\ge N$.
Then step <1>5 gives
\[
a_n
\le
2\log(1+a_n)
\]
for $n\ge N$.
The series on the right converges by step <1>6, so the comparison test gives
\[
\sum_{n=N}^{\infty}a_n<\infty.
\]
Adding the finitely many initial terms proves convergence of the full series.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\lim_{n\to\infty}P_n
\text{ exists and is nonzero}
\iff
\sum_{n=1}^{\infty}a_n<\infty
}.
\]


::: pf-proof

Step <1>3 proves the forward construction from convergence of $\sum a_n$, and step <1>7 proves the converse.

:::

:::

::: pf-qed

Step <1>8 is the required equivalence.

:::

:::
