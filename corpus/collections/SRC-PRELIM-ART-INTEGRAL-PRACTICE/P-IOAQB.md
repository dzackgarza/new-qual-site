---
schema: qual/card@1
id: P-IOAQB
kind: problem
title: Integrals of $\frac{1}{x(\ln x)^2}$ and $\frac{1}{x^2}\cos\frac{1}{x}$
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
  note: Corrected the sign of the first stored antiderivative.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int\frac{dx}{x(\ln x)^2},
\qquad
\int_2^\infty\frac{dx}{x(\ln x)^2},
\]
and
\[
\int \frac1{x^2}\cos\!\left(\frac1x\right)\,dx.
\]
:::

::: solution
For the first integral, let $u=\ln x$, so $du=dx/x$:
\[
\int\frac{dx}{x(\ln x)^2}
=\int u^{-2}\,du
=\boxed{-\frac1{\ln x}+C}.
\]
Thus
\[
\int_2^\infty\frac{dx}{x(\ln x)^2}
=\lim_{R\to\infty}\left[-\frac1{\ln x}\right]_{2}^{R}
=\boxed{\frac1{\ln2}}.
\]
For the second antiderivative, let $u=1/x$, so $du=-dx/x^2$:
\[
\boxed{\int \frac1{x^2}\cos\!\left(\frac1x\right)\,dx=-\sin\!\left(\frac1x\right)+C.}
\]
:::
