---
schema: qual/card@1
id: P-EQFMD
kind: problem
title: Antiderivatives of $\frac{1\pm\sin x}{1+\cos x}$ and $\frac{1}{1+\sin x+\cos
  x}$
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
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Compute, on each interval where the integrand is defined,
\[
\int \frac{1-\sin x}{1+\cos x}\,dx,
\qquad
\int \frac{1+\sin x}{1+\cos x}\,dx,
\qquad
\int \frac{dx}{1+\sin x+\cos x}.
\]
:::

::: {.solution}
Use the tangent half-angle substitution
\[
u=\tan\frac x2,
\qquad
\sin x=\frac{2u}{1+u^2},
\qquad
\cos x=\frac{1-u^2}{1+u^2},
\qquad
dx=\frac{2\,du}{1+u^2}.
\]

<1>1. The minus-sign numerator.
::: {.proof}
Substitution gives
\[
\frac{1-\sin x}{1+\cos x}\,dx
=\left(1-\frac{2u}{1+u^2}\right)du.
\]
Hence
\[
\boxed{
\int \frac{1-\sin x}{1+\cos x}\,dx
=u-\log(1+u^2)+C,
\qquad u=\tan\frac x2.}
\]
Equivalently,
\[
\tan\frac x2+2\log\left|\cos\frac x2\right|+C
\]
or, after absorbing the constant \(\log2\),
\[
\tan\frac x2+\log|1+\cos x|+C.
\]
:::

<1>2. The plus-sign numerator.
::: {.proof}
Similarly,
\[
\frac{1+\sin x}{1+\cos x}\,dx
=\left(1+\frac{2u}{1+u^2}\right)du,
\]
so
\[
\boxed{
\int \frac{1+\sin x}{1+\cos x}\,dx
=u+\log(1+u^2)+C.}
\]
Equivalently,
\[
\tan\frac x2-2\log\left|\cos\frac x2\right|+C
=\tan\frac x2-\log|1+\cos x|+C.
\]
:::

<1>3. The denominator \(1+\sin x+\cos x\).
::: {.proof}
The same substitution gives
\[
\frac{dx}{1+\sin x+\cos x}
=\frac{du}{1+u}.
\]
Therefore
\[
\boxed{
\int\frac{dx}{1+\sin x+\cos x}
=\log\left|1+\tan\frac x2\right|+C.}
\]
:::
:::
