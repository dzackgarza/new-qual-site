---
schema: qual/card@1
id: D-GIUR3
kind: definition
title: Lefschetz duality
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations:
- kind: related-to
  target: T-QNYSB
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and $M$ a compact [[D-YD6DR|$R$-orientable]] $n$-[[D-MN6QW|manifold with boundary]] $\del M$, with fundamental class $[M]\in H_n(M, \del M; R)$.
The \dfn{Lefschetz duality maps} are the [[D-RQS4J|cap products]] with $[M]$,
$$
D_M\colon H^k(M, \del M; R)\to H_{n-k}(M; R), \qquad D_M\colon H^k(M; R)\to H_{n-k}(M, \del M; R),
$$
given by $D_M(\varphi) = [M]\frown\varphi$.
:::

::: {.theorem}
In the situation of the definition, both maps $D_M$ are isomorphisms for every $k$.
:::

::: {.remark}
For $\del M = \emptyset$ the theorem is [[D-QP7WI|Poincaré duality]].
The version in which $\del M$ is decomposed as a union of two compact $(n-1)$-manifolds with common boundary is [[T-QNYSB]].
:::

::: {.concept}
See [@Hat02, §3.3, Theorem 3.43].
:::
