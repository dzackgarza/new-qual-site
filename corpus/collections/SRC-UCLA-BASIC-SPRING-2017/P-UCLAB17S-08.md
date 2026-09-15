---
schema: qual/card@1
id: P-UCLAB17S-08
kind: problem
title: A trapezoid-rule error estimate by the second derivative
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
Show that there is a constant $C$ such that every $C^2$ function $f:\mathbb R\to\mathbb R$ satisfies
\[
\left|\frac{f(0)+f(1)}2-\int_0^1f(x)\,dx\right|\le C\int_0^1|f''(x)|\,dx.
\]
:::
