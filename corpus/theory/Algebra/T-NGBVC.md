---
schema: qual/card@1
id: T-NGBVC
kind: theorem
title: Finite extensions are algebraic
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.theorem}
Let $L/K$ be a field extension with $[L:K]<\infty$.
Then every $\alpha\in L$ is algebraic over $K$.
:::

::: {.proof}
Let $n=[L:K]$.
The $n+1$ elements $1,\alpha,\ldots,\alpha^n$ of the $n$-dimensional $K$-vector space $L$ are linearly dependent, so there are $c_0,\ldots,c_n\in K$, not all zero, with $\sum_{i=0}^n c_i\alpha^i=0$.
Thus $\alpha$ is a root of the nonzero polynomial $\sum_{i=0}^n c_ix^i\in K[x]$.
:::
