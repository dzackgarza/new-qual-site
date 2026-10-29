---
schema: qual/card@1
id: T-MODVB
kind: definition
title: Locally free sheaves are vector bundles
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Vector Bundles
  - Line Bundles
relations:
- kind: uses
  target: D-MODOX
- kind: related-to
  target: D-QNTZY
review: draft
prompts:
- What is a locally free sheaf, and what is its rank?
- What is the correspondence between locally free sheaves and vector bundles?
- Which direction of the correspondence is the sheaf of sections?
---

Vector bundles and locally free sheaves are the same gluing data: transition functions in $\GL_n$, viewed geometrically or as sheaves of sections.

::: {.definition title="Locally free"}
Let $(X,\OO_X)$ be a ringed space and let $\mcf$ be an $\OO_X$-module.
$\mcf$ is \dfn{free} if $\mcf \cong \bigoplus_{i \in I} \OO_X$ for some index set $I$, whose cardinality is its rank; it is free of rank $n$ if $\mcf \cong \OO_X\sumpower{n}$.
$\mcf$ is \dfn{locally free} if $X$ has an open cover $\theset{U_j}$ with each $\restrictionof{\mcf}{U_j}$ free, and locally free of rank $n$ if each $\restrictionof{\mcf}{U_j}$ is free of rank $n$.
The rank of a locally free sheaf is constant on each connected component of $X$.
An \dfn{invertible sheaf} is a locally free sheaf of rank $1$.
:::

::: {.theorem title="Bundles and sheaves"}
Taking a rank-$n$ vector bundle $\pi: E \to X$ to its sheaf of sections $U \mapsto \theset{s: U \to E \mid \pi s = \id}$ is an equivalence between rank-$n$ vector bundles on $X$ and locally free $\OO_X$-modules of rank $n$.
:::

::: {.remark}
Both objects are glued from trivialisations on a cover and transition functions in $\GL_n(\OO_X(U_{ij}))$ satisfying the cocycle condition; the equivalence identifies these two constructions.

A locally free sheaf is quasicoherent, and on a locally Noetherian scheme it is coherent when the rank is finite.
The fibre $\mcf \tensor \kappa(x)$ recovers the bundle's fibre.
A coherent sheaf on a reduced locally Noetherian scheme is locally free exactly when the function
$$
x\longmapsto\dim_{\kappa(x)}\bigl(\mcf\tensor_{\OO_X}\kappa(x)\bigr)
$$
is locally constant; the local algebra input is the reduced-local criterion in [[T-DEFNAKA]].
:::
