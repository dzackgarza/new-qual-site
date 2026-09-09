---
schema: qual/card@1
id: P-UCTOP-SU07-6
kind: problem
title: π_3(RP^3 ∨ S^3) via Hurewicz
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Use the Hurewicz theorem to calculate $\pi_3(\mathbb{RP}^3 \vee S^3)$.

::: {.solution}
<1>1. The universal cover of
$$
X=\mathbb{RP}^3\vee S^3
$$
is obtained from the universal cover $S^3\to\mathbb{RP}^3$ by attaching one copy of $S^3$ at each of the two lifts of the wedge point.
::: {.proof}
The fundamental group of $X$ is $\mathbb Z/2$, contributed by the $\mathbb{RP}^3$ summand, since $S^3$ is simply connected. Pulling the simply connected wedge summand up to the universal cover attaches a copy at each point of the fiber over the wedge point, which has two elements.
:::

<1>2. Thus the universal cover $\widetilde X$ is homotopy equivalent to
$$
S^3\vee S^3\vee S^3.
$$
:::
::: {.proof}
The underlying lifted $\mathbb{RP}^3$ is $S^3$, with two further $S^3$'s attached at two points. Move one attachment point to the other along an arc in the first $S^3$; contracting that arc gives the stated wedge up to homotopy.
:::

<1>3. The space $\widetilde X$ is $2$-connected and
$$
H_3(\widetilde X;\mathbb Z)\cong\mathbb Z^3.
$$
:::
::: {.proof}
A wedge of three $3$-spheres is simply connected and has no homology in degrees $1,2$. Its third homology is the direct sum of the three fundamental classes.
:::

<1>4. By Hurewicz,
$$
\pi_3(\widetilde X)\cong H_3(\widetilde X)\cong\mathbb Z^3.
$$
:::
::: {.proof}
Since $\widetilde X$ is $2$-connected, the degree-$3$ Hurewicz homomorphism is an isomorphism.
:::

<1>5. Therefore
$$
\boxed{\pi_3(\mathbb{RP}^3\vee S^3)\cong\mathbb Z^3}.
$$
:::
::: {.proof}
A covering map induces isomorphisms on all homotopy groups in degrees at least $2$, so $\pi_3(X)\cong\pi_3(\widetilde X)$.
:::
:::

