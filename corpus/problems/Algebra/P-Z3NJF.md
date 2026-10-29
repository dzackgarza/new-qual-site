---
schema: qual/card@1
id: P-Z3NJF
kind: problem
title: Symmetry groups of the tetrahedron, cube, and icosahedron
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Geometry
  - Permutations
relations: []
review: draft
---

::: {.problem}
Identify both the orientation-preserving rotational symmetry group and the full Euclidean symmetry group of a regular tetrahedron, cube, and icosahedron.
:::

::: {.solution}
Place each solid with its center at the origin, so every symmetry is an orthogonal map. Write $\operatorname{Rot}(X)$ for the rotation group of a solid $X$ and $\operatorname{Sym}(X)$ for its full symmetry group. The rotation group has index at most $2$ in the full group, being the kernel of $\det\colon\operatorname{Sym}(X)\to\{\pm1\}$.

::: pf

::: pf-step

$\operatorname{Rot}(\text{tetrahedron})\cong A_4$ and $\operatorname{Sym}(\text{tetrahedron})\cong S_4$.

::: pf-proof

A symmetry is determined by its action on the four vertices, which span $\RR^3$ affinely, so both groups embed in $S_4$. The rotations act transitively on the vertices, and the stabilizer of a vertex is the cyclic group of order $3$ of rotations about the axis through it, so $\abs{\operatorname{Rot}}=12$. The only subgroup of order $12$ in $S_4$ is $A_4$. The reflection in the plane through one edge and the midpoint of the opposite edge swaps the two vertices off that plane, so it is a transposition. A subgroup of $S_4$ containing $A_4$ and a transposition is $S_4$.

:::

:::

::: pf-step

$\operatorname{Rot}(\text{cube})\cong S_4$ and $\operatorname{Sym}(\text{cube})\cong S_4\times C_2$.

::: pf-proof

The rotations act transitively on the six faces with stabilizer the cyclic group of order $4$ about the face axis, so $\abs{\operatorname{Rot}}=24$. They permute the four body diagonals. A rotation fixing every diagonal maps each vertex to itself or its antipode; since it preserves the adjacency of vertices and has determinant $1$, it is the identity. Hence $\operatorname{Rot}$ embeds in $S_4$ with order $24$, so $\operatorname{Rot}\cong S_4$. The central inversion $-I$ is a symmetry of determinant $-1$ commuting with every orthogonal map, so
$$
\operatorname{Sym}(\text{cube})=\operatorname{Rot}\times\{\pm I\}\cong S_4\times C_2.
$$

:::

:::

::: pf-step

$\operatorname{Rot}(\text{icosahedron})\cong A_5$ and $\operatorname{Sym}(\text{icosahedron})\cong A_5\times C_2$.

::: pf-proof

The rotations act transitively on the twelve vertices with stabilizer the cyclic group of order $5$ about the vertex axis, so $\abs{\operatorname{Rot}}=60$. The thirty edges form fifteen pairs of opposite edges, and these fall into five triples of mutually perpendicular pairs; the rotations permute the five triples, and only the identity rotation fixes all five. Hence $\operatorname{Rot}$ embeds in $S_5$ with index $2$. The only subgroup of index $2$ in $S_5$ is $A_5$. The icosahedron is centrally symmetric, so $-I$ is a symmetry of determinant $-1$ commuting with every rotation, and
$$
\operatorname{Sym}(\text{icosahedron})=\operatorname{Rot}\times\{\pm I\}\cong A_5\times C_2.
$$

:::

:::

:::

:::
