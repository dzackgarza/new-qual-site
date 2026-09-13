---
schema: qual/card@1
id: P-BKS10-9B
kind: problem
title: A binomial Ramsey bound by induction
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
---

::: {.problem}
Prove that if every edge of the complete graph on
\[
\binom{m+n}{m}
\]
vertices is colored red or blue, then there is either a complete red subgraph on \(m+1\) vertices or a complete blue subgraph on \(n+1\) vertices.

Hint: choose a vertex, partition the remaining vertices according to the color of their edge to it, and induct on \(m+n\).
:::
