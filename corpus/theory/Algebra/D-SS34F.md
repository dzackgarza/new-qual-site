---
schema: qual/card@1
id: D-SS34F
kind: definition
title: Invariant factor decomposition
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.definition}
Let $G$ be a finitely generated abelian group, and for $n\geq 1$ let $C_n$ denote the cyclic group of order $n$.
An \dfn{invariant factor decomposition} of $G$ is an isomorphism
$$
G \cong \ZZ^r \times \prod_{k=1}^m C_{n_k}
$$
with $r,m\geq 0$ and integers $n_1,\ldots,n_m\geq 2$ such that $n_1 \divides n_2\divides \cdots \divides n_m$.
The integers $n_1,\ldots,n_m$ are the \dfn{invariant factors} of $G$.
:::

::: {.theorem}
Every finitely generated abelian group $G$ has an invariant factor decomposition, the direct product of the free abelian group $\ZZ^r$ and finitely many finite cyclic groups.
The integers $r$ and $m$ and the invariant factors $n_1,\ldots,n_m$ are uniquely determined by $G$.
:::
