---
schema: qual/card@1
id: FD-JJFZ3
kind: corollary
title: Irreducible-polynomial dichotomy in a normal extension
slogan: 'Over a normal extension, an irreducible polynomial either splits completely or has no root.'
prompts:
- What does an irreducible $p(x) \in K[x]$ do in a normal extension $L/K$?
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
relations: []
review: draft
---

::: {.corollary}
Let $L/K$ be a [[D-LZTAK|normal]] algebraic field extension and let $p\in K[x]$ be irreducible.
Then either $p$ has no root in $L$, or $p$ splits into linear factors in $L[x]$.
:::

::: {.proof}
If $p$ has a root in $L$, normality of $L/K$ says that $p$ splits into linear factors in $L[x]$.
Thus failure to split forces $p$ to have no root in $L$.
:::
