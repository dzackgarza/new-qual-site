---
schema: qual/card@1
id: P-TOPS06A
kind: problem
title: "Cohomology ring, manifold property, and fundamental group of a hexagon with opposite edges identified"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Fundamental Group
  - Manifolds
  - Cell Complexes
relations: []
review: draft
---

::: problem
Let $X$ be the topological space obtained by taking a regular hexagon and identifying opposite edges in a parallel fashion as shown.

(a) Calculate the integral cohomology ring of $X$.

(b) Can $X$ be homotopy equivalent to a two dimensional compact manifold?

(c) Calculate the fundamental group of $X$.
:::

::: {.solution}
<1>1. Pairing opposite sides of the regular hexagon by the indicated parallel translations gives a torus.
::: {.proof}
The regular hexagon tiles the plane by translations in a rank-two lattice. Identifying each pair of opposite parallel sides is exactly the quotient of one fundamental hexagon by that lattice, hence produces $\mathbb R^2/\Lambda\cong T^2$.
:::

<1>2. Therefore
$$\boxed{\pi_1(X)\cong\mathbb Z^2.}$$
::: {.proof}
The fundamental group of the torus is the lattice of deck translations of its universal cover $\mathbb R^2$.
:::

<1>3. If $u,v\in H^1(X;\mathbb Z)$ are the dual generators, then
$$\boxed{H^*(X;\mathbb Z)\cong\Lambda_{\mathbb Z}(u,v),\qquad |u|=|v|=1.}$$
Equivalently, $u^2=v^2=0$ and $u\smile v$ generates $H^2(X;\mathbb Z)\cong\mathbb Z$.
::: {.proof}
This is the standard integral cohomology ring of $T^2=S^1\times S^1$, from Künneth and the cross product.
:::

<1>4. In particular, $X$ is not merely homotopy equivalent to a compact $2$-manifold: it is itself homeomorphic to the compact orientable surface $T^2$.
::: {.proof}
This is exactly the quotient identification in <1>1.
:::
:::
