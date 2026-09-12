---
schema: qual/card@1
id: P-E5WUU
kind: problem
title: Evaluate $\int_0^1\int_y^1\sin(x^2)\,dx\,dy$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Multivariable Calculus
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
\int_0^1\int_y^1\sin(x^2)\,dx\,dy.
\]
:::

::: solution
The region is $0\le y\le x\le1$. Reversing the order of integration,
\[
\int_0^1\int_y^1\sin(x^2)\,dx\,dy
=\int_0^1\int_0^x\sin(x^2)\,dy\,dx
=\int_0^1x\sin(x^2)\,dx.
\]
With $u=x^2$,
\[
\int_0^1x\sin(x^2)\,dx
=\frac12\int_0^1\sin u\,du
=\frac{1-\cos1}{2}
=\boxed{\sin^2\!\left(\frac12\right)}.
\]
:::
