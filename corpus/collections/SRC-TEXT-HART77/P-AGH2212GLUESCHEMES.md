---
schema: qual/card@1
id: P-AGH2212GLUESCHEMES
kind: problem
title: Glueing a family of schemes along open subschemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Glueing
  - Disjoint Unions
relations: []
review: draft
---

::: {.problem}
Generalize the glueing procedure of the text as follows.
Let $\ts{X_i}$ be a possibly infinite family of schemes.
For each $i \neq j$ suppose given an open subset $U_{ij} \subseteq X_i$ with its induced scheme structure.
Suppose also given for each $i \neq j$ an isomorphism of schemes $\phi_{ij}: U_{ij} \to U_{ji}$ such that

1. for each $i, j$, $\phi_{ji} = \phi_{ij}\inv$, and

2. for each $i, j, k$, $\phi_{ij}(U_{ij} \intersect U_{ik}) = U_{ji} \intersect U_{jk}$ and $\phi_{ik} = \phi_{jk} \circ \phi_{ij}$ on $U_{ij} \intersect U_{ik}$.

Then show that there is a scheme $X$, together with morphisms $\psi_i: X_i \to X$ for each $i$, such that

1. $\psi_i$ is an isomorphism of $X_i$ onto an open subscheme of $X$,

2. the $\psi_i(X_i)$ cover $X$,

3. $\psi_i(U_{ij}) = \psi_i(X_i) \intersect \psi_j(X_j)$, and

4. $\psi_i = \psi_j \circ \phi_{ij}$ on $U_{ij}$.

We say that $X$ is obtained by **glueing** the schemes $X_i$ along the isomorphisms $\phi_{ij}$.
An interesting special case is when the family $X_i$ is arbitrary but all the $U_{ij}$ and $\phi_{ij}$ are empty; then $X$ is called the **disjoint union** of the $X_i$ and is denoted $\coprod X_i$.
:::
