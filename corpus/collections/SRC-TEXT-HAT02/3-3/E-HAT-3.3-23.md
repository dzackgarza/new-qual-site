---
schema: qual/card@1
id: E-HAT-3.3-23
kind: problem
title: Simplicial vs. singular compactly supported cohomology
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 23; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 23; it matches the printed text. The printed sentence beginning "This can be done by showing that $\Delta_i^c(X;G)$ is the union of its subgroups ..." was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: compact support means finitely many simplices, so both complexes are
    filtered unions over the cofinite subcomplexes, and on each such subcomplex the simplicial and
    singular theories agree naturally; exactness of filtered limits then identifies the two
    colimits.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct.
    Added: the justification that a compact subset of a locally compact Delta-complex meets only
    finitely many simplices, which the card asserted in one clause; the description of the
    compactly supported cochains as those vanishing off a finite union of simplices, in both
    directions; the directedness of the index set under reverse inclusion; the naturality of the
    comparison isomorphism in A; and the reference to [[E-HAT-3.3-17]] for the exactness of
    filtered colimits that the card quotes as 'filtered direct limits are exact'. No statement
    was changed. Not claimed: a retained solution set; the collection's provenance is the
    Hatcher textbook, whose text is not retained here.
---

::: {.problem}
Show that for a locally compact $\Delta$-complex $X$ the simplicial and singular cohomology groups $H_c^i(X; G)$ are isomorphic.
This can be done by showing that $\Delta_i^c(X; G)$ is the union of its subgroups $\Delta^i(X, A; G)$ as $A$ ranges over subcomplexes of $X$ that contain all but finitely many simplices, and likewise $C_c^i(X; G)$ is the union of its subgroups $C^i(X, A; G)$ for the same family of subcomplexes $A$.
:::

::: {.solution}
Throughout $X$ is a locally compact $\Delta$-complex, $G$ an abelian group, $\Delta^{i}_{c}(X;G)$ the compactly supported simplicial cochains and $C^{i}_{c}(X;G)$ the compactly supported singular cochains; $A$ always ranges over the subcomplexes of $X$ that contain all but finitely many simplices, ordered by reverse inclusion. The exercise is Hatcher, *Algebraic Topology*, §3.3 Exercise 23.

::: pf

::: {.pf-step #compact}
(i) A cochain in $\Delta^{i}_{c}(X;G)$ is nonzero on only finitely many $i$-simplices, so $\Delta^{i}_{c}(X;G) = \bigcup_{A}\Delta^{i}(X,A;G)$; and the same holds for singular cochains, $C^{i}_{c}(X;G) = \bigcup_{A}C^{i}(X,A;G)$.

::: pf-proof
Local compactness gives each point a compact neighbourhood, and a compact subset of a $\Delta$-complex meets only finitely many simplices: a simplex is the image of a closed simplex, and if a compact set met infinitely many distinct simplices their diameters would have to tend to $0$, forcing an accumulation point at which no neighbourhood would be compact (equivalently, the union of the interiors of the simplices met would give an infinite locally finite family inside a compact set). Hence a cochain whose support is compact is supported in a finite union of simplices, that is it vanishes on all but finitely many; conversely a cochain vanishing off finitely many simplices has support in a finite union of compact simplices, which is compact. The two equalities follow: a cochain vanishing on $A$ is one supported in the complement of $A$, a union of finitely many simplices, and every compactly supported cochain arises this way for the subcomplex $A$ spanned by the simplices on which it vanishes.

:::

:::

::: {.pf-step #filtered}
(ii) The two unions are filtered colimits over the directed set of such $A$.

::: pf-proof
If $A$ and $A'$ contain all but finitely many simplices then so does $A \cap A'$, and $A \cap A' \subseteq A, A'$; so under reverse inclusion the index set is directed. Each $\Delta^{i}(X,A;G) \to \Delta^{i}(X,A';G)$ for $A' \subseteq A$ is injective with the evident description, so the colimit of the system of subgroups is their union, and similarly for the singular groups.

:::

:::

::: {.pf-step #compare}
(iii) For each such $A$ the comparison map $H^{i}_{\Delta}(X,A;G) \to H^{i}_{\mathrm{sing}}(X,A;G)$ is an isomorphism, natural in $A$.

::: pf-proof
For a $\Delta$-complex the simplicial chains of $(X,A)$ compute the singular homology of the pair: the inclusion of the simplicial chain complex into the singular one is a chain homotopy equivalence, natural in the pair, so the induced map on cohomology with any coefficients is an isomorphism. Naturality in $A$ is inherited from the naturality of the chain map.

:::

:::

::: {.pf-step #exact}
(iv) For a filtered colimit of cochain complexes, cohomology commutes with the colimit: $H^{i}\bigl(\varinjlim_{A}C_{A}\bigr) \cong \varinjlim_{A}H^{i}(C_{A})$.

::: pf-proof
$H^{i} = \ker d^{i+1}/\operatorname{im}d^{i}$ is built from kernels and images, and filtered colimits of modules are exact — the same statement proved in [[E-HAT-3.3-17]] for chain complexes — so $\ker$ and $\operatorname{im}$ may be moved outside the colimit, and a filtered colimit of quotients is the quotient of the colimits.

:::

:::

::: pf-step
$H^{i}_{c,\Delta}(X;G) \cong H^{i}_{c,\mathrm{sing}}(X;G)$ for every $i$.

::: pf-proof
By steps [](#compact){.pf-ref} and [](#filtered){.pf-ref} the compactly supported complexes are the filtered colimits of the cochain complexes of the pairs $(X,A)$, so $H^{i}_{c,\Delta}(X;G) = \varinjlim_{A}H^{i}_{\Delta}(X,A;G)$ and $H^{i}_{c,\mathrm{sing}}(X;G) = \varinjlim_{A}H^{i}_{\mathrm{sing}}(X,A;G)$ by step [](#exact){.pf-ref}. Step [](#compare){.pf-ref} gives a natural isomorphism at each $A$, and a natural isomorphism of directed systems induces an isomorphism of their colimits; hence the two compactly supported cohomologies agree.

:::

:::

:::
:::
