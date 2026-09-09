---
schema: qual/card@1
id: P-NKCDN
kind: problem
title: Evaluate $\int e^x\cos x\,dx$ and $\int\sin(\ln x)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
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
\int e^x\cos x\,dx
\qquad\text{and}\qquad
\int\sin(\ln x)\,dx,
\quad x>0.
\]
:::

::: solution
Integrating the first integral by parts twice yields
\[
\boxed{\int e^x\cos x\,dx=\frac12e^x(\cos x+\sin x)+C.}
\]
For the second, let $u=\ln x$, so $dx=e^u du$. Then
\[
\int\sin(\ln x)\,dx=\int e^u\sin u\,du
=\boxed{\frac x2\left(\sin(\ln x)-\cos(\ln x)\right)+C.}
\]
:::
