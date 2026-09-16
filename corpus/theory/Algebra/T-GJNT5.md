---
schema: qual/card@1
id: T-GJNT5
kind: theorem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a finite group and $H \leq G$ a subgroup.
Then $\abs H$ divides $\abs G$, and $[G:H] = \abs G/ \abs H$.
:::

::: {.proof}
The left cosets of $H$ partition $G$ ([[PR-VUKHO]]), and each coset $gH$ has $\abs H$ elements because $h\mapsto gh$ is a bijection $H\to gH$.
Hence $\abs G=[G:H]\,\abs H$.
:::
