---
schema: qual/card@1
id: P-BKF84-7
kind: problem
title: Compute the Vandermonde determinant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
---

::: {.problem}
Let $A$ be the $n\times n$ matrix whose $i$-th row is
\[
(1,x_i,x_i^2,\ldots,x_i^{n-1}).
\]
Show that
\[
\det A=\prod_{i>j}(x_i-x_j).
\]
:::
