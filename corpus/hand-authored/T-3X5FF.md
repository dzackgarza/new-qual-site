---
schema: qual/card@1
id: T-3X5FF
kind: theorem
title: 'Sylow''s third theorem: numerical constraints'
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: T-OBPSZ
- kind: uses
  target: T-RRK4J
review: reviewed
---

::: {.theorem}
Write $\abs G=p^a m$ with $p\nmid m$, and let $n_p$ be the number of Sylow
$p$-subgroups. Then
$$
n_p\mid m,
\qquad
n_p\equiv1\pmod p,
\qquad
n_p=[G:N_G(P)]
$$
for every Sylow $p$-subgroup $P$.
:::

The index formula is orbit-stabilizer for conjugation on the set of Sylow
$p$-subgroups. Conjugacy makes that action transitive, while the fixed-point
congruence gives $n_p\equiv1\pmod p$.
