---
schema: qual/card@1
id: E-F8ETH
kind: problem
title: The Klein bottle as a connected sum of two projective planes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

(a) Show that the Klein bottle is homeomorphic to $P^2 \# P^2$.
[Hint: Split the square in Figure 74.11 along a diagonal, flip one of the resulting triangular pieces over, and paste the two pieces together along the edge labelled $b$.]

(b) Show how to picture the 4-fold projective plane as an immersed surface in $\mathbb{R}^3$.
:::

::: {.solution}
(a) Use the standard square model of the Klein bottle. Its edge scheme may be written
\[
aba^{-1}b.
\]
Cut the square along a diagonal. Flip one of the two resulting triangles and reglue along the edge labelled \(b\), as indicated in the hint. After this cut-and-paste, the boundary word becomes
\[
aabb,
\]
which is the standard polygon scheme for the connected sum \(P^2\#P^2\). Cutting, flipping, and regluing along whole edges does not change the quotient surface, so
\[
\boxed{K\cong P^2\#P^2.}
\]

(b) Consequently
\[
P^2\#P^2\#P^2\#P^2\cong K\#K.
\]
Take two standard immersions of the Klein bottle in \(\mathbb R^3\), place them in disjoint balls, and choose on each a small disk lying in a regular embedded patch and disjoint from its self-intersection set. Remove the interiors of these two disks. Join the two resulting boundary circles by a thin embedded tube whose interior misses both immersed surfaces. On each original piece use the given Klein-bottle immersion, and on the tube use the embedding just chosen. Along collars of the boundary circles these maps agree after the usual smoothing/reparametrization, so together they give an immersion
\[
K\#K\looparrowright\mathbb R^3.
\]
Via part (a), this is an immersion of the four-fold projective plane. Thus the desired picture is obtained by taking two immersed Klein bottles and joining them by a tube at regular patches.
:::
