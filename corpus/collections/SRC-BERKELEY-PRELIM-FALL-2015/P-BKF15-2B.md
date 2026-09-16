---
schema: qual/card@1
id: P-BKF15-2B
kind: problem
title: A function starting at $1$ that cannot increase above $1$ stays at most $1$
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
  note: Statement checked against F15_Exam.pdf problem 2B; restored the lost arrow and the bullets for the last two hypotheses.
---

::: {.problem}
Let $f \colon [0, \infty) \to \mathbb{R}$ be a function, and assume that:

- $f$ is continuous on $[0, \infty)$;
- $f$ is differentiable on $(0, \infty)$;
- $f'(x) \leq 0$ for all $x > 0$ such that $f(x) > 1$; and
- $f(0) = 1$.

Prove that $f(x) \leq 1$ for all $x \geq 0$.
:::
