---
schema: qual/card@1
id: P-F6K7Y
kind: problem
title: Antiderivatives of powers of $\sec x$ and $\tan x$
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
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected the final logarithmic form in item 8 and removed the unresolved question marks.
---

::: problem
Evaluate
\[
\int\sec^3x\,dx,\quad \int\sec^4x\,dx,\quad
\int\tan^2x\,dx,\quad \int\tan^3x\,dx,
\]
\[
\int\tan^4x\,dx,\quad
\int\sec^3x\tan^3x\,dx,
\quad
\int(\tan^4x+\tan^2x)\,dx,
\]
and
\[
\int\frac{2\sin^2x}{\cos^3x}\,dx.
\]
:::

::: solution
Standard reduction and $u$-substitutions give
\[
\boxed{\int\sec^3x\,dx
=\frac12\bigl(\sec x\tan x+\ln|\sec x+\tan x|\bigr)+C,}
\]
\[
\boxed{\int\sec^4x\,dx=\tan x+\frac13\tan^3x+C,}
\]
\[
\boxed{\int\tan^2x\,dx=\tan x-x+C,}
\]
\[
\boxed{\int\tan^3x\,dx=\frac12\tan^2x+\ln|\cos x|+C,}
\]
\[
\boxed{\int\tan^4x\,dx=\frac13\tan^3x-\tan x+x+C.}
\]
For the mixed powers, use $u=\sec x$ in the first and $u=\tan x$ in the second:
\[
\boxed{\int\sec^3x\tan^3x\,dx=\frac15\sec^5x-\frac13\sec^3x+C,}
\]
\[
\boxed{\int(\tan^4x+\tan^2x)dx=\frac13\tan^3x+C.}
\]
Finally,
\[
\frac{2\sin^2x}{\cos^3x}=2(\sec^3x-\sec x),
\]
so
\[
\boxed{\int\frac{2\sin^2x}{\cos^3x}dx
=\sec x\tan x-\ln|\sec x+\tan x|+C.}
\]
Using $(\sec x-\tan x)(\sec x+\tan x)=1$, this is equivalently
\[
\sec x\tan x+\ln|\sec x-\tan x|+C.
\]
:::
