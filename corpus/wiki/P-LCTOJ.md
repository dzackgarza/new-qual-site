---
schema: qual/card@1
id: P-LCTOJ
kind: problem
title: "Let $X = \\RR^3 - \\Delta^{(1)}$, the complement of the skeleton of regu\u2026"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - homology
  - homotopy
relations: []
review: draft
---

Let $X = \RR^3 - \Delta^{(1)}$, the complement of the skeleton of regular tetrahedron, and compute $\pi_1(X)$ and $H_*(X)$.

::: {.solution}
Lay the graph out flat in the plane, then take a maximal tree - these leaves 3 edges, and so $\pi_1(X) = \ZZ^{\ast 3}$.

Moreover $X \homotopic S^1\vee S^1 \vee S^1$ which has only a 1-skeleton, thus $H_*(X) = [\ZZ, \ZZ^3, 0\rightarrow]$.
:::
