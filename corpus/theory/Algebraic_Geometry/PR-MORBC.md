---
schema: qual/card@1
id: PR-MORBC
kind: proposition
title: Which properties are stable under base change and composition
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Fibre Products
  - Morphisms
relations:
- kind: uses
  target: D-MORFIB
review: draft
prompts:
- Name some properties of morphisms preserved by base change.
- Is properness stable under base change?
---

::: {.proposition}
The following are stable under arbitrary base change and under composition: open and closed immersions, affine, finite, integral, quasicompact, locally of finite type, of finite type, quasi-finite, flat, surjective, separated, proper, projective, smooth, unramified, étale.
:::

::: {.remark}
The list is not worth memorising as a list; what is worth having is the reason it is so long.
A property defined by a condition on the ring maps in an affine cover is stable under base change whenever the corresponding module-theoretic condition survives $\wait \tensor_B B'$, and finite generation, flatness, and surjectivity all do.

The instructive entries are the ones that are *not* on it.
Being an isomorphism onto the image, being a closed map, and being dominant are not stable, and universal closedness is defined by forcing the issue: it is exactly "closed after every base change", which is why the definition of proper contains the word universally.
$\AA^1_k \to \Spec k$ is closed and not universally closed, and the witness is again the hyperbola in $\fiberprod{\AA^1}{k}{\AA^1}$.

Stability under base change is what makes a property a statement about fibres, and that is its real use: a proper morphism has proper fibres, a flat morphism has flat base changes, and a smooth morphism stays smooth after any extension of the base field.
:::
