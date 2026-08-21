---
schema: qual/card@1
id: D-TPTOG
kind: definition
title: Mapping Path Space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Function Spaces
relations: []
review: draft
---

::: {.definition title="Mapping Path Space"}
For a map $f: X\to Y$, the **mapping path space** is
\[
E_f \da \ts{ (x, \gamma) \in X \cross Y^I \st \gamma(0) = f(x) }
.\]
The inclusion $X \injects E_f$, $x\mapsto (x, \const_{f(x)})$, is a deformation retract, and $E_f \to Y$, $(x,\gamma)\mapsto \gamma(1)$, is a fibration, so every map factors as a homotopy equivalence followed by a fibration.
It is dual to the mapping cylinder in the sense of Eckmann-Hilton.
:::

::: {.concept}
See Hatcher, §4.3, p. 407.
:::
