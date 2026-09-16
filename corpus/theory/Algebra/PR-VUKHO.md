---
schema: qual/card@1
id: PR-VUKHO
kind: proposition
title: Cosets are equal or disjoint
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
Let $G$ be a group, $H\leq G$ a subgroup, and $x,y\in G$.
Then the left cosets $xH$ and $yH$ are either equal or disjoint.
:::

::: {.proof}
Suppose $g\in xH\cap yH$, say $g=xh=yh'$ with $h,h'\in H$.
Then $x=yh'h^{-1}\in yH$, so $xH\subseteq yHH=yH$; by symmetry $yH\subseteq xH$.
:::
