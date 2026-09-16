---
schema: qual/card@1
id: P-BKS81-4
kind: problem
title: Global dynamics approaching the unit circle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Consider
\[
\frac{dx}{dt}=y+x(1-x^2-y^2),
\qquad
\frac{dy}{dt}=-x+y(1-x^2-y^2).
\]

1. Show that for every initial condition $(x(0),y(0))=(x_0,y_0)$ there is a unique solution defined for all $t\in\mathbb R$.
2. Show that if $x_0\ne0$ and $y_0\ne0$, then the solution approaches the circle $x^2+y^2=1$ as $t\to\infty$.
:::
