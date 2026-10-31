---
schema: qual/card@1
id: E-HAT-2.1-10
kind: problem
title: Quotient of paired triangles is a surface with a Delta-complex structure
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 10; the stored statement matches the corrected online text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
(a) Show the quotient space of a finite collection of disjoint 2-simplices obtained by identifying pairs of edges is always a surface, locally homeomorphic to $\RR^2$.

(b) Show the edges can always be oriented so as to define a $\Delta$-complex structure on the quotient surface.
[This is more difficult.]
:::

::: {.solution}
Let $X$ be the quotient. A point in the interior of a triangle has a disk neighborhood. An interior point of a quotient edge has two half-disk neighborhoods, one from each paired edge, glued along their diameter; their union is a disk.

At a quotient vertex $v$, take a short segment across each triangle corner mapping to $v$. These segments form the link $L_v$. Each endpoint is paired with exactly one other endpoint by an edge identification, so every vertex of this finite graph has degree two. The graph is connected: the paired-edge identifications that make the original triangle vertices represent the same quotient vertex also join their corner segments. Hence $L_v$ is a connected finite $2$-regular graph, so $L_v\cong S^1$. A small neighborhood of $v$ is the cone on $L_v$ and is a disk. Thus every point of $X$ has a neighborhood homeomorphic to $\RR^2$, and there is no boundary. This proves (a).

For (b), use the branching theorem for surface triangulations. In [Benedetti, Lemma 2.14](https://arxiv.org/pdf/1903.12596), every ideal triangulation of a closed surface with marked vertex set admits a branching: one orientation on each quotient edge that is induced by a linear ordering of the three abstract vertices in every triangle. The paper's definition permits self-adjacent and multiply adjacent triangles and explicitly describes a triangulation by paired abstract triangle edges. These are the edge identifications defining $X$ here. Its standing condition $\chi(X)-\#V<0$ follows from $F=2(\#V-\chi(X))>0$, where $F$ is the number of triangles. Apply the lemma to each connected component of $X$. The resulting edge orientations satisfy precisely Hatcher's $\Delta$-complex compatibility condition, proving (b).
:::
