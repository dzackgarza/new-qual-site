---
schema: qual/card@1
id: P-UVSXF
kind: problem
title: Antiderivative of $x\sqrt{x+1}$
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
  note: Corrected the exponent in the stored substitution work.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int x\sqrt{x+1}\,dx.
\]
:::

::: solution
Let $u=x+1$, so $x=u-1$ and $du=dx$. Then
\[
(u-1)u^{1/2}=u^{3/2}-u^{1/2},
\]
so
\[
\int x\sqrt{x+1}\,dx
=\frac25u^{5/2}-\frac23u^{3/2}+C.
\]
Therefore
\[
\boxed{\int x\sqrt{x+1}\,dx=\frac25(x+1)^{5/2}-\frac23(x+1)^{3/2}+C.}
\]
:::
