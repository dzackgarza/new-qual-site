---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-08
kind: problem
title: The universal cover and an index-two subgroup of the infinite dihedral group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G=\mathbb Z_2*\mathbb Z_2=\langle a,b\mid a^2=b^2=1\rangle$.
Find the presentation complex $X_G$ and the universal cover of $X_G$, $\widetilde X_G$.
Find an index two subgroup of $G$ and the corresponding covering space.
:::

::: {.solution}
The presentation complex of
\[
G=\langle a,b\mid a^2,b^2\rangle
\]
has one \(0\)-cell, two \(1\)-cells \(a,b\), and two \(2\)-cells attached by the degree-two words \(a^2\) and \(b^2\). Equivalently,
\[
X_G\cong \mathbb{RP}^2\vee\mathbb{RP}^2.
\]

Its universal cover can be described as a bi-infinite chain of \(2\)-spheres. Consecutive spheres meet in one point, and the sphere types alternate between the lifts of the two \(\mathbb{RP}^2\) summands. More explicitly, the lifted \(1\)-skeleton is the Cayley graph of \(\mathbb Z_2*\mathbb Z_2\), a bi-infinite line with alternating \(a\)- and \(b\)-steps; over each \(a\)-pair of adjacent vertices the two lifted \(a\)-edges and the two lifted \(a^2\)-cells form a copy of \(S^2\), and similarly for \(b\). This tree of simply connected pieces is simply connected, hence is \(\widetilde X_G\).

For an index-two subgroup, define
\[
\varepsilon:G\to\mathbb Z/2,
\qquad
\varepsilon(a)=\varepsilon(b)=1.
\]
Then
\[
H=\ker\varepsilon=\langle ab\rangle\cong\mathbb Z
\]
has index \(2\). The corresponding covering has two vertices \(v_0,v_1\). The lifts of the \(a\)-circle form a \(2\)-edge circle between these vertices, filled by two lifted \(a^2\)-cells to make a sphere; the \(b\)-cells form a second sphere with the same two vertices. Thus the index-two cover is two copies of \(S^2\) glued together at two distinct points. Its fundamental group is \(\mathbb Z\), agreeing with \(H\).
:::
