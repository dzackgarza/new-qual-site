---
schema: qual/card@1
id: D-COHRIF
kind: definition
title: Higher direct images
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Cohomology
  - Morphisms
relations:
- kind: uses
  target: D-COHDER
review: draft
prompts:
- What is the higher direct image?
- Compute $R^i f_* \mcf$ for $f$ an affine morphism.
---

::: {.definition}
For $f: X \to Y$, the functor $f_*$ is left exact; set $R^i f_* \mcf \da R^i(f_*)(\mcf)$.
Equivalently, $R^i f_* \mcf$ is the sheafification of
\[
V \mapsto H^i\qty{f\inv(V), \restrictionof{\mcf}{f\inv(V)}} .
\]
:::

::: {.remark}
Read it as the cohomology of $\mcf$ along the fibres of $f$: a sheaf on the base recording how the cohomology of the fibres varies.
Two computations pin it down.

If $Y = \Spec A$ is affine, then $R^i f_* \mcf = \widetilde{H^i(X,\mcf)}$, so nothing new appears over an affine base.
If $f$ is an affine morphism and $\mcf$ is quasicoherent, then $R^{i>0} f_* \mcf = 0$ and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$; a closed immersion is the case used constantly, which is why cohomology can be computed after pushing a sheaf forward from a projective subscheme to the ambient $\PP^n$.

For $f$ projective and $\mcf$ coherent, $R^i f_* \mcf$ is coherent, which is the relative form of Serre finiteness.
:::
