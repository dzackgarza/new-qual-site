---
schema: qual/card@1
id: D-QP7WI
kind: definition
title: Poincaré duality
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
  - Orientation
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and $M$ a closed [[D-YD6DR|$R$-orientable]] $n$-manifold with [[D-TS7TZ|fundamental class]] $[M]\in H_n(M;R)$.
The \dfn{Poincaré duality map} is
$$
D\colon H^k(M;R)\to H_{n-k}(M;R),\qquad D(\alpha)\coloneqq[M]\frown\alpha,
$$
given by the [[D-RQS4J|cap product]] with $[M]$.
:::

::: {.theorem}
In this situation $D\colon H^k(M;R)\to H_{n-k}(M;R)$ is an isomorphism for every $k$ [@Hat02, Theorem 3.30].
:::
