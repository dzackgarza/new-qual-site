---
schema: qual/card@1
id: P-W6TOK
kind: problem
title: Antiderivatives of $\frac{x}{x^4-16}$ and $\frac{x\tan^{-1}x}{(x^2+1)^2}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
  - Partial Fractions
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

::: problem
Compute, on each interval where the integrand is defined,
\[
\int \frac{x}{x^4-16}\,dx,
\qquad
\int \frac{x\arctan x}{(x^2+1)^2}\,dx.
\]
:::

::: solution
<1>1. Integrate \(x/(x^4-16)\).
::: proof
Let \(u=x^2\), so \(du=2x\,dx\). Then
\[
\int\frac{x}{x^4-16}\,dx
=\frac12\int\frac{du}{u^2-16}.
\]
Since
\[
\frac1{u^2-16}=\frac18\left(\frac1{u-4}-\frac1{u+4}\right),
\]
we get
\[
\boxed{
\int\frac{x}{x^4-16}\,dx
=\frac1{16}\log\left|\frac{x^2-4}{x^2+4}\right|+C.}
\]
:::

<1>2. Integrate \(x\arctan x/(1+x^2)^2\).
::: proof
Integrate by parts with
\[
u=\arctan x,
\qquad
dv=\frac{x\,dx}{(1+x^2)^2}.
\]
Then
\[
du=\frac{dx}{1+x^2},
\qquad
v=-\frac1{2(1+x^2)},
\]
so
\[
I=-\frac{\arctan x}{2(1+x^2)}
+\frac12\int\frac{dx}{(1+x^2)^2}.
\]
For the remaining integral, put \(x=\tan t\). Then
\[
\int\frac{dx}{(1+x^2)^2}
=\int\cos^2t\,dt
=\frac t2+\frac{\sin2t}{4}+C.
\]
Since \(t=\arctan x\) and \(\sin2t=2x/(1+x^2)\),
\[
\int\frac{dx}{(1+x^2)^2}
=\frac12\arctan x+\frac{x}{2(1+x^2)}+C.
\]
Therefore
\[
\boxed{
\int\frac{x\arctan x}{(1+x^2)^2}\,dx
=-\frac{\arctan x}{2(1+x^2)}
+\frac{x}{4(1+x^2)}
+\frac14\arctan x+C.}
\]
:::
:::
