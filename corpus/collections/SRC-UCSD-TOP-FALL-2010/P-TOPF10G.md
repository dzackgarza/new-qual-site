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
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The computation is correct. The two sphere summands are simply connected, so
    the fundamental group of the wedge is that of the projective plane, of order
    two, and the universal cover is the double cover of that summand, a sphere,
    with two copies of each of the two lifted sphere summands attached at the two
    lifts of the wedge point; the resulting space is homotopy equivalent to a wedge
    of five spheres, with second homology of rank five. That cover is simply
    connected, so Hurewicz identifies its second homotopy group with its second
    homology, and covering maps induce isomorphisms on homotopy above degree one.
    Nothing was changed.
---

::: {.problem}
Use the Hurewicz theorem to calculate $\pi_2$ of the space $\RP^2 \vee S^2 \vee S^2$ (that is, the one-point union of a projective plane and two spheres).
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
X=\RP^2\vee S^2\vee S^2.
$$
Then $\pi_1(X)\cong\ZZ/2$.

::: pf-proof

The two sphere summands are simply connected.

:::

:::

::: pf-step

The universal cover is obtained from $S^2\to\RP^2$ by attaching two copies of each $S^2$ wedge summand, one at each lift of the wedge point. Hence
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
H_2(\widetilde X;\ZZ)\cong\ZZ^5.
$$

::: pf-proof

This is the homology of a wedge of five $2$-spheres.

:::

:::

::: pf-step

By the Hurewicz theorem,
$$
\pi_2(\widetilde X)\cong H_2(\widetilde X)\cong\ZZ^5.
$$

::: pf-proof

For a simply connected space, the degree-$2$ Hurewicz map is an isomorphism.

:::

:::

::: pf-step

Therefore
$$
\boxed{\pi_2(\RP^2\vee S^2\vee S^2)\cong\ZZ^5.}
$$

::: pf-proof

The universal covering map induces an isomorphism on $\pi_2$.

:::

:::

:::

:::
