---
schema: qual/card@1
id: P-UCLARA12S-03
kind: problem
title: Piecewise averages converge in L1
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
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f\in L^1([0,1])$.
For $n\in\mathbb N$, define
\[
f_n(x)=n\int_{k/n}^{(k+1)/n}f(y)\,dy
\]
whenever $x\in[k/n,(k+1)/n)$ and $0\le k\le n-1$.
Prove that $f_n\to f$ in $L^1([0,1])$.
:::
