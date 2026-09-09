---
schema: qual/card@1
id: P-XIKRI
kind: problem
title: Evaluate $\int\frac{4x^3+2x}{x^4+1}\,dx$
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
\int\frac{4x^3+2x}{x^4+1}\,dx.
\]
:::

::: solution
Split the integral:
\[
\int\frac{4x^3}{x^4+1}\,dx+\int\frac{2x}{x^4+1}\,dx.
\]
The first is $\ln(x^4+1)$. In the second, put $u=x^2$, so $du=2x\,dx$ and the denominator is $u^2+1$. Thus
\[
\boxed{\int\frac{4x^3+2x}{x^4+1}\,dx=\ln(x^4+1)+\arctan(x^2)+C.}
\]
:::
