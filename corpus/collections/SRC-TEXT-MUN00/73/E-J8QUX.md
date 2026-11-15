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
    Searched outside the checkout (issue #144) for §73 Exercise 4 (printed p. 445); queries and sets are in the
    COMPLAINTS.md entry for §66--§73 of SRC-TEXT-MUN00. Query used: "two-dimensional CW complex metrizable
    perfect map Munkres exercise 73.4 quotient space compact Hausdorff solution". Nothing located: Murayama's
    selection answers §73 Exercise 1 and the Klein bottle exercise, not this one; dbFin has no §73 page, the
    fourteen repositories stop at Chapter 3, and no course page found treats these sections. Nothing was
    transcribed. The card's own proof was re-read against Theorem 26.2 (printed p. 165) for compact fibres and
    Theorem 34.1 (printed p. 215) for the metrization: it proves second countability of X directly from a
    countable base of E, which is the step the exercise's hint leaves to the reader, and then applies the
    Urysohn metrization theorem to the compact Hausdorff space X. Nothing changed.
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
---

::: {.exercise}

Show that the space constructed in [[E-VYYH3]] is in fact metrizable.
[Hint: The quotient map is a perfect map.]
:::

::: {.solution}

Let $E=A\sqcup B_1\sqcup\cdots\sqcup B_m$ and $q:E\to X$ be as in the construction of Exercise 2, and let $d$ be a metric for $E$, which is compact metrizable.

::: pf

::: pf-step

$q$ is a closed map with compact fibres.

::: pf-proof

For closedness, let $C\subseteq E$ be closed and let $f_i$ be the restriction of the attaching map to $\operatorname{Bd}B_i$. The saturation of $C$ is
$$
q^{-1}q(C)=C\cup\bigcup_{i=1}^m\Bigl(f_i(C\cap\operatorname{Bd}B_i)\cup f_i^{-1}\bigl(f_i(C\cap\operatorname{Bd}B_i)\bigr)\cup f_i^{-1}(C\cap A)\Bigr):
$$
a point of $A$ lies in it when it lies in $C$ or is $f_i(x)$ for some $x\in C\cap\operatorname{Bd}B_i$; a point $x$ of $\operatorname{Bd}B_i$ lies in it when $x\in C$, when $f_i(x)\in C\cap A$, or when $f_i(x)=f_i(x')$ for some $x'\in C\cap\operatorname{Bd}B_i$; and a point of $\operatorname{Int}B_i$ lies in it only when it lies in $C$. Each piece is closed: $C$ by hypothesis; $f_i(C\cap\operatorname{Bd}B_i)$, because $C\cap\operatorname{Bd}B_i$ is compact and its image is compact (Theorem 26.5, printed p. 166), hence closed in the Hausdorff space $A$ (Theorem 26.3, printed p. 165); and the two preimages, because $f_i$ is continuous and the sets they come from are closed in $A$. A finite union of closed sets is closed, so $q(C)$ is closed and $q$ is a closed map. The fibre $q^{-1}(x)$ is a closed subset of the compact space $E$, hence compact (Theorem 26.2, printed p. 165). So $q$ is perfect.

:::

:::

::: pf-step

$E$ is second-countable and $X$ has a countable base.

::: pf-proof

$E$ is the topological sum of the second-countable spaces $A$ (a compact subspace of $\RR^2$: the wedge of $n$ circles imbeds in the plane as the union of $n$ circles, printed p. 434, and that union is compact; $\RR^2$ is second-countable by Example 1, printed p. 190, with Theorem 30.2, printed p. 191) and the finitely many disks $B_i$ (subspaces of $\RR^2$); a finite sum of second-countable spaces is second-countable. Let $\mathcal{B}$ be a countable base for $E$, and let $\mathcal{C}$ be the family of the sets $X\setminus q(E\setminus U)$ for $U$ a finite union of members of $\mathcal{B}$; $\mathcal{C}$ is countable, the finite subsets of a countable set being countable, and its members are open in $X$ because $q$ is closed (step 1) and $U$ is open. Claim: $\mathcal{C}$ is a base for $X$. Let $x\in W$ with $W$ open in $X$; the compact set $F=q^{-1}(x)$ is contained in the open set $q^{-1}(W)$, so finitely many $U_1,\dots,U_r\in\mathcal{B}$ cover $F$ with $\bigcup U_i\subseteq q^{-1}(W)$. Put $U=\bigcup U_i$, a finite union of members of $\mathcal{B}$; then $x\in X\setminus q(E\setminus U)$ and $X\setminus q(E\setminus U)\subseteq W$: indeed $U\subseteq q^{-1}(W)$ gives $E\setminus U\supseteq E\setminus q^{-1}(W)$, hence $q(E\setminus U)\supseteq X\setminus W$.

:::

:::

::: pf-step

$X$ is metrizable.

::: pf-proof

$X$ is compact Hausdorff by Exercise 2(a), hence normal (Theorem 32.3, printed p. 202) and so regular (the definition, printed p. 195, gives regularity from normality). With the countable base of step 2, Theorem 34.1 (printed p. 215) gives a metric for $X$.

:::

:::

::: pf-qed

$X$ is a compact Hausdorff space with a countable base, hence metrizable.

:::

:::
:::
