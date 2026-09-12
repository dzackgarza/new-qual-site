---
schema: qual/card@1
id: E-HAT-2.1-10
kind: problem
title: Quotient of disjoint 2-simplices with edge identifications is always a surface
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
  note: Proved the quotient is a surface using links of vertices and gave an explicit branching construction orienting all quotient edges so each triangle inherits a vertex ordering.
---

(a) Show the quotient space of a finite collection of disjoint 2 simplices obtained by identifying pairs of edges is always a surface, locally homeomorphic to $\mathbb{R}^2$.

(b) Show the edges can always be oriented so as to define a $\Delta$-complex structure on the quotient surface.
[This is more difficult.]

::: {.solution}
Let $q$ be the quotient map from the disjoint union of the finitely many triangles to the quotient $X$.

<1>1. Every point in the image of the interior of a triangle has a neighborhood homeomorphic to $\mathbb R^2$, and every point in the interior of an identified edge has such a neighborhood as well.
::: {.proof}
For an interior point this is immediate because $q$ is injective on the interior of each triangle. For a point in the interior of a quotient edge, exactly two open half-disks, one from each of the paired edges, are glued along their diameter. Their union is an open disk.
:::

<1>2. If $v$ is a quotient vertex, its link is a circle.
::: {.proof}
Choose, in each triangle corner mapping to $v$, a small radial segment cutting off that corner. The union of these segments, after the edge identifications, is the link $L_v$.

Before taking the quotient, each corner contributes an interval. Its two endpoints lie on the two edge germs meeting at that corner. Since every original edge is paired with exactly one other edge, every endpoint of every such interval is identified with exactly one other endpoint. Hence each vertex of the finite graph $L_v$ has degree two.

Moreover $L_v$ is connected. Indeed, two original triangle vertices represent the same quotient vertex $v$ precisely when one can pass from one to the other through a finite sequence of endpoint identifications coming from the paired edges. The same sequence joins the corresponding corner intervals in $L_v$. Thus $L_v$ is a finite connected graph all of whose vertices have degree two, hence
\[
L_v\cong S^1.
\]
:::

<1>3. A sufficiently small neighborhood of each quotient vertex is a disk. Therefore $X$ is a closed surface.
::: {.proof}
A small neighborhood of $v$ is the cone on the link $L_v$. By <1>2 this is
\[
C(S^1)\cong D^2.
\]
Together with <1>1, every point of $X$ has a neighborhood homeomorphic to $\mathbb R^2$. Since every original edge was paired, there is no boundary. This proves part (a).
:::

For part (b), call an orientation of the quotient edges **admissible** if on the boundary of no triangle are the three edge directions cyclic. Equivalently, in each triangle there is a vertex at which both incident edges point outward, and then the three vertices can be ordered uniquely up to the evident choice so that every edge points from the smaller endpoint to the larger one.

<1>4. Choose a total ordering of the quotient vertices and orient every non-loop edge from the smaller endpoint to the larger endpoint. Every triangle having at least two distinct quotient vertices is then already admissibly oriented, independently of the orientations of loop edges.
::: {.proof}
If the three quotient vertices are distinct, the largest vertex is a sink and the smallest is a source. If exactly two quotient vertices occur, the two non-loop sides both point from the smaller quotient vertex to the larger one, so the repeated larger vertex is a sink or the repeated smaller vertex is a source. Hence a cyclic orientation is impossible in either case.
:::

It remains only to orient loop edges at a quotient vertex $v$ so that triangles whose three vertices all map to $v$ are admissible.

<1>5. Fix $v$. Let $H_v$ be the finite set of half-edges at $v$, cyclically ordered by the link circle $L_v$. Let
\[
T:H_v\to H_v
\]
be the fixed-point-free involution exchanging the two half-edges of each loop edge, and let $S$ be the cyclic successor map on $H_v$.
For each half-edge $h$, the three corners of the unique triangle incident between $h$ and $S(h)$ form the orbit
\[
h,\quad X(h),\quad X^2(h),
\qquad X=T\circ S,
\]
and $X^3(h)=h$.
::: {.proof}
Starting with the corner interval between the consecutive half-edges $h$ and $S(h)$, crossing the edge containing $S(h)$ takes one to the paired half-edge $T(S(h))=X(h)$ in the same original triangle. Repeating this operation moves to the next corner of that triangle, and after the three corners one returns to the starting one. Hence $X^3(h)=h$ on the three half-edges associated to that triangle.
:::

<1>6. There exists a place to cut the cyclic order on $H_v$ such that the following procedure orients every loop edge and makes every all-$v$ triangle admissible: traverse the half-edges once from the chosen cut; when a loop edge is encountered for the first time, orient it so that this first half-edge is its outgoing half-edge.
::: {.proof}
For any chosen cut, every triangle not meeting the cut is admissible. Indeed, let $a$ be the first of its three edge occurrences whose underlying loop is oriented during the traversal, and let $x$ be the corner from which $a$ points outward. The other edge $b$ at $x$ is encountered next around the link before the second half-edge of $a$, so either $b$ is still unoriented and is oriented outward at $x$, or it was oriented earlier with its first half-edge at $x$; in either case $x$ is a source for that triangle.

Thus only the triangle straddling the cut can possibly fail. We choose the cut so that it does not fail. To see such a cut exists, regard $X=T\circ S$ from <1>5. For a half-edge $h$, the three points
\[
h,\ X(h),\ X^2(h)
\]
appear around the cyclic order either in that same cyclic order or in the opposite cyclic order. Call the corresponding triangle good in the latter case. There is at least one good triangle. Otherwise $X$ would preserve the cyclic order on every three-point orbit. Then for every $h$, $X(S(h))$ would lie strictly in the cyclic interval from $S(h)$ to $X(h)$. Iterating $S$ would produce a strictly nested cyclic sequence of nonempty intervals, impossible in the finite cyclic set $H_v$.

Choose a half-edge $h$ belonging to a good triangle and place the cut immediately after the appropriate corner of that triangle. For this triangle the first-occurrence rule makes two incident edges point outward at one of its corners, precisely because the cyclic order of its $X$-orbit is reversed. Hence the cut triangle is also admissible. All other triangles were already admissible by the first paragraph.
:::

<1>7. Performing the construction of <1>6 independently at every quotient vertex orients all loop edges, and together with <1>4 gives an admissible orientation of every quotient edge.
::: {.proof}
A loop edge is based at exactly one quotient vertex, so the constructions at distinct vertices are independent. Triangles with at least two distinct quotient vertices are handled by <1>4; triangles with all three vertices equal are handled by <1>6.
:::

<1>8. The admissible edge orientations define a $\Delta$-complex structure on $X$.
::: {.proof}
For each triangle, admissibility means its three oriented sides are not cyclic. Therefore its three abstract vertices can be linearly ordered so that each side is directed from the smaller vertex to the larger vertex. Whenever two edges are identified in the quotient, they carry the same chosen quotient-edge orientation, so the identification preserves these induced vertex orderings. This is exactly the compatibility condition for the characteristic maps of the triangles to define a $\Delta$-complex structure.
:::
:::
