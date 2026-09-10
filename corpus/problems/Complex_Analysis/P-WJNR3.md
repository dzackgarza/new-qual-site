---
schema: qual/card@1
id: P-WJNR3
kind: problem
title: $\int_0^\infty\frac{\sin^3 x}{x^3}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

:::{.problem}
Calculate
\[
\int_0^\infty {\sin^3(x) \over x^3} \, dx
.\]
:::

::: solution
Let
\[
I=\int_0^\infty\frac{\sin^3x}{x^3}\,dx.
\]
Integrating by parts with $dv=x^{-3}\,dx$ gives
\[
I=\frac32\int_0^\infty\frac{\sin^2x\cos x}{x^2}\,dx,
\]
because the boundary term vanishes at both $0$ and $\infty$. Using
\[
\cos x-\cos3x=4\sin^2x\cos x,
\]
we obtain
\[
I=\frac38\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx.
\]

For $0<a<b$, integration by parts together with the Dirichlet integral gives
\[
\int_0^\infty\frac{\cos(ax)-\cos(bx)}{x^2}\,dx
=\int_0^\infty\frac{b\sin(bx)-a\sin(ax)}x\,dx
=\frac\pi2(b-a).
\]
Taking $a=1$ and $b=3$ yields
\[
\int_0^\infty\frac{\cos x-\cos3x}{x^2}\,dx=\pi.
\]
Therefore
\[
\boxed{I=\frac{3\pi}{8}}.
\]
:::

