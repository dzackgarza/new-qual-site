---
schema: qual/card@1
id: P-CEVX4
kind: problem
title: $\pi_1(S^1 \times S^1)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Product Topology
relations: []
review: draft
---

::: problem
- Compute $\pi_1(S^1 \cross S^1)$
:::

::: {.solution}
<1>1. For path-connected spaces, fundamental groups commute with products:
$$\pi_1(X\times Y,(x_0,y_0))\cong\pi_1(X,x_0)\times\pi_1(Y,y_0).$$
::: {.proof}
A loop in a product is exactly a pair of loops, and homotopies are likewise coordinatewise.
:::

<1>2. Since $\pi_1(S^1)\cong\mathbb Z$,
$$\boxed{\pi_1(S^1\times S^1)\cong\mathbb Z\times\mathbb Z.}$$
::: {.proof}
Apply <1>1 to the two circle factors.
:::
:::
