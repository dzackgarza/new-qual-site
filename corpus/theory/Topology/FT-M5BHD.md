---
schema: qual/card@1
id: FT-M5BHD
kind: theorem
title: A continuous bijection from a compact space to a Hausdorff space is a homeomorphism
prompts:
- When is a continuous bijection from a compact space to a Hausdorff space a homeomorphism?
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
---

::: {.theorem}
Let $f\colon X\to Y$ be a continuous bijection.
If $X$ is compact and $Y$ is [[D-ZFRV4|Hausdorff]], then $f$ is a homeomorphism [@Mun00, Theorem 26.6].
:::

::: {.remark}
The theorem rests on three facts: closed subspaces of compact spaces are compact [@Mun00, Theorem 26.2], continuous images of compact spaces are compact [@Mun00, Theorem 26.5], and compact subspaces of Hausdorff spaces are closed [@Mun00, Theorem 26.3].
Together they show that $f$ is a closed map.
:::
