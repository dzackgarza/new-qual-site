---
schema: qual/card@1
id: P-BKF09-4B
kind: problem
title: Berkeley Fall 2009 prelim problem 4B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Determine the number of rotationally distinct colorings by two colors of the edges of a regular tetrahedron T .
:::

::: {.solution}
The number of colorings with 0, 1, 2, 3, 4, 5, 6 red edges is 1, 1, 2, 4, 2, 1, 1.   
Total 12.

Solution 2: According to Cauchy’s theorem, the number of orbits of a finite group (of 12 rotations of the tetrahedron in this case) on a finite set (of all 2-color colorings of the edges) is equal to the average number of fixed points of group elements. A rotation g permutes the edges, and in the cycle decomposition of this permutation, the edges of the same cycle must have the same color for the coloring to be fixed by g, and vice versa. The identity rotation has 6 cycles (of length 1), each of the 8 rotations through the angle $1 2 0 ^ { \circ }$has 2 cycles (of length 3 each), and each of the 3 rotations by$1 8 0 ^ { \circ }$has 4 cycles (of lengths 1,1,2,2). Thus, the average number of fixed points is$${ \frac { 1 } { 1 2 } } \left( 1 \times 2 ^ { 6 } + 8 \times 2 ^ { 2 } + 3 \times 2 ^ { 4 } \right) = { \frac { 1 4 4 } { 1 2 } } = 1 2 .$$
:::
