---
schema: qual/card@1
id: P-UCTOP-FA11-6
kind: problem
title: π_3 of Poincare homology sphere wedge S^3
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

Let $P$ be the Poincaré homology sphere, a 3-manifold whose fundamental group has order 120 and whose universal cover is $S^3$.
Compute $\pi_3$ of the one-point union $P \vee S^3$.

::: {.solution}
<1>1. The universal cover of $P\vee S^3$ is obtained from the universal cover $S^3\to P$ by attaching one copy of $S^3$ at each lift of the wedge point.
::: {.proof}
The $S^3$ summand is simply connected. The fiber over the wedge point in the universal cover of $P$ has cardinality $|\pi_1(P)|=120$, so the lifted wedge summand contributes $120$ attached copies of $S^3$.
:::

<1>2. Hence the universal cover is homotopy equivalent to a wedge of $121$ copies of $S^3$.
::: {.proof}
There is one underlying $S^3$ from the universal cover of $P$ and $120$ additional $S^3$ summands attached at distinct points. Connect all attachment points to one chosen point by a tree in the underlying $S^3$ and contract that tree; this produces the wedge up to homotopy.
:::

<1>3. Therefore its third homology is
$$
H_3(\widetilde{P\vee S^3};\mathbb Z)\cong\mathbb Z^{121}.
$$
::: {.proof}
Reduced homology of a finite wedge is the direct sum of the reduced homology groups of the summands.
:::

<1>4. The universal cover is $2$-connected, so Hurewicz gives
$$
\pi_3(\widetilde{P\vee S^3})\cong\mathbb Z^{121}.
$$
::: {.proof}
A wedge of $3$-spheres is $2$-connected. Apply the Hurewicz theorem in degree $3$.
:::

<1>5. Consequently
$$
\boxed{\pi_3(P\vee S^3)\cong\mathbb Z^{121}}.
$$
::: {.proof}
Covering maps induce isomorphisms on homotopy groups in degrees at least $2$.
:::
:::
