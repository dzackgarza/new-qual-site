---
schema: qual/card@1
id: P-LMEKH
kind: problem
title: The subgroup $\langle aba^{-1}b^{-1},\, a^2ba^{-2}b^{-1},\, a^{-1}bab^{-1},\,
  aba^{-2}b^{-1}a\rangle$ of the free group on two generators
classification:
  areas:
  - topology
  topics:
  - Groups
  - Covering Spaces
relations: []
review: draft
---

::: {.problem}
Let $G = <a, b>$ and $H \leq G$ where $H = <aba^{-1}b^{-1},~ a^2ba^{-2}b^{-1},~ a^{-1}bab^{-1},~ aba^{-2}b^{-1}a>$.
To what well-known group is $H$ isomorphic?
:::

::: {.solution}
<1>1. Build the Stallings core graph of the subgroup from the four based loops representing the given generators and fold equal-labelled edges with common initial vertex.
::: {.proof}
Stallings folding preserves the subgroup represented by the based labelled graph and terminates in the finite core graph for a finitely generated subgroup of a free group.
:::

<1>2. After folding, the core has $8$ vertices and $10$ unoriented edges.
::: {.proof}
Using labels $a,b$ and inverses, the folded positive-labelled edges may be taken as
$$
(0,a,1),(0,b,3),(1,a,5),(1,b,2),(2,a,6),(3,a,2),(5,b,6),(9,a,0),(9,b,10),(10,a,3),
$$
with vertex set $\{0,1,2,3,5,6,9,10\}$. Thus $V=8$ and $E=10$.
:::

<1>3. Therefore
$$\operatorname{rank}H=E-V+1=10-8+1=3.$$
::: {.proof}
The fundamental group of a connected finite graph is free of rank $E-V+1$, and the Stallings core has fundamental group isomorphic to $H$.
:::

<1>4. Hence
$$\boxed{H\cong F_3.}$$
::: {.proof}
Every subgroup of a free group is free, and <1>3 determines its rank.
:::
:::
