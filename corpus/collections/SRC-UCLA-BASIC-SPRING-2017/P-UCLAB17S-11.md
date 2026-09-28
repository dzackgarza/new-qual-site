---
schema: qual/card@1
id: P-UCLAB17S-11
kind: problem
title: Pointwise convergence of a subsequence of primitives
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $f_n:[0,1]\to\mathbb R$ be continuous and satisfy
\[
|f_n(x)|\le 1+\frac{n}{1+n^2x^2}.
\]
Define $F_n(x)=\int_0^x f_n(t)\,dt$. Show that there is a subsequence $n_k\to\infty$ such that $F_{n_k}(x)$ converges for every $x\in[0,1]$.
:::
