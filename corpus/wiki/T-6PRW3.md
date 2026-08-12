---
schema: qual/card@1
id: T-6PRW3
kind: theorem
title: "Tonelli (Non-Negative, Measurable)"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.theorem title="Tonelli (Non-Negative, Measurable)"}
For $f(x, y)$ **non-negative and measurable**, for almost every $x\in \RR^n$,

- $f_x(y)$ is a **measurable** function

- $F(x) = \int f(x, y) ~dy$ is a **measurable** function,

- For $E$ measurable, the slices $E_x \definedas \theset{y \suchthat (x, y) \in E}$ are measurable.

- $\int f = \int \int F$, i.e. any iterated integral is equal to the original.
:::
