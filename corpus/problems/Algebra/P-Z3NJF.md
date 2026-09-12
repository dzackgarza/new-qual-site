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

::: problem
Identify both the orientation-preserving rotational symmetry group and the full Euclidean symmetry group of a regular tetrahedron, cube, and icosahedron.
:::

::: solution
For a regular tetrahedron, the rotational symmetry group acts faithfully on the four vertices. The orientation-preserving permutations are exactly the even permutations, so
\[
\operatorname{Rot}(\text{tetrahedron})\cong A_4.
\]
Every permutation of the four vertices is realized by a Euclidean symmetry, hence
\[
\operatorname{Sym}(\text{tetrahedron})\cong S_4.
\]

For a cube, rotations act faithfully on the four body diagonals. Every permutation of these four diagonals is realized by a rotation, so
\[
\operatorname{Rot}(\text{cube})\cong S_4.
\]
The central inversion $x\mapsto -x$ is an orientation-reversing symmetry commuting with every rotation. Every full symmetry is either a rotation or central inversion followed by a rotation. Therefore
\[
\operatorname{Sym}(\text{cube})\cong S_4\times C_2.
\]

For an icosahedron, the rotational symmetry group has order $60$ and is isomorphic to
\[
A_5.
\]
One realization is its faithful action on the five inscribed cubes in the icosahedron. The icosahedron is centrally symmetric, and central inversion again commutes with all rotations. Hence
\[
\operatorname{Sym}(\text{icosahedron})\cong A_5\times C_2.
\]

Thus
\[
\begin{array}{c|cc}
 & \text{rotations} & \text{full symmetries}\\ \hline
\text{tetrahedron} & A_4 & S_4\\
\text{cube} & S_4 & S_4\times C_2\\
\text{icosahedron} & A_5 & A_5\times C_2
\end{array}
\]
:::
