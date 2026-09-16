---
schema: qual/card@1
id: P-UCLAB16S-03
kind: problem
title: First-order error of a Riemann sum
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Suppose $f:[0,1]\to\mathbb R$ is continuously differentiable.
Show that the limit
\[
\lim_{n\to\infty} n\left(\sum_{k=0}^{n} f\!\left(\frac{k}{n}\right)-n\int_0^1 f(x)\,dx\right)
\]
exists and compute its value.
:::
