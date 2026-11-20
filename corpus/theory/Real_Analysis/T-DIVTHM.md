---
schema: qual/card@1
id: T-DIVTHM
kind: theorem
title: The divergence theorem
slogan: 'flux across a closed surface equals the integral of the divergence over the solid it bounds'
classification:
  areas:
  - real-analysis
  topics:
  - Divergence Theorem
  - Vector Calculus
relations: []
review: draft
---

::: {.theorem}
Let $M\subseteq\RR^n$ be a compact $n$-manifold, let $N$ be the unit normal vector field to $\bd M$ that points outwards from $M$, and let $G$ be a vector field defined on an open set of $\RR^n$ containing $M$.
Then
$$
\int_M (\operatorname{div}G)\,dV = \int_{\bd M}\inner{G}{N}\,dS,
$$
the first integral with respect to $n$-volume and the second with respect to $(n-1)$-volume.

This is [@Mun91, Theorem 38.8].
:::
