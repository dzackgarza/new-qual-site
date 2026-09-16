---
schema: qual/card@1
id: P-TNPRX
kind: problem
title: When a cyclic group is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
Give a necessary and sufficient condition for a cyclic group to be solvable.
:::

::: {.solution}
Every cyclic group is abelian, and every abelian group is solvable: its commutator subgroup is trivial.

Thus if $G$ is cyclic,
\[
G'=[G,G]=1,
\]
so the derived series terminates after one step.

Hence the necessary and sufficient condition is vacuous:
\[
\boxed{\text{every cyclic group is solvable}.}
\]
:::
