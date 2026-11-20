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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the card's own argument; no published solution covers this
    exercise, so the card keeps its own and says so. Two things were repaired in the restructure. The
    hinted inclusion closure S(C,U) is contained in S(C,V) for closure U in V is now proved from the
    regularity of Y rather than asserted, and the compactness step of the regular half now runs
    through the finite subcover of the W_y over the compact set f(C_i) and the closure of a finite
    union, rather than positing U_i outright. Nothing else was changed; the statement was checked
    against Munkres, Topology (2000), Section 46 Exercise 6, printed p. 288, with the compact-open
    subbasis on printed p. 287, the definition of regularity on printed p. 195, Lemma 31.1 on printed
    p. 196, Theorem 17.8 on printed p. 99 and Theorem 26.5 on printed p. 166.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the card's own argument; no published solution covers this
    exercise, so the card keeps its own and says so. Two things were repaired in the restructure. The
    hinted inclusion closure S(C,U) is contained in S(C,V) for closure U in V is now proved from the
    regularity of Y rather than asserted, and the compactness step of the regular half now runs
    through the finite subcover of the W_y over the compact set f(C_i) and the closure of a finite
    union, rather than positing U_i outright. Nothing else was changed; the statement was checked
    against Munkres, Topology (2000), Section 46 Exercise 6, printed p. 288, with the compact-open
    subbasis on printed p. 287, the definition of regularity on printed p. 195, Lemma 31.1 on printed
    p. 196, Theorem 17.8 on printed p. 99 and Theorem 26.5 on printed p. 166.
---

::: {.exercise}

Show that in the compact-open topology, $\mathcal{C}(X, Y)$ is Hausdorff if $Y$ is Hausdorff, and regular if $Y$ is regular.
[Hint: If $\overline{U} \subset V$, then $\overline{S(C, U)} \subset S(C, V)$.]
:::

::: {.solution}

This argument is the card's own: no retained set proves the exercise, and the two located partial sources are named here rather than cited as proof. Math StackExchange 542926 ("In compact-open topology, $\mathcal{C}(X,Y)$ is Hausdorff if $Y$ is Hausdorff", 2013) carries the Hausdorff half, with Brian M. Scott's answer 542943 taking the singleton $\theset{x}$ as the compact set; that answer then sets up the hint for the regular half and stops, and the argument below is written out from the hint. The AoPS post *Topology by Munkres Chapter 7 | Day 17* answers the exercise at its item 6 of §46 with its formulas lost in the extraction, and the site serves an automated request a human check, which is not worked around; the searches are recorded in `COMPLAINTS.md`.

The statement was checked against Munkres, *Topology* (2000), §46 Exercise 6. Throughout, $X$ and $Y$ are spaces and $\mathcal{C}(X,Y)$ is the set of continuous maps $X\to Y$ with the compact-open topology, generated by the subbasis
$$
S(C,U)\coloneqq\theset{f\in\mathcal{C}(X,Y)\mid f(C)\subset U},
$$
over the compact subsets $C\subset X$ and the open subsets $U\subset Y$ (§46); the finite intersections of members of this subbasis are a basis. A *regular* space is one whose one-point sets are closed and in which a point can be separated from a closed set not containing it by disjoint open sets (§31), and for such a space Lemma 31.1(a) is available: every neighbourhood of a point contains the closure of a neighbourhood of it.

::: pf

