---
schema: qual/card@1
id: P-BKS19-9A
kind: problem
title: Fast-growing series $\sum 1/f(n)$ avoiding a countable set
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
---

::: {.problem}
Let $S$ be a countable set of real numbers.
Show that there are functions $g_n:\mathbb N\to\mathbb N$ such that if $f:\mathbb N\to\mathbb N$ satisfies
\[
f(n+1)>g_n(f(n))\qquad\text{for all }n,
\]
then
\[
A=\sum_{n=1}^{\infty}\frac1{f(n)}
\]
converges to a real number that is not in $S$.
:::
