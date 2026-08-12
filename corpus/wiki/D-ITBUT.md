---
schema: qual/card@1
id: D-ITBUT
kind: definition
title: "Quotient Map"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Quotient Map"}
A map $q:X\to Y$ is a **quotient map** if and only if

1. $q$ is surjective, and

2. $U$ is open in $Y\iff q ^{-1} (U)$ is open in $X$

> Note that $\implies$ comes from the definition of continuity of $q$, but $\impliedby$ is a stronger condition.

Equivalently:

- $p$ maps *saturated* subsets of $X$ to open subsets of $Y$, or

- If $U$ is open in $X$, then $(q\inv \circ q)(U)$ is again open in $X$.
:::
