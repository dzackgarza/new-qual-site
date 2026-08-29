---
schema: qual/card@1
id: T-SZRXI
kind: theorem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: reviewed
---

::: {.theorem}
If $H$ is a subgroup of a finite group $G$, then
$$
\abs G = [G:H]\abs H.
$$
In particular, $\abs H$ divides $\abs G$, and the order of every element of $G$ divides $\abs G$.

::: {.proof}
The left cosets of $H$ partition $G$.
Multiplication by a coset representative is a bijection $H\to gH$, so every coset has $\abs H$ elements.
There are $[G:H]$ cosets, and summing their equal sizes gives the formula.
:::
:::
