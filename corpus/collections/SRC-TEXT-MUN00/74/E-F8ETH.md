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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Review repair of part (b). The earlier step justified the connecting tube by "R^3 minus
    a compact set is path connected", which is false: the complement of a torus in R^3 has
    two components, and a compact set can separate. The step is replaced by a construction
    in which the free region is named and shown to be free. Translate the second copy so
    that the first coordinate separates the two images; at the point of maximal x on the
    first image the tangent plane is vertical, because both v and -v are tangents of a
    sheet lying in a half space, and no second sheet can pass through that point, since its
    tangent plane would also be caught in the same vertical plane and the sheets cross
    transversally; so the sheet there is a graph over the vertical plane. Then the collar
    annulus from the graph's boundary circle to a flat circle, and a thin solid cylinder
    about a polygonal arc leaving the extreme point in the direction of increasing x and
    running in the open slab between the two images, have interiors disjoint from both
    images (the collar by the strict inequality of the graph over its boundary circle, the
    cylinder because the slab misses the first image, all of whose points have x at most
    the maximum, and the second, all of whose points have x at least the minimum). The
    removal of a disc from each surface and the gluing of the annulus gives K#K, and the
    corners are rounded in the free region. The construction is stated with its hypotheses
    (transversal self-intersections, as in Figure 74.11) rather than assumed.
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
Take two copies $\Sigma_1,\Sigma_2$ of the image of the standard immersion of $K$ in $\RR^3$ (Figure 74.11, printed p. 454), whose sheets meet transversally along its double curves. The construction below uses no general existence of a path in a complement: it exhibits the region in which the tube runs and shows that both images miss it.

::: {.pf-step #place}
After a translation of the second copy, the first coordinate $x$ satisfies $\max \restrictionof{x}{\Sigma_1}<\min \restrictionof{x}{\Sigma_2}$, and the points $q_1\in\Sigma_1$ of maximal $x$ and $q_2\in\Sigma_2$ of minimal $x$ each lie on a single sheet, which is a graph over the vertical plane through that point.

::: pf-proof
The images are compact, so translating the second copy far in the positive $x$ direction gives the inequality. Let $c=x(q_1)$ and let $p_1$ be a preimage of $q_1$; near $p_1$ the surface is a $2$-disc through $q_1$ lying in $\{x\le c\}$. A tangent vector $v$ of that disc at $q_1$ is the velocity of a curve in the disc through $q_1$, and so is $-v$; along both, $x\le c$ with equality at $q_1$, whence $\mathrm{d}x(v)=0$. So the tangent plane there is $\{x=c\}$. Two sheets through $q_1$ would each have tangent plane contained in $\{x=c\}$ and hence equal to it, contradicting that the sheets cross transversally; so exactly one sheet passes through $q_1$, the immersion is injective near $p_1$, and the sheet is a graph $\{(c+\psi(u,v),u,v)\}$ over a disc in $\{x=c\}$ with $\psi\le0$. The same holds at $q_2$.
:::

:::

::: {.pf-step #free}
With $x_j=x(q_j)$ there are a closed disc $D_j$ on the $j$-th surface around $p_j$, a collar annulus $A_j$ from $\partial f_j(D_j)$ to the flat circle of radius $\rho$ in the plane $\{x=x_j\}$ about $q_j$, and a thin solid cylinder about a polygonal arc from $q_1$ to $q_2$, such that the interiors of $A_1$, $A_2$ and the cylinder miss $\Sigma_1\cup\Sigma_2$ and one another.

::: pf-proof
Choose $\rho$ so small that the ball of radius $3\rho$ about $q_j$ meets $\Sigma_j$ only in the sheet over $q_j$: this holds for small $\rho$ because the immersion is injective near $p_j$ and $\Sigma_j$ is compact, so the part of $\Sigma_j$ outside the sheet stays at a positive distance from $q_j$. Take $D_j$ the preimage of the sheet over the disc of radius $\rho$, so $\partial f_j(D_j)$ is the graph over the circle of radius $\rho$. The collar $A_j$ is the annulus swept between that graph and the flat circle,
$$
A_j=\{(x_j+s\psi(u,v),\,u,\,v):\ u^2+v^2=\rho^2,\ 0\le s\le1\},
$$
whose interior points have $x_j+\psi(u,v)<x<x_j$ and $u^2+v^2=\rho^2$; such a point is on the sheet only if it equals $(x_j+\psi(u,v),u,v)$, which the strict inequality $x>x_j+\psi(u,v)$ excludes, and it is on no other part of $\Sigma_j$ because it lies in the ball of radius $3\rho$ about $q_j$. The open slab $\{x_1<x<x_2\}$ misses $\Sigma_1$, all of whose points have $x\le x_1$, and misses $\Sigma_2$, all of whose points have $x\ge x_2$; so a thin solid cylinder about a polygonal arc from $q_1$ to $q_2$ that leaves $q_1$ in the direction of increasing $x$, runs in the closed slab, and enters $q_2$ in the direction of decreasing $x$ has its interior in $\{x>x_1\}\cup\{x<x_2\}$ near its two ends and in the slab between, hence disjoint from both images; taking it thin enough keeps it inside the region of the previous sentence and away from the two collars.
:::

:::

::: {.pf-step #glue}
The union of the two punctured surfaces, the two collars and the tube is the image of an immersion of $K\#K$.

::: pf-proof
Remove the interiors of $D_1$ and $D_2$. What remains of $\Sigma_j$ is a surface with boundary circle $\partial f_j(D_j)$; glue the collar $A_j$ along that circle and the flat circle of the tube's side surface along its other boundary circle. The four pieces meet only along circles, their interiors are pairwise disjoint by step [](#free){.pf-ref}, and each piece is embedded where it lies; so the resulting space is a surface embedded in $\RR^3$ up to the pre-existing self-intersections of the two copies, that is, the map from the quotient surface to $\RR^3$ is locally injective. Cutting a disc out of each of two surfaces and gluing in an annulus along the two boundary circles produces their connected sum, so the quotient surface is $K\#K$. If a smooth immersion is wanted, the corners along the three circles are rounded inside small tubes about them, which lie in the free region. Composing with the homeomorphism of step [](#b-homeo){.pf-ref} gives the required immersion of $P^2\#P^2\#P^2\#P^2$.
:::

:::

:::

:::
:::


:::

:::
:::

A second published argument for (a) reaches the same conclusion from two pieces rather than from operations on the scheme: it is that of John Hughes, answers 1041446 (https://math.stackexchange.com/a/1041446, 2014-11-27) and 1039828 (https://math.stackexchange.com/a/1039828, 2014-11-26) to Math StackExchange question 1039819, "Connected sum of projective plane $\cong$ Klein bottle" (https://math.stackexchange.com/questions/1039819, asked by iwriteonbananas on 2014-11-26). A projective plane with an open disc deleted is a Möbius band, and the Klein bottle splits along a circle into two Möbius bands; hence both $P^2\#P^2$ and $K$ are two Möbius bands glued along their boundary circles, and are homeomorphic. Both inputs are shown there by sequences of figures, with the words "this is easy to see" and "you can check for yourself", and no homeomorphism is written down; the argument therefore carries the same conclusion as the passage above but not the elementary operations, which is what the printed hint asks for. Part (b) is not treated in that thread.
