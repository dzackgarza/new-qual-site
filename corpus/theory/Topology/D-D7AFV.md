---
schema: qual/card@1
id: D-D7AFV
kind: definition
title: Isolated point
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Limits
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $A\subseteq X$.
A point $p\in A$ is an \dfn{isolated point} of $A$ if $p$ is not a [[D-Y6JAS|limit point]] of $A$.
:::

::: {.proposition}
A point $p\in A$ is an isolated point of $A$ if and only if there is a [[D-JMRPA|neighborhood]] $U$ of $p$ with $U\cap A = \ts{p}$.
:::

::: {.proof}
The point $p$ fails to be a limit point of $A$ exactly when some neighborhood $U$ of $p$ satisfies $(U\sm\ts{p})\cap A = \emptyset$.
Since $p\in U\cap A$, this is the condition $U\cap A = \ts{p}$.
:::
