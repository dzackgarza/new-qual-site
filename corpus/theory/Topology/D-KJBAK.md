---
schema: qual/card@1
id: D-KJBAK
kind: definition
title: Dense subspace
prompts:
- In terms of closure, when is $A \subset X$ dense in $X$?
- When is a subset $A \subseteq X$ dense in $X$?
- What is a dense subset?
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
  - Density
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
A subset $Q\subseteq X$ is \dfn{dense} in $X$ if every [[D-JMRPA|neighborhood]] of every point $x\in X$ intersects $Q$ [@Mun00].
:::

::: {.proposition}
A subset $Q\subseteq X$ is dense in $X$ if and only if its [[D-ASXW6|closure]] is $\cl_X(Q) = X$, if and only if every nonempty open subset of $X$ meets $Q$.
:::
