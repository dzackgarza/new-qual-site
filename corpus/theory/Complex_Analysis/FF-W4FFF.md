---
schema: qual/card@1
id: FF-W4FFF
kind: fact
title: Cross-ratio map
slogan: 'The cross-ratio normalizes three marked points to $1$, $0$, and $\infty$.'
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

This is the cross ratio of [@Ahl73, ch. 3, §3.2, The Cross Ratio], where $(z_1,z_2,z_3,z_4)$ is defined as $(z_1-z_3)(z_2-z_4)/\bigl((z_1-z_4)(z_2-z_3)\bigr)$ and Theorem 12 of that section states its invariance under linear transformations.
:::
