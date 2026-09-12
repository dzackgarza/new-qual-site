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
The fibre $X_y$ is a scheme over $\kappa(y)$. Its scheme structure supports invariants such as dimension and, under the relevant finiteness hypotheses, length, genus, and cohomology.
Base change to $\Spec\OO_{Y,y}$ instead retains the part of the family over the generalisations of $y$.

The underlying space of $X_y$ is homeomorphic to $f^{-1}(y)$.
The fibres of $\Spec \ZZ[i] \to \Spec \ZZ$ over closed points are two points, one point, or a nonreduced point according as $p$ splits, is inert, or ramifies. In each case the coordinate algebra has dimension $2$ over $\FF_p$.
This morphism is finite flat of rank $2$, since $\ZZ[i]$ is free of rank $2$ over $\ZZ$.
:::
