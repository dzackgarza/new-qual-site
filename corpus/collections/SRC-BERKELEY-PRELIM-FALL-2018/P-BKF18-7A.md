---
schema: qual/card@1
id: P-BKF18-7A
kind: problem
title: Entry bound for a positive semidefinite matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $A=(a_{ij})$ is a real symmetric $n\times n$ matrix with nonnegative eigenvalues.
Show that
\[
|a_{ij}|\le \sqrt{a_{ii}a_{jj}}
\]
for all distinct $i,j\le n$.
:::

::: {.solution}
Since A is symmetric with nonnegative eigenvalues, we may diagonalize A as $A = U D U ^ { T }$ with $U$ orthogonal and $D$ diagonal with nonnegative entries, so $A = B ^ { T } B$ for $B ^ { T } = U D ^ { 1 / 2 }$ . Thus, A is a Gram matrix, i.e., $a _ { i j } = \langle v _ { i } , v _ { j } \rangle$ where $v _ { i }$ are the columns of $B ,$ so by the Cauchy--Schwarz inequality $\abs{ a _ { i j } } \leq \| v _ { i } \| \| v _ { j } \| = \sqrt { a _ { i i } a _ { j j } }$ , as desired.
:::
