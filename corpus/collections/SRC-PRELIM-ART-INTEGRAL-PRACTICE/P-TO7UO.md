---
schema: qual/card@1
id: P-TO7UO
kind: problem
title: Antiderivative of $\frac{1+e^x}{1-e^x}$
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
  note: Corrected the missing factor of 2 in the stored antiderivative.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int \frac{1+e^x}{1-e^x}\,dx.
\]
:::

::: solution
Put $u=e^x$, so $dx=du/u$. Then
\[
\frac{1+u}{u(1-u)}=\frac1u+\frac2{1-u}.
\]
Hence
\[
\int \frac{1+e^x}{1-e^x}\,dx
=\ln u-2\ln|1-u|+C
=\boxed{x-2\ln|1-e^x|+C}.
\]
:::
