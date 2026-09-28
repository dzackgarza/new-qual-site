---
schema: qual/card@1
id: D-ZFRV4
kind: definition
title: Hausdorff space
prompts:
- What does it mean for a space to be Hausdorff?
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Separation Axioms
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{Hausdorff}, or $T_2$, if for all $p, q \in X$ with $p\neq q$ there exist disjoint open sets $U, V\subseteq X$ with $p\in U$ and $q\in V$.
:::

::: {.proposition}
In a Hausdorff space, every sequence converges to at most one point [@Mun00].
:::
