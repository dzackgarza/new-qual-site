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
- State and prove Serre's criterion for affineness.
- Can the Noetherian hypothesis be weakened?
- What fails without quasicompactness?
---

::: {.theorem}
Let $X$ be a Noetherian scheme.
The following are equivalent:

- $X$ is affine;

- $H^p(X, \mcf) = 0$ for all quasicoherent $\mcf$ and all $p > 0$;

- $H^1(X, \mci) = 0$ for every coherent sheaf of ideals $\mci$.
:::

::: {.remark title="How the proof goes"}
The implications down the list are the content of affine vanishing and a triviality.
Back up: it is enough to produce $f_1,\ldots,f_r \in A = \OO_X(X)$ generating the unit ideal with each $X_{f_i}$ affine, since then $X \to \Spec A$ is an isomorphism.

For a closed point $p$, let $U$ be an affine neighbourhood and $Z = X \sm U$.
The ideal sequence
\[
0 \to \mci_{Z \union \ts{p}} \to \mci_Z \to k(p) \to 0
\]
has $H^1$ of the left term zero by hypothesis, so some $f \in \mci_Z(X)$ is nonzero at $p$.
Then $X_f = U_f$ is affine and contains $p$.
Quasicompactness extracts a finite subcover, and those $f$ generate the unit ideal because they have no common zero.
:::

::: {.remark title="The two follow-ups"}
*Weakening Noetherian.* The criterion holds for quasicompact quasi-separated schemes, with $\mci$ ranging over quasicoherent ideals rather than coherent ones.
Noetherian is used only to have coherent ideals available and to extract finite subcovers, and both can be arranged directly.

*Dropping quasicompactness.* The conclusion fails.
An infinite disjoint union of affine schemes has vanishing higher cohomology for every quasicoherent sheaf, being a disjoint union of affines, but it is not affine: its ring of global sections is an infinite product, and the comparison map is not an isomorphism.
The finite subcover in the proof is where quasicompactness enters, and without it the $f_i$ need not be finite in number.
:::
