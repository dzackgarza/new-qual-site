---
schema: qual/card@1
id: PR-PYYRK
kind: proposition
title: A subgroup is normal if and only if it is a union of conjugacy classes
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Conjugacy
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a group and $N\leq G$ a subgroup.
Then $N$ is [[D-EKE4Q|normal]] in $G$ if and only if $N$ is a union of [[D-HLDEY|conjugacy classes]] of $G$.
In that case $N=\coprod_{i} C(h_i)$, where $h_i$ runs over a set of representatives of the conjugacy classes of $G$ contained in $N$.
:::

::: {.proof}
If $N\normal G$ and $h\in N$, then $ghg^{-1}\in N$ for all $g\in G$, so $C(h)\subseteq N$ and $N=\bigcup_{h\in N}C(h)$.
Conversely, if $N$ is a union of conjugacy classes, then for $h\in N$ and $g\in G$ we have $ghg^{-1}\in C(h)\subseteq N$, so $gNg^{-1}\subseteq N$ for all $g$; applying this to $g^{-1}$ gives $gNg^{-1}=N$.
Distinct conjugacy classes are disjoint, so the union is disjoint.
:::
