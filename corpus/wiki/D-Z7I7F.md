---
schema: qual/card@1
id: D-Z7I7F
kind: definition
title: Homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition title="Homotopic"}
Two maps $f, g: X\to Y$ are **homotopic**, written $f\homotopic g$, iff there is a continuous $H: X\cross I \to Y$ with $H(\wait, 0) = f$ and $H(\wait, 1) = g$.
Two paths $\gamma, \eta$ with the same endpoints are **homotopic rel endpoints** iff the homotopy additionally fixes them, $H(0,t) = \gamma(0)$ and $H(1,t) = \gamma(1)$ for all $t$.
Homotopy is an equivalence relation, and it is this rel-endpoints version that $\pi_1$ quotients by.
:::

::: {.concept}
See Hatcher, pp. 3 and 25; Munkres, §51.
:::
