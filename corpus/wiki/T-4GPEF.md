---
schema: qual/card@1
id: T-4GPEF
kind: theorem
title: "Fubini (Integrable)"
classification:
  areas:
  - real-analysis
  topics:
  - fubini-tonelli
  - integrals
relations: []
review: draft
---

::: {.theorem title="Fubini (Integrable)"}
For $f(x, y)$ **integrable**, for almost every $x\in \RR^n$,

- $f_x(y)$ is an **integrable** function

- $F(x) \definedas \int f(x, y) ~dy$ is an **integrable** function,

- For $E$ measurable, the slices $E_x \definedas \theset{y \suchthat (x, y) \in E}$ are measurable.

- $\int f = \int \int f(x,y)$, i.e. any iterated integral is equal to the original
:::
