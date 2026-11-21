---
schema: qual/card@1
id: E-J8QUX
kind: problem
title: Two-dimensional CW complexes with finitely many cells are metrizable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Metrization
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §73 Exercise 4, printed p. 445. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The hint's perfect map
    is used in the form "a closed surjection with compact fibres from a second-countable space has a
    second-countable image", which is proved on the card: the countable family got by pushing a countable base
    through the closed map. Metrizability then follows from Theorem 34.1 (printed p. 215), the space being
    compact Hausdorff hence regular. Checked against Exercise 2 of this section (printed p. 445) for
    compactness and Hausdorffness.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §73 Exercise 4, printed p. 445. Searched outside the checkout for issue #144; the thread the throttled
    address could not open was read from the orchestrator's machine, recorded in tmp/sources/mse-searches-144.md,
    thread tmp/sources/mse-1745722-E-J8QUX.md. Math StackExchange 1745722, "Quotient of compact metric space is
    metrizable (when Hausdorff)?" (asked 2016-04-16), has two answers, both read whole, and both prove this exercise
    in general form. Answer 1749351 by Brian M. Scott (2016-04-19) proves that a quotient of a compact metric space
    onto a Hausdorff space has a countable base and so is metrizable, and answers the thread's second question in
    the negative with X = [0,1], Q = [0,1] cap the rationals and Y = X/Q; it is transcribed on the card, whose steps
    2 and 3 are that proof. Answer 1749361 by Eric Wofsey (2016-04-19) proves the same metrizability through the
    separability of C(K) and the Stone-Weierstrass theorem, which the book does not have, and nothing of it is used.
    That the E and X of this exercise satisfy the hypotheses is steps 1 and 3 of the card. Murayama's selection
    answers §73 Exercise 1 and the Klein bottle exercise, not this one; dbFin has no §73 page, the fourteen
    repositories stop at Chapter 3, and no course page found treats these sections. The card's proof was re-read
    against Theorem 26.2 (printed p. 165), Theorem 30.2 (printed p. 191) and Theorem 34.1 (printed p. 215).
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Three defects reported by a reader of this card. (a) Step 1 said that closedness of q is step 1 of
    Exercise 2's card; that step there proves compactness and Hausdorffness of X from the normality of A and
    does not prove that q is closed, so the saturation argument is now written out here, for the m cells of
    this construction: the saturation of a closed C is C together with, for each i, the image of C cap Bd B_i
    under the attaching map, the preimage of that image, and the preimage of C cap A, each piece closed
    because the image of a compact set is compact and closed in the Hausdorff A and the preimages are closed
    by continuity. (b) Step 2 defined the base family as the sets X - q(E - U) for U in a countable base, but
    the argument uses a finite union of base elements, which need not be a base element; the family is now
    indexed by the finite unions of members of the base, still countable, and the step records that its
    members are open because q is closed. (c) Step 2 asserted that A is a compact subspace of R^2 without a
    reference; the remark on printed p. 434 that the wedge of n circles imbeds in the plane as a union of n
    circles is now cited, and that union is compact. Step 3 was re-read and kept.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    A reader's defect in step 1, checked against the book and repaired. The saturation written there was
    indexed by the restrictions of the attaching map to one boundary circle at a time, so it omitted a point
    of one boundary circle whose image in A is also the image of a point of a boundary circle of another
    cell: with C = {x'} and x' in Bd B_1, a y in Bd B_2 with f(y) = f(x') has q(y) = q(x'), so y lies in the
    saturation and in no displayed piece. That cannot happen in the one-cell case, and Exercise 2 attaches m
    cells by one map f defined on the union of the boundary circles (printed p. 445), so step 1 now treats f
    as that single map, on D = the disjoint union of the Bd B_i: the saturation is
    C union K union f^{-1}(K union (C cap A)) with K = f(C cap D). K is compact, hence closed in the
    Hausdorff A (Theorems 26.5 and 26.3, printed pp. 166 and 165), which is what makes the union closed; the
    enumeration of the three kinds of point now separates f(x) = f(c) for c in C cap D, the cross-cell case
    the old formula lost, from f(x) in C cap A. The card also concluded q(C) is closed with no reason given;
    the quotient property of X is now stated. The unused metric on E introduced in the preamble is dropped:
    no step uses it, and step 2 needs only second countability. Steps 2 and 3 are unchanged, and the printed
    statement (Exercise 4, printed p. 445) is untouched.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader's defect in step 3, checked against the book and repaired. The step concluded "X is compact Hausdorff
    by Exercise 2(a)", and Exercise 2(a) (printed p. 445) asks only for Hausdorffness. Compactness is now derived: X
    = q(E) with E the finite topological sum of the compact space A and the compact balls B_i, and q continuous, so
    X is compact by Theorem 26.5 (printed p. 166); Hausdorffness is Exercise 2(a), and normality, regularity and
    Theorem 34.1 (printed p. 215) follow as before. The rest of step 3 and steps 1 and 2 are unchanged, as is the
    printed statement (Exercise 4, printed p. 445).
---

::: {.exercise}

Show that the space constructed in [[E-VYYH3]] is in fact metrizable.
[Hint: The quotient map is a perfect map.]
:::

::: {.solution}

The theorem proved below is that of Brian M. Scott, answer 1749351 (https://math.stackexchange.com/a/1749351) to Math StackExchange question 1745722, "Quotient of compact metric space is metrizable (when Hausdorff)?" (2016-04-19): a quotient of a compact metric space onto a Hausdorff space is metrizable, and the thread's second question is answered there in the negative, a quotient of a compact metric space need not be second countable. Steps 2 and 3 are his proof, written for this $E$ and $X$: $E$ is compact metric, a finite topological sum of the compact subspace $A$ of the plane and the unit balls $B_i$, and $X$ is Hausdorff by Exercise 2(a). Step 1 is this card's own verification that $q$ is the closed map with compact fibres that the exercise's hint names: Scott obtains closedness instead from compactness of $E$ and Hausdorffness of $X$, so what the argument uses is the property, and either derivation supplies it. The other answer, 1749361 (https://math.stackexchange.com/a/1749361) by Eric Wofsey (2016-04-19), proves the same theorem through the separability of $C(K)$ and the Stone–Weierstrass theorem, which the book does not have, and nothing of it is used.

Let $E=A\sqcup B_1\sqcup\cdots\sqcup B_m$ and $q:E\to X$ be as in the construction of Exercise 2, with attaching map $f:\bigsqcup_{i=1}^m\operatorname{Bd}B_i\to A$, a single map defined on the union of the boundary circles (Exercises 2 and 4 of §73).

::: pf

::: pf-step

$q$ is a closed map with compact fibres.

::: pf-proof

Write $D=\bigsqcup_{i=1}^m\operatorname{Bd}B_i$, and for closed $C\subseteq E$ put $K=f(C\cap D)$. The saturation of $C$ is
$$
q^{-1}q(C)=C\cup K\cup f^{-1}\bigl(K\cup(C\cap A)\bigr).
$$
The map $q$ sends $x\in D$ to $f(x)$ and is injective on $A$ and on each $\operatorname{Int}B_i$. So $a\in A$ satisfies $q(a)\in q(C)$ exactly when $a\in C$ or $a=f(x)$ for some $x\in C\cap D$, that is $a\in C\cup K$; a point $x\in D$ satisfies $q(x)\in q(C)$ exactly when $x\in C$, or $f(x)=f(c)$ for some $c\in C\cap D$, or $f(x)\in C\cap A$, the last two being $x\in f^{-1}(K)$ and $x\in f^{-1}(C\cap A)$; and a point of $\operatorname{Int}B_i$ satisfies it exactly when it lies in $C$. The second of those cases is the one the single map $f$ contributes: boundary points of two different cells with the same image in $A$ are one point of $X$, so each lies in the saturation of the other, whichever cell $C$ meets.

Each piece is closed: $C$ by hypothesis; $C\cap D$ is closed in the compact space $D$, hence compact, so $K=f(C\cap D)$ is compact (Theorem 26.5) and therefore closed in the Hausdorff space $A$ (Theorem 26.3); $C\cap A$ is closed in $A$, so $K\cup(C\cap A)$ is closed in $A$ and its preimage is closed in $D$, hence in $E$. A finite union of closed sets is closed, so $q^{-1}q(C)$ is closed; $X$ carries the quotient topology, so a subset of $X$ is closed exactly when its preimage is, and $q(C)$ is closed. The fibre $q^{-1}(x)$ is a closed subset of the compact space $E$, hence compact (Theorem 26.2). So $q$ is perfect.

:::

:::

::: pf-step

$E$ is second-countable and $X$ has a countable base.

::: pf-proof

$E$ is the topological sum of the second-countable spaces $A$ (a compact subspace of $\RR^2$: the wedge of $n$ circles imbeds in the plane as the union of $n$ circles, printed p. 434, and that union is compact; $\RR^2$ is second-countable by Example 1, with Theorem 30.2) and the finitely many disks $B_i$ (subspaces of $\RR^2$); a finite sum of second-countable spaces is second-countable. Let $\mathcal{B}$ be a countable base for $E$, and let $\mathcal{C}$ be the family of the sets $X\setminus q(E\setminus U)$ for $U$ a finite union of members of $\mathcal{B}$; $\mathcal{C}$ is countable, the finite subsets of a countable set being countable, and its members are open in $X$ because $q$ is closed (step 1) and $U$ is open. Claim: $\mathcal{C}$ is a base for $X$. Let $x\in W$ with $W$ open in $X$; the compact set $F=q^{-1}(x)$ is contained in the open set $q^{-1}(W)$, so finitely many $U_1,\dots,U_r\in\mathcal{B}$ cover $F$ with $\bigcup U_i\subseteq q^{-1}(W)$. Put $U=\bigcup U_i$, a finite union of members of $\mathcal{B}$; then $x\in X\setminus q(E\setminus U)$ and $X\setminus q(E\setminus U)\subseteq W$: indeed $U\subseteq q^{-1}(W)$ gives $E\setminus U\supseteq E\setminus q^{-1}(W)$, hence $q(E\setminus U)\supseteq X\setminus W$.

:::

:::

::: pf-step

$X$ is metrizable.

::: pf-proof

$X$ is compact, being $q(E)$ with $E$ compact — a finite topological sum of the compact space $A$ and the compact balls $B_i$ — and $q$ continuous, by Theorem 26.5; it is Hausdorff by Exercise 2(a). Hence it is normal (Theorem 32.3) and so regular (the definition, gives regularity from normality). With the countable base of step 2, Theorem 34.1 gives a metric for $X$.

:::

:::

::: pf-qed

$X$ is a compact Hausdorff space with a countable base, hence metrizable.

:::

:::
:::
