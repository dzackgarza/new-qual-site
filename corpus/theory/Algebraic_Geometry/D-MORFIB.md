---
schema: qual/card@1
id: D-MORFIB
kind: definition
title: The fibre of a morphism as a base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibres
  - Fibre Products
  - Residue Fields
relations:
- kind: related-to
  target: D-VKR54
review: draft
prompts:
- What is the fibre of a morphism of schemes?
- Why is the fibre taken over the residue field rather than the point?
---

::: {.definition title="Fibre"}
For $f : X \to Y$ and $y \in Y$ with residue field $\kappa(y) = \OO_{Y,y}/\mfm_y$, the **fibre** is
\[
X_y \da \fiberprod{X}{Y}{\Spec \kappa(y)} .
\]
:::

::: {.remark}
The definition is a base change and not a preimage, and that is the point: $f^{-1}(y)$ is only a set, while $X_y$ is a scheme over a field, so it has a dimension, a length, a genus, and a cohomology.
Taking $\kappa(y)$ rather than $\OO_{Y,y}$ is what makes it a scheme over a field; taking $\OO_{Y,y}$ instead gives the local picture of the family near $y$, which is the other useful base change.

The underlying space of $X_y$ is homeomorphic to $f^{-1}(y)$, so nothing is lost and the scheme structure is gained.
That structure is where the exam questions live: the fibres of $\Spec \ZZ[i] \to \Spec \ZZ$ are two points, one point, or a fat point according as $p$ splits, is inert, or ramifies, and the length of the fibre is $2$ in every case.
That constancy is flatness, and it is the model for every statement that a numerical invariant is constant in a flat family.
:::
