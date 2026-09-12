---
schema: qual/card@1
id: P-OY6YK
kind: problem
title: Integrals of $\frac{x^2+2x+1}{x\sqrt{x^2-1}}$ and $\frac{x+16}{\sqrt{x^2-4x+8}}$
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
  note: Replaced branch-sensitive inverse-secant notation by an arctangent primitive and restored constants/domains.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate, on intervals where the real-valued integrands are defined,
\[
\int\frac{x^2+2x+1}{x\sqrt{x^2-1}}\,dx
\]
and
\[
\int\frac{x+16}{\sqrt{x^2-4x+8}}\,dx.
\]
:::

::: solution
For the first integral, split
\[
\frac{x^2+2x+1}{x\sqrt{x^2-1}}
=\frac{x}{\sqrt{x^2-1}}+\frac2{\sqrt{x^2-1}}+\frac1{x\sqrt{x^2-1}}.
\]
The three primitives are respectively
\[
\sqrt{x^2-1},\qquad 2\ln|x+\sqrt{x^2-1}|,
\qquad \arctan\sqrt{x^2-1}.
\]
Thus
\[
\boxed{\sqrt{x^2-1}+2\ln|x+\sqrt{x^2-1}|+\arctan\sqrt{x^2-1}+C.}
\]

For the second integral, write
\[
x^2-4x+8=(x-2)^2+4,
\qquad x+16=(x-2)+18.
\]
Then
\[
\boxed{\int\frac{x+16}{\sqrt{x^2-4x+8}}\,dx
=\sqrt{x^2-4x+8}+18\ln\!\left|x-2+\sqrt{x^2-4x+8}\right|+C.}
\]
:::
