---
schema: qual/card@1
id: P-PV5GI
kind: problem
title: Integrals of $\frac{\sqrt{1+\ln x}}{x\ln x}$, $\frac{7-\ln x}{x(3+\ln x)}$,
  $\frac{\sec^2 x}{1+\tan x}$, $\frac{\sin x}{\sqrt{4-\cos^2 x}}$, and $\frac{\sec^2
  x}{\sqrt{9-\tan^2 x}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the sign of the final arcsine antiderivative and restored absolute values/constants where required.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate the five antiderivatives
\[
\int\frac{\sqrt{1+\ln x}}{x\ln x}\,dx,
\quad
\int\frac{7-\ln x}{x(3+\ln x)}\,dx,
\]
\[
\int\frac{\sec^2x}{1+\tan x}\,dx,
\quad
\int\frac{\sin x}{\sqrt{4-\cos^2x}}\,dx,
\quad
\int\frac{\sec^2x}{\sqrt{9-\tan^2x}}\,dx,
\]
on intervals where the displayed expressions are real and defined.
:::

::: solution
For the first, put $u=\sqrt{1+\ln x}$. Then $\ln x=u^2-1$ and $dx/x=2u\,du$, so
\[
\frac{\sqrt{1+\ln x}}{x\ln x}\,dx
=\frac{2u^2}{u^2-1}\,du
=\left(2+\frac1{u-1}-\frac1{u+1}\right)du.
\]
Hence
\[
\boxed{2\sqrt{1+\ln x}+\ln\left|\frac{\sqrt{1+\ln x}-1}{\sqrt{1+\ln x}+1}\right|+C.}
\]

For the second,
\[
\frac{7-\ln x}{3+\ln x}=-1+\frac{10}{3+\ln x},
\]
so
\[
\boxed{-\ln x+10\ln|3+\ln x|+C.}
\]

For the third, $u=1+\tan x$ gives
\[
\boxed{\ln|1+\tan x|+C.}
\]

For the fourth, $u=\cos x/2$ gives $du=-\tfrac12\sin x\,dx$ and
\[
\boxed{-\arcsin\!\left(\frac{\cos x}{2}\right)+C.}
\]

For the fifth, $u=\tan x/3$ gives $du=\tfrac13\sec^2x\,dx$ and
\[
\boxed{\arcsin\!\left(\frac{\tan x}{3}\right)+C.}
\]
The sign here is positive; the stored negative sign came from an incorrect sign in $du$.
:::
