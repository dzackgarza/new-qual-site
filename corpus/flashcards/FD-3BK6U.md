---
schema: qual/card@1
id: FD-3BK6U
kind: definition
title: Chebyshev's Inequality
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
---

::: {.definition}
$$
\mu\qty{\{x \in\RR^n \suchthat \abs{f(x)} \geq \alpha\}} \leq \qty{\norm{f}_p \over \alpha }^p \quad \forall \alpha, p
.$$
Take $p=1$ to obtain
$$
\mu\qty{\{x \in \RR^n\suchthat \abs{f(x)} \geq \alpha\}} \leq {1\over \alpha } \int \abs{f(x)} \, dx \quad \forall \alpha
.$$
:::
