---
schema: qual/card@1
id: T-5IOUR
kind: theorem
title: Serre's cohomological criterion for affineness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Criterion
  - Affine Schemes
  - Cohomology
relations:
- kind: uses
  target: T-SK599
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- State Serre's criterion for affineness.
- Can the Noetherian hypothesis be weakened?
- What fails without quasicompactness?
---

::: {.theorem}
Let $X$ be a Noetherian scheme.
The following are equivalent:

(i) $X$ is affine.

(ii) $H^p(X, \mcf) = 0$ for all quasicoherent $\mcf$ and all $p > 0$.

(iii) $H^1(X, \mci) = 0$ for every coherent sheaf of ideals $\mci$.

[@Har10a, Theorem III.3.7]
:::

::: {.remark title="The two follow-ups"}
*Weakening Noetherian.* The criterion holds for quasicompact quasi-separated schemes, with $\mci$ ranging over quasicoherent ideals rather than coherent ones.
Noetherian is used only to have coherent ideals available and to extract finite subcovers, and both can be arranged directly.

*Dropping quasicompactness.* The conclusion fails.
An infinite disjoint union of affine schemes has vanishing higher cohomology for every quasicoherent sheaf, being a disjoint union of affines, but it is not affine: its ring of global sections is an infinite product, and the comparison map is not an isomorphism.
The finite subcover in the proof is where quasicompactness enters, and without it the $f_i$ need not be finite in number.
:::
