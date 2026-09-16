---
schema: qual/card@1
id: P-BKS17-3A
kind: problem
title: Positive functions satisfying $\int_x^y f(x)f(y)/f(t)^2\,dt=\sin(y-x)$
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
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 4 problem 3A.
---

::: {.problem}
Suppose we have a continuous positive function $f : (0, \pi) \to (0, \infty)$ such that for all $x, y \in (0, \pi)$ we have

$$
\int_x^y \frac{f(x) f(y)}{f^2(t)} \, dt = \sin(y - x).
$$

(a) Show that $\sin(z - x) f(y) = \sin(y - x) f(z) + \sin(z - y) f(x)$.

(b) Find all possibilities for $f$.
:::
