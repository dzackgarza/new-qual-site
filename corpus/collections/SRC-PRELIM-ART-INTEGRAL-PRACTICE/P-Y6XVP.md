---
schema: qual/card@1
id: P-Y6XVP
kind: problem
title: Antiderivative of $e^{x+e^x}$
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
\int e^{x+e^x}\,dx.
\]
:::

::: solution
Since $e^{x+e^x}=e^x e^{e^x}$, let $u=e^x$. Then $du=e^x\,dx$, so
\[
\boxed{\int e^{x+e^x}\,dx=e^{e^x}+C.}
\]
:::
