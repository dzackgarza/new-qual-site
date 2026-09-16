---
schema: qual/card@1
id: D-5KMYI
kind: definition
title: Chain homotopy
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring, let $(C_*, \del^C)$ and $(D_*, \del^D)$ be chain complexes of $R$-modules, and let $f, g\colon C_*\to D_*$ be [[D-36ONS|chain maps]].
A \dfn{chain homotopy} from $f$ to $g$ is a family of $R$-linear maps $h_i\colon C_i\to D_{i+1}$, $i\in\ZZ$, such that
$$
f_i - g_i = \del^D_{i+1}\circ h_i + h_{i-1}\circ \del^C_i \quad\text{for all } i\in\ZZ
.$$
The chain maps $f$ and $g$ are \dfn{chain homotopic} if a chain homotopy from $f$ to $g$ exists.
:::

::: {.concept}
[@Hat02, §2.1, p. 111].
:::
