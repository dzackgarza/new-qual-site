---
schema: qual/card@1
id: T-MODVB
kind: theorem
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

::: {.definition title="Locally free"}
$\mcf$ is \dfn{free} if $\mcf \cong \bigoplus_{i \in I} \OO_X$ for some index set $I$, whose cardinality is its rank; it is free of rank $n$ if $\mcf \cong \OO_X\sumpower{n}$.
$\mcf$ is **locally free** if $X$ has an open cover $\ts{U_j}$ with each $\ro{\mcf}{U_j}$ free, and locally free of rank $n$ if each $\ro{\mcf}{U_j}$ is free of rank $n$.
The rank of a locally free sheaf is constant on each connected component of $X$.
An **invertible sheaf** is a locally free sheaf of rank $1$.
:::

::: {.theorem title="Bundles and sheaves"}
Taking a rank-$n$ vector bundle $\pi: E \to X$ to its sheaf of sections $U \mapsto \ts{s: U \to E \mid \pi s = \id}$ is an equivalence between rank-$n$ vector bundles on $X$ and locally free $\OO_X$-modules of rank $n$.
:::

::: {.remark}
Both objects are glued from the same data — trivialisations on a cover, and transition functions in $\GL_n(\OO_X(U_{ij}))$ satisfying the cocycle condition — so the equivalence is really the statement that each is a name for that data.
The sheaf side is the one to compute with, because it lives in an abelian category where kernels, cokernels and cohomology exist; the bundle side is the one that makes geometric statements about fibres legible.

A locally free sheaf is quasicoherent, and on a locally Noetherian scheme it is coherent when the rank is finite: local freeness is the strongest of the three conditions, and the questions about it are questions about the transition data.
The fibre $\mcf \tensor \kappa(x)$ recovers the bundle's fibre, and a coherent sheaf on a reduced locally Noetherian scheme is locally free exactly when the fibre dimension $x \mapsto \dim_{\kappa(x)} \mcf \tensor \kappa(x)$ is locally constant.
:::
