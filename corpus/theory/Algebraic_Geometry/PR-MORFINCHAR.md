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
A morphism of locally Noetherian schemes is **finite** exactly when it is **proper** and **quasi-finite**, equivalently proper with finite fibres.
Without Noetherian hypotheses the correct statement is: finite exactly when proper, locally of finite presentation, and with finite fibres.
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
