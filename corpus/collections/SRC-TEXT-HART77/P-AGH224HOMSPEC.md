---
schema: qual/card@1
id: P-AGH224HOMSPEC
kind: problem
title: Morphisms to an affine scheme are ring maps into global sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Adjoint Functors
  - Global Sections
relations: []
review: draft
---

::: {.problem}
Let $A$ be a ring and let $(X, \OO_X)$ be a scheme.
Given a morphism $f: X \to \Spec A$, we have an associated map on sheaves $f^{\sharp}: \OO_{\Spec A} \to f_* \OO_X$.
Taking global sections we obtain a homomorphism $A \to \Gamma(X, \OO_X)$.
Thus there is a natural map
\[
\alpha: \Hom_{\Sch}(X, \Spec A) \to \Hom_{\Ring}\qty{A, \Gamma(X, \OO_X)}.
\]
Show that $\alpha$ is bijective.
:::
