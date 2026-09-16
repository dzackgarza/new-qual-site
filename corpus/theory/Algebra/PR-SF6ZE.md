---
schema: qual/card@1
id: PR-SF6ZE
kind: proposition
title: Tower law for subgroups
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
Let $G$ be a group and $K\leq H \leq G$ subgroups.
Then
$$
[G: K] = [G:H]\, [H: K]
$$
as cardinals; in particular $[G:K]$ is finite if and only if $[G:H]$ and $[H:K]$ are both finite.
:::

::: {.proof}
Write $G=\coprod_{i\in I}g_iH$ and $H=\coprod_{j\in J}h_jK$ as disjoint unions of left cosets, with $\abs{I}=[G:H]$ and $\abs{J}=[H:K]$.
Then $G=\bigcup_{i,j}g_ih_jK$.
If $g_ih_jK=g_{i'}h_{j'}K$, then $g_ih_j\in g_{i'}h_{j'}K\subseteq g_{i'}H$, so $g_iH=g_{i'}H$ and $i=i'$; cancelling $g_i$ gives $h_jK=h_{j'}K$ and $j=j'$.
Hence the cosets $g_ih_jK$ are pairwise distinct, and $[G:K]=\abs{I\times J}$.
:::
