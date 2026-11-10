---
schema: qual/card@1
id: E-H5NO6
kind: problem
title: Retracts of Hausdorff spaces and the plane
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.4, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235),
    checked against Munkres, Topology (2000), Section 35 Exercise 4, printed p. 223, Exercise 31.5 and
    Theorem 23.5. Its three parts are the card's: Y is the equalizer of the retraction and the
    identity, hence closed in a Hausdorff Z; a retract of the connected plane is connected while a
    two-point set is not; and x -> x/|x| retracts the punctured plane onto the circle. What was
    corrected: "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 35.4, printed
    p. 13, argues (b) by "since A is Hausdorff as a subspace of R^2, there are disjoint open sets
    for each of the points in A, which form a separation of A", which is not valid as stated -- every
    Hausdorff space would be disconnected by that reasoning; the card uses connectedness of the
    plane, which is Moller's argument.
---

::: {.exercise}

Let $Z$ be a topological space.
If $Y$ is a subspace of $Z$, we say that $Y$ is a retract of $Z$ if there is a continuous map $r: Z \to Y$ such that $r(y) = y$ for each $y \in Y$.

(a) Show that if $Z$ is Hausdorff and $Y$ is a retract of $Z$, then $Y$ is closed in $Z$.

(b) Let $A$ be a two-point set in $\RR^2$.
Show that $A$ is not a retract of $\RR^2$.

(c) Let $S^1$ be the unit circle in $\RR^2$; show that $S^1$ is a retract of $\RR^2 - \theset{\mathbf{0}}$, where $\mathbf{0}$ is the origin.
Can you conjecture whether or not $S^1$ is a retract of $\RR^2$?
:::

::: {.solution}
(a) Let $i:Y\hookrightarrow Z$ be inclusion and $r:Z\to Y$ a retraction. Then
$$
R=i\circ r:Z\to Z
$$
is continuous, and
$$
Y=\{z\in Z:R(z)=z\}.
$$
Since $Z$ is Hausdorff, the equalizer of $R$ and the identity map is closed. Hence $Y$ is closed in $Z$.

(b) If a two-point set $A\subset\RR^2$ were a retract, the retraction $r:\RR^2\to A$ would be a continuous surjection. But $\RR^2$ is connected, so its continuous image $A$ would be connected, whereas a two-point subspace of the Hausdorff plane is disconnected. Contradiction.

(c) The radial map
$$
r:\RR^2\setminus\{0\}\to S^1,
\qquad
r(x)=\frac{x}{\norm{x}},
$$
is continuous and restricts to the identity on $S^1$, so $S^1$ is a retract of the punctured plane.

One should conjecture that $S^1$ is not a retract of the whole plane. This is true; it is the classical no-retraction theorem for the disk/circle, proved later by algebraic-topological methods.
:::
