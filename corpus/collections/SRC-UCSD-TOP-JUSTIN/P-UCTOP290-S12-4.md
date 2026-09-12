---
schema: qual/card@1
id: P-UCTOP290-S12-4
kind: problem
title: "The torus and the wedge S^1 vee S^1 vee S^2 are not homotopy-equivalent"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
  - Homotopy Equivalence
relations: []
review: draft
---

::: problem
Show that $S^1 \times S^1$ and $S^1 \vee S^1 \vee S^2$ are not homotopy-equivalent.
:::

::: {.solution}
<1>1. The torus has degree-one classes $\alpha,\beta\in H^1(T^2;\mathbb Z)$ with
$$
\alpha\smile\beta
$$
a generator of $H^2(T^2;\mathbb Z)\cong\mathbb Z$.
::: {.proof}
Take $\alpha,\beta$ Poincaré dual to the two standard circle factors. Their representing cycles intersect transversely once, so their cup product evaluates to $1$ on the fundamental class.
:::

<1>2. In
$$
Y=S^1\vee S^1\vee S^2,
$$
the cup product of any two degree-one classes is zero.
::: {.proof}
Every degree-one class is supported on the two $S^1$ wedge summands. Products between classes from different wedge summands vanish, and each individual $S^1$ has no degree-two cohomology. Hence all products in $H^1(Y)\otimes H^1(Y)\to H^2(Y)$ are zero.
:::

<1>3. Therefore $T^2$ and $S^1\vee S^1\vee S^2$ are not homotopy-equivalent.
::: {.proof}
A homotopy equivalence induces an isomorphism of graded cohomology rings. The nonzero product in <1>1 cannot correspond under any ring isomorphism to the identically zero degree-one product in <1>2.
:::
:::
