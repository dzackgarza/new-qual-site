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
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 4, printed p. 454. The hint's cut-and-paste replaced by the elementary operations Munkres carries out on aba^{-1}b in Example 1 of Section 76, printed p. 458, ending at aacc, the standard scheme of P^2#P^2. What was corrected: the card asserted that the cut and flip produce aabb without exhibiting an operation; the five operations with their intermediate words now appear. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 4, printed p. 454. The hint's cut-and-paste replaced by the elementary operations Munkres carries out on aba^{-1}b in Example 1 of Section 76, printed p. 458, ending at aacc, the standard scheme of P^2#P^2. What was corrected: the card asserted that the cut and flip produce aabb without exhibiting an operation; the five operations with their intermediate words now appear. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

(a) Show that the Klein bottle is homeomorphic to $P^2 \# P^2$.
[Hint: Split the square in Figure 74.11 along a diagonal, flip one of the resulting triangular pieces over, and paste the two pieces together along the edge labelled $b$.]

(b) Show how to picture the 4-fold projective plane as an immersed surface in $\RR^3$.
:::

::: {.solution}
(a) Use the standard square model of the Klein bottle, whose edge scheme is $aba^{-1}b$. The reduction to $aabb$ is the sequence of elementary operations that Munkres carries out in Example 1 of §76, printed p. 458, on this very scheme:

$$\begin{array}{ll}
a b a^{-1} b \longrightarrow a b c^{-1}\ \text{and}\ c a^{-1} b & \text{by cutting},\\
\longrightarrow c^{-1} a b\ \text{and}\ b^{-1} a c^{-1} & \text{by permuting the first and flipping the second},\\
\longrightarrow c^{-1} a a c^{-1} & \text{by pasting},\\
\longrightarrow a a c c & \text{by permuting and relabelling},
\end{array}$$

using operations (i), (iv), (v), (ii) and (iii) of the list on printed p. 458. The word $aacc$ is the standard scheme $(a_1a_1)(a_2a_2)$ of the connected sum $P^2\#P^2$, Theorem 74.4, so $K\cong P^2\#P^2$. The cut-and-paste of the printed hint is the geometric picture of the first three steps: the cut along the diagonal produces the auxiliary label $c$, and the flip of the second piece is the reversal of one of the resulting schemes.

(b) Consequently
$$
P^2\#P^2\#P^2\#P^2\cong K\#K.
$$
Take two standard immersions of the Klein bottle in $\RR^3$, place them in disjoint balls, and choose on each a small disk lying in a regular embedded patch and disjoint from its self-intersection set. Remove the interiors of these two disks. Join the two resulting boundary circles by a thin embedded tube whose interior misses both immersed surfaces. On each original piece use the given Klein-bottle immersion, and on the tube use the embedding just chosen. Along collars of the boundary circles these maps agree after the usual smoothing/reparametrization, so together they give an immersion
$$
K\#K\looparrowright\RR^3.
$$
Via part (a), this is an immersion of the four-fold projective plane. Thus the desired picture is obtained by taking two immersed Klein bottles and joining them by a tube at regular patches.
:::
