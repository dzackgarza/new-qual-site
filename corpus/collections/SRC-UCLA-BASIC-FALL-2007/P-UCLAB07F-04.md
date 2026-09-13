---
schema: qual/card@1
id: P-UCLAB07F-04
kind: problem
title: Midpoint quadrature error from a bounded second derivative
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Suppose $f:\mathbb R\to\mathbb R$ is twice differentiable and $|f''(x)|\le B$.

(a) Prove that
\[\left|2Af(0)-\int_{-A}^{A}f(x)\,dx\right|\le \frac{A^3}{3}B.\]

(b) Use part (a) to justify
\[\left|\int_a^b f(x)\,dx-\frac{b-a}{n}\sum_{k=1}^n f\!\left(a+\frac{2k-1}{2n}(b-a)\right)\right|\le Cn^{-2},\]
where $C$ is independent of $n$.
:::
