---
schema: qual/card@1
id: E-HAT-1.3-4
kind: problem
title: "Simply-connected covering space of a sphere with diameter"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Constructed the universal covers as trees of copies of the sphere joined by lifts of the added arcs and checked the covering neighborhoods at the attachment points.
---

Construct a simply-connected covering space of the space $X \subset \mathbb{R}^3$ that is the union of a sphere and a diameter.
Do the same when $X$ is the union of a sphere and a circle intersecting it in two points.

::: {.solution}
Let $p,q\in S^2$ be the two endpoints of the added diameter in the first space.

<1>1. For the sphere-with-diameter space, construct $\widetilde X$ from copies
\[
S_n^2\cong S^2,
\qquad n\in\mathbb Z,
\]
by adjoining an interval $I_n$ from the point $q_n\in S_n^2$ to the point $p_{n+1}\in S_{n+1}^2$ for every $n$.
::: {.proof}
Here $p_n,q_n$ denote the copies of $p,q$ in $S_n^2$.
Thus the incidence pattern is the infinite line
\[
\cdots-S_{-1}^2-I_{-1}-S_0^2-I_0-S_1^2-I_1-\cdots .
\]
:::

<1>2. Define
\[
P:\widetilde X\to X
\]
by mapping every $S_n^2$ homeomorphically onto the sphere and every $I_n$ homeomorphically onto the diameter, with its endpoints sent to $q$ and $p$ respectively.
Then $P$ is a covering map.
::: {.proof}
Away from $p$ and $q$, the assertion is immediate: a small neighborhood lies either in the sphere away from the attachment points or in the interior of the diameter, and its inverse image is a disjoint union of copies.

Choose a small disk neighborhood $D_p$ of $p$ in the sphere and a short initial subinterval $J_p$ of the diameter meeting the sphere only at $p$.
The union
\[
U_p=D_p\cup J_p
\]
is a neighborhood of $p$ in $X$.
For each $n$, its lift at $p_n$ is the union of the copy of $D_p$ in $S_n^2$ and the terminal short segment of $I_{n-1}$ ending at $p_n$.
These lifted neighborhoods are pairwise disjoint and each maps homeomorphically to $U_p$.

The same construction at $q$ uses the initial segment of $I_n$ issuing from $q_n$.
Thus $p$ and $q$ are evenly covered as well.
:::

<1>3. The covering space $\widetilde X$ is simply connected.
::: {.proof}
Each sphere $S_n^2$ and each interval $I_n$ is simply connected, adjacent pieces meet in a single point, and the incidence graph is the infinite line, hence a tree.
Any loop has compact image, so it meets only finitely many of these pieces and lies in a finite subtree of the graph of spaces.
Repeated application of van Kampen along point intersections shows that every such finite union is simply connected.
Hence
\[
\pi_1(\widetilde X)=0.
\]
:::

<1>4. Now let $X'$ be the union of $S^2$ with a circle meeting the sphere exactly at $p$ and $q$.
Write the two arcs of the added circle from $p$ to $q$ as $A$ and $B$.
Let
\[
F_2=\langle a,b\rangle
\]
be the free group on two generators.
::: {.proof}
The two arcs $A$ and $B$ are disjoint except at their endpoints $p,q$.
The symbols $a,b$ will record which of these two arc types is crossed in the covering.
:::

<1>5. Construct $\widetilde X'$ from a copy $S_g^2$ of the sphere for every $g\in F_2$ as follows:

- for each $g$, attach an interval $A_g$ from $p_g\in S_g^2$ to $q_{ga}\in S_{ga}^2$;
- for each $g$, attach an interval $B_g$ from $p_g\in S_g^2$ to $q_{gb}\in S_{gb}^2$.

::: {.proof}
If each sphere copy is collapsed to a vertex, the resulting incidence graph has vertex set $F_2$ and edges
\[
g\longleftrightarrow ga,
\qquad
g\longleftrightarrow gb.
\]
This is the Cayley graph of $F_2$ with respect to $a,b$, hence a tree.
:::

<1>6. Map each $S_g^2$ homeomorphically to the sphere, each $A_g$ homeomorphically to $A$, and each $B_g$ homeomorphically to $B$.
This defines a covering map
\[
P':\widetilde X'\to X'.
\]
::: {.proof}
Away from $p,q$, the local covering property is immediate.

At $p_g$, exactly one lift of a short initial segment of $A$ and one lift of a short initial segment of $B$ issue from the sphere sheet $S_g^2$, namely the segments in $A_g$ and $B_g$.
Together with a small disk neighborhood of $p_g$ in $S_g^2$, they map homeomorphically to the corresponding neighborhood of $p$ in $X'$.

At $q_g$, the incident lifted terminal segments are those of
\[
A_{ga^{-1}}\quad\text{and}\quad B_{gb^{-1}},
\]
again giving exactly one lift of each local branch at $q$.
Thus neighborhoods of both intersection points are evenly covered.
:::

<1>7. The space $\widetilde X'$ is simply connected.
::: {.proof}
Its sphere pieces are simply connected and their incidence graph is the Cayley tree from <1>5.
As in <1>3, every loop lies in a finite subtree of sphere and interval pieces, and van Kampen along the point intersections gives trivial fundamental group.
:::

<1>8. Therefore the constructions in <1>1 and <1>5 are simply connected covering spaces of the two requested spaces.
::: {.proof}
The covering properties are <1>2 and <1>6, and simple connectivity is <1>3 and <1>7.
:::
:::
