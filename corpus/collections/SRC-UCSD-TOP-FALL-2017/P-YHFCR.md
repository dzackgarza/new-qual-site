---
schema: qual/card@1
id: P-YHFCR
kind: problem
title: $\pi_1$ of the unit cube's faces union four space diagonals
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $X$ be the subspace of the unit cube $I^3$ consisting of the union of the 6 faces and the 4 internal diagonals.
Compute $\pi_1(X)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The union of the six faces of the cube is its boundary sphere $S^2$.

::: pf-proof

The boundary of a cube is homeomorphic to $S^2$.

:::

:::

::: {.pf-step #s2}

The four space diagonals meet at the cube center and have the eight cube vertices as their endpoints. Thus their union is a tree with one central vertex and eight edges, whose eight leaves lie on $S^2$.

::: pf-proof

Each space diagonal is the union of two radial segments from the center to a pair of opposite vertices, and distinct diagonals meet only at the center.

:::

:::

::: {.pf-step #s3}

Contract the simply connected subspace $S^2$ to a point. The resulting graph has two vertices joined by eight parallel edges, so its fundamental group is free of rank $8-2+1=7$.

::: pf-proof

Attaching a tree to a simply connected CW complex along its leaves and then collapsing that simply connected subcomplex does not change the fundamental group; van Kampen gives the same conclusion directly. The rank formula for a connected graph is $E-V+1$.

:::

:::

::: pf-step

Therefore
$$\boxed{\pi_1(X)\cong F_7.}$$

::: pf-proof

Apply steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
