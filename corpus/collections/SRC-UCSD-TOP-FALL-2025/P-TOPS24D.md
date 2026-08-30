---
schema: qual/card@1
id: P-TOPS24D
kind: problem
title: Homology of the cube with opposite faces glued by 180° rotations
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $X$ be the space obtained by gluing opposite pairs of faces of a standard cube $I^3$ via 180 degree rotations, as shown.
Compute the homology $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. $X$ has one $0$-cell, three $1$-cells, three $2$-cells, one $3$-cell.
Proof: the cube has 8 vertices identified to one, 12 edges identified into 3 classes of 4 parallel edges, 6 faces identified into 3 pairs.

<1>2. Cellular chain complex: $0 \to \mathbb{Z} \xrightarrow{\partial_3} \mathbb{Z}^3 \xrightarrow{\partial_2} \mathbb{Z}^3 \xrightarrow{\partial_1} \mathbb{Z} \to 0$.
Proof: <1>1.

<1>3. $\partial_1 =0$ (single $0$-cell).
Proof: each $1$-cell is a loop.

<1>4. Each $2$-cell is attached with degree $2$ (the $180^\circ$ rotation identifies opposite edges with a twist, giving boundary $2\cdot$generator).
Proof: the gluing map has degree $2$ on the $1$-skeleton.

<1>5. Hence $\partial_2$ is multiplication by $2$ on each $2$-cell.
Proof: <1>4.

<1>6. $\partial_3 =0$ (the $3$-cell is attached by a map of degree $0$ for this orientable gluing).
Proof: orientability.

<1>7. Therefore $H_0(X)=\mathbb{Z}$, $H_1(X)=\mathbb{Z}^3/2\mathbb{Z}^3 \cong (\mathbb{Z}/2)^3$, $H_2(X)=0$, $H_3(X)=\mathbb{Z}$.
Proof: <1>2, <1>5, <1>6; $H_1 = \ker\partial_1/\operatorname{im}\partial_2 = \mathbb{Z}^3/2\mathbb{Z}^3$, $H_2 = \ker\partial_2/\operatorname{im}\partial_3 =0$.

<1>8. Q.E.D.
Proof: <1>7.
:::
