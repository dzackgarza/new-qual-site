---
schema: qual/card@1
id: P-PRACT20-W4-13
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 13"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Let A be a $2 \times 2$ real matrix.
Which of the following are necessarily true: (a) All entries of $A ^ { 2 }$ are non-negative, (b) the determinant of $A ^ { 2 }$ is non-negative, (c) if A has two distinct eigenvalues then $A ^ { 2 }$ has two distinct eigenvalues.
:::

::: {.solution}
It is not necessarily the case that all entries of $A ^ { 2 }$ are positive.
Indeed,

$$
A = { \binom { 1 } { 0 } } \quad { \overset { - 1 } { 1 } } \quad \implies \quad A ^ { 2 } = { \binom { 1 } { 0 } } \quad { \overset { - 2 } { 1 } } \quad
$$

which has a negative entry.
Thus (a) is not necessarily true.
For (c), notice that

$$
A = { \binom { - 1 } { 0 } } \quad 0 \quad \quad
$$

has distinct eigenvalues by $A ^ { 2 } = I$ does not.
Thus (c) is not necessarily true.
Property (b) is necessarily true since the determinant is multiplicative:

$$
\operatorname* { d e t } ( A ^ { 2 } ) = \operatorname* { d e t } ( A ) ^ { 2 } \geq 0 .
$$
:::
