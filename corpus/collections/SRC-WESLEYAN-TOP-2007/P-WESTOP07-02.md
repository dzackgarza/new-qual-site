---
schema: qual/card@1
id: P-WESTOP07-02
kind: problem
title: Fundamental group of three triangular loops joined by two segments
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
In this problem a *triangle* consists only of its three edges and three vertices. Let $T_1,T_2,T_3\subset\RR^2$ be the triangles with vertices
\[
(5,5),(7,5),(6,6),
\]
\[
(-5,-5),(-6,-6),(-4,-6),
\]
and
\[
(17,-5),(18,-6),(16,-6),
\]
respectively. Let $P$ be the closed segment from $(-5,-5)$ to $(5,5)$ and let $Q$ be the closed segment from $(7,5)$ to $(17,-5)$. Put
\[
X=T_1\cup T_2\cup T_3\cup P\cup Q.
\]
Compute, with proof,
\[
\pi_1(X,(0,0)).
\]
:::

::: {.solution}

The space
$$
X
$$
is a finite connected graph.

::: pf

::: pf-step

The three triangles
$$
T_1,T_2,T_3
$$
are pairwise disjoint, and the segments
$$
P,Q
$$
connect them in a tree-like fashion:
$$
T_2
\xleftrightarrow{\ P\ }
T_1
\xleftrightarrow{\ Q\ }
T_3.
$$


::: pf-proof

By the listed coordinates, the triangles lie in disjoint regions of the plane. The segment
$$
P
$$
meets
$$
T_2
$$
at
$$
(-5,-5)
$$
and
$$
T_1
$$
at
$$
(5,5),
$$
while
$$
Q
$$
meets
$$
T_1
$$
at
$$
(7,5)
$$
and
$$
T_3
$$
at
$$
(17,-5).
$$
No additional intersections occur. Hence
$$
X
$$
is connected.

:::

:::

::: pf-step

Choose from each triangle
$$
T_i
$$
two of its three edges so that the chosen two edges form a path through all three vertices of
$$
T_i.
$$
Let
$$
K
$$
be the union of these six chosen triangle edges together with
$$
P
$$
and
$$
Q.
$$
Then
$$
K
$$
is a maximal tree in
$$
X.
$$


::: pf-proof

Within each
$$
T_i,
$$
the two chosen edges contain all three vertices and contain no cycle. Adding
$$
P
$$
and
$$
Q
$$
connects the three resulting paths without creating a cycle, because the connecting pattern itself is a tree.

Thus
$$
K
$$
is connected and contains no cycle, so it is a tree. It contains every vertex of
$$
X.
$$
The only edges of
$$
X
$$
not in
$$
K
$$
are the one omitted edge from each triangle. Adding any one of those omitted edges creates the corresponding triangular cycle. Hence
$$
K
$$
is maximal.

:::

:::

::: {.pf-step #s1-3}

Collapsing
$$
K
$$
to a point produces a wedge of three circles:
$$
\boxed{
X/K
\cong
S^1\vee S^1\vee S^1}.
$$


::: pf-proof

All vertices and all tree edges lie in
$$
K,
$$
so after collapsing
$$
K
$$
to a point, each of the three omitted triangle edges becomes a loop based at that single point. There are exactly three such edges and no further cells. Thus the quotient is a bouquet of three circles.

:::

:::

::: {.pf-step #s1-4}

The quotient map
$$
X\to X/K
$$
is a homotopy equivalence.


::: pf-proof

A tree is contractible. In a finite graph, collapsing a contractible subtree to a point preserves the homotopy type. Equivalently, one may successively collapse leaf edges of
$$
K
$$
until the entire tree is reduced to one vertex; each elementary edge collapse is a deformation retraction.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\pi_1(X,(0,0))
\cong
\pi_1(S^1\vee S^1\vee S^1).
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
X
$$
is homotopy equivalent to
$$
X/K.
$$
Step [](#s1-3){.pf-ref} identifies the latter with a wedge of three circles. Homotopy equivalences induce isomorphisms on fundamental groups.

:::

:::

::: {.pf-step #s1-6}

The fundamental group is the free group on three generators:
$$
\boxed{
\pi_1(X,(0,0))
\cong
F_3
\cong
\langle a,b,c\mid\ \rangle.}
$$


::: pf-proof

The fundamental group of a wedge of
$$
r
$$
circles is the free group of rank
$$
r.
$$
Applying this with
$$
r=3
$$
to step [](#s1-5){.pf-ref} gives the result.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required computation.

:::

:::

:::
