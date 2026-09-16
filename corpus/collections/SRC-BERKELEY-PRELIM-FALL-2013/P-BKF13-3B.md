---
schema: qual/card@1
id: P-BKF13-3B
kind: problem
title: Integrability of $\int_x^1 f(t)/t\,dt$ for integrable $f$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in g and moved the codomain inside math against F13_Exam.pdf page 14 problem 3B.
---

::: {.problem}
Suppose that $f : (0, 1) \to \mathbf{R}$ is a continuous function with $\int_0^1 |f(t)| \, dt < \infty$. Define $g : (0, 1) \to \mathbf{R}$ by

$$
g(x) = \int_x^1 \frac{f(t)}{t} \, dt.
$$

Show that $\int_0^1 |g(x)| \, dx < \infty$.
:::
