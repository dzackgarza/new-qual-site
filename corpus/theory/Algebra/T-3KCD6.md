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
By [[E-NNTQB|Lagrange's theorem]], the order of every element of $G$ divides $\abs G$. Cauchy's theorem is a partial converse: every prime divisor of $\abs G$ is the order of an element, although a composite divisor need not be.
[[T-WRMBM|Sylow's first theorem]] strengthens it: if $p^a$ is the largest power of $p$ dividing $\abs G$, then $G$ has a subgroup of order $p^a$.
:::
