---
schema: qual/card@1
id: P-YLFU2
kind: problem
title: Let $M$ be a finitely generated module over $R$ a PID.
classification:
  areas:
  - algebra
  topics:
  - structure-theorem
  - modules
  - principal-ideal-domains
relations: []
review: draft
solved: false
---

::: problem
Let $M$ be a finitely generated module over $R$ a PID.

Then
$$
M \cong F \oplus \bigoplus_{i=1}^n R/(d_i)
$$

where $F$ is free of finite rank and $R/(d_i)$ are cyclic torsion modules (the *invariant factors*) satisfying $d_1 \divides d_2 \divides \cdots \divides d_n$.

Equivalently,

$$
M \cong F \oplus \bigoplus_{i=1}^n R/(p_i^{s_i})
$$

where $F$ is free of finite rank, $p^i \in R$ are (not necessarily distinct) prime elements (the *elementary divisors*), and $s_i \in \ZZ^{\geq 1}$.
:::
