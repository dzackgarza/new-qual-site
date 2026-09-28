---
schema: qual/card@1
id: P-BKF18-1B
kind: problem
title: Integral-test error for the Basel series
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Estimate $\pi^2/6=\sum_{n=1}^{\infty}1/n^2$ by the sum of the first $N$ terms.
What is the smallest $N$ such that the error is at most $10^{-6}$?
Use the integral test.
:::

::: {.solution}
The integral test shows that $\begin{array} { r } { 1 / ( N + 1 ) < \sum _ { n = N + 1 } ^ { \infty } 1 / n ^ { 2 } < 1 / N . } \end{array}$ , so $N = 1 0 ^ { 6 }$

Score:
:::
