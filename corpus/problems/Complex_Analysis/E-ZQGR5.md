---
schema: qual/card@1
id: E-ZQGR5
kind: exercise
title: Radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

::: {.exercise}
Find the radius of convergence of

- $\sum a^k z^k$ for $a$ a constant.

- $\sum a^{k^2}z^k$
:::

::: {.solution}
\envlist

- $R = {1 \over \limsup \abs{a^k}^{1\over k}} = {1\over \abs{a}}$

- $R = {1 \over \limsup \abs{a^{k^2}}^{1\over k}} = {1\over \limsup \abs{a}^k}$, so $R=\infty$ if $\abs{a}< 1$, $R=0$ if $\abs{a}<1$, and $R=1$ if $\abs{a} = 1$.
:::
