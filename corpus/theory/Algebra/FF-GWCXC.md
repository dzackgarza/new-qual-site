---
schema: qual/card@1
id: FF-GWCXC
kind: fact
title: Groups of order 14
prompts:
- What are the groups of order 14?
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
Up to isomorphism, the groups of order $14$ are the cyclic group $\ZZ/14\ZZ$, which is abelian, and the [[D-4R2Z5|dihedral group]] $D_7$ of order $14$, which is nonabelian.
:::

::: {.proof}
Let $\abs G=14$.
By [[FT-ZENUU|Sylow's theorems]], the number of Sylow $7$-subgroups divides $2$ and is congruent to $1$ modulo $7$, so there is a unique, hence normal, Sylow $7$-subgroup $N\cong\ZZ/7\ZZ$.
A Sylow $2$-subgroup $H\cong\ZZ/2\ZZ$ meets $N$ trivially and $NH=G$, so $G\cong N\rtimes_\theta H$ for a homomorphism $\theta\colon H\to\Aut(N)\cong(\ZZ/7\ZZ)^\times$.
The elements of order dividing $2$ in $(\ZZ/7\ZZ)^\times$ are $\pm1$.
If $\theta$ is trivial, $G\cong\ZZ/7\ZZ\times\ZZ/2\ZZ\cong\ZZ/14\ZZ$; if the generator of $H$ acts by inversion, $G\cong D_7$.
:::
