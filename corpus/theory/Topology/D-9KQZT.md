---
schema: qual/card@1
id: D-9KQZT
kind: definition
title: Homeomorphism
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Continuity
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A bijection $f\colon X\to Y$ is a \dfn{homeomorphism} if both $f$ and $f\inv\colon Y\to X$ are [[D-AEAAD|continuous]].
The spaces $X$ and $Y$ are \dfn{homeomorphic}, written $X\cong Y$, if there exists a homeomorphism $X\to Y$.
:::

::: {.remark}
For a bijection $f\colon X\to Y$ the following are equivalent: $f$ is a homeomorphism; $f$ is continuous and open; for every $U\subseteq X$, $U$ is open in $X$ if and only if $f(U)$ is open in $Y$.
A homeomorphism therefore induces a bijection between the topologies of $X$ and $Y$, and every property defined in terms of open sets holds for $X$ if and only if it holds for $Y$.
An injective continuous map $f\colon X\to Y$ that is a homeomorphism onto $f(X)$ with the subspace topology is a [[D-BCNUH|topological embedding]].
:::

::: {.concept}
[@Mun00].
:::
