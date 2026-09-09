---
schema: qual/card@1
id: P-R67LO
kind: problem
title: Antiderivatives of trigonometric products of $\sin x$ and $\cos x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
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
\int(\sin x+\cos x)^2dx,
\]
\[
\int\frac32\sin(2x)(\sin x+\cos x)dx,
\quad
\int\cos^2x(1+\sin x)dx,
\]
\[
\int\sin^3x\cos^5x\,dx,
\quad
\int\cos^3x\sin x\,dx,
\quad
\int\sin^3x\sqrt{\cos x}\,dx.
\]
:::

::: solution
Direct expansion/substitution gives, respectively,
\[
\boxed{x-\frac12\cos2x+C,}
\]
\[
\boxed{\sin^3x-\cos^3x+C,}
\]
\[
\boxed{-\frac13\cos^3x+\frac12(x+\sin x\cos x)+C,}
\]
\[
\boxed{-\frac16\cos^6x+\frac18\cos^8x+C,}
\]
\[
\boxed{-\frac14\cos^4x+C,}
\]
and, on intervals where $\sqrt{\cos x}$ is real,
\[
\boxed{-\frac23\cos^{3/2}x+\frac27\cos^{7/2}x+C.}
\]
For example, the fourth follows by writing $\sin^3x=\sin x(1-\cos^2x)$ and taking $u=\cos x$; the other odd-power cases are analogous.
:::
