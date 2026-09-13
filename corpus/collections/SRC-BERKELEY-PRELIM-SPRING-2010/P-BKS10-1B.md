---
schema: qual/card@1
id: P-BKS10-1B
kind: problem
title: Uniform convergence and the mean value of an oscillatory series
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
Show that
\[
f(x)=\sum_{n=0}^\infty \frac{e^{i\sqrt n\,x}}{n^2+1}
\]
converges uniformly for real \(x\). Prove that
\[
\lim_{R\to+\infty}\frac1{2R}\int_{-R}^{R}f(x)\,dx
\]
exists and calculate it.
:::
