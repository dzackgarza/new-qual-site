---
schema: qual/card@1
id: P-CASP05D
kind: problem
title: "Polynomial approximation for the reciprocal of a nonvanishing analytic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $K \subset \mathbb{C}$ be a compact set.
Assume that $\mathbb{C} \setminus K$ is connected and $0 \notin K$.
Prove that for any analytic function $f$ in an open neighborhood of $K$ nowhere vanishing on $K$, and any $\epsilon > 0$, there exists a polynomial $P$, satisfying $$|f(z)P(z) - 1| \leq \epsilon, \quad \forall z \in K.$$
:::

::: {.solution}
Because $f$ is analytic near $K$ and nonzero on $K$, compactness gives an open
neighborhood $U$ of $K$ on which $f$ has no zeros. Thus $1/f$ is holomorphic on
$U$.

Since $\mathbb C\setminus K$ is connected, Runge's theorem in its polynomial
form approximates functions holomorphic near $K$ uniformly on $K$ by
polynomials. Let
\[
A=\max_{z\in K}|f(z)|.
\]
Choose a polynomial $P$ such that
\[
\sup_K\left|P-\frac1f\right|<\frac{\epsilon}{A}
\]
(the case $A=0$ cannot occur because $f$ is nonvanishing on $K$). Then for
every $z\in K$,
\[
|f(z)P(z)-1|
\le |f(z)|\left|P(z)-\frac1{f(z)}\right|
<\epsilon.
\]
:::
