---
schema: qual/card@1
id: PR-YY3JG
kind: proposition
title: Larger subgroups have smaller index
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a group and $H\leq K \leq G$ subgroups.
Then
$$
\abs{G} = [G:1] \geq [G:H] \geq [G:K] \geq [G:G] = 1
$$
as cardinals.
In particular, for arbitrary subgroups $H, K\leq G$, applying this to $H \cap K \leq H\leq G$ and $H\cap K\leq K\leq G$ gives $[G: H \cap K] \geq [G:H]$ and $[G:H\cap K]\geq[G:K]$.
:::

::: {.proof}
By the [[PR-SF6ZE|tower law]], $[G:H]=[G:K]\,[K:H]\geq[G:K]$ since $[K:H]\geq1$; the outer inequalities are the cases $H=1$ and $K=G$.
:::
