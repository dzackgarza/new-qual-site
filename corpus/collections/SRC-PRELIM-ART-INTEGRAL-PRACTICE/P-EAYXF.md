---
schema: qual/card@1
id: P-EAYXF
kind: problem
title: Evaluate $\int\frac{e^x}{e^x+1}\,dx$
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
\int \frac{e^x}{e^x+1}\,dx.
\]
:::

::: solution
Let $u=e^x+1$, so $du=e^x\,dx$. Then
\[
\boxed{\int \frac{e^x}{e^x+1}\,dx=\ln(e^x+1)+C.}
\]
:::
