---
schema: qual/card@1
id: ST-DKYXZ
kind: strategy
title: Count Sylow subgroups before classifying a finite group
classification:
  areas:
  - algebra
  topics:
  - groups
relations:
- kind: uses
  target: T-3X5FF
review: reviewed
---

::: {.strategy title="Sylow counting workflow"}
For each prime $p$ dividing $\abs G$:

1. Write down every divisor of the prime-to-$p$ factor that is congruent to
   $1$ modulo $p$; these are the only possible values of $n_p$.
2. A forced value $n_p=1$ gives a normal Sylow subgroup.
3. If several values remain, count the nonidentity elements contributed by
   distinct Sylow subgroups. Do not assume different Sylow subgroups intersect
   trivially unless their order or another argument proves it.
4. Use normality to form products of subgroups and then test whether conjugation
   between the factors is trivial.

Keep the identity out of overlapping element counts and add it back exactly
once.
:::
