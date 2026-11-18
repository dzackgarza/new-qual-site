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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Page repairs, checked page by page against the 2000
    edition: Example 1 of §76 is on printed p. 461, not p. 458, and the list of elementary
    operations (i)-(vii) is on printed p. 460, not p. 458; Theorem 74.4 is on printed
    p. 453, and it is cited for the standard schemes because its proof reads the relation
    off the scheme (a_1a_1)...(a_m a_m), with Theorem 77.5 (printed p. 469) naming the
    surface. Wording repaired: the prose called this "the reduction to aabb" while its
    display ends at aacc. Each of the four scheme steps is checked against the printed
    display: the cut along the diagonal from v0 to v2 gives abc^{-1} and a^{-1}bc, whose
    cyclic permutation is the printed ca^{-1}b; the flip of ca^{-1}b is b^{-1}ac^{-1}; the
    paste along b, with b in the role of the letter c of operation (ii), gives
    c^{-1}aac^{-1}; and a cyclic permutation followed by the sign change of c gives aacc.
    Part (b) is the card's own argument: the connected sum is associative up to
    homeomorphism, and a compactly supported immersion punctured in two regular patches
    and joined by an embedded tube gives an immersion of the connected sum. What was not
    done: no explicit parametrization of the immersed Klein bottles is written out, the
    figure of §74 Exercise 3 being cited for it.
---

::: {.exercise}

(a) Show that the Klein bottle is homeomorphic to $P^2 \# P^2$.
[Hint: Split the square in Figure 74.11 along a diagonal, flip one of the resulting triangular pieces over, and paste the two pieces together along the edge labelled $b$.]

(b) Show how to picture the 4-fold projective plane as an immersed surface in $\RR^3$.
:::

::: {.solution}
Part (a) is the book's own derivation: Munkres carries it out as Example 1 of §76, printed p. 461, using the elementary operations on schemes listed on printed p. 460, and the four steps below are that display with each operation named and checked. Part (b) is not treated in the retained thread (Math StackExchange 1039819, whose four answers are recorded in the audit), so its argument is the card's own. A second published route to (a), that of John Hughes, is recorded after the proof.

Throughout, a labelling scheme for a polygonal region denotes the quotient space obtained by pasting its edges in pairs as the labels direct (§74), and $K$ is the Klein bottle.

::: pf

