---
schema: qual/card@1
id: P-D75SD
kind: problem
title: Evaluate $\int\sin(x)\cos(\cos(x))\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
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
\int \sin x\,\cos(\cos x)\,dx.
\]
:::

::: solution
Let $u=\cos x$, so $du=-\sin x\,dx$. Then
\[
\int \sin x\,\cos(\cos x)\,dx
=-\int\cos u\,du
=\boxed{-\sin(\cos x)+C}.
\]
:::
