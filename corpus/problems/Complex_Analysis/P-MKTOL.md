---
schema: qual/card@1
id: P-MKTOL
kind: problem
title: $\int_0^\infty\frac{\sqrt{x}}{1+x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

:::{.problem}
Calculate
\[
\int_0^\infty {\sqrt x \over 1 + x^2} \, dx
.\]

:::

::: solution
Use the standard beta-integral identity
\[
\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx
=\frac\pi n\csc\frac{\pi a}{n},
\qquad 0<a<n.
\]
Here $a=3/2$ and $n=2$, because $\sqrt x=x^{1/2}=x^{a-1}$. Therefore
\[
\int_0^\infty\frac{\sqrt x}{1+x^2}\,dx
=\frac\pi2\csc\frac{3\pi}{4}
=\frac\pi2\cdot\sqrt2
=\boxed{\frac{\pi}{\sqrt2}}.
\]

Equivalently, the beta-integral identity itself follows from a keyhole contour
for $z^{a-1}/(1+z^n)$.
:::

