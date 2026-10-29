---
schema: qual/card@1
id: E-BPEP3
kind: problem
title: Entire functions with a pole at infinity are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
  - Poles
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Find all entire functions with have poles at infinity"; the statement corrects "with" to "which".
---

::: {.problem}
Find all entire functions which have poles at $\infty$.
:::

::: {.solution}
Let $f(z) = \sum_{k\geq 0}c_k z^k$ be entire and $g(z) \coloneqq f(1/z) = \sum_{k\geq 0}c_k z^{-k}$ for $z\neq0$.

::: pf

::: pf-step
If $\infty$ is a pole of order $m\ge1$ of $f$, then $f$ is a polynomial of degree $m$.

::: pf-proof
By definition, $0$ is then a pole of order $m$ of $g$.
The series for $g$ is its Laurent series on $\theset{z\neq0}$, so $c_k=0$ for $k>m$ and $c_m\neq0$.
:::

:::

::: pf-step
The entire functions with a pole at $\infty$ are exactly the $\boxed{\text{nonconstant polynomials}}$.

::: pf-proof
A polynomial of degree $m\ge1$ gives $g(z)=\sum_{k=0}^mc_kz^{-k}$ with $c_m\neq0$, which has a pole of order $m$ at $0$.
Combine with the previous step.
:::

:::

:::

:::
