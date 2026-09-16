---
schema: qual/card@1
id: L-DJKXL
kind: lemma
title: Fixed-point congruence for $p$-groups
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: D-WYC7C
- kind: uses
  target: T-QYDVH
review: reviewed
---

::: {.lemma}
Let $p$ be a prime, let $P$ be a finite group of order $p^a$, and let $P$ [[D-WYC7C|act]] on a finite set $X$, with fixed-point set $X^P=\theset{x\in X\suchthat g\cdot x=x\text{ for every }g\in P}$.
Then
$$
\abs X\equiv\abs{X^P}\pmod p.
$$
:::

::: {.proof}
Partition $X$ into its $P$-orbits.
A fixed point contributes an orbit of size one.
Every other orbit $P\cdot x$ has size $[P:P_x]$ by the orbit-stabilizer theorem, which is a power of $p$ larger than one.
Those nontrivial orbit sizes vanish modulo $p$, leaving only the fixed points.
:::
