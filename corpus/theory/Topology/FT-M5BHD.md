---
schema: qual/card@1
id: FT-M5BHD
kind: theorem
title: A continuous bijection from a compact space to a Hausdorff space is a homeomorphism
slogan: 'Compact-to-Hausdorff continuous bijections are homeomorphisms.'
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
If $X$ is compact and $Y$ is [[D-ZFRV4|Hausdorff]], then $f$ is a homeomorphism [@Mun00].
:::

::: {.remark}
Closed subspaces of compact spaces are compact, continuous images of compact spaces are compact, and compact subspaces of Hausdorff spaces are closed [@Mun00].
Hence $f$ is a closed map, so $\inverseof{f}$ is continuous.
:::
