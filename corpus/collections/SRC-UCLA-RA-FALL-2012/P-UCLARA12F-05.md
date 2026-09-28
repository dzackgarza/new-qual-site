---
schema: qual/card@1
id: P-UCLARA12F-05
kind: problem
title: A quadratic identity under bounded L2 convergence
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
Let $(f_n)$ be a sequence of functions $f_n:\mathbb R^3\to\mathbb R$ such that
\[
\sup_n\|f_n\|_{L^2}<\infty.
\]
Show that if $f_n$ converges almost everywhere to a function $f:\mathbb R^3\to\mathbb R$, then
\[
\int_{\mathbb R^3}\left(|f_n|^2-|f_n-f|^2-|f|^2\right)\,dx\longrightarrow0.
\]
:::
