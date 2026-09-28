---
schema: qual/card@1
id: T-3KCD6
kind: theorem
title: Cauchy's theorem
slogan: 'Every prime divisor of a finite group order occurs as an element order.'
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Cosets and Lagrange
  - p-Groups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a finite group and $p$ a prime dividing $\abs{G}$.
Then $G$ has an element of order $p$, and hence a subgroup of order $p$.
:::

::: {.remark}
By [[T-SZRXI|Lagrange's theorem]], the order of every element of $G$ divides $\abs G$; conversely, Cauchy's theorem gives an element of order $p$ for every prime $p$ dividing $\abs G$.
[[T-WRMBM|Sylow's first theorem]] strengthens it: if $p^a$ is the largest power of $p$ dividing $\abs G$, then $G$ has a subgroup of order $p^a$.
:::
