---
schema: qual/card@1
id: E-HAT-1.B-3
kind: problem
title: "Graph products of trivial groups are free"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Observed that the graph-of-spaces model collapses to the underlying graph when every vertex and edge group is trivial, so its fundamental group is free.
---

::: {.problem}
Show that every graph product of trivial groups is free.
:::

::: {.solution}
Let $\Gamma$ be the underlying graph of the graph of groups.
Assume every vertex group and every edge group is trivial.

::: pf

::: pf-step

Every classifying space used for a vertex or edge group is a point.

::: pf-proof

A $K(1,1)$ is a point.
Thus each vertex space in the graph-of-spaces construction is a point, and each edge mapping cylinder is just an interval joining the two endpoint vertex spaces, or a loop interval when the edge is a loop.

:::

:::

::: {.pf-step #s2}

Consequently the graph-of-spaces realization $K\Gamma$ is naturally homeomorphic to the underlying graph $\Gamma$.

::: pf-proof

Replacing every vertex group by a point and every edge group by a point leaves exactly one $0$-cell for each vertex of $\Gamma$ and one $1$-cell for each edge, attached according to the incidence data of $\Gamma$.
This is precisely the geometric realization of the graph.

:::

:::

::: {.pf-step #s3}

The fundamental group of each connected component of a graph is free.

::: pf-proof

Choose a maximal tree $T$ in a connected component.
Collapsing $T$ to a point is a homotopy equivalence and leaves a wedge of one circle for each edge not in $T$.
Hence the fundamental group is a free group on these remaining edges.

:::

:::

::: pf-step

Therefore every graph product of trivial groups is free.

::: pf-proof

By step [](#s2){.pf-ref} its fundamental group is the fundamental group of the underlying graph, and step [](#s3){.pf-ref} shows this group is free.

:::

:::

:::

:::
