---
schema: qual/card@1
id: FD-COPFN
kind: definition
title: Deformation Retract
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations:
- kind: variant-of
  target: FD-BDEI2
review: draft
---

::: {.definition}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a morphism $F:X\cross I$ to $X$ such that $F(x, 0) = x, F(x, 1)\in A, F(a, 1) = a$.
Equivalently it is a homotopy between a retraction and the identity.
:::
