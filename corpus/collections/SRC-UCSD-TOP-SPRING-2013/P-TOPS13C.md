---
schema: qual/card@1
id: P-TOPS13C
kind: problem
title: "Fundamental group of a sphere with chords: disjoint and intersecting cases"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy Type
  - Cell Complexes
relations: []
review: draft
---

::: problem
(a) Let $X \subset \mathbb{R}^3$ be the union of a $2$-dimensional sphere and two disjoint chords intersecting the sphere only at their endpoints.
Compute the fundamental group of $X$ by finding a more standard space $Y$ which is homotopy equivalent to $X$.
Give a short explanation for why $X$ and $Y$ are homotopy equivalent.

(b) Now let $X$ be obtained similarly as the union of a $2$-dimensional sphere and two chords intersecting the sphere only at their endpoints, but such that the chords intersect at precisely one point lying in the interior of each chord.
What is the fundamental group of $X$?
:::

::: {.solution}
<1>1. In part (a), each chord adds one independent $1$-cell to the simply connected sphere, and the two disjoint chords can be arranged independently. Thus
$$
X\simeq S^2\vee S^1\vee S^1.
$$
::: {.proof}
Choose disjoint arcs on the sphere connecting the chord endpoints to a common basepoint and collapse a spanning tree formed from these arcs. This deformation does not change the sphere's homotopy type and turns each chord into a loop attached at the basepoint.
:::

<1>2. Therefore in part (a)
$$
\boxed{\pi_1(X)\cong F_2.}
$$
::: {.proof}
The sphere summand is simply connected and the two circle summands generate a free group of rank two.
:::

<1>3. In part (b), collapse the sphere-side connecting tree as above. The two intersecting chords become a graph with two vertices (the common sphere basepoint and the interior intersection point) joined by four edges.
::: {.proof}
Each chord is split into two segments by the unique interior intersection. After all four endpoints on the sphere are moved to the common basepoint through a spanning tree on the sphere, the four resulting chord segments run between the two stated vertices.
:::

<1>4. This graph has rank
$$
4-2+1=3,
$$
so the space is homotopy equivalent to $S^2$ wedged with three circles.
::: {.proof}
A connected graph with $E$ edges and $V$ vertices has free fundamental group of rank $E-V+1$; collapsing a maximal tree yields a bouquet of that many circles.
:::

<1>5. Hence in part (b)
$$
\boxed{\pi_1(X)\cong F_3.}
$$
::: {.proof}
The $S^2$ summand contributes no fundamental group.
:::
:::
