---
schema: qual/card@1
id: P-NHFXM
kind: problem
title: Antiderivatives of $\frac{1}{\sin x+\cos x}$ and $\frac{\sin x}{1\pm\sin x}$
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
\int\frac{dx}{\sin x+\cos x},
\qquad
\int\frac{\sin x}{1+\sin x}\,dx,
\qquad
\int\frac{\sin x}{1-\sin x}\,dx.
\]
Also deduce antiderivatives of \(1/(1+\sin x)\) and \(\tan x/(\tan x+\sec x)\).
:::

::: {.solution}
<1>1. Integrate \(1/(\sin x+\cos x)\).
::: {.proof}
Since
\[
\sin x+\cos x=\sqrt2\sin\left(x+\frac\pi4\right),
\]
we obtain
\[
\int\frac{dx}{\sin x+\cos x}
=\frac1{\sqrt2}\int \csc\left(x+\frac\pi4\right)\,dx.
\]
Using \(\int\csc u\,du=\log|\tan(u/2)|+C\),
\[
\boxed{
\int\frac{dx}{\sin x+\cos x}
=\frac1{\sqrt2}\log\left|\tan\left(\frac x2+\frac\pi8\right)\right|+C.}
\]
Equivalently this is
\[
-\frac1{\sqrt2}\log\left|\csc\left(x+\frac\pi4\right)+\cot\left(x+\frac\pi4\right)\right|+C.
\]
:::

<1>2. Integrate \(\sin x/(1+\sin x)\).
::: {.proof}
Write
\[
\frac{\sin x}{1+\sin x}=1-\frac1{1+\sin x}.
\]
Rationalizing,
\[
\frac1{1+\sin x}
=\frac{1-\sin x}{\cos^2x}
=\sec^2x-\sec x\tan x.
\]
Hence
\[
\int\frac{dx}{1+\sin x}=\tan x-\sec x+C,
\]
and therefore
\[
\boxed{
\int\frac{\sin x}{1+\sin x}\,dx
=x+\sec x-\tan x+C.}
\]
Since
\[
\frac{\tan x}{\tan x+\sec x}=\frac{\sin x}{1+\sin x},
\]
the same antiderivative applies to that quotient.
:::

<1>3. Integrate \(\sin x/(1-\sin x)\).
::: {.proof}
Now
\[
\frac{\sin x}{1-\sin x}=-1+\frac1{1-\sin x},
\]
and
\[
\frac1{1-\sin x}
=\frac{1+\sin x}{\cos^2x}
=\sec^2x+\sec x\tan x.
\]
Thus
\[
\boxed{
\int\frac{\sin x}{1-\sin x}\,dx
=-x+\tan x+\sec x+C.}
\]
:::
:::
