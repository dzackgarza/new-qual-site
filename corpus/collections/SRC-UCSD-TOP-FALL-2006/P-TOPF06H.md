---
schema: qual/card@1
id: P-TOPF06H
kind: problem
title: "Suspension of a connected space is simply connected"
classification:
  areas:
  - topology
  topics:
  - Suspensions
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Let $X$ be a connected space.
Show that the suspension of $X$, $\Sigma X$, is simply connected.
Can we drop the connectedness assumption?
:::

::: {.solution}

::: pf

::: pf-step

Write the suspension as the union of the two cones
$$
\Sigma X=C_+X\cup C_-X.
$$
Each cone is contractible.

::: pf-proof

A cone contracts to its cone point.

:::

:::

::: pf-step

If $X$ is connected, enlarge the two open cone neighborhoods slightly so that their intersection deformation retracts onto $X$ and is connected.

::: pf-proof

Using the quotient model $X\times[-1,1]$ with the end copies collapsed, take the images of $X\times(-1,1]$ and $X\times[-1,1)$. Their intersection is $X\times(-1,1)$, homotopy equivalent to $X$ and connected.

:::

:::

::: pf-step

Van Kampen then gives
$$
\pi_1(\Sigma X)=1.
$$

::: pf-proof

Both cone neighborhoods have trivial fundamental group. Since their intersection is path-connected, van Kampen identifies the fundamental group of the union with the pushout of two trivial groups, hence the trivial group.

:::

:::

::: pf-step

Connectedness cannot be dropped: for $X=S^0$,
$$
\Sigma S^0\cong S^1,
$$
which is not simply connected.

::: pf-proof

The suspension of two points is two arcs sharing their two endpoints, which is a circle; its fundamental group is $\mathbb Z$.

:::

:::

:::

:::
