---
schema: qual/card@1
id: FF-2NPCE
kind: fact
title: Groups of order 10
prompts:
- What are the groups of order 10?
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
Up to isomorphism, the groups of order $10$ are the cyclic group $\ZZ/10\ZZ$, which is abelian, and the [[D-4R2Z5|dihedral group]] $D_5$ of order $10$, which is nonabelian.
:::

::: {.proof}
Let $\abs G=10$.
By [[FT-ZENUU|Sylow's theorems]], the number of Sylow $5$-subgroups divides $2$ and is congruent to $1$ modulo $5$, so there is a unique, hence normal, Sylow $5$-subgroup $N\cong\ZZ/5\ZZ$.
A Sylow $2$-subgroup $H\cong\ZZ/2\ZZ$ meets $N$ trivially and $NH=G$, so $G\cong N\rtimes_\theta H$ for a homomorphism $\theta\colon H\to\Aut(N)\cong(\ZZ/5\ZZ)^\times$.
The elements of order dividing $2$ in $(\ZZ/5\ZZ)^\times$ are $\pm1$.
If $\theta$ is trivial, $G\cong\ZZ/5\ZZ\times\ZZ/2\ZZ\cong\ZZ/10\ZZ$; if the generator of $H$ acts by inversion, $G\cong D_5$.
:::
