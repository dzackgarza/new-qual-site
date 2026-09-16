---
schema: qual/card@1
id: P-HEOYS
kind: problem
title: Colorings of a tetrahedron with $C$ colors up to symmetry
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
  - Permutations
relations: []
review: draft
---

::: {.problem}
Let a regular tetrahedron be colored with $C$ available colors.

1. Count colorings of its four vertices (equivalently, its four faces) up to the full symmetry group.
2. Count colorings of its six edges up to the full symmetry group.
3. How do the answers change if only orientation-preserving rotational symmetries are allowed?
:::

::: {.solution}
The full symmetry group of a tetrahedron is $S_4$, of order $24$, acting naturally on the four vertices; the rotational subgroup is $A_4$, of order $12$.

<1>1. Vertices or faces under all symmetries.
The cycle types in the natural action of $S_4$ are
\[
1^4,\quad 2\,1^2,\quad 2^2,\quad 3\,1,\quad 4,
\]
with multiplicities $1,6,3,8,6$. A permutation with $k$ cycles fixes exactly $C^k$ colorings. Burnside's lemma gives
\[
\frac{C^4+6C^3+3C^2+8C^2+6C}{24}
=
\boxed{\frac{C^4+6C^3+11C^2+6C}{24}}.
\]
Equivalently this is $\binom{C+3}{4}$, since the full $S_4$ action only remembers the multiset of four colors.

<1>2. Edges under all symmetries.
Identify the six edges with the two-element subsets of $\{1,2,3,4\}$. The five conjugacy types above induce respectively $6,4,4,2,2$ cycles on the edge set. Hence Burnside gives
\[
\boxed{\frac{C^6+9C^4+14C^2}{24}}.
\]

<1>3. Rotations only.
The subgroup $A_4$ consists of the identity, three double transpositions, and eight $3$-cycles.
For vertices/faces the corresponding cycle counts are $4,2,2$, so the number of rotational orbits is
\[
\boxed{\frac{C^4+11C^2}{12}}.
\]
For edges the cycle counts are $6,4,2$, giving
\[
\boxed{\frac{C^6+3C^4+8C^2}{12}}.
\]
:::
