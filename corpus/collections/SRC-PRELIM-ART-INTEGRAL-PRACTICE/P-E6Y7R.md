---
schema: qual/card@1
id: P-E6Y7R
kind: problem
title: Antiderivatives of $x\arcsin(1/x)$, $x\arctan x$, and $x\sin(2x)$
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
  note: Corrected the sign of the x cos(2x) term.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int x\arcsin\!\left(\frac1x\right)\,dx
\quad (x>1),
\]
\[
\int x\arctan x\,dx,
\qquad
\int_0^1x\arctan x\,dx,
\]
and
\[
\int x\sin(2x)\,dx.
\]
:::

::: solution
For the first integral, integration by parts with $u=\arcsin(1/x)$ and $dv=x\,dx$ gives
\[
\boxed{\int x\arcsin\!\left(\frac1x\right)\,dx
=\frac12\left(x^2\arcsin\!\left(\frac1x\right)+\sqrt{x^2-1}\right)+C.}
\]

For the second,
\[
\boxed{\int x\arctan x\,dx
=\frac12\left((x^2+1)\arctan x-x\right)+C.}
\]
Therefore
\[
\boxed{\int_0^1x\arctan x\,dx=\frac\pi4-\frac12.}
\]

Finally, integration by parts with $u=x$ and $dv=\sin(2x)dx$ gives
\[
\boxed{\int x\sin(2x)\,dx
=-\frac12x\cos(2x)+\frac14\sin(2x)+C.}
\]
The stored positive sign in front of $x\cos(2x)$ was incorrect.
:::
