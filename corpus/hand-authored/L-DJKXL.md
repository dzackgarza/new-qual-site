---
schema: qual/card@1
id: L-DJKXL
kind: lemma
title: Fixed-point congruence for p-groups
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: D-WYC7C
- kind: uses
  target: T-OBPSZ
review: reviewed
---

::: {.lemma}
Let a finite group $P$ of order $p^a$ act on a finite set $X$. Then
$$
\abs X\equiv \abs{X^P}\pmod p.
$$

::: {.proof}
Partition $X$ into its $P$-orbits. A fixed point contributes an orbit of size
one. Every other orbit has size $[P:P_x]$, which is a power of $p$ larger than
one by orbit-stabilizer. Those nontrivial orbit sizes vanish modulo $p$, leaving
only the fixed points.
:::
:::
