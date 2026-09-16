---
schema: qual/card@1
id: D-Y6JAS
kind: definition
title: Limit point
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Limits
  - Closure
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$, and $x\in X$.
The point $x$ is a \dfn{limit point} of $A$ if every [[D-JMRPA|neighborhood]] of $x$ meets $A\sm\ts{x}$.
:::

::: {.proposition}
A point $x\in X$ is a limit point of $A\subseteq X$ if and only if $x\in \cl_{X}(A\sm\ts{x})$, the [[D-ASXW6|closure]] of $A\sm\ts{x}$ in $X$.
:::
