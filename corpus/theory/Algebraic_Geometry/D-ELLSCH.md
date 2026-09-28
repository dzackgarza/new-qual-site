---
schema: qual/card@1
id: D-ELLSCH
kind: definition
title: Elliptic curves over a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Families
  - Moduli
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- What is an elliptic curve over a scheme?
---

::: {.definition}
An \dfn{elliptic curve over a scheme} $S$ is a proper smooth morphism $p \colon E \to S$ with a section $e \colon S \to E$ whose geometric fibres are connected curves of genus $1$.
:::

::: {.proposition}
Locally on $S$, an elliptic curve is a Weierstrass cubic: every point of $S$ has an affine neighbourhood $\Spec A$ over which $E$ is the closed subscheme of $\PP^2_A$ cut out by
\[
y^2 z + a_1 xyz + a_3 y z^2 = x^3 + a_2 x^2 z + a_4 x z^2 + a_6 z^3
\]
with discriminant $\Delta \in A^\times$, and $e$ is the point $[0:1:0]$.
The fibres are elliptic curves over the residue fields, and the group laws on the fibres come from a morphism $E \times_S E \to E$ making $E$ a commutative group scheme over $S$.
:::

::: {.example}
Over $S = \Spec \ZZ[1/6][a, b][\Delta^{-1}]$ with $\Delta = -16(4a^3 + 27b^2)$, the curve $y^2 z = x^3 + a x z^2 + b z^3$ is an elliptic curve; its fibre over a point of $S$ is the Weierstrass curve with the images of $a$ and $b$.
Over $\Spec \ZZ$, the equation $y^2 z = x^3 - x z^2$ has discriminant $64$, so it defines an elliptic curve over $\Spec \ZZ[1/2]$ but not over $\Spec \ZZ$.
:::
