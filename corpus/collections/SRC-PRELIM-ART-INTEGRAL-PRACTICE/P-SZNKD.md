---
schema: qual/card@1
id: P-SZNKD
kind: problem
title: Evaluate $\int\frac{x^2}{1+x^6}\,dx$
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
\int\frac{x^2}{1+x^6}\,dx.
\]
:::

::: solution
Let $u=x^3$, so $du=3x^2\,dx$. Therefore
\[
\boxed{\int\frac{x^2}{1+x^6}\,dx=\frac13\arctan(x^3)+C.}
\]
:::
