---
schema: qual/card@1
id: P-TOPF10G
kind: problem
title: '$\pi_2(\RP^2\vee S^2\vee S^2)$ via the Hurewicz theorem'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Hurewicz Theorem
  - Projective Spaces
  - Spheres
relations: []
review: draft
---

::: {.problem}
Use the Hurewicz theorem to calculate $\pi_2$ of the space $\mathbb{RP}^2 \vee S^2 \vee S^2$ (that is, the one-point union of a projective plane and two spheres).
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
X=\mathbb{RP}^2\vee S^2\vee S^2.
$$
Then $\pi_1(X)\cong\mathbb Z/2$.

::: pf-proof

The two sphere summands are simply connected.

:::

:::

::: pf-step

The universal cover is obtained from $S^2\to\mathbb{RP}^2$ by attaching two copies of each $S^2$ wedge summand, one at each lift of the wedge point. Hence
$$
\widetilde X\simeq\bigvee^5 S^2.
$$

::: pf-proof

There is the covering sphere itself plus four lifted wedge spheres. Moving the attachment points together along an arc and collapsing the arc gives a wedge of five spheres up to homotopy.

:::

:::

::: pf-step

The universal cover is simply connected and
$$
H_2(\widetilde X;\mathbb Z)\cong\mathbb Z^5.
$$

::: pf-proof

This is the homology of a wedge of five $2$-spheres.

:::

:::

::: pf-step

By the Hurewicz theorem,
$$
\pi_2(\widetilde X)\cong H_2(\widetilde X)\cong\mathbb Z^5.
$$

::: pf-proof

For a simply connected space, the degree-$2$ Hurewicz map is an isomorphism.

:::

:::

::: pf-step

Therefore
$$
\boxed{\pi_2(\mathbb{RP}^2\vee S^2\vee S^2)\cong\mathbb Z^5.}
$$

::: pf-proof

The universal covering map induces an isomorphism on $\pi_2$.

:::

:::

:::

:::
