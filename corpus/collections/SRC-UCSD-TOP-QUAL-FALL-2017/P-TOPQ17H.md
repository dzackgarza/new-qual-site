---
schema: qual/card@1
id: P-TOPQ17H
kind: problem
title: '$\pi_3(P\vee S^3)$ for the Poincaré homology sphere $P$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Universal Cover
  - Homology Spheres
relations: []
review: draft
---

::: problem
Let $P$ be the Poincaré homology sphere, a $3$-manifold whose fundamental group has order $120$ and whose universal cover is $S^3$.
Compute $\pi_3$ of the one-point union $P \vee S^3$.
:::

::: {.solution}
<1>1. Set
$$
X=P\vee S^3.
$$
Then $\pi_1(X)=\pi_1(P)$ has order $120$.
::: {.proof}
The sphere summand is simply connected.
:::

<1>2. The universal cover $\widetilde X$ is obtained from the universal cover $S^3\to P$ by attaching one copy of $S^3$ at each of the $120$ lifts of the wedge point.
::: {.proof}
The fiber of the universal cover over the wedge point has cardinality equal to the order of the deck group, namely $120$. The simply connected wedge summand lifts independently at every point of this fiber.
:::

<1>3. Therefore
$$
\widetilde X\simeq\bigvee^{121}S^3.
$$
::: {.proof}
There is the original covering $S^3$ plus $120$ attached $S^3$ summands. Moving their attachment points together along a tree in the original $S^3$ and collapsing that tree gives the wedge up to homotopy.
:::

<1>4. The universal cover is $2$-connected and
$$
H_3(\widetilde X;\mathbb Z)\cong\mathbb Z^{121}.
$$
::: {.proof}
A wedge of $121$ copies of $S^3$ has these properties.
:::

<1>5. By Hurewicz and covering-space invariance of higher homotopy groups,
$$
\boxed{\pi_3(P\vee S^3)\cong\mathbb Z^{121}.}
$$
::: {.proof}
Hurewicz gives $\pi_3(\widetilde X)\cong H_3(\widetilde X)$, and the universal covering map induces an isomorphism on $\pi_3$.
:::
:::
