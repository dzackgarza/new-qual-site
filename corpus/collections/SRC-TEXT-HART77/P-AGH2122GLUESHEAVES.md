---
schema: qual/card@1
id: P-AGH2122GLUESHEAVES
kind: problem
title: Glueing sheaves along an open cover with cocycle data
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Glueing
  - Descent
relations: []
review: draft
---

::: {.problem}
Let $X$ be a topological space, let $\mathfrak{U} = \ts{U_i}$ be an open cover of $X$, and suppose we are given for each $i$ a sheaf $\mcf_i$ on $U_i$, and for each $i, j$ an isomorphism
\[
\phi_{ij}: \ro{\mcf_i}{U_i \intersect U_j} \to \ro{\mcf_j}{U_i \intersect U_j}
\]
such that

1. for each $i$, $\phi_{ii} = \id$, and

2. for each $i, j, k$, $\phi_{ik} = \phi_{jk} \circ \phi_{ij}$ on $U_i \intersect U_j \intersect U_k$.

Show that there exists a unique sheaf $\mcf$ on $X$, together with isomorphisms $\psi_i: \ro{\mcf}{U_i} \to \mcf_i$, such that for each $i, j$ one has $\psi_j = \phi_{ij} \circ \psi_i$ on $U_i \intersect U_j$.
We say that $\mcf$ is obtained by **glueing** the sheaves $\mcf_i$ via the isomorphisms $\phi_{ij}$.
:::
