---
schema: qual/card@1
id: P-UCLARA12F-10
kind: problem
title: Pointwise convergence on an accumulating set determines a normal family
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
Let $(f_n)$ be a sequence of holomorphic functions on $\mathbb D$ satisfying $|f_n(z)|\le1$ for every $z\in\mathbb D$ and every $n$.
Let
\[
A=\{z\in\mathbb D:\lim_{n\to\infty}f_n(z)\text{ exists}\}.
\]
Show that if $A$ has an accumulation point in $\mathbb D$, then there exists a holomorphic function $f$ on $\mathbb D$ such that $f_n\to f$ locally uniformly on $\mathbb D$.
:::
