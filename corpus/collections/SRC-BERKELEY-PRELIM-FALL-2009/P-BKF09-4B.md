---
schema: qual/card@1
id: P-BKF09-4B
kind: problem
title: Two-colorings of the edges of a tetrahedron up to rotation
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's prose had a corrupted sentence — 'A second count is
    Burnside's lemma, which the solution above states as Cauchy's theorem., the number of orbits
    ...' — which garbled the retained sheet's 'Solution 2: According to Cauchy's theorem, the
    number of orbits ...'; the text is restored from the sheet
    (assets/attachments/f09solutions.pdf, Problem 4B on PDF p. 6) and split into steps. Added:
    the description of the twelve rotations and their cycle types, the fixed-colouring count
    2^{c(g)}, and a justification of the direct count 1,1,2,4,2,1,1, which the sheet stated
    without argument — the four three-edge orbits being the four triangles, the four stars, and
    the two classes of six Hamiltonian paths.
---

::: {.problem}
Determine the number of rotationally distinct colorings by two colors of the edges of a regular tetrahedron $T$.
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Fall 2009, solutions** (`assets/attachments/f09solutions.pdf`), Problem 4B, PDF p. 6, which gives two counts. The group acting is the rotation group of the regular tetrahedron, of order $12$, acting on the six edges, and the colourings are the $2^{6}$ assignments of two colours to the edges.

::: pf

::: {.pf-step #group}
The rotation group of the tetrahedron has $12$ elements, and a rotation permutes the six edges.

::: pf-proof
Each rotation permutes the four vertices, and the resulting map to $A_{4}$ is an isomorphism: $12$ rotations, namely the identity, the $8$ rotations through $\\pm120^{\\circ}$ about the axis through a vertex and the centre of the opposite face, and the $3$ rotations through $180^{\\circ}$ about an axis through the midpoints of a pair of opposite edges. A rotation carries edges to edges.

:::

:::

::: {.pf-step #burnside}
The number of rotationally distinct colourings is the average number of fixed colourings.

::: pf-proof
This is Burnside's lemma, which the sheet calls Cauchy's theorem: for a finite group $G$ acting on a finite set $S$, the number of orbits equals $\\frac{1}{\\abs{G}}\\sum_{g \\in G}\\abs{S^{g}}$, where $S^{g}$ is the set of points fixed by $g$. A colouring is fixed by a rotation exactly when all edges in each cycle of the induced permutation of the edges carry the same colour, so the number of fixed colourings is $2^{c(g)}$, where $c(g)$ is the number of cycles of $g$ on the six edges.

:::

:::

::: {.pf-step #cycles}
The cycle counts are $c = 6$ for the identity, $c = 2$ for each of the $8$ rotations through $120^{\\circ}$, and $c = 4$ for each of the $3$ rotations through $180^{\\circ}$.

::: pf-proof
The identity fixes every edge, giving six cycles of length $1$. A rotation through $120^{\\circ}$ fixes the two edges at the vertex on its axis and cyclically permutes the other four in two $3$-cycles, giving $2$ cycles. A rotation through $180^{\\circ}$ about the axis through the midpoints of two opposite edges fixes those two edges and swaps the other four in two transpositions, giving the cycle type $1,1,2,2$, that is $4$ cycles.

:::

:::

::: {.pf-step #average}
The average is $\frac{1}{12}\bigl(1\cdot2^{6} + 8\cdot2^{2} + 3\cdot2^{4}\bigr) = \frac{144}{12} = 12$.

::: pf-proof
Substituting the cycle counts of step [](#cycles){.pf-ref} into step [](#burnside){.pf-ref}: the three terms are $2^{6} = 64$, $8\\cdot2^{2} = 32$ and $3\\cdot2^{4} = 48$, whose sum is $144$, and $144/12 = 12$.

:::

:::

::: {.pf-step #direct}
Counting by the number of red edges gives $1, 1, 2, 4, 2, 1, 1$ orbits for $0, 1, \\ldots, 6$ red edges, totalling $12$.

::: pf-proof
The rotation group is transitive on the six edges and on pairs of opposite edges, and $A_{4}$ on four objects is transitive on $3$-element subsets. The $21$ subsets of edges fall into these classes: for $0$ and $6$ red edges one colouring each; for $1$ and $5$, one orbit each by transitivity on edges; for $2$, the $12$ adjacent pairs and the $3$ opposite pairs give two orbits, and for $4$ the complements give two more; for $3$, the $20$ three-element subsets are $4$ triangles, $4$ stars at a vertex and $12$ Hamiltonian paths, and each path is fixed by the involution reversing it, so the $12$ paths form two orbits of $6$. That is $1+1+2+4+2+1+1 = 12$.

:::

:::

::: pf-step
There are $\boxed{12}$ rotationally distinct two-colourings of the edges of the tetrahedron.

::: pf-proof
Step [](#average){.pf-ref} and step [](#direct){.pf-ref} are the two counts of the sheet and they agree.

:::

:::

:::
:::
