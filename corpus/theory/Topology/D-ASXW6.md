---
schema: qual/card@1
id: D-ASXW6
kind: definition
title: Closure of a set
classification:
  areas:
  - topology
  topics:
  - Closure
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $U\subseteq X$.
The \dfn{closure} of $U$ in $X$ is the intersection of all closed subsets of $X$ containing $U$,
$$
\cl_X(U) \coloneqq \Intersect_{\substack{B\supseteq U \\ B \text{ closed in } X}} B
,$$
also written $\bar U$.
:::

::: {.remark}
If $Y\subseteq X$ is a subspace containing $U$, the closure of $U$ in $Y$ is $\cl_Y(U) = \cl_X(U) \intersect Y$ [@Mun00, Theorem 17.4].
A point $x\in X$ lies in $\cl_X(U)$ if and only if every [[D-JMRPA|neighborhood]] of $x$ in $X$ intersects $U$ [@Mun00, Theorem 17.5].
:::
