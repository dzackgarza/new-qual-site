---
schema: qual/card@1
id: FF-TEGRU
kind: fact
title: Groups of order 6
prompts:
- What are the groups of order 6?
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
relations: []
review: draft
---

::: {.fact}
Up to isomorphism, the groups of order $6$ are the cyclic group $\ZZ/6\ZZ$, which is abelian, and the [[D-4R2Z5|dihedral group]] $D_3\cong S_3$ of order $6$, which is nonabelian.
:::

::: {.proof}
Let $\abs G=6$.
By [[FT-ZENUU|Sylow's theorems]], the number of Sylow $3$-subgroups divides $2$ and is congruent to $1$ modulo $3$, so there is a unique, hence normal, Sylow $3$-subgroup $N\cong\ZZ/3\ZZ$.
A Sylow $2$-subgroup $H\cong\ZZ/2\ZZ$ meets $N$ trivially and $NH=G$, so $G\cong N\rtimes_\theta H$ for a homomorphism $\theta\colon H\to\Aut(N)\cong\theset{\pm1}$.
If $\theta$ is trivial, $G\cong\ZZ/3\ZZ\times\ZZ/2\ZZ\cong\ZZ/6\ZZ$; otherwise the generator of $H$ acts by inversion and $G\cong D_3$.
:::
