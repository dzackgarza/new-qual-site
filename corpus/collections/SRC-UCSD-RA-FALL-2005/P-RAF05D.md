---
schema: qual/card@1
id: P-RAF05D
kind: problem
title: "l^infinity is not separable"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Separability
  - Bounded Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2005 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Prove that $\ell^\infty$ (the space of all bounded sequences of complex numbers with the sup norm) is not separable.
:::

::: solution
<1>1. Construct an uncountable separated family.
::: proof
For each subset $A\subseteq\mathbb N$, let
\[
x^A=(x^A_n)_{n\ge1},
\qquad
x^A_n=\mathbf1_A(n).
\]
Then $x^A\in\ell^\infty$ and $\|x^A\|_\infty\le1$.

If $A\ne B$, choose $n\in A\triangle B$. Then
\[
|x^A_n-x^B_n|=1,
\]
so
\[
\|x^A-x^B\|_\infty=1.
\]
Thus
\[
\{x^A:A\subseteq\mathbb N\}
\]
is an uncountable $1$-separated subset of $\ell^\infty$.
:::

<1>2. A separable metric space cannot contain such a family.
::: proof
Suppose $\ell^\infty$ were separable, and let $D$ be a countable dense subset. The open balls
\[
B(x^A,1/3),
\qquad A\subseteq\mathbb N,
\]
are pairwise disjoint because the centers are distance $1$ apart.

Since $D$ is dense, every such ball contains at least one point of $D$. Pairwise disjointness forces distinct balls to contain distinct points of $D$. Hence there could be only countably many such balls, contradicting the uncountability of $\mathcal P(\mathbb N)$.

Therefore
\[
\boxed{\ell^\infty\text{ is not separable}.}
\]
:::
:::
