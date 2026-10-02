---
schema: qual/card@1
id: FD-T7IQV
kind: proposition
title: Solvability via composition factors
prompts:
- When is a group solvable, in terms of its composition factors?
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
relations:
- kind: uses
  target: D-DFIDP
- kind: uses
  target: D-FYX4I
review: draft
---

::: {.proposition}
Let $G$ be a finite group.
Then $G$ is [[D-DFIDP|solvable]] if and only if the composition factors in a [[D-FYX4I|composition series]] of $G$ are all abelian.
:::

::: {.proof}
If $G$ has a composition series with abelian factors, that series is a normal series with abelian successive quotients, so $G$ is solvable.

Conversely, suppose $G$ is solvable. Every subgroup and quotient of a solvable group is solvable, so every composition factor of $G$ is both simple and solvable. A nontrivial simple solvable group is abelian: if its commutator subgroup were the whole group, its derived series would never reach the identity, while if the commutator subgroup is proper, simplicity forces it to be trivial. Hence every composition factor is abelian.
:::
