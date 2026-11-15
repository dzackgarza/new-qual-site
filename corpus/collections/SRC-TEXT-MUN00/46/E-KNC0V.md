---
schema: qual/card@1
id: E-KNC0V
kind: problem
title: Separation properties of the compact-open topology
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 6 (printed p. 288) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the book's definition of the compact-open
    topology in §46 and the exercise's own hint. Hausdorff: for f(x) != g(x) take disjoint open U, V about the
    two values, and the subbasic sets S({x},U) and S({x},V) are disjoint. Regular: given a basic neighbourhood
    N = intersection of S(C_i, V_i) of f, regularity of Y applied to the point f(c) inside the open V_i gives
    for each c in C_i an open U with f(c) in U and closure(U) in V_i, and compactness of f(C_i) reduces to
    finitely many, so f lies in M = intersection of S(C_i, U_i) with closure(M) inside N. The hinted inclusion
    closure(S(C,U)) in S(C,V) for closure(U) in V is proved: if h(x) is outside V for some x in C, then h(x) is
    outside the closed set closure(U), and regularity of Y gives an open W about h(x) missing U, so S({x},W) is
    a neighbourhood of h disjoint from S(C,U). Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 542926, "In compact-open topology,
    C(X,Y) is Hausdorff if Y is Hausdorff" (2013-10-28), carries the Hausdorff half of this exercise:
    the accepted answer 542943 by Brian M. Scott takes the singleton {x} as the compact set and
    separates f from g by S({x},U_1) and S({x},U_2), which is the card's first paragraph. That answer
    then sets up the exercise's hint for the regular half and stops, asking the reader what follows
    from taking K = {x} and W = Y - closure(U); the card's second paragraph is that argument carried
    out, with the hinted inclusion proved, and it remains the card's own. The AoPS blog post by
    cinnamon_e, "Topology by Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), also answers the exercise at its item 6 of
    §46, with its formulas lost; the queries of this pass are in the COMPLAINTS.md entry for
    §43--§50.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Munkres' regular spaces have closed one-point sets by definition (Section 31, printed p. 195),
    and the proof of the regular half argued only that every neighbourhood of a point of C(X,Y)
    contains the closure of a neighbourhood, which is Lemma 31.1(a) and needs that closedness for the
    other half of the definition. A reader of this card reported it. The proof now records that the
    Hausdorff half gives closed one-point sets by Theorem 17.8, that a regular Y is Hausdorff so that
    half applies to Y, and that the shrinking property together with closedness of one-point sets is
    Lemma 31.1(a). The Hausdorff half, the hinted inclusion and the compact-open argument are
    unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the regular half asserted an open U_i with f(C_i) contained in
    U_i and the closure of U_i contained in V_i from compactness of f(C_i) and regularity of Y, without
    the finite-subcover step that supplies one set from the pointwise ones. The proof now applies
    regularity at each point y of f(C_i) to the point and the closed set Y - V_i, which does not contain
    it, obtaining an open W_y whose closure lies in V_i; the W_y cover the compact set f(C_i), so
    finitely many do, and their union is the U_i wanted, the closure of a finite union being the union of
    the closures. Nothing else on the card was changed.
---

::: {.exercise}

Show that in the compact-open topology, $\mathcal{C}(X, Y)$ is Hausdorff if $Y$ is Hausdorff, and regular if $Y$ is regular.
[Hint: If $\overline{U} \subset V$, then $\overline{S(C, U)} \subset S(C, V)$.]
:::

::: {.solution}
Assume $Y$ Hausdorff. If $f\ne g$ in $C(X,Y)$, choose $x$ with $f(x)\ne g(x)$ and disjoint open neighborhoods $U,V$ of these values. Since $\{x\}$ is compact, the subbasic sets
$$
S(\{x\},U),\qquad S(\{x\},V)
$$
are disjoint neighborhoods of $f,g$. Hence $C(X,Y)$ is Hausdorff, and by Theorem 17.8 its one-point sets are closed.

Now assume $Y$ regular. A regular space is Hausdorff, so the argument just given applies with $Y$ regular, and $C(X,Y)$ has closed one-point sets; that is one of the two conditions Munkres' definition of regularity imposes, and it remains to shrink a basic neighborhood
$$
N=\bigcap_{i=1}^n S(C_i,V_i)
$$
of $f$. For each $i$ and each $y\in f(C_i)$, regularity of $Y$ applied to the point $y$ and the closed set $Y-V_i$, which does not contain it, gives an open $W_y$ with
$$
y\in W_y,\qquad \overline{W_y}\subset V_i.
$$
The sets $W_y$ over the points $y$ of $f(C_i)$ cover it, and $f(C_i)$ is compact, so finitely many of them, say for $y_1,\dots,y_m$, cover it; their union $U_i$ is open with
$$
f(C_i)\subset U_i,\qquad \overline{U_i}\subset V_i,
$$
the closure of a finite union being the union of the closures.
Put $M=\bigcap_iS(C_i,U_i)$. Then $f\in M$. The hinted inclusion
$$
\overline{S(C,U)}\subset S(C,V)\quad(\overline U\subset V)
$$
follows because if $h(C)$ is not contained in $V$, choose $x\in C$ with $h(x)\notin V$; the evaluation neighborhood at $x$ avoiding $\overline U$ separates $h$ from $S(C,U)$. Therefore
$$
\overline M\subset\bigcap_i\overline{S(C_i,U_i)}\subset N.
$$
So every neighborhood of a point $f$ contains the closure of a neighborhood of $f$, which with the closedness of one-point sets is Lemma 31.1(a); the function space is regular.
:::
