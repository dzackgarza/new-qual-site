---
schema: qual/card@1
id: D-RMQ7W
kind: definition
title: "Mapping Cylinder"
classification:
  areas:
  - topology
  topics:
  - homotopy
  - retracts
  - cell-complexes
relations: []
review: draft
---

::: {.definition title="Mapping Cylinder"}
For a map $f: X\to Y$, the **mapping cylinder** is
\[
M_f \da \qty{ (X\cross I) \disjoint Y } / \qty{ (x, 1) \sim f(x) }
.\]
It deformation retracts onto $Y$ by sliding along the segments $\ts{x}\cross I$, so $f$ factors as an inclusion followed by a homotopy equivalence,
\[
X \injects M_f \mapsvia{\homotopic} Y
.\]
:::

::: {.concept}
See Hatcher, p. 2.
:::
