---
schema: qual/card@1
id: P-UNHGI
kind: problem
title: Antiderivative of $\frac{x+1}{x^2+2x+3}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int\frac{x+1}{x^2+2x+3}\,dx.
\]
:::

::: solution
Let $u=x^2+2x+3$, so $du=2(x+1)\,dx$. Therefore
\[
\boxed{\int\frac{x+1}{x^2+2x+3}\,dx=\frac12\ln(x^2+2x+3)+C.}
\]
:::
