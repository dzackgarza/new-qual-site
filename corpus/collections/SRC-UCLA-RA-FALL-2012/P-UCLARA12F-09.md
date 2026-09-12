---
schema: qual/card@1
id: P-UCLARA12F-09
kind: problem
title: Repeated values accumulating at zero force constancy
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Suppose $f$ is holomorphic in the unit disc $\mathbb D$, and $(x_n)$ is a sequence of real numbers satisfying
\[
0<x_{n+1}<x_n<1
\]
for all $n$ and $x_n\to0$.
Show that if
\[
f(x_{2n+1})=f(x_{2n})
\]
for every $n$, then $f$ is constant.
:::
