---
schema: qual/card@1
id: D-SCHSUB
kind: definition
title: Open and closed subschemes, and closed immersions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Closed Immersions
  - Ideal Sheaves
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- What is an open subscheme? A closed subscheme?
- What do closed subschemes of an affine scheme correspond to?
---

::: {.definition}
An \dfn{open subscheme} of $X$ is an open $U \subseteq \abs{X}$ with $\OO_U \da \ro{\OO_X}{U}$; every open subset of a scheme is a scheme in exactly one way.

A **closed immersion** $i: Z \to X$ is a morphism which is a homeomorphism onto a closed subset and for which $i^\sharp: \OO_X \to i_* \OO_Z$ is surjective.
A **closed subscheme** is an equivalence class of closed immersions into $X$.
:::

::: {.proposition}
Closed subschemes of $\Spec A$ correspond exactly to ideals $\mfa \normal A$, via $Z = \Spec(A/\mfa)$.
In general, closed subschemes of $X$ correspond to quasicoherent ideal sheaves $\mci \subseteq \OO_X$, with $\OO_Z = \OO_X/\mci$.
:::

::: {.remark}
The asymmetry is the content: an open subset carries a *unique* scheme structure, and a closed subset carries *many*. $V(x)$ and $V(x^2)$ in $\AA^1$ are the same closed set and different closed subschemes, and the distinction is the whole reason the definition is phrased with an ideal sheaf rather than a subset.

The follow-up is why surjectivity is demanded on sheaves rather than on sections: it is a condition on stalks, and $\OO_X(X) \to \OO_Z(Z)$ can fail to be surjective even for a closed immersion once $X$ is not affine.

Neither notion is closed under the other's operation: a closed subscheme of an open subscheme is a **locally closed subscheme**, which is what "immersion" without a qualifier means.
:::
