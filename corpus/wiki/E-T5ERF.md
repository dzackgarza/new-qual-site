---
schema: qual/card@1
id: E-T5ERF
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$ near $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - mean-value-property
  - cauchy-estimates
  - holomorphic-functions
relations: []
review: draft
solved: false
---

::: problem
Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$.
Show that for any $s<r$, there exists a constant $c>0$ such that $$||f||_{(\infty, s)} \leq c ||f||_{(1, r)},$$ where $\displaystyle |f||_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$ and $\displaystyle ||f||_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.

> Note: Exercise 3.8.20 on p.107 in Stein et al is a straightforward consequence of this stronger result using the integral form of the Cauchy-Schwarz inequality in real analysis.
:::
