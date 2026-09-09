---
schema: qual/card@1
id: P-FDWKY
kind: problem
title: Partial-fraction antiderivatives of six rational functions
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
Evaluate the six rational antiderivatives
\[
\int\frac{x}{x-1}\,dx,
\quad
\int\frac{7x+5}{x^2+x-2}\,dx,
\quad
\int\frac{x}{x^2-x-6}\,dx,
\]
\[
\int\frac{1+x^2}{1-x^2}\,dx,
\quad
\int\frac{dx}{x(x-1)^2},
\quad
\int\frac{x}{(x+5)^2}\,dx.
\]
:::

::: solution
Using elementary partial fractions,
\[
\frac{x}{x-1}=1+\frac1{x-1},
\]
so
\[
\boxed{x+\ln|x-1|+C.}
\]
Also
\[
\frac{7x+5}{(x+2)(x-1)}=\frac3{x+2}+\frac4{x-1},
\]
hence
\[
\boxed{3\ln|x+2|+4\ln|x-1|+C.}
\]
Next,
\[
\frac{x}{(x-3)(x+2)}=\frac{3/5}{x-3}+\frac{2/5}{x+2},
\]
so
\[
\boxed{\frac35\ln|x-3|+\frac25\ln|x+2|+C.}
\]
Further,
\[
\frac{1+x^2}{1-x^2}=-1+\frac1{x+1}-\frac1{x-1},
\]
therefore
\[
\boxed{-x+\ln|x+1|-\ln|x-1|+C.}
\]
For the repeated factor,
\[
\frac1{x(x-1)^2}=\frac1x-\frac1{x-1}+\frac1{(x-1)^2},
\]
which gives
\[
\boxed{\ln|x|-\ln|x-1|-\frac1{x-1}+C.}
\]
Finally,
\[
\frac{x}{(x+5)^2}=\frac1{x+5}-\frac5{(x+5)^2},
\]
so
\[
\boxed{\ln|x+5|+\frac5{x+5}+C.}
\]
:::
