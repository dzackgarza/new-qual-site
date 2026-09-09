---
schema: qual/card@1
id: P-PHHXJ
kind: problem
title: Integrals of $\sqrt{1-x^2}$, $\sqrt{16-x^2}$ on $[-4,4]$, and $(1+x)\sqrt{1-x^2}$
  on $[-1,1]$
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
\int\sqrt{1-x^2}\,dx,
\qquad
\int_{-4}^{4}\sqrt{16-x^2}\,dx,
\]
and
\[
\int_{-1}^{1}(1+x)\sqrt{1-x^2}\,dx.
\]
:::

::: solution
For the antiderivative, set $x=\sin u$. Then $dx=\cos u\,du$ and
\[
\sqrt{1-x^2}=\cos u
\]
on the principal substitution interval, so
\[
\int\sqrt{1-x^2}\,dx
=\int\cos^2u\,du
=\frac12\left(u+\sin u\cos u\right)+C.
\]
Thus
\[
\boxed{\int\sqrt{1-x^2}\,dx=\frac12\left(\arcsin x+x\sqrt{1-x^2}\right)+C.}
\]

The graph of $y=\sqrt{16-x^2}$ is the upper semicircle of radius $4$, so
\[
\boxed{\int_{-4}^{4}\sqrt{16-x^2}\,dx=8\pi.}
\]
Finally,
\[
\int_{-1}^{1}(1+x)\sqrt{1-x^2}\,dx
=\int_{-1}^{1}\sqrt{1-x^2}\,dx
+\int_{-1}^{1}x\sqrt{1-x^2}\,dx.
\]
The second integrand is odd, hence its integral is $0$, while the first integral is the area of a semicircle of radius $1$. Therefore
\[
\boxed{\int_{-1}^{1}(1+x)\sqrt{1-x^2}\,dx=\frac\pi2.}
\]
:::
