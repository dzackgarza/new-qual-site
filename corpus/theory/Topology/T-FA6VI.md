---
schema: qual/card@1
id: T-FA6VI
kind: theorem
title: Characterizations of continuous maps
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Closure
  - Point-Set Topology
relations: []
review: draft
---

::: {.theorem}
Let $f\colon X\to Y$ be a map of topological spaces.
The following are equivalent:

- $f$ is continuous;

- $f(\cl_X(A)) \subseteq \cl_Y(f(A))$ for every $A\subseteq X$;

- $f\inv(B)$ is closed in $X$ for every closed $B\subseteq Y$;

- for each $x\in X$ and each neighborhood $V$ of $f(x)$, there is a neighborhood $U$ of $x$ such that $f(U) \subseteq V$

[@Mun00].
:::
