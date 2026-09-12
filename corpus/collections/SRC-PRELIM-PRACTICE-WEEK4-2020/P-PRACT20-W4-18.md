---
schema: qual/card@1
id: P-PRACT20-W4-18
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 18"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
If A, B are subspaces of V , which of the following are necessarily subspaces of $V ?$ (a) A + B = {x + y : x ∈ A, y ∈ B}, (b) A ∪ B, (c) A ∩ B, (d) $A ^ { c } = \{ x \in V : x \notin A \}$
:::

::: {.solution}
(a) and (c) are necessarily subspaces.
To see that (d) doesn’t define a subspace, note that the zero vector is in A which means it is not in $A ^ { c }$ . To see that (b) does not necessarily define a subspace, consider $A = \operatorname { s p a n } \left( e _ { 1 } \right)$ and $B = \mathrm { s p a n } \left( e _ { 2 } \right)$ . Then $A \cup B$ is the coordinate axes.
Both $\textstyle { \binom { 1 } { 0 } }$ and $\binom { 0 } { 1 }$ are in $A \cup B$ but the sum 1 is not.
:::
