---
schema: qual/card@1
id: FF-W4FFF
kind: fact
title: Cross-ratio map
prompts:
- What is the cross-ratio map, and where does it send $z_2, z_3, z_4$?
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.fact}
Let $z_2,z_3,z_4\in\CC$ be distinct.
The cross-ratio map is the [[D-FRVBV|Möbius transformation]]
$$
R(z) \coloneqq (z, z_2, z_3, z_4) \coloneqq {z - z_3\over z-z_4}\cdot{z_2 - z_4 \over z_2 - z_3}.
$$
It satisfies $R(z_2)=1$, $R(z_3)=0$, and $R(z_4)=\infty$.
:::
