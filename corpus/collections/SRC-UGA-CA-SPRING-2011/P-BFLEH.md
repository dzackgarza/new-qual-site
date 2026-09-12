---
schema: qual/card@1
id: P-BFLEH
kind: problem
title: $\int_0^\infty\frac{\cos x-\cos 4x}{x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

:::{.problem}
Calculate
\[
\int_0^\infty {\cos(x) - \cos(4x) \over x^2} \, dx
.\]
:::

::: solution
For $a>0$, integration by parts gives
\[
\int_0^\infty\frac{1-\cos(ax)}{x^2}\,dx
=a\int_0^\infty\frac{\sin(ax)}x\,dx.
\]
The boundary term vanishes at both endpoints. By the standard indented
upper-half-plane contour for $e^{iaz}/z$,
\[
\int_0^\infty\frac{\sin(ax)}x\,dx=\frac\pi2.
\]
Hence
\[
\int_0^\infty\frac{1-\cos(ax)}{x^2}\,dx=\frac{\pi a}{2}.
\]
Subtracting the cases $a=1$ and $a=4$ in the appropriate order,
\[
\int_0^\infty\frac{\cos x-\cos4x}{x^2}\,dx
=\frac{4\pi}{2}-\frac{\pi}{2}
=\boxed{\frac{3\pi}{2}}.
\]
:::
