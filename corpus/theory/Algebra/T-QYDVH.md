---
schema: qual/card@1
id: T-QYDVH
kind: theorem
title: Orbit-stabilizer theorem
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
relations: []
review: draft
---

::: {.theorem}
Let a group $G$ [[D-WYC7C|act]] on a set $X$, and let $x\in X$ have orbit $Gx$ and stabilizer $G_x$.
Then
$$
\size{Gx} = [G: G_x],
$$
and if $G$ is finite, then $\size{Gx} = \size{G} / \size{G_x}$.
:::

::: {.remark}
The map $G/G_x\to Gx$, $gG_x\mapsto gx$, is a well-defined bijection of sets, which gives the equality $\size{Gx} = [G:G_x]$.
:::