::: {.pf-step #hausdorff}

If $Y$ is Hausdorff, then $\mathcal{C}(X,Y)$ is Hausdorff.

:::: pf-proof

Let $f\neq g$ in $\mathcal{C}(X,Y)$.

::: {.pf-step #separate-values}

There is a point $x_{0}\in X$ with $f(x_{0})\neq g(x_{0})$, and $Y$ has disjoint open sets $U\ni f(x_{0})$ and $V\ni g(x_{0})$.

::: pf-proof

Since $f\neq g$ the maps differ at some point $x_{0}$. The space $Y$ is Hausdorff, so the distinct points $f(x_{0})$ and $g(x_{0})$ have disjoint open neighbourhoods $U$ and $V$.

:::

:::

::: {.pf-step #slices}

$S(\theset{x_{0}},U)$ and $S(\theset{x_{0}},V)$ are disjoint neighbourhoods of $f$ and of $g$.

::: pf-proof

The set $\theset{x_{0}}$ is compact, since any family of open sets covering it has a member containing $x_{0}$ and that one member covers it; so both sets are subbasis elements. Since $f(x_{0})\in U$ and $g(x_{0})\in V$, one has $f\in S(\theset{x_{0}},U)$ and $g\in S(\theset{x_{0}},V)$. If $h$ lay in both, then $h(x_{0})\in U\cap V=\varnothing$, which is impossible; so they are disjoint.

:::

:::

::::

:::

::: {.pf-step #shrink}

If $Y$ is regular, then every neighbourhood of a point of $\mathcal{C}(X,Y)$ contains the closure of a neighbourhood of it, and one-point sets in $\mathcal{C}(X,Y)$ are closed.

:::: pf-proof

Suppose $Y$ regular. Two claims are needed for Lemma 31.1(a): the closedness of one-point sets, and the shrinking of neighbourhoods.

::: {.pf-step #closed-points}

$Y$ is Hausdorff, so one-point sets in $\mathcal{C}(X,Y)$ are closed.

::: pf-proof

A regular space is Hausdorff, because its one-point sets are closed and a point can be separated from a closed set not containing it (§31). Hence $\mathcal{C}(X,Y)$ is Hausdorff by step [](#hausdorff){.pf-ref}, and in a Hausdorff space every finite point set is closed (Theorem 17.8).

:::

:::

::: {.pf-step #hint}

Let $C\subset X$ be compact and $U,V\subset Y$ open with $\overline{U}\subset V$. Then $\overline{S(C,U)}\subset S(C,V)$.

::: pf-proof

Let $h\in\mathcal{C}(X,Y)$ with $h\notin S(C,V)$, that is, with $h(x)\notin V$ for some $x\in C$. Since $U\subset\overline{U}\subset V$, the point $h(x)$ does not lie in the closed set $\overline{U}$; regularity of $Y$ applied to the point $h(x)$ and that closed set gives disjoint open sets containing them, and in particular an open $Z\ni h(x)$ with $Z\cap\overline{U}=\varnothing$.

The set $S(\theset{x},Z)$ is a subbasis element, since $\theset{x}$ is compact --- one member of any open cover of it already covers it --- and it contains $h$. If $g\in S(\theset{x},Z)$, then $g(x)\in Z$ and so $g(x)\notin\overline{U}$, whence $g(x)\notin U$ and $g\notin S(C,U)$, because $x\in C$. Therefore $S(\theset{x},Z)\cap S(C,U)=\varnothing$, and every neighbourhood of $h$ fails to meet $S(C,U)$; so $h$ is not in the closure of $S(C,U)$, and $\overline{S(C,U)}\subset S(C,V)$.

:::

:::

::: {.pf-step #basic}

Let $f\in\mathcal{C}(X,Y)$ and let $N=\bigcap_{i=1}^{n}S(C_{i},V_{i})$ be a basic neighbourhood of $f$. There is a neighbourhood $M$ of $f$ with $\overline{M}\subset N$.

:::: pf-proof

Suppose $f\in S(C_{i},V_{i})$ for each $i$, which is what membership of $f$ in the basic neighbourhood $N$ means, and write $C_{i}$ for the compact sets and $V_{i}$ for the open sets involved.

::: {.pf-step #shrunk}

For each $i$ there is an open $U_{i}\subset Y$ with $f(C_{i})\subset U_{i}$ and $\overline{U_{i}}\subset V_{i}$.

::: pf-proof

Fix $i$. For $y\in f(C_{i})$ one has $y\in V_{i}$, since $f\in S(C_{i},V_{i})$; regularity of $Y$ applied to the point $y$ and the closed set $Y-V_{i}$, which does not contain it, gives disjoint open sets, one containing $y$ — call it $W_{y}$ — and one containing $Y-V_{i}$; since the latter is open and disjoint from $W_{y}$ it is disjoint from $\overline{W_{y}}$, so $\overline{W_{y}}\subset V_{i}$.

The sets $W_{y}$, $y\in f(C_{i})$, cover $f(C_{i})$, and $f(C_{i})$ is compact, being the image of the compact set $C_{i}$ under the continuous map $f$ (Theorem 26.5); so finitely many of them, say for $y_{1},\dots,y_{m}$, cover it. The union $U_{i}\coloneqq W_{y_{1}}\cup\cdots\cup W_{y_{m}}$ is open and contains $f(C_{i})$, and $\overline{U_{i}}=\overline{W_{y_{1}}}\cup\cdots\cup\overline{W_{y_{m}}}\subset V_{i}$, the closure of a finite union being the union of the closures.

:::

:::

::: pf-step

$M\coloneqq\bigcap_{i=1}^{n}S(C_{i},U_{i})$ is a neighbourhood of $f$ and $\overline{M}\subset N$.

::: pf-proof

$f\in M$ because $f(C_{i})\subset U_{i}$ for every $i$. For each $i$, step [](#hint){.pf-ref} applied to $C_{i}$, $U_{i}$ and $V_{i}$ --- whose hypotheses hold by step [](#shrunk){.pf-ref} --- gives $\overline{S(C_{i},U_{i})}\subset S(C_{i},V_{i})$, and therefore
$$
\overline{M}=\overline{\bigcap_{i=1}^{n}S(C_{i},U_{i})}\subset\bigcap_{i=1}^{n}\overline{S(C_{i},U_{i})}\subset\bigcap_{i=1}^{n}S(C_{i},V_{i})=N,
$$
the first inclusion holding because the closure of an intersection is contained in the intersection of the closures.

:::

:::

::::

:::

::: pf-step

Every neighbourhood in $\mathcal{C}(X,Y)$ of a point contains the closure of a neighbourhood of it, and one-point sets in $\mathcal{C}(X,Y)$ are closed.

::: pf-proof

Let $f\in\mathcal{C}(X,Y)$ and let $O$ be a neighbourhood of $f$. The finite intersections of the subbasis elements $S(C,U)$ form a basis for the compact-open topology, so there is a basic neighbourhood $N$ of $f$ with $N\subset O$; step [](#basic){.pf-ref} then gives a neighbourhood $M$ of $f$ with $\overline{M}\subset N\subset O$. One-point sets are closed by step [](#closed-points){.pf-ref}.

:::

:::

::::

:::

::: pf-step

Therefore $\mathcal{C}(X,Y)$ is Hausdorff if $Y$ is Hausdorff, and regular if $Y$ is regular.

::: pf-proof

The first assertion is step [](#hausdorff){.pf-ref}. For the second, suppose $Y$ regular: step [](#shrink){.pf-ref} gives that one-point sets are closed and that every neighbourhood $O$ of a point $f$ contains the closure of a neighbourhood of $f$ — take a basic neighbourhood $N$ of $f$ with $N\subset O$, which exists because the finite intersections of the subbasis $S(C,U)$ are a basis, and shrink $N$ as in step [](#basic){.pf-ref}. With one-point sets closed, Lemma 31.1(a) makes $\mathcal{C}(X,Y)$ regular, and the separation of a point from a closed set is the second clause in the definition of regularity in Munkres.

:::

:::

:::

:::
