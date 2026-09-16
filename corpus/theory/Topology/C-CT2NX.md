---
schema: qual/card@1
id: C-CT2NX
kind: corollary
title: Euler characteristic of a connected sum of surfaces
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
---

::: {.corollary}
Let $A$ and $B$ be closed surfaces, and let $A \# B$ be their connected sum.
Then the [[D-QK5BM|Euler characteristics]] satisfy
$$
\chi(A \# B) = \chi(A) + \chi(B) - 2
.$$
:::

::: {.proof}
Choose finite CW structures on $A$ and $B$ in which a closed disk $D_A \subseteq A$, respectively $D_B \subseteq B$, is the closure of a single $2$-cell.
Removing the open $2$-cell gives CW complexes $A' \coloneqq A \sm D_A^\circ$ and $B' \coloneqq B \sm D_B^\circ$ with $\chi(A') = \chi(A) - 1$ and $\chi(B') = \chi(B) - 1$, whose boundary circles are subcomplexes.
After subdividing so that the two boundary circles have the same number of vertices and edges, $A \# B$ is the CW complex obtained by identifying these circles by a cellular homeomorphism.
Counting cells, $\chi(A\# B) = \chi(A') + \chi(B') - \chi(S^1) = \chi(A) + \chi(B) - 2$, since $\chi(S^1) = 0$.
:::
