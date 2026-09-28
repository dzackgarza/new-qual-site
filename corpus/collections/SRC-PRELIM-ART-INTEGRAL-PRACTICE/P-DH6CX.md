---
schema: qual/card@1
id: P-DH6CX
kind: problem
title: The substitution $u=1/x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: The collection has no preserved provenance and explicitly records that the original drill sheet was not found. Repository history contains no earlier version with the missing integrand, so the original problem statement cannot be recovered from available sources.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
- **Solution:** $u = \frac{1}{x}$, $du = -\frac{1}{x^2}\,dx$

- **Used 2018**
:::

::: {.solution}
For a continuous function $\Phi$, the substitution $u=1/x$, $du=-x^{-2}\,dx$ gives
\[
\int \frac{\Phi(1/x)}{x^2}\,dx=-\int \Phi(u)\,du.
\]
:::
