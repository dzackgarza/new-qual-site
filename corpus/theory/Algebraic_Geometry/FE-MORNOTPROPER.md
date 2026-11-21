---
schema: qual/card@1
id: FE-MORNOTPROPER
kind: example
title: The affine line is of finite type and not proper
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Separated Morphisms
  - Counterexamples
relations:
- kind: uses
  target: D-8XX95
review: draft
prompts:
- Give a morphism of finite type that is not proper.
- Why is $\AA^1_k\to\Spec k$ not proper?
---

::: {.example}
Let $k$ be a field and let $X=\AA^1_k$ with its structure morphism $f\colon X\to\Spec k$.
Then $f$ is separated and of finite type, and it is not proper: after the base change $X\times_k X=\AA^2_k\to\AA^1_k$, the projection is not a closed map, since the hyperbola $xy=1$ is closed in $\AA^2_k$ and its image is $\AA^1_k\sm\theset{0}$ [@Har77, Example II.4.6.1] ([[D-8XX95]]).
:::
