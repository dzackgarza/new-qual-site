---
schema: qual/card@1
id: D-6POU4
kind: definition
title: Intersection form of a manifold
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Poincaré Duality
  - Manifolds
relations: []
review: draft
---

::: {.definition}
Let $M$ be a closed, connected, oriented $2k$-manifold with [[D-TS7TZ|fundamental class]] $[M]\in H_{2k}(M;\ZZ)$.
The \dfn{intersection form} of $M$ is the bilinear form
$$
I\colon H^k(M;\ZZ)\cross H^k(M;\ZZ) \to \ZZ, \qquad I(a, b)\coloneqq \inner{a\smile b}{[M]}
,$$
where $\smile$ is the [[D-B2JER|cup product]] and $\inner{\wait}{\wait}$ is the [[D-VP4LC|Kronecker pairing]].
:::

::: {.remark}
Graded commutativity of the cup product gives $I(a, b) = (-1)^k I(b, a)$, so $I$ is symmetric when $k$ is even, that is, when $\dim M\equiv 0 \pmod 4$, and skew-symmetric when $k$ is odd.
By [[D-QP7WI|Poincaré duality]], $I$ vanishes on torsion classes and induces a nondegenerate form on $H^k(M;\ZZ)/\text{torsion}$ whose Gram matrix has determinant $\pm1$.
:::

::: {.concept}
[@Hat02].
:::
