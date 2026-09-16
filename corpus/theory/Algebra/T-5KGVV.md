---
schema: qual/card@1
id: T-5KGVV
kind: theorem
title: Equality of left cosets
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group, $H\leq G$ a subgroup, and $a,b\in G$.
Then
$$
aH = bH \iff a^{-1} b \in H \iff b^{-1} a\in H.
$$
:::

::: {.proof}
If $aH=bH$, then $b=b\cdot e\in aH$, so $b=ah$ with $h\in H$ and $a^{-1}b=h\in H$.
If $a^{-1}b=h\in H$, then $bH=ahH=aH$.
Finally, $b^{-1}a=(a^{-1}b)^{-1}$, and $H$ is closed under inverses.
:::
