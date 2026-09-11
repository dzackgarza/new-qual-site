---
schema: qual/card@1
id: P-BKF18-7B
kind: problem
title: Multivariate Gaussian integral with a linear term
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
For a real symmetric positive definite matrix $A$ and $v\in\mathbb R^n$, show that
\[
\int_{\mathbb R^n}\exp(-x^TAx+2v^Tx)\,dx
=\frac{\pi^{n/2}}{\sqrt{\det A}}\exp(v^TA^{-1}v).
\]
You may assume that $\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi$.
:::
