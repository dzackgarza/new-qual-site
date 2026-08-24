---
schema: qual/card@1
id: P-QJ7MD
kind: problem
title: A subgroup of index $2$ is normal; the same for index the smallest prime dividing
  $|G|$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: problem
- (**Important**) Show that if $H\leq G$ and $[G: H] = 2$ then $H$ is normal.

  > Index 2 implies partition into 2 left cosets: $H, gH$, or two right cosets $H, Hg'$ Note that $gH = G\sm H = Hg'$ Pick $x$, want to show that $xHx\inv = H$, so $xH = Hx$.
  > Case 1: $x\in H\implies xH = H = Hx$ Case 2: $xH\neq H \implies xH = gH$.
  > Similarly $Hx \neq H \implies Hx = Hg'$, so $$xH = gH = G\sm H = Hg' = Hx$$

  - Suppose that the same result holds with 2 replaced by $p$ defined as the smallest prime factor of $\size G$
:::
