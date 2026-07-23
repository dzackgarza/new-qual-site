---
schema: qual/card@1
id: P-MD2U3
kind: problem
title: "How many isomorphism classes are there of groups of order 45?"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
How many isomorphism classes are there of groups of order 45?

Describe a representative from each class.

:::{.concept}
\envlist

- Sylow theorems:
- $n_p \cong 1 \mod p$
- $n_p \divides m$.

:::

:::{.solution}
\envlist

- It turns out that $n_3 = 1$ and $n_5 = 1$, so $G \cong S_3 \cross S_5$ since both subgroups are normal.

- There is only one possibility for $S_5$, namely $S_5\cong \ZZ/(5)$.

- There are two possibilities for $S_3$, namely $S_3 \cong \ZZ/(3^2)$ and $\ZZ/(3)^2$.

- Thus

- $G \cong \ZZ/(9) \cross \ZZ/(5)$, or
- $G \cong \ZZ/(3)^2 \cross \ZZ/(5)$.

:::

