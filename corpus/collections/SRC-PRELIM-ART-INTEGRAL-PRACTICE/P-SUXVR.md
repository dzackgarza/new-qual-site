---
schema: qual/card@1
id: P-SUXVR
kind: problem
title: Antiderivatives of $1/(x^2\sqrt{x^2-a^2})$ and $1/(x\sqrt{x^2-a^2})$
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
  note: Replaced branch-dependent inverse-secant forms by branch-safe primitives and restored constants.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Evaluate, on intervals where the real-valued integrands are defined,
\[
\int\frac{dx}{x^2\sqrt{x^2-a^2}},
\]
together with the special cases $a=2$, $a=3$, and
\[
\int\frac{dx}{x^2\sqrt{4x^2-1}}.
\]
Also evaluate
\[
\int\frac{dx}{2x\sqrt{x^2-16}}.
\]
:::

::: solution
For $a\ne0$,
\[
\frac{d}{dx}\left(\frac{\sqrt{x^2-a^2}}{a^2x}\right)
=\frac1{x^2\sqrt{x^2-a^2}},
\]
so
\[
\boxed{\int\frac{dx}{x^2\sqrt{x^2-a^2}}
=\frac{\sqrt{x^2-a^2}}{a^2x}+C.}
\]
Hence
\[
\boxed{\int\frac{dx}{x^2\sqrt{x^2-4}}=\frac{\sqrt{x^2-4}}{4x}+C,}
\]
\[
\boxed{\int\frac{dx}{x^2\sqrt{x^2-9}}=\frac{\sqrt{x^2-9}}{9x}+C.}
\]
Likewise,
\[
\boxed{\int\frac{dx}{x^2\sqrt{4x^2-1}}
=\frac{\sqrt{4x^2-1}}{x}+C,}
\]
as direct differentiation verifies.

For the final integral, put $u=\sqrt{x^2-16}$. Since $u\,du=x\,dx$ and $x^2=u^2+16$,
\[
\int\frac{dx}{2x\sqrt{x^2-16}}
=\frac12\int\frac{du}{u^2+16}
=\boxed{\frac18\arctan\!\left(\frac{\sqrt{x^2-16}}4\right)+C.}
\]
This form avoids the branch conventions inherent in $\sec^{-1}(x/4)$.
:::
