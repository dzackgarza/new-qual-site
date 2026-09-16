---
schema: qual/card@1
id: FF-Q6XCL
kind: fact
title: Groups of order 15
prompts:
- What are the groups of order 15?
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Cyclic Groups
relations: []
review: draft
---

::: {.fact}
Every group of order $15$ is isomorphic to the cyclic group $\ZZ/15\ZZ$.
:::

::: {.proof}
Let $\abs G=15$.
By [[FT-ZENUU|Sylow's theorems]], the number of Sylow $3$-subgroups divides $5$ and is congruent to $1$ modulo $3$, and the number of Sylow $5$-subgroups divides $3$ and is congruent to $1$ modulo $5$; both numbers are $1$.
So $G$ has normal subgroups $P\cong\ZZ/3\ZZ$ and $Q\cong\ZZ/5\ZZ$ with $P\cap Q=\theset{e}$ and $\abs{PQ}=15$, and [[FT-7NMQR]] gives $G\cong\ZZ/3\ZZ\times\ZZ/5\ZZ\cong\ZZ/15\ZZ$.
:::