::: {.pf-step #operations}
Each of the elementary operations (i)--(vii) on a labelling scheme replaces a scheme by one whose quotient space is homeomorphic to it, and $K$ is the quotient of the square by the scheme $aba^{-1}b$.

::: pf-proof
The list of operations and their justification are on printed p. 460: (i) cut, (ii) paste, (iii) relabel, including the change of sign of the exponent of a label, (iv) permute cyclically, (v) flip, (vi) cancel and (vii) uncancel. Each is a cut-and-paste of the polygonal region, and the composite of the resulting quotient maps is the original one. The Klein bottle is the space obtained from a square by the scheme $aba^{-1}b$ (Example 1 of §76, printed p. 461; §74 Exercise 3, printed p. 454).
:::

:::

::: {.pf-step #a}
(a) $K$ is homeomorphic to $P^2\#P^2$.

::: pf-proof

::: {.pf-step #cut}
The scheme $aba^{-1}b$ is equivalent to the pair of schemes $abc^{-1}$ and $ca^{-1}b$.

::: pf-proof
This is operation (i), the cut. Read the boundary of the square as the cycle $v_0\xrightarrow{a}v_1\xrightarrow{b}v_2\xrightarrow{a^{-1}}v_3\xrightarrow{b}v_0$, and cut along the diagonal from $v_0$ to $v_2$, labelling it $c$ with the orientation $v_0\to v_2$. The triangle $v_0v_1v_2$ then has scheme $abc^{-1}$, the edge $c$ being traversed backwards, and the triangle $v_2v_3v_0$ has scheme $a^{-1}bc$, which is the cyclic permutation of $ca^{-1}b$. This is the printed hint's cut along the diagonal.
:::

:::

::: {.pf-step #flip}
The pair $abc^{-1}$ and $ca^{-1}b$ is equivalent to the pair $c^{-1}ab$ and $b^{-1}ac^{-1}$.

::: pf-proof
A cyclic permutation of $abc^{-1}$ is $c^{-1}ab$, by operation (iv). The formal inverse of $ca^{-1}b$ is $b^{-1}(a^{-1})^{-1}c^{-1}=b^{-1}ac^{-1}$, by operation (v), the flip which turns one triangle over.
:::

:::

::: {.pf-step #paste}
The pair $c^{-1}ab$ and $b^{-1}ac^{-1}$ is equivalent to the single scheme $c^{-1}aac^{-1}$.

::: pf-proof
Write the first scheme as $y_0b$ with $y_0=c^{-1}a$ and the second as $b^{-1}y_1$ with $y_1=ac^{-1}$; the label $b$ occurs in them with exponents $+1$ and $-1$ and nowhere else, so operation (ii), the paste, applies with $c$ there read as $b^{-1}$, and it replaces the pair by $y_0y_1=c^{-1}aac^{-1}$.
:::

:::

::: {.pf-step #standard}
$c^{-1}aac^{-1}$ is equivalent to $aacc$, which is the scheme of $P^2\#P^2$; hence $K\cong P^2\#P^2$.

::: pf-proof
A cyclic permutation of $c^{-1}aac^{-1}$ is $aac^{-1}c^{-1}$ by operation (iv), and changing the sign of the exponent of every occurrence of $c$ replaces it by $aacc$ by operation (iii). By Theorem 74.4 (printed p. 453) the $m$-fold projective plane is the quotient of the $2m$-gon with scheme $(a_1a_1)\cdots(a_ma_m)$, so for $m=2$ its scheme is $(a_1a_1)(a_2a_2)$, a relabelling of $aacc$; and Theorem 77.5 (printed p. 469) names the connected sum of two projective planes as the $2$-fold projective plane. Since steps [](#cut){.pf-ref}, [](#flip){.pf-ref} and [](#paste){.pf-ref} are sequences of elementary operations, the quotient spaces are homeomorphic by step [](#operations){.pf-ref}, which is (a).
:::

:::

:::

:::

::: {.pf-step #b}
(b) The four-fold projective plane is homeomorphic to $K\#K$ and is immersed in $\RR^3$ by two immersed Klein bottles joined by a tube.

::: pf-proof

::: {.pf-step #b-homeo}
$P^2\#P^2\#P^2\#P^2\cong K\#K$.

::: pf-proof
The connected sum of a finite family of surfaces is formed by deleting one open disc from each member of a disjoint union and pasting the resulting boundary circles in a chain (§74); regrouping the chain does not change the quotient, so the connected sum is associative and commutative up to homeomorphism. Hence $P^2\#P^2\#P^2\#P^2\cong(P^2\#P^2)\#(P^2\#P^2)$, and each factor is $K$ by step [](#a){.pf-ref}.
:::

:::

::: {.pf-step #b-immersion}
$K\#K$ has an immersion in $\RR^3$, so the four-fold projective plane does.

::: pf-proof
Take two copies of the standard immersion of $K$ in $\RR^3$ (Figure 74.11, printed p. 454), placed in disjoint open balls. For an immersion of a compact surface the set of double points is a compact one-dimensional subspace of the surface, so its complement is nonempty and open; choose in it a point $p_j$ of the $j$-th copy, with a closed disc $D_j$ around $p_j$ on which the immersion is injective and whose image meets no double point. Remove the interiors of $D_1$ and $D_2$ and keep the restriction of each immersion, which is an embedding of a collar of the boundary circle $\partial D_j$ onto a neighbourhood of the image circle. Join the two image circles by an embedded tube, a copy of $S^1\times[0,1]$ meeting each image surface exactly in one of the circles and otherwise disjoint from both, which is possible because $\RR^3$ minus a compact set is path connected and the two circles are joined by a polygon avoiding the compact images. On the tubes use the embedding, and on the punctured surfaces the given immersions; along each boundary circle the two agree after the reparametrization given by the collar, so the three pieces define a continuous map of the quotient $K\#K$ to $\RR^3$ which is locally injective, hence an immersion. Composing with the homeomorphism of step [](#b-homeo){.pf-ref} gives the required immersion of $P^2\#P^2\#P^2\#P^2$.
:::

:::

:::

:::

:::
:::

A second published argument for (a) reaches the same conclusion from two pieces rather than from operations on the scheme: it is that of John Hughes, answers 1041446 (https://math.stackexchange.com/a/1041446, 2014-11-27) and 1039828 (https://math.stackexchange.com/a/1039828, 2014-11-26) to Math StackExchange question 1039819, "Connected sum of projective plane $\cong$ Klein bottle" (https://math.stackexchange.com/questions/1039819, asked by iwriteonbananas on 2014-11-26). A projective plane with an open disc deleted is a Möbius band, and the Klein bottle splits along a circle into two Möbius bands; hence both $P^2\#P^2$ and $K$ are two Möbius bands glued along their boundary circles, and are homeomorphic. Both inputs are shown there by sequences of figures, with the words "this is easy to see" and "you can check for yourself", and no homeomorphism is written down; the argument therefore carries the same conclusion as the passage above but not the elementary operations, which is what the printed hint asks for. Part (b) is not treated in that thread.
