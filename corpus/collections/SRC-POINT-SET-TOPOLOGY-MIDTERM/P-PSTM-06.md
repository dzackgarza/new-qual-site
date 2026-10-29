---
schema: qual/card@1
id: P-PSTM-06
kind: problem
title: A quotient of a discrete space is discrete
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $X$ be a discrete topological space, and let $\sim$ be an equivalence relation on $X$.
Prove that $X/\!\sim$, endowed with the quotient topology, is also a discrete space.
:::

::: {.solution}
Let $p\colon X \to X/\!\sim$ be the quotient map.

::: pf

::: pf-step
Every subset $U \subseteq X/\!\sim$ is open, so $X/\!\sim$ is discrete.

::: pf-proof
In the quotient topology, $U$ is open if and only if $p^{-1}(U)$ is open in $X$.
Every subset of $X$ is open, because $X$ is discrete, so $p^{-1}(U)$ is open.
:::

:::

:::
:::
