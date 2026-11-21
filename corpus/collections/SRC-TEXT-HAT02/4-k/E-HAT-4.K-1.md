---
schema: qual/card@1
id: E-HAT-4.K-1
kind: problem
title: Gluing weak equivalences across CW subcomplex covers
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 1 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked the transfer: an intersection of
    subcomplexes is a subcomplex, hence a CW complex, so a weak equivalence between them is a
    homotopy equivalence by Corollary 4.33; the $f_J$ assemble to a map of the intersection diagrams
    because $f$ carries $U_j$ into $V_j$; Proposition 4G.1 upgrades vertexwise equivalences to an
    equivalence of realizations; and the subcomplex-cover form of Proposition 4G.2 (Exercise 4 of
    §4.G) gives each realization equivalent to $X$ or $Y$. Added: the explicit indexing of the
    diagram by nonempty finite $J$ with its inclusions, and the commutativity of the square with
    $f$, which the prose asserted in a clause. No defect found in the statement, §4.K Exercise 1; no
    retained solution set covers it, so the argument is the card's own.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 495 carries the running head 486.
    The durable part of the locator is that printed page; the file path names this machine's copy and
    `tmp/sources` does not survive a VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 4.K of Hatcher, *Algebraic Topology* (2002), printed p. 486, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Show that Corollary 4K.2 remains valid when $X$ and $Y$ are CW complexes and the subspaces $U_i$ and $V_i$ are subcomplexes rather than open sets.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it transfers the open-cover argument of §4.K to subcomplexes by way of the homotopy-colimit machinery of §4.G.

::: pf

::: {.pf-step #restrictions}
Let $f\colon X\to Y$ carry each subcomplex $U_i$ into $V_i$ and suppose each restriction $f_J\colon\bigcap_{j\in J}U_j\to\bigcap_{j\in J}V_j$, for $J$ finite and nonempty, is a weak homotopy equivalence. Then every $f_J$ is a homotopy equivalence.

::: pf-proof
An intersection of subcomplexes of a CW complex is a subcomplex, hence a CW complex, and the same holds on the $Y$ side. A weak homotopy equivalence between CW complexes is a homotopy equivalence: this is the homology form of Whitehead's theorem, Corollary 4.33 on p. 367.
:::

:::

::: {.pf-step #diagram-map}
The maps $f_J$ give a map of the diagrams of intersections over the index sets, and the induced map of their realizations is a homotopy equivalence.

::: pf-proof
Indexing the intersections by the nonempty finite sets $J$, with $J\subseteq J'$ giving the inclusion $\bigcap_{J'}U\hookrightarrow\bigcap_JU$, one has a diagram of spaces and inclusions whose realization is the homotopy colimit of Section 4.G; the $f_J$ commute with these inclusions because $f$ respects the subcomplexes, so they define a map of the realizations. By step [](#restrictions){.pf-ref} every map of vertex spaces in that diagram is a homotopy equivalence, and Proposition 4G.1 (p. 458) says that a map of such realizations is a homotopy equivalence when its maps on vertex spaces are.
:::

:::

::: {.pf-step #colimit-to-union}
Each realization maps to $X$, respectively $Y$, by a homotopy equivalence.

::: pf-proof
The subcomplex-cover form of Proposition 4G.2, which is Exercise 4 of §4.G on p. 460, states that the realization of the intersection diagram of a cover by subcomplexes maps to the union of the subcomplexes by a homotopy equivalence. The union of the subcomplexes is $X$ on one side and $Y$ on the other, by the hypothesis that the $U_i$ cover $X$ and the $V_i$ cover $Y$.
:::

:::

::: {.pf-step}
$f$ is a homotopy equivalence, so Corollary 4K.2 holds for subcomplex covers.

::: pf-proof
The square formed by the realization maps of step [](#diagram-map){.pf-ref} and the two equivalences of step [](#colimit-to-union){.pf-ref} commutes with $f$, and a composite of homotopy equivalences is one; so $f$ is a homotopy equivalence and in particular a weak homotopy equivalence, which is the conclusion of Corollary 4K.2 (p. 478) under the weaker hypothesis of open covers.
:::

:::

:::
:::
