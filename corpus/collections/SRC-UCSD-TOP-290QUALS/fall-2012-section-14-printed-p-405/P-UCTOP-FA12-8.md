---
schema: qual/card@1
id: P-UCTOP-FA12-8
kind: problem
title: π_2 of p-fold cover of S^3 wedge S^2
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Let $L$ be a space which is $p$-fold covered by $S^3$, for some $p \geq 1$.
Compute the second homotopy group of the one-point union $\pi_2(L \vee S^2)$.
:::

::: {.solution}

::: pf

::: {.pf-step #universal-cover-order-p}
Since $S^3$ is simply connected, the given $p$-fold covering $S^3\to L$ is the universal cover and
$$
|\pi_1(L)|=p.
$$

::: pf-proof
The number of sheets of a connected universal covering equals the order of the fundamental group when that order is finite.
:::

:::

::: pf-step
The universal cover of $L\vee S^2$ is obtained from $S^3$ by attaching one copy of $S^2$ at each of the $p$ lifts of the wedge point.

::: pf-proof
The $S^2$ summand is simply connected, so it lifts independently at every point of the fiber over the wedge point of $L$. That fiber has $p$ points by step [](#universal-cover-order-p){.pf-ref}.
:::

:::

::: pf-step
This universal cover is homotopy equivalent to
$$
S^3\vee\bigvee_{j=1}^{p}S^2.
$$

::: pf-proof
Join the $p$ attachment points by a tree in the underlying $S^3$ and contract the tree. This moves all sphere attachments to one wedge point without changing homotopy type.
:::

:::

::: pf-step
Therefore
$$
H_2(\widetilde{L\vee S^2};\mathbb Z)\cong\mathbb Z^p.
$$

::: pf-proof
Only the $p$ copies of $S^2$ contribute to degree-$2$ homology.
:::

:::

::: pf-step
Since the universal cover is simply connected, Hurewicz gives
$$
\pi_2(\widetilde{L\vee S^2})\cong\mathbb Z^p.
$$

::: pf-proof
For a simply connected space, the Hurewicz homomorphism $\pi_2\to H_2$ is an isomorphism.
:::

:::

::: pf-step
Hence
$$
\boxed{\pi_2(L\vee S^2)\cong\mathbb Z^p}.
$$

::: pf-proof
Covering maps induce isomorphisms on homotopy groups in degrees at least $2$.
:::

:::

:::

:::
