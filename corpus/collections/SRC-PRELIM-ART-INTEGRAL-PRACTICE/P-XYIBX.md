---
schema: qual/card@1
id: P-XYIBX
kind: problem
title: Evaluate $\int\frac{1-\sqrt{x}}{1+\sqrt{x}}\,dx$
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
  note: Corrected the first stored logarithmic antiderivative and normalized constants, absolute values, and real domains across the bundle.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate the following antiderivatives on intervals where the real-valued integrands are defined:

1. $\displaystyle \int \frac{1-\sqrt x}{1+\sqrt x}\,dx$.
2. $\displaystyle \int \frac{dx}{\sqrt x+2\sqrt[3]x}$.
3. $\displaystyle \int \frac{dx}{\sqrt x-\sqrt[3]x}$.
4. $\displaystyle \int \frac{dx}{\sqrt x+\sqrt[4]x}$.
5. $\displaystyle \int \frac{\sqrt[3]x+1}{\sqrt[3]x-1}\,dx$.
6. $\displaystyle \int \frac{dx}{(x+1)\sqrt x}$ and $\displaystyle \int \frac{dx}{2x\sqrt{x-1}}$.
7. $\displaystyle \int \frac{x}{\sqrt[3]{x+1}}\,dx$.
8. $\displaystyle \int \frac{dx}{x\sqrt{4x-1}}$.
9. $\displaystyle \int \frac{2\,dx}{x\sqrt{25x^4-1}}$.
10. $\displaystyle \int \frac{dx}{\sqrt x\sqrt{1-4x}}$.
11. $\displaystyle \int \frac{6-2x}{\sqrt{9-x^2}}\,dx$.
12. $\displaystyle \int \frac{dx}{\sqrt{x\sqrt x-x^2}}$.
:::

::: solution
For (1), let $t=\sqrt x$. Then $dx=2t\,dt$ and
\[
2t\frac{1-t}{1+t}=-2t+4-\frac4{t+1}.
\]
Hence
\[
\boxed{-x+4\sqrt x-4\ln(1+\sqrt x)+C.}
\]
The stored $\ln(1+x)$ was incorrect.

For (2), put $t=x^{1/6}$. Then
\[
\frac{dx}{\sqrt x+2\sqrt[3]x}=\frac{6t^3}{t+2}\,dt,
\]
so polynomial division gives
\[
\boxed{2\sqrt x-6\sqrt[3]x+24\sqrt[6]x-48\ln|\sqrt[6]x+2|+C.}
\]

For (3), with the same $t=x^{1/6}$,
\[
\frac{dx}{\sqrt x-\sqrt[3]x}=\frac{6t^3}{t-1}\,dt,
\]
thus
\[
\boxed{2\sqrt x+3\sqrt[3]x+6\sqrt[6]x+6\ln|\sqrt[6]x-1|+C.}
\]

For (4), let $t=x^{1/4}$. Then
\[
\frac{dx}{\sqrt x+\sqrt[4]x}=\frac{4t^2}{t+1}\,dt,
\]
so
\[
\boxed{2\sqrt x-4\sqrt[4]x+4\ln|\sqrt[4]x+1|+C.}
\]

For (5), let $t=\sqrt[3]x$. Since $dx=3t^2dt$,
\[
3t^2\frac{t+1}{t-1}=3t^2+6t+6+\frac6{t-1},
\]
whence
\[
\boxed{x+3x^{2/3}+6x^{1/3}+6\ln|x^{1/3}-1|+C.}
\]

For the first integral in (6), let $t=\sqrt x$:
\[
\boxed{\int\frac{dx}{(x+1)\sqrt x}=2\arctan\sqrt x+C.}
\]
For the second, let $t=\sqrt{x-1}$:
\[
\boxed{\int\frac{dx}{2x\sqrt{x-1}}=\arctan\sqrt{x-1}+C.}
\]

For (7), let $u=x+1$:
\[
\boxed{\frac35(x+1)^{5/3}-\frac32(x+1)^{2/3}+C.}
\]

For (8), let $u=\sqrt{4x-1}$. Then
\[
\boxed{2\arctan\sqrt{4x-1}+C.}
\]

For (9), let $u=\sqrt{25x^4-1}$. Since $u^2+1=25x^4$, the transformed integrand is $du/(1+u^2)$, giving
\[
\boxed{\arctan\sqrt{25x^4-1}+C.}
\]

For (10), let $u=2\sqrt x$. Then $du=dx/\sqrt x$, so
\[
\boxed{\arcsin(2\sqrt x)+C.}
\]
On $0<x<1/4$ this is equivalent, up to an additive constant, to $\tfrac12\arcsin(8x-1)$.

For (11), split the integral:
\[
\int\frac6{\sqrt{9-x^2}}\,dx-\int\frac{2x}{\sqrt{9-x^2}}\,dx,
\]
which gives
\[
\boxed{6\arcsin\!\left(\frac x3\right)+2\sqrt{9-x^2}+C.}
\]

For (12), let $u=x^{1/4}$. Since
\[
\sqrt{x\sqrt x-x^2}=x^{3/4}\sqrt{1-\sqrt x},
\]
and $dx=4u^3du$, we obtain
\[
\boxed{4\arcsin(x^{1/4})+C.}
\]
:::
