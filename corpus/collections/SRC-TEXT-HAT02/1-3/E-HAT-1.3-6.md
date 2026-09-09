---
schema: qual/card@1
id: E-HAT-1.3-6
kind: problem
title: "Composition of covering spaces need not be a covering space"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 6 and its covering-space figure; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Twisted one circle in each attached shrinking wedge, with the chosen circle index tending to infinity along the covering line, so the double cover is locally valid but the composite has no evenly covered neighborhood at the wedge point.
---

Let $X$ be the shrinking wedge of circles in Example 1.25, and let $\tilde{X}$ be its covering space shown in the figure.
Construct a two-sheeted covering space $Y \to \tilde{X}$ such that the composition $Y \to \tilde{X} \to X$ of the two covering spaces is not a covering space.
Note that a composition of two covering spaces does have the unique path lifting property, however.

::: {.solution}
Let
\[
X=\bigcup_{m\ge1}C_m
\]
be the shrinking wedge, with common point $x_0$ and with the circles numbered so that their diameters tend to zero.
In the covering $q:\widetilde X\to X$ shown in the source figure, the horizontal line maps to $C_1$ as the usual universal cover
\[
\mathbb R\to S^1,
\]
and at every integer point $n\in\mathbb Z$ there is an attached shrinking wedge
\[
E_{n,2}\cup E_{n,3}\cup\cdots
\]
with
\[
q|_{E_{n,m}}:E_{n,m}\longrightarrow C_m
\]
a homeomorphism for $m\ge2$.

<1>1. Choose integers
\[
r_n\ge2,
\qquad n\in\mathbb Z,
\]
such that
\[
r_n\longrightarrow\infty
\quad\text{as }|n|\to\infty.
\]
For example, take
\[
r_n=|n|+2.
\]
::: {.proof}
The only required property is that the selected circle in the attached wedge at the $n$th integer becomes arbitrarily small in the base as $|n|$ grows.
:::

<1>2. Construct a two-sheeted space
\[
p:Y\to\widetilde X
\]
as follows.
Start with two disjoint copies
\[
\widetilde X^{(0)},\qquad \widetilde X^{(1)}.
\]
For each integer $n$, choose a point
\[
z_n\in E_{n,r_n}
\]
different from the attachment point, cut both copies of the circle $E_{n,r_n}$ at the corresponding point, and cross-glue the two pairs of cut endpoints.
Leave all other points in the two copies unglued.
::: {.proof}
After cross-gluing, the two copies of the selected circle combine into one circle that maps to $E_{n,r_n}$ as the connected two-sheeted covering of a circle.
Every unselected circle and every part of the horizontal line still has two disjoint copies mapping homeomorphically to its original copy.

The selected cut points form a closed discrete subset of $\widetilde X$: there is only one in the wedge attached at each integer point of the horizontal line, and these integer attachment points have no finite accumulation along the line.
Thus the cross-gluings are locally finite.
Consequently every point of $\widetilde X$ has a neighborhood whose inverse image is two disjoint copies, except along a selected circle where one uses the standard local charts of the connected double cover $S^1\to S^1$.
Hence $p$ is a two-sheeted covering map.
:::

<1>3. Suppose the composite
\[
q\circ p:Y\to X
\]
were a covering map.
Then the wedge point $x_0$ would have an evenly covered neighborhood $U$.
::: {.proof}
This is the definition of a covering map applied at $x_0$.
:::

<1>4. Every neighborhood $U$ of $x_0$ in the shrinking wedge $X$ contains all circles $C_m$ for sufficiently large $m$.
::: {.proof}
The shrinking wedge is the planar union of circles whose diameters tend to zero at the common point $x_0$.
Choose an ambient Euclidean ball
\[
B_\varepsilon(x_0)
\]
such that
\[
X\cap B_\varepsilon(x_0)\subseteq U.
\]
For all sufficiently large $m$, the entire circle $C_m$ lies inside this ball.
:::

<1>5. Choose $n$ so large that
\[
C_{r_n}\subseteq U.
\]
Then the inverse image
\[
(q\circ p)^{-1}(C_{r_n})
\]
contains a connected circle mapping two-to-one onto $C_{r_n}$.
::: {.proof}
By <1>1 and <1>4, such $n$ exists.
The circle $E_{n,r_n}\subseteq\widetilde X$ maps homeomorphically to $C_{r_n}$ under $q$.
By construction in <1>2, its inverse image in $Y$ contains the connected double-covering circle obtained by cross-gluing the two copies of $E_{n,r_n}$.
Thus the restriction of $q\circ p$ to this circle has degree two.
:::

<1>6. This contradicts the assumption that $U$ is evenly covered by $q\circ p$.
::: {.proof}
If $U$ were evenly covered, every connected sheet of
\[
(q\circ p)^{-1}(U)
\]
would map homeomorphically onto $U$.
The connected double-covering circle from <1>5 lies in one such sheet because its image $C_{r_n}$ is contained in $U$.
Restricting a homeomorphism of that sheet to the inverse image of $C_{r_n}$ would be injective.
But <1>5 gives two distinct points on this circle over every point of $C_{r_n}$.
This is impossible.
:::

<1>7. Therefore
\[
\boxed{q\circ p:Y\to X\text{ is not a covering map}.}
\]
::: {.proof}
The contradiction in <1>6 shows that no evenly covered neighborhood of $x_0$ can exist for the composite.
Both individual maps $p$ and $q$ are covering maps by construction and by the source figure.
:::

<1>8. Nevertheless, the composite has unique path lifting.
::: {.proof}
Given a path in $X$ and a chosen initial point in $Y$, first lift the path uniquely through the covering $q:\widetilde X\to X$, then lift that unique path uniquely through $p:Y\to\widetilde X$.
Existence and uniqueness at the two stages give existence and uniqueness for the composite.
:::
:::
