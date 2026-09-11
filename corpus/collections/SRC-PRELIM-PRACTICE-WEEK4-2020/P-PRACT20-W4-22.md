---
schema: qual/card@1
id: P-PRACT20-W4-22
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 22"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that matrices A, $B \in \mathbb { R } ^ { n \times n }$ satisfy $A B - B A = A$ . Show that A is not invertible.\
If instead we assume $A \neq B , A ^ { 3 } = B ^ { 3 }$ and $A ^ { 2 } B = B ^ { 2 } A$ , show that $A ^ { 2 } + B ^ { 2 }$ is not invertible.
:::

::: {.solution}
For the first part, if A was invertible, we would have

$$
( A B - B A ) A ^ { - 1 } = A A ^ { - 1 } \quad \Longrightarrow \quad A B A ^ { - 1 } = B + I .
$$

This would mean that B and $B + I$ are similar which is impossible since the $\operatorname { t r } ( B + I ) = n + \operatorname { t r } ( B )$ whereas similarity has to preserve the trace.

For the second part, notice that

$$
( A ^ { 2 } + B ^ { 2 } ) A = A ^ { 3 } + B ^ { 2 } A = B ^ { 3 } + A ^ { 2 } B = ( B ^ { 2 } + A ^ { 2 } ) B = ( A ^ { 2 } + B ^ { 2 } ) B .
$$

If $A ^ { 2 } + B ^ { 2 }$ was invertible, then we would have $A = B$ , but we’ve assumed that $A \neq B$ , and thus $A ^ { 2 } + B ^ { 2 }$ must not be invertible.
:::
