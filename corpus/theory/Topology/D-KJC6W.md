---
schema: qual/card@1
id: D-KJC6W
kind: definition
title: Closed set
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
Let $X$ be a topological space.
A subset $A\subseteq X$ is \dfn{closed} in $X$ if its complement $X\sm A$ is open in $X$.
:::

::: {.proposition}
Let $X$ be a topological space and $A\subseteq X$.

(a) $A$ is closed in $X$ if and only if $A$ contains every [[D-Y6JAS|limit point]] of $A$ in $X$.

(b) If $Y\subseteq X$ is a subspace with the [[D-LB2LS|subspace topology]] and $A\subseteq Y$, then $A$ is closed in $Y$ if and only if $A = C\cap Y$ for some closed $C\subseteq X$, and the [[D-ASXW6|closure]] of $A$ in $Y$ is $\cl_Y(A) = \cl_X(A)\cap Y$.
:::

::: {.concept}
See [@Mun00, §17, Theorems 17.2 and 17.4 and Corollary 17.7].
:::
