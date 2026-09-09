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

::: problem
Let a tetrahedron be colored with $C$ colors. Compute the number of colorings up to symmetry in each of the following natural conventions:

1. color the vertices (equivalently the faces), modulo the full tetrahedral symmetry group;
2. color the vertices (equivalently the faces), modulo rotations only;
3. color the edges, modulo the full symmetry group;
4. color the edges, modulo rotations only.
:::


::: {.solution}
Use Burnside's lemma.

For vertices, the full symmetry group is $S_4$ acting on four vertices. Its cycle types are
\[
1^4,\quad 2\,1^2,\quad 2^2,\quad 3\,1,\quad 4
\]
with multiplicities $1,6,3,8,6$. A coloring fixed by a permutation with $r$ cycles has $C^r$ choices. Hence
\[
N_{\mathrm{vert,full}}=\frac{C^4+6C^3+11C^2+6C}{24}.
\]
The same formula applies to face colorings.

For rotations only, the group is $A_4$. Its elements are the identity, eight $3$-cycles, and three double transpositions, so
\[
N_{\mathrm{vert,rot}}=\frac{C^4+11C^2}{12}.
\]

For edges, identify the six edges with the $2$-subsets of $\{1,2,3,4\}$. The induced cycle counts are $6$ for the identity, $4$ for a transposition, $4$ for a double transposition, $2$ for a $3$-cycle, and $2$ for a $4$-cycle. Therefore
\[
N_{\mathrm{edge,full}}=\frac{C^6+9C^4+14C^2}{24}.
\]
Restricting to $A_4$ gives
\[
N_{\mathrm{edge,rot}}=\frac{C^6+3C^4+8C^2}{12}.
\]
These four formulas cover the standard meanings of coloring a tetrahedron up to symmetry.
:::
