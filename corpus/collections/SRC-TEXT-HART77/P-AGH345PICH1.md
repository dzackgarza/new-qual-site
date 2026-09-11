---
schema: qual/card@1
id: P-AGH345PICH1
kind: problem
title: The Picard group as first cohomology of the sheaf of units
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Picard Group
  - Invertible Sheaves
relations: []
review: draft
---

::: problem
For any ringed space $(X, \mco_X)$, let $\Pic X$ be the group of isomorphism classes of invertible sheaves (II, §6). Show that $\Pic X \cong H^1(X, \mco_X^*)$, where $\mco_X^*$ denotes the sheaf whose sections over an open set $U$ are the units in the ring $\Gamma(U, \mco_X)$, with multiplication as the group operation.

Hint: For any invertible sheaf $\mcl$ on $X$, cover $X$ by open sets $U_i$ on which $\mcl$ is free, and fix isomorphisms $\varphi_i: \mco_{U_i} \iso \ro{\mcl}{U_i}$.
Then on $U_i \intersect U_j$, we get an isomorphism $\varphi_i\inv \circ \varphi_j$ of $\mco_{U_i \intersect U_j}$ with itself.
These isomorphisms give an element of $\check{H}^1(\mathfrak{U}, \mco_X^*)$.
Now use (Ex.
4.4).
:::
