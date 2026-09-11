---
schema: qual/card@1
id: PR-ET5PQ
kind: proposition
title: $H^1$ classifies line bundles and extensions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Line Bundles
  - Picard Group
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- What is the connection between $H^1$ and line bundles?
- What does $H^1$ classify besides line bundles?
---

::: {.proposition}
$\Pic(X) \cong H^1(X, \OO_X^*)$, and for $\OO_X$-modules $\mathcal{F}, \mathcal{G}$ the extensions
\[
0 \to \mathcal{F} \to \mathcal{E} \to \mathcal{G} \to 0
\]
up to equivalence are classified by $\operatorname{Ext}^1(\mathcal{G},\mathcal{F})$, which is $H^1(X, \mathcal{F} \tensor \mathcal{G}\dual)$ when $\mathcal{G}$ is locally free.
:::

::: {.remark}
The isomorphism is the Čech description read backwards: a line bundle is trivial on some cover, the transition functions $g_{ij} \in \OO^*(U_i \intersect U_j)$ satisfy the cocycle condition, and changing the trivialisations changes them by a coboundary.
So $H^1$ of the units is the group of line bundles, with tensor product as the group law.

This is the same phenomenon as the failure of right exactness on sections in [[algebraic-geometry/sheaves/stalks-and-exactness|stalks and exactness]], and it is worth saying so: in both cases $H^1$ measures the failure of local data to be global, once as sections that do not glue and once as trivialisations that do not agree.

On a complex manifold the exponential sequence makes it explicit,
\[
H^1(X,\OO) \to H^1(X,\OO^*) \to H^2(X,\ZZ) ,
\]
where the second map is the first Chern class: the topological type of a line bundle, with $H^1(X,\OO)$ measuring how many holomorphic structures carry it.
:::
