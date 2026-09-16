---
schema: qual/card@1
id: PR-4EVYE
kind: proposition
title: The Cauchy condensation test
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
---

::: {.proposition}
Let $(a_k)_{k\geq1}$ be a nonincreasing sequence of nonnegative real numbers.
Then
$$
\sum_{k\geq 1} a_k < \infty \iff \sum_{k\geq 1} 2^k a_{2^k}<\infty .
$$
:::

::: {.proof}
Group the terms in dyadic blocks $2^k\le j<2^{k+1}$.
Since $(a_j)$ is nonincreasing, each block satisfies
$$
2^k a_{2^{k+1}}\le\sum_{j=2^k}^{2^{k+1}-1}a_j\le 2^k a_{2^k}.
$$
Summing over $0\le k\le K$ gives
$$
\frac12\sum_{k=1}^{K+1}2^{k}a_{2^{k}}\le\sum_{j=1}^{2^{K+1}-1}a_j\le\sum_{k=0}^{K}2^k a_{2^k}.
$$
Both series have nonnegative terms, so their partial sums are nondecreasing, and these bounds show that one sequence of partial sums is bounded if and only if the other is; the term $a_1$ omitted from $\sum_{k\geq1}2^ka_{2^k}$ does not affect convergence.
:::
