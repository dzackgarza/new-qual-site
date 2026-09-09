---
schema: qual/card@1
id: P-UUACQ
kind: problem
title: Antiderivative of $\frac{x}{\sqrt{4-x^4}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
  - Trigonometric Substitution
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
Evaluate, on an interval where the integrand is real,
\[
\int\frac{x}{\sqrt{4-x^4}}\,dx.
\]
:::

::: solution
Let $u=x^2/2$, so $du=x\,dx$ and
\[
\sqrt{4-x^4}=2\sqrt{1-u^2}.
\]
Therefore
\[
\int\frac{x}{\sqrt{4-x^4}}\,dx
=\frac12\int\frac{du}{\sqrt{1-u^2}}
=\boxed{\frac12\arcsin\!\left(\frac{x^2}{2}\right)+C.}
\]
:::
