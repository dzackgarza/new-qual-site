---
schema: qual/card@1
id: P-FHLRF
kind: problem
title: $\pi_1(S^1\vee S^1)$ and $\pi_1(S^1\times S^1)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Product Topology
relations: []
review: draft
---

::: problem
- Compute $\pi_1(S^1 \vee S^1)$

- Compute $\pi_1(S^1 \cross S^1)$
:::

::: {.solution}
<1>1. The figure-eight satisfies
$$\boxed{\pi_1(S^1\vee S^1)\cong F_2.}$$
::: {.proof}
Apply van Kampen to neighborhoods of the two circle summands whose intersection is contractible. The result is the free product $\mathbb Z*\mathbb Z$.
:::

<1>2. The torus satisfies
$$\boxed{\pi_1(S^1\times S^1)\cong\mathbb Z^2.}$$
::: {.proof}
Fundamental groups commute with products, so $\pi_1(S^1\times S^1)\cong\pi_1(S^1)\times\pi_1(S^1)\cong\mathbb Z^2$.
:::
:::
