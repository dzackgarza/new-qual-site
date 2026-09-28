---
schema: qual/card@1
id: ST-DKYXZ
kind: strategy
title: Count Sylow subgroups before classifying a finite group
classification:
  areas:
  - algebra
  topics:
  - Groups
relations:
- kind: uses
  target: T-3X5FF
review: reviewed
---

::: {.strategy}
Let $G$ be a finite group.
For each prime $p$ dividing $\abs G$, write $\abs G=p^am$ with $p\notdivides m$ and let $n_p$ be the number of [[D-7TQ2M|Sylow $p$-subgroups]] of $G$.

1. List the divisors of $m$ that are congruent to $1$ modulo $p$; by the Sylow theorems these are the only possible values of $n_p$.

2. If $n_p=1$ is forced, the Sylow $p$-subgroup is [[D-EKE4Q|normal]].

3. If several values remain, count the nonidentity elements contributed by distinct Sylow subgroups.
   When $a=1$, distinct Sylow $p$-subgroups have order $p$, intersect trivially, and contribute $n_p(p-1)$ elements of order $p$; when $a\geq2$, bound the intersections of distinct Sylow $p$-subgroups separately before counting.

4. Use normal Sylow subgroups to form products of subgroups, and determine whether the conjugation action of one factor on another is trivial.

In overlapping element counts, count only nonidentity elements and add the identity once.
:::
