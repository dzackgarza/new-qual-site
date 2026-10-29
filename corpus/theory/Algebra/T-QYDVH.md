---
schema: qual/card@1
id: T-QYDVH
kind: theorem
title: Orbit-stabilizer theorem
slogan: 'An orbit has one point for each coset of the stabilizer.'
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
\abs{Gx} = [G: G_x],
$$
and if $G$ is finite, then $\abs{Gx} = \abs{G} / \abs{G_x}$.
:::

::: {.remark}
The map $G/G_x\to Gx$, $gG_x\mapsto gx$, is a well-defined bijection of sets, which gives the equality $\abs{Gx} = [G:G_x]$.
:::
