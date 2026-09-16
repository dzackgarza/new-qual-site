---
schema: qual/card@1
id: D-3KS2F
kind: definition
title: Boundary of a subset
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $A\subseteq X$.
The \dfn{boundary} of $A$ is $\bd A \coloneqq \cl_X(A) \sm A^\circ$, where $\cl_X(A)$ is the [[D-ASXW6|closure]] of $A$ and $A^\circ$, its interior, is the set of [[D-5VCMJ|interior points]] of $A$.
:::

::: {.remark}
A point $p\in X$ lies in $\bd A$ if and only if every [[D-JMRPA|neighborhood]] of $p$ intersects both $A$ and $X\sm A$.
:::
