---
schema: qual/card@1
id: P-MKEL2
kind: problem
title: Evaluate $\int\frac{1}{e^x+e^{-x}}\,dx$
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
  note: Corrected the sign of the arcsine antiderivative in the second integral.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate
\[
\int\frac{dx}{e^x+e^{-x}},
\qquad
\int\frac{e^x}{1+e^{2x}}\,dx,
\]
and, on the real domain $x>0$,
\[
\int\frac{dx}{\sqrt{e^{2x}-1}}.
\]
:::

::: solution
Since
\[
\frac1{e^x+e^{-x}}=\frac{e^x}{1+e^{2x}},
\]
letting $u=e^x$ gives
\[
\boxed{\int\frac{dx}{e^x+e^{-x}}=\int\frac{e^x}{1+e^{2x}}\,dx=\arctan(e^x)+C.}
\]
For the second type, let $u=e^{-x}$. Since $du=-e^{-x}dx$ and
\[
\sqrt{e^{2x}-1}=\frac{\sqrt{1-u^2}}{u}
\qquad (u>0),
\]
we get
\[
\int\frac{dx}{\sqrt{e^{2x}-1}}
=-\int\frac{du}{\sqrt{1-u^2}}
=\boxed{-\arcsin(e^{-x})+C}.
\]
Equivalently, with $v=\sqrt{e^{2x}-1}$,
\[
\boxed{\int\frac{dx}{\sqrt{e^{2x}-1}}=\arctan\sqrt{e^{2x}-1}+C'},
\]
and the two primitives differ by the constant $\pi/2$ on $x>0$.
:::
