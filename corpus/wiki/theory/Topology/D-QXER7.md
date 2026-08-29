---
schema: qual/card@1
id: D-QXER7
kind: definition
title: Limit
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
For a diagram $F: J \to \mathcal C$, a **limit** is an object $L$ together with maps $\pi_j : L \to F(j)$ commuting with the diagram, universal with that property: any other such cone $\ts{\psi_j: Y\to F(j)}$ factors through a unique $Y\to L$.
Products, pullbacks, and inverse limits are limits; the dual notion, reversing all arrows, is a colimit.
:::

::: {.concept}
See Weibel, *An Introduction to Homological Algebra*, Variation 2.6.9, which defines the limit as the colimit of the opposite diagram and records that it is right adjoint to the diagonal functor, hence left exact.
The dual construction is the colimit, 2.6.7 there.
:::
