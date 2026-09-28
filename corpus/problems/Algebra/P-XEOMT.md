---
schema: qual/card@1
id: P-XEOMT
kind: problem
title: $[A_n,A_n]=A_n$ for $n\geq 5$
classification:
  areas:
  - algebra
  topics:
  - Commutators
  - Permutations
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that $[A_n, A_n] = A_n$ for $n\geq 5$, so $A_{n\geq 5}$ is nonabelian.
:::

::: {.solution}
For $n\ge5$, the group $A_n$ is simple and nonabelian. The commutator subgroup
\[
[A_n,A_n]
\]
is characteristic, hence normal, in $A_n$. It is nontrivial because $A_n$ is nonabelian: for example, the $3$-cycles
\[
(123),\qquad(345)
\]
do not commute.

By simplicity, any nontrivial normal subgroup of $A_n$ is all of $A_n$. Therefore
\[
\boxed{[A_n,A_n]=A_n\qquad(n\ge5)}.
\]
In particular, $A_n$ is perfect and therefore nonabelian.
:::
