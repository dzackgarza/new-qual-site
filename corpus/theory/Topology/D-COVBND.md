---
schema: qual/card@1
id: D-COVBND
kind: proposition
title: Covering spaces of manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Manifolds
relations: []
review: draft
---

::: {.proposition}
Let $B$ be a manifold with boundary and $p\colon A\to B$ a covering map.
Then $A$ is a manifold with boundary and $p^{-1}(\bd B)=\bd A$ [@Hat02, §3.3].
:::

::: {.proof}
Each $b\in B$ has an open neighborhood $U$ homeomorphic to $\RR^n$ or to the half-space $\RR^n_+$, and $p^{-1}(U)$ is a disjoint union of open sets each mapped homeomorphically onto $U$.
Each point of $A$ therefore has a neighborhood homeomorphic to $\RR^n$ or $\RR^n_+$, so $A$ is a manifold with boundary.
By the definition of the boundary through local homology, $b\in\bd B$ exactly when $H_n(B,B\sm\theset b;\ZZ)=0$; a point of $A$ over such a $b$ has a neighborhood homeomorphic to $\RR^n_+$ and lies in $\bd A$, and a point over $B\sm\bd B$ has a neighborhood homeomorphic to $\RR^n$ and does not.
:::
