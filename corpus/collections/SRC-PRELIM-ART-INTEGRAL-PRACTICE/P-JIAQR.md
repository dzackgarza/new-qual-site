---
schema: qual/card@1
id: P-JIAQR
kind: problem
title: Evaluate $\int\frac{x}{1+x^4}\,dx$
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
\int\frac{x}{1+x^4}\,dx.
\]
:::

::: solution
Let $u=x^2$, so $du=2x\,dx$. Then
\[
\boxed{\int\frac{x}{1+x^4}\,dx=\frac12\arctan(x^2)+C.}
\]
:::
