---
schema: qual/card@1
id: P-UCLARA11F-04
kind: problem
title: Weighted time derivative implies an L2 limit
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
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f\in C^\infty([0,\infty)\times[0,1])$ satisfy
\[
\int_0^\infty\int_0^1 |\partial_t f(t,x)|^2(1+t^2)\,dx\,dt<\infty.
\]
Prove that there exists $g\in L^2([0,1])$ such that $f(t,\cdot)\to g$ in $L^2([0,1])$ as $t\to\infty$.
:::
