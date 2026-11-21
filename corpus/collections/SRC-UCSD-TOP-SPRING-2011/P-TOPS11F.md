---
schema: qual/card@1
id: P-TOPS11F
kind: problem
title: '$\pi_3(P\vee S^3)$ for a spherical $3$-manifold with $\cardinality{\pi_1(P)}=120$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Universal Cover
  - Manifolds
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. pi_1(P v S^3) = pi_1(P) has order 120, so the universal cover is
    120-sheeted; over P it is the given S^3, and the sphere summand is simply connected so it lifts as
    a copy at each of the 120 points of the fibre. The cover is therefore homotopy equivalent to a
    wedge of 121 three-spheres, which is 2-connected with pi_3 = H_3 = Z^121 by Hurewicz, and a
    covering map is an isomorphism on pi_3. Checked the count (120 + 1, not 120), that Hurewicz needs
    the 2-connectedness which the wedge supplies, and that the wedge-of-spheres model is reached up to
    homotopy by joining the attachment points along a tree. Not checked: the printed exam, which was
    not re-read in this pass.
---

::: {.problem}
Let $P$ be a $3$-manifold whose fundamental group has order $120$ and whose universal cover is $S^3$.
Compute $\pi_3$ of the one-point union $P \vee S^3$.
:::

::: {.solution}

::: pf

::: pf-step
Set
$$
X=P\vee S^3.
$$
Then $\pi_1(X)=\pi_1(P)$ has order $120$.

::: pf-proof
The sphere summand is simply connected.
:::

:::

::: pf-step
The universal cover $\widetilde X$ is obtained from the universal cover $S^3\to P$ by attaching one copy of $S^3$ at each of the $120$ lifts of the wedge point.

::: pf-proof
The fiber of the universal cover over the wedge point has cardinality equal to the order of the deck group, namely $120$. The simply connected wedge summand lifts independently at every point of this fiber.
:::

:::

::: pf-step
Therefore
$$
\widetilde X\simeq\bigvee^{121}S^3.
$$

::: pf-proof
There is the original covering $S^3$ plus $120$ attached $S^3$ summands. Moving their attachment points together along a tree in the original $S^3$ and collapsing that tree gives the wedge up to homotopy.
:::

:::

::: pf-step
The universal cover is $2$-connected and
$$
H_3(\widetilde X;\ZZ)\cong\ZZ^{121}.
$$

::: pf-proof
A wedge of $121$ copies of $S^3$ has these properties.
:::

:::

::: pf-step
By Hurewicz and covering-space invariance of higher homotopy groups,
$$
\boxed{\pi_3(P\vee S^3)\cong\ZZ^{121}.}
$$

::: pf-proof
Hurewicz gives $\pi_3(\widetilde X)\cong H_3(\widetilde X)$, and the universal covering map induces an isomorphism on $\pi_3$.
:::

:::

:::

:::
