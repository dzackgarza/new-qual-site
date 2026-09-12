---
schema: qual/card@1
id: P-XRZVW
kind: problem
title: Antiderivatives of $\frac{1}{\sqrt{x^2+25}}$ and $\frac{1}{(1+x^2)^{3/2}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
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
Evaluate
\[
\int\frac{dx}{\sqrt{x^2+25}}
\qquad\text{and}\qquad
\int\frac{dx}{(1+x^2)^{3/2}}.
\]
:::

::: solution
For the first integral, the standard hyperbolic/trigonometric substitution gives
\[
\boxed{\int\frac{dx}{\sqrt{x^2+25}}
=\ln\!\left(x+\sqrt{x^2+25}\right)+C.}
\]
The logarithm's argument is positive for every real $x$.

For the second,
\[
\frac{d}{dx}\left(\frac{x}{\sqrt{1+x^2}}\right)
=\frac1{(1+x^2)^{3/2}},
\]
so
\[
\boxed{\int\frac{dx}{(1+x^2)^{3/2}}
=\frac{x}{\sqrt{1+x^2}}+C.}
\]
:::
