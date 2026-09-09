---
schema: qual/card@1
id: P-KAQ4G
kind: problem
title: Evaluate $\int\frac{\sin x}{\cos^2 x}\,dx$ and $\int\csc(ax)\cot(ax)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
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
\int\frac{\sin x}{\cos^2x}\,dx
\qquad\text{and}\qquad
\int\csc(ax)\cot(ax)\,dx,
\]
where $a\ne0$.
:::

::: solution
Using $\sin x/\cos^2x=\tan x\sec x$ and $(\sec x)'=\sec x\tan x$,
\[
\boxed{\int\frac{\sin x}{\cos^2x}\,dx=\sec x+C.}
\]
Also $(\csc(ax))'=-a\csc(ax)\cot(ax)$, so
\[
\boxed{\int\csc(ax)\cot(ax)\,dx=-\frac1a\csc(ax)+C.}
\]
:::
