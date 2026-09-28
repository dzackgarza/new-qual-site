---
schema: qual/card@1
id: P-UCLAB05S-AN4
kind: problem
title: Total variation of a continuously differentiable function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 4 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Suppose $f:\mathbb R\to\mathbb R$ is $C^1$.
Show that
\[
\lim_{n\to\infty}
\sum_{j=1}^n
\left|f\!\left(\frac{j-1}{n}\right)-f\!\left(\frac jn\right)\right|
=\int_0^1|f'(t)|\,dt.
\]
:::
