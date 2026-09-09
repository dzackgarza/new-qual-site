---
schema: qual/card@1
id: P-GLK4G
kind: problem
title: Antiderivatives of $e^{x^{1/a}}$, $e^x\sin x$, and $e^x\cos x$
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
  note: Corrected the missing factor 3 in the cube-root exponential antiderivative.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Use $u=x^{1/a}$ to reduce
\[
\int e^{x^{1/a}}\,dx,
\]
and evaluate the special cases
\[
\int e^{\sqrt x}\,dx,
\qquad
\int e^{\sqrt[3]x}\,dx.
\]
Also evaluate
\[
\int e^x\sin x\,dx,
\qquad
\int \frac{\sin(\sqrt x)e^{\sqrt x}}{\sqrt x}\,dx,
\qquad
\int e^x\cos x\,dx.
\]
:::

::: solution
With $u=x^{1/a}$, so $x=u^a$ and $dx=a u^{a-1}du$,
\[
\int e^{x^{1/a}}\,dx=a\int u^{a-1}e^u\,du.
\]
For positive integer $a$ this is elementary by repeated integration by parts.

For $a=2$,
\[
\boxed{\int e^{\sqrt x}\,dx=2(\sqrt x-1)e^{\sqrt x}+C.}
\]
For $a=3$,
\[
\boxed{\int e^{\sqrt[3]x}\,dx=3\left(x^{2/3}-2x^{1/3}+2\right)e^{x^{1/3}}+C.}
\]
The stored formula omitted this factor $3$.

Integration by parts twice gives
\[
\boxed{\int e^x\sin x\,dx=\frac12e^x(\sin x-\cos x)+C,}
\]
\[
\boxed{\int e^x\cos x\,dx=\frac12e^x(\cos x+\sin x)+C.}
\]
Finally, putting $u=\sqrt x$ gives
\[
\int \frac{\sin(\sqrt x)e^{\sqrt x}}{\sqrt x}\,dx
=2\int e^u\sin u\,du
=\boxed{e^{\sqrt x}(\sin\sqrt x-\cos\sqrt x)+C.}
\]
:::
