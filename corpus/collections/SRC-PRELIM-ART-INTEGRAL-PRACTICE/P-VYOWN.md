---
schema: qual/card@1
id: P-VYOWN
kind: problem
title: Antiderivatives of $\frac{x+\sin x}{1+\cos x}$ and $\frac{xe^x}{(e^x+1)^2}$
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
\int\frac{x+\sin x}{1+\cos x}\,dx
\]
and
\[
\int\frac{x e^x}{(e^x+1)^2}\,dx.
\]
:::

::: solution
Since
\[
\frac{\sin x}{1+\cos x}=\tan\frac x2,
\qquad
\frac1{1+\cos x}=\frac12\sec^2\frac x2,
\]
the first integrand is the derivative of $x\tan(x/2)$. Hence
\[
\boxed{\int\frac{x+\sin x}{1+\cos x}\,dx=x\tan\frac x2+C.}
\]

For the second, integrate by parts using
\[
\frac{e^x}{(e^x+1)^2}
=-\frac{d}{dx}\frac1{e^x+1}.
\]
Then
\[
\int\frac{x e^x}{(e^x+1)^2}\,dx
=-\frac{x}{e^x+1}+\int\frac{dx}{e^x+1}.
\]
Since
\[
\int\frac{dx}{e^x+1}=x-\ln(e^x+1)+C,
\]
we obtain
\[
\boxed{\int\frac{x e^x}{(e^x+1)^2}\,dx
=\frac{x e^x}{e^x+1}-\ln(e^x+1)+C.}
\]
:::
