---
schema: qual/card@1
id: L-MYZOX
kind: lemma
title: Abel's test for power series on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
relations: []
review: draft
---

::: {.lemma}
Let $(c_k)_{k\ge0}$ be a nonincreasing sequence of nonnegative real numbers with $c_k\to0$, and let $f(z)\coloneqq\sum_{k\ge0}c_kz^k$.
Then the series $f(z)$ converges for every $z$ with $\abs{z}=1$ and $z\neq1$.
:::

::: {.proof}
Let $\abs{z}=1$ with $z\neq1$.
The partial sums of $\sum_k z^k$ satisfy $\abs{\sum_{k=0}^{N}z^k}=\abs{\frac{1-z^{N+1}}{1-z}}\le\frac{2}{\abs{1-z}}$ for every $N$, so they are bounded.
Since $(c_k)$ is nonincreasing with limit $0$, [[FT-3ZL25|Dirichlet's test]] applied to $a_k=c_k$ and $b_k=z^k$ shows that $\sum_k c_kz^k$ converges.
:::
