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
By definition of the quotient topology, a subset $U$ of $X/\!\sim$ is open if and only if $p^{-1}(U)$ is an open subset of $X$. Every subset of $X$ is open, since $X$ has the discrete topology.
Hence every subset of $X/\!\sim$ is open; that is to say, $X/\!\sim$ is discrete.
:::
