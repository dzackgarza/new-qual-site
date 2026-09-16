---
schema: qual/card@1
id: T-EN5H4
kind: theorem
title: $S_n$ is solvable if and only if $n\leq 4$
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
relations: []
review: draft
---

::: {.theorem}
Let $n\geq1$.
The symmetric group $S_n$ is [[D-DFIDP|solvable]] if and only if $n\leq 4$.
:::

::: {.proof}
For $n\leq4$, $S_n$ is isomorphic to a subgroup of $S_4$, and subgroups of solvable groups are solvable.
The series $\theset{e}\normal V_4\normal A_4\normal S_4$, with $V_4=\theset{e,(12)(34),(13)(24),(14)(23)}$, has abelian quotients $V_4$, $C_3$, and $C_2$, so $S_4$ is solvable.

For $n\geq5$, $A_n$ is [[D-T2NZ4|simple]] and nonabelian.
Its commutator subgroup $[A_n,A_n]$ is normal and nontrivial, so $[A_n,A_n]=A_n$, and the [[D-W2QAA|derived series]] of $A_n$ is constant at $A_n$ and never reaches $\theset e$.
Hence $A_n$ is not solvable, and neither is $S_n$, which contains it.
:::
