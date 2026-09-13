---
schema: qual/card@1
id: P-BKF05-6B
kind: problem
title: Unique nearest points in closed convex subsets of Euclidean space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
---

::: {.problem}
Let \(K\subseteq\mathbb R^n\) be nonempty, closed, and convex. Show that for every \(x\in\mathbb R^n\) there exists a unique \(y\in K\) minimizing the Euclidean distance to \(x\); equivalently,
\[
\|x-y\|<\|x-z\|
\]
for every \(z\in K\setminus\{y\}\).
:::
