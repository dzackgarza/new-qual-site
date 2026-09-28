---
schema: qual/card@1
id: D-36ONS
kind: definition
title: Chain map
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring and let $(C_*, \del^C)$ and $(D_*, \del^D)$ be chain complexes of $R$-modules, with $\del^C_i\colon C_i\to C_{i-1}$ and $\del^D_i\colon D_i\to D_{i-1}$.
A \dfn{chain map} $f\colon C_*\to D_*$ is a family of $R$-linear maps $f_i\colon C_i\to D_i$, $i\in\ZZ$, such that
$$
f_{i-1}\circ\del^C_i = \del^D_i \circ f_i \quad\text{for all } i\in\ZZ
.$$
:::
