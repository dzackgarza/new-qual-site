---
schema: qual/card@1
id: P-LG4RJ
kind: problem
title: Every $p$-group is solvable
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that every finite $p$-group is solvable.
:::

::: {.solution}
We argue by induction on $|G|$.

If $|G|=1$, the result is trivial. Let $G$ be a nontrivial finite $p$-group. Its center is nontrivial, so choose a subgroup
\[
C\le Z(G)
\]
of order $p$. Then $C\trianglelefteq G$ and $C$ is abelian.

The quotient $G/C$ is again a finite $p$-group of smaller order. By induction, $G/C$ is solvable.

A group extension of a solvable group by a solvable normal subgroup is solvable. Since $C$ is abelian, hence solvable, and $G/C$ is solvable, it follows that $G$ is solvable.

Equivalently, iterating this argument gives a normal series whose successive factors all have order $p$, hence are cyclic and abelian.
:::
