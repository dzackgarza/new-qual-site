---
schema: qual/card@1
id: E-MUN-6-5
kind: problem
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?
:::

::: {.solution}
No. If $B=\varnothing$ and $A=\NN$, then $A\times B=\varnothing$ is
finite, while $A$ is infinite.

If both factors are nonempty, finiteness of $A\times B$ does imply that
each factor is finite. Fixing $b_0\in B$ gives an injection
$a\mapsto(a,b_0)$ from $A$ into $A\times B$. Fixing $a_0\in A$ gives an
injection $b\mapsto(a_0,b)$ from $B$ into $A\times B$. Each image is a
subset of a finite set, hence finite by [[E-MUN-6-2]].
Each factor is in bijection with its image, so both factors are finite.
:::
