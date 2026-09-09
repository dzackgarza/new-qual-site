---
schema: qual/card@1
id: P-YFZRX
kind: problem
title: Evaluate $\int x\sec^{-1}(x)\,dx$
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
  note: Corrected the second mislabeled inverse-trigonometric integral and made the branch domain explicit.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
For $x>1$, evaluate
\[
\int x\,\sec^{-1}(x)\,dx
\qquad\text{and}\qquad
\int x\,\csc^{-1}(x)\,dx.
\]
:::

::: solution
For $x>1$,
\[
\frac{d}{dx}\sec^{-1}x=\frac1{x\sqrt{x^2-1}},
\qquad
\frac{d}{dx}\csc^{-1}x=-\frac1{x\sqrt{x^2-1}}.
\]
Integration by parts gives
\[
\boxed{\int x\sec^{-1}x\,dx
=\frac12\left(x^2\sec^{-1}x-\sqrt{x^2-1}\right)+C,}
\]
and
\[
\boxed{\int x\csc^{-1}x\,dx
=\frac12\left(x^2\csc^{-1}x+\sqrt{x^2-1}\right)+C.}
\]
:::
