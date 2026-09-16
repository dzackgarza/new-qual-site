---
schema: qual/card@1
id: PR-MORFINCHAR
kind: proposition
title: Finite equals proper plus quasi-finite
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Proper Morphisms
  - Quasi-finite Morphisms
relations:
- kind: uses
  target: D-MORFIN
- kind: uses
  target: D-8XX95
review: draft
prompts:
- Give a criterion for a morphism to be finite.
- How are finite, proper, and projective related?
---

::: {.proposition}
Let $\pi \colon X \to Y$ be a morphism of schemes.

1. $\pi$ is finite if and only if it is integral and locally of finite type.

2. If $\pi$ is finite, then it is quasi-finite: every fibre is a finite discrete set [@Har10a, Exercise II.3.5].

3. If $\pi$ is finite, then $X \cong \operatorname{\mathbf{Proj}}_Y \mathcal{S}$ over $Y$ for a quasicoherent graded $\OO_Y$-algebra $\mathcal{S}$ generated in degree $1$ by the finite type module $\mathcal{S}_1$; in particular $\pi$ is projective in the sense of [[D-SCHRELSPECPROJ]], and proper.

4. A morphism of locally Noetherian schemes is finite exactly when it is proper and quasi-finite, equivalently proper with finite fibres [@Har10a, Exercise III.11.2].
Without Noetherian hypotheses: finite exactly when proper, locally of finite presentation, and with finite fibres.
:::

::: {.remark}
This is the characterisation to quote, because it converts a condition on modules into two conditions one can see.
The implications to keep straight run
\[
\text{finite} \implies \text{projective} \implies \text{proper} \implies \text{universally closed},
\]
with none of them reversible: $\PP^1_k \to \Spec k$ is projective and not finite, and the standard non-projective proper example is a complete non-projective threefold, which is worth naming but not constructing.

The converse direction, proper plus finite fibres giving finite, is the one that does real work: it is how one knows the normalisation of a variety is a finite morphism, and how a proper morphism with zero-dimensional fibres is recognised as an affine one.
:::
