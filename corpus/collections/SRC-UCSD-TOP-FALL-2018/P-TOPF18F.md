---
schema: qual/card@1
id: P-TOPF18F
kind: problem
title: '$\pi_3(\RP^4\vee S^3)$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Hurewicz Theorem
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Calculate the homotopy group $\pi_3(\mathbb{RP}^4 \vee S^3)$.
(Here $\vee$ denotes the one-point union of the two spaces.)
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
X=\mathbb{RP}^4\vee S^3.
$$
Then $\pi_1(X)\cong\mathbb Z/2$.

::: pf-proof

The $S^3$ summand is simply connected and $\pi_1(\mathbb{RP}^4)=\mathbb Z/2$.

:::

:::

::: pf-step

The universal cover $\widetilde X$ is obtained from $S^4$ by attaching a copy of $S^3$ at each of the two lifts of the wedge point, hence
$$
\widetilde X\simeq S^4\vee S^3\vee S^3.
$$

::: pf-proof

The universal cover of $\mathbb{RP}^4$ is $S^4$. The simply connected wedge summand lifts once at each point of the two-element fiber over the wedge point. Moving the attachment points together along an arc gives the stated wedge up to homotopy.

:::

:::

::: pf-step

The space $\widetilde X$ is $2$-connected and
$$
H_3(\widetilde X;\mathbb Z)\cong\mathbb Z^2.
$$

::: pf-proof

The wedge contains two $3$-sphere summands and one $4$-sphere summand; it has no homology or homotopy in degrees $1,2$.

:::

:::

::: pf-step

By Hurewicz,
$$
\pi_3(\widetilde X)\cong H_3(\widetilde X)\cong\mathbb Z^2.
$$

::: pf-proof

The degree-$3$ Hurewicz map is an isomorphism for a $2$-connected space.

:::

:::

::: pf-step

Therefore
$$
\boxed{\pi_3(\mathbb{RP}^4\vee S^3)\cong\mathbb Z^2.}
$$

::: pf-proof

A covering map induces isomorphisms on homotopy groups in degrees at least $2$.

:::

:::

:::

:::
