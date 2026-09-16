---
schema: qual/card@1
id: D-UI7ZL
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
Let $X$ be a [[D-2TZAI|topological space]].
A subset $U \subseteq X$ is \dfn{closed} in $X$ if its complement $X\sm U$ is open in $X$.
If $Y \subseteq X$ carries the [[D-LB2LS|subspace topology]] and $U \subseteq Y$, then $U$ is \dfn{closed in the subspace} $Y$ if $Y\sm U$ is open in $Y$.
:::

::: {.proposition}
Let $X$ be a topological space and $U\subseteq X$.

(a) $U$ is closed in $X$ if and only if every [[D-Y6JAS|limit point]] of $U$ in $X$ lies in $U$.

(b) $U$ is closed in $X$ if and only if $\cl_X(U) = U$, where $\cl_X(U)$ is the [[D-ASXW6|closure]] of $U$ in $X$.

(c) If $Y\subseteq X$ is a subspace and $U\subseteq Y$, then $U$ is closed in $Y$ if and only if $U = Y \intersect V$ for some closed subset $V$ of $X$.
:::

::: {.concept}
[@Mun00].
:::
