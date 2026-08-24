---
schema: qual/card@1
id: E-PYJZO
kind: exercise
title: Standard sector
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise title="Standard sector"}
Find a conformal map from the sector $\ts{\Arg(z) \in (0, \alpha)} \to \DD$.
:::

::: {.solution}
The picture:

![](../../assets/30_Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_22-13-13.png)

In steps:

- Map the sector to $\HH$ using $z\mapsto z^{\pi/\alpha}$, choosing a branch cut for $\Log$ along $\RR_{\leq 0}$.

- Map $\HH\to \DD$ using the standard $z\mapsto {z-i\over z+i}$.
:::
