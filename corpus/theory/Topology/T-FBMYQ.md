---
schema: qual/card@1
id: T-FBMYQ
kind: theorem
title: Excision
slogan: 'For $Z\subseteq A\subseteq X$ with $\cl_X(Z)\subseteq A^\circ$, removing $Z$ from $X$ and $A$ does not change $H_*(X, A)$.'
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.theorem}
Given subspaces $Z \subseteq A \subseteq X$ with $\cl_X(Z) \subseteq \interiorof{A}$, the inclusion of pairs induces isomorphisms
$$
H_n(X\sm Z,\, A\sm Z) \mapsvia{\sim} H_n(X, A) \qquad \text{for all } n
.$$
Equivalently, for subspaces $A, B\subseteq X$ with $X = \interiorof{A} \union \interiorof{B}$, the inclusion $(B, A\intersect B)\injects (X, A)$ induces isomorphisms $H_n(B, A\intersect B)\mapsvia{\sim} H_n(X,A)$ for all $n$.
The two forms are related by $B = X\sm Z$ [@Hat02].
:::
