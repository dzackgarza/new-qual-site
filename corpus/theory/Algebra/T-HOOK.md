---
schema: qual/card@1
id: T-HOOK
kind: theorem
title: The hook length formula
slogan: '$f^\lambda=n!/\prod_{c\in\lambda}h(c)$'
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
  - Young Tableaux
relations: []
review: draft
---

::: {.theorem}
Let $\lambda$ be a partition of $n$, and for a cell $c$ of the Young diagram of $\lambda$ let $h(c)$ be its hook length, the number of cells in the same row to its right, in the same column below it, and the cell itself.
Then the number of standard Young tableaux of shape $\lambda$ is
$$
f^\lambda = \frac{n!}{\prod_{c\in\lambda}h(c)},
$$
and this is the dimension of the irreducible representation $S^\lambda$ of $S_n$ indexed by $\lambda$.
:::
