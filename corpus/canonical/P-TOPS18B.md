---
schema: qual/card@1
id: P-TOPS18B
kind: problem
title: "Mayer-Vietoris computation of a closed 4-manifold from gluing two copies of B^2 x S^2"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Manifolds
  - Intersection Theory
  - Homotopy Type
relations: []
review: draft
solved: false
---

::: problem
Let $S^2$ be the standard unit sphere, and let $R_\theta : S^2 \to S^2$ be the operation of rotation through angle $\theta$ anticlockwise about the $z$-axis.
Let $M$ be the closed $4$-manifold obtained by gluing together two copies $A_1, A_2$ of $B^2 \times S^2$ along their common boundary $S^1 \times S^2$; specifically, identify
$$
(e^{i\theta}, v) \in \partial A_1 \sim (e^{i\theta}, R_\theta(v)) \in \partial A_2 \quad \text{for all } e^{i\theta} \in S^1, v \in S^2.
$$
Use Mayer-Vietoris to compute $H_*(M; \mathbb{Z})$.
Give an example of another closed $4$-manifold $N$ with the same homology, and use intersection theory to show that $M$ and $N$ are not homotopy-equivalent.
:::
