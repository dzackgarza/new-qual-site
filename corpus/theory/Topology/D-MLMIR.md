---
schema: qual/card@1
id: D-MLMIR
kind: definition
title: Boundary of a manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$ and let $M$ be a [[D-MN6QW|topological $n$-manifold with boundary]].
The \dfn{boundary} of $M$ is the subspace
$$
\del M \coloneqq \theset{x\in M \st H_n(M, M\setminus\theset{x}; \ZZ) = 0}
$$
[@Hat02, §3.3, p. 253].
:::

::: {.proposition}
A point $x\in M$ lies in $\del M$ if and only if a neighborhood of $x$ is carried homeomorphically onto an open subset of $\theset{y\in\RR^n \st y_n\geq 0}$ with $x$ going to a point with $y_n = 0$; for every other point, $H_n(M, M\setminus\theset{x};\ZZ)\cong\ZZ$.
The boundary $\del M$ is an $(n-1)$-manifold with empty boundary [@Hat02, §3.3, p. 253].
:::
