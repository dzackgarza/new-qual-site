---
schema: qual/card@1
id: D-MORNORMREG
kind: definition
title: Normal and regular morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Smooth Morphisms
  - Normal Schemes
relations:
- kind: uses
  target: D-DEFFLAT
- kind: related-to
  target: D-MORSM
review: draft
prompts:
- What is a normal morphism?
- What is a regular morphism?
---

::: {.definition}
A morphism of locally Noetherian schemes $f \colon X \to Y$ is \dfn{normal}, respectively \dfn{regular}, if it is flat and for every $y \in Y$ the fibre $X_y$ is geometrically normal, respectively geometrically regular, over $\kappa(y)$: $X_y \times_{\kappa(y)} \Spec L$ is normal, respectively regular, for every finite field extension $L/\kappa(y)$.
A ring map $A \to B$ of Noetherian rings is normal or regular when $\Spec B \to \Spec A$ is.
:::

::: {.proposition}
1. A morphism locally of finite type is regular exactly when it is smooth.
2. If $f \colon X \to Y$ is flat, $Y$ is regular (respectively normal) and the fibres of $f$ are regular (respectively normal), then $X$ is regular (respectively normal).
3. For a Noetherian local ring $A$, the completion map $A \to \hat{A}$ is regular exactly when $A$ has geometrically regular formal fibres; this holds for every local ring essentially of finite type over a field, and it is part of the definition of an excellent ring.
:::

::: {.example}
In characteristic $p$, the Frobenius $\Spec \FF_p(t^{1/p}) \to \Spec \FF_p(t)$ is flat and its only fibre is a field, but the fibre is not geometrically reduced: after base change to $\FF_p(t^{1/p})$ it becomes $\FF_p(t^{1/p})[x]/(x - t^{1/p})^p$.
So this map is not regular, although both schemes are regular.
:::
