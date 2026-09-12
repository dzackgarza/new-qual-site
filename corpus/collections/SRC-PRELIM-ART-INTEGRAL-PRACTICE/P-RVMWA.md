---
schema: qual/card@1
id: P-RVMWA
kind: problem
title: Antiderivatives of powers of $\sin x$ and $\cos x$
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
Evaluate the antiderivatives
\[
\int\sin^2x\,dx,\quad \int\cos^2x\,dx,\quad
\int\sin^3x\,dx,\quad \int\cos^3x\,dx,
\]
\[
\int(1+\sin x)^3\,dx,\quad
\int(1+\cos x)^3\,dx,
\]
\[
\int\sin^4x\,dx,\quad \int\cos^4x\,dx,
\quad \int(\cos^4x-\sin^4x)\,dx,
\]
and
\[
\int \frac{\sin^3\sqrt x}{2\sqrt x}\,dx.
\]
:::

::: solution
Using the power-reduction identities and elementary substitutions,
\[
\boxed{\int\sin^2x\,dx=\frac12(x-\sin x\cos x)+C,}
\]
\[
\boxed{\int\cos^2x\,dx=\frac12(x+\sin x\cos x)+C,}
\]
\[
\boxed{\int\sin^3x\,dx=\frac13\cos^3x-\cos x+C,}
\]
\[
\boxed{\int\cos^3x\,dx=\sin x-\frac13\sin^3x+C.}
\]
With $u=\sqrt x$, the nested-radical variant is
\[
\boxed{\int \frac{\sin^3\sqrt x}{2\sqrt x}\,dx
=\frac13\cos^3\sqrt x-\cos\sqrt x+C.}
\]
Expanding the cubes gives
\[
\boxed{\int(1+\sin x)^3dx
=\frac52x+\frac13\cos^3x-4\cos x-\frac34\sin2x+C,}
\]
\[
\boxed{\int(1+\cos x)^3dx
=\frac52x-\frac13\sin^3x+4\sin x+\frac34\sin2x+C.}
\]
Reduction formulas yield
\[
\boxed{\int\sin^4x\,dx
=\frac38x-\frac38\sin x\cos x-\frac14\sin^3x\cos x+C,}
\]
\[
\boxed{\int\cos^4x\,dx
=\frac38x+\frac38\sin x\cos x+\frac14\sin x\cos^3x+C.}
\]
Finally $\cos^4x-\sin^4x=\cos2x$, so
\[
\boxed{\int(\cos^4x-\sin^4x)dx=\frac12\sin2x+C.}
\]
:::
