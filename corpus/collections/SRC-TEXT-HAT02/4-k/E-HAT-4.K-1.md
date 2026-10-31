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
---

::: {.problem}
Show that Corollary 4K.2 remains valid when $X$ and $Y$ are CW complexes and the subspaces $U_i$ and $V_i$ are subcomplexes rather than open sets.
:::

::: {.solution}
Let $f:X\to Y$ carry each subcomplex $U_i$ into $V_i$, and suppose that its restriction
$$
f_J:\bigcap_{j\in J}U_j\longrightarrow\bigcap_{j\in J}V_j
$$
is a weak homotopy equivalence for every nonempty finite index set $J$. These intersections are CW subcomplexes. Whitehead's theorem therefore makes each $f_J$ a homotopy equivalence.

Form the complexes of spaces associated to the two intersection diagrams, as in Section 4.G. The maps $f_J$ give a map between their realizations. Proposition 4G.1 says that this map is a homotopy equivalence because every map on a vertex space is one. By the subcomplex-cover version of Proposition 4G.2 (Exercise 4 of Section 4.G), each realization maps by a homotopy equivalence to the union of its subcomplexes, namely $X$ or $Y$. These maps commute with $f$. Hence $f$ is a homotopy equivalence, and in particular the weak homotopy equivalence asserted by Corollary 4K.2.
:::
