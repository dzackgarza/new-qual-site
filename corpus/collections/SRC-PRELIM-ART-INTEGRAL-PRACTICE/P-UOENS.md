---
schema: qual/card@1
id: P-UOENS
kind: problem
title: Evaluate $\int\sin x\cos x\cot x\tan x\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
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
\int \sin x\cos x\cot x\tan x\,dx.
\]
:::

::: solution
Where the integrand is defined,
\[
\cot x\tan x=1,
\]
so
\[
\int \sin x\cos x\,dx
=\boxed{\frac12\sin^2x+C.}
\]
The antiderivative extends across removable singularities of the simplified expression in the usual interval-by-interval sense.
:::
