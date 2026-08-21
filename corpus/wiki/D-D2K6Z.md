---
schema: qual/card@1
id: D-D2K6Z
kind: definition
title: Coboundary
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homological Algebra
relations: []
review: draft
---

::: {.definition title="Coboundary"}
Dualizing a chain complex by $C^n(X; G) \da \Hom(C_n(X), G)$ gives the coboundary $\delta^n: C^n \to C^{n+1}$ defined by $\delta \psi \da \psi \circ \del$.
A **coboundary** is an element of $B^n(X; G)\da \im \delta^{n-1}$, and $\delta\circ\delta = 0$ since $\del\circ\del = 0$.
:::

::: {.concept}
See Hatcher, §3.1, p. 198.
:::
