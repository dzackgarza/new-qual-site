---
schema: qual/card@1
id: P-PAVWJ
kind: problem
title: Integrals of rational functions with $x^2+1$ in the denominator
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Partial Fractions
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
Evaluate the nine rational antiderivatives listed below:
\[
\frac{x^2}{x^2+1},\quad
\frac{4x^2+x+7}{x^2+1},\quad
\frac{3x^2+x+3}{x(x^2+1)},\quad
\frac{2x-3}{x^3+x},
\]
\[
\frac{4x^2-11x-19}{(x-5)(x^2+1)},\quad
\frac{3x^2+2x-7}{(x-5)(x^2+1)},
\]
\[
\frac{-2x+4}{(x^2+1)(x-1)^2},\quad
\frac{x^4+2x^3+5x^2+4x+6}{x^3+x^2+x+1},
\]
and
\[
\frac{2x^5+4x^3+4x}{x^4+1}.
\]
:::

::: solution
The corresponding primitives are, respectively,
\[
\boxed{x-\arctan x+C,}
\]
\[
\boxed{4x+\frac12\ln(x^2+1)+3\arctan x+C,}
\]
\[
\boxed{3\ln|x|+\arctan x+C,}
\]
\[
\boxed{-3\ln|x|+\frac32\ln(x^2+1)+2\arctan x+C,}
\]
\[
\boxed{\ln|x-5|+\frac32\ln(x^2+1)+4\arctan x+C,}
\]
\[
\boxed{3\ln|x-5|+2\arctan x+C,}
\]
\[
\boxed{-2\ln|x-1|-\frac1{x-1}+\ln(x^2+1)+\arctan x+C,}
\]
\[
\boxed{\frac12x^2+x+3\ln|x+1|+2\arctan x+C,}
\]
and
\[
\boxed{x^2+\ln(x^4+1)+\arctan(x^2)+C.}
\]
Each follows directly from the partial-fraction decompositions already encoded in the card; differentiating the displayed primitives recovers the corresponding rational integrand.
:::
