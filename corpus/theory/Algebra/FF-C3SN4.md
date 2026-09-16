---
schema: qual/card@1
id: FF-C3SN4
kind: fact
title: Groups of order 9
prompts:
- What are the groups of order 9?
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - p-Groups
relations: []
review: draft
---

::: {.fact}
Up to isomorphism, the groups of order $9$ are $\ZZ/9\ZZ$ and $(\ZZ/3\ZZ)^2$.
Both are abelian.
:::

::: {.proof}
A group $G$ of order $p^2$, $p$ prime, has nontrivial [[D-NK7G7|center]] $Z(G)$ by the class equation.
If $Z(G)\ne G$, then $G/Z(G)$ has order $p$ and is cyclic, which forces $G$ to be abelian, a contradiction.
So $G$ is abelian, and the classification of finite abelian groups gives $\ZZ/p^2\ZZ$ or $(\ZZ/p\ZZ)^2$.
:::
