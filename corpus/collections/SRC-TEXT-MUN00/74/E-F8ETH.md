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
  date: 2026-11-15
  note: >-
    Munkres §74 Exercise 4(a),(b), printed p. 454. Searched outside the checkout for issue #146; the record
    is tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-1039819-E-F8ETH.md, read
    whole. Math StackExchange 1039819 has four answers, all read: 1041446 and 1039828 by John Hughes
    (2014-11-27 and 2014-11-26), 4982596 by Parcly Taxel (2024-10-10) and 4206516 by Li-Chung Wang
    (2021-07-25). The two Hughes answers prove (a) by exhibiting K and P^2#P^2 each as two Möbius bands
    glued along their boundary, both inputs shown by figures and asserted to be "easy to see"; that argument
    is now stated on the card with its URL, as a second route to the same conclusion, and the card keeps the
    elementary operations it had, which are the printed hint's route. Parcly Taxel's answer is a single
    figure. Li-Chung Wang's answer proves the homeomorphism through Munkres, Elements of Algebraic Topology,
    Figure 6.9, which is a different book and is cited there, not this exercise. Part (b) is not answered in
    the thread, so the card's (b) stays its own. Rejected in the search: mse 1658581 (a link only) and
    5052779 (an isomorphism of groups, not a homeomorphism of surfaces).
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

A second published argument for (a) reaches the same conclusion from two pieces rather than from operations on the scheme: it is that of John Hughes, answers 1041446 (https://math.stackexchange.com/a/1041446, 2014-11-27) and 1039828 (https://math.stackexchange.com/a/1039828, 2014-11-26) to Math StackExchange question 1039819, "Connected sum of projective plane $\cong$ Klein bottle" (https://math.stackexchange.com/questions/1039819, asked by iwriteonbananas on 2014-11-26). A projective plane with an open disc deleted is a Möbius band, and the Klein bottle splits along a circle into two Möbius bands; hence both $P^2\#P^2$ and $K$ are two Möbius bands glued along their boundary circles, and are homeomorphic. Both inputs are shown there by sequences of figures, with the words "this is easy to see" and "you can check for yourself", and no homeomorphism is written down; the argument therefore carries the same conclusion as the passage above but not the elementary operations, which is what the printed hint asks for. Part (b) is not treated in that thread.
:::
