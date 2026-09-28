---
schema: qual/card@1
id: D-53LTN
kind: definition
title: Characteristic subgroups
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Automorphisms
  - Normal Subgroups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group.
A [[D-IQ4OX|subgroup]] $H\leq G$ is \dfn{characteristic} in $G$, written $H \ch G$, if $\phi(H) \leq H$ for every $\phi \in \Aut(G)$.
:::

::: {.remark}
If $H \ch G$, then $\phi(H) = H$ for every $\phi\in\Aut(G)$: applying the definition to $\phi^{-1}$ gives $\phi^{-1}(H)\leq H$, so $H\leq\phi(H)$.
The automorphisms need not fix $H$ pointwise.
:::
