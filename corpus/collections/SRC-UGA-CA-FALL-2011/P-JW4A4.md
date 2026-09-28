---
schema: qual/card@1
id: P-JW4A4
kind: problem
title: $\int_0^\infty\frac{\sqrt{x}}{(x+1)^2}\,dx$
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

::: {.problem}
Calculate
\[
\int_0^\infty {\sqrt x \over (x+1)^2} \,dx
.\]

:::

::: {.solution}
Use the keyhole contour about the positive real axis for
\[
F(z)=\frac{z^{1/2}}{(1+z)^2},
\]
with the branch $0<\arg z<2\pi$. On the upper bank,
$z^{1/2}=\sqrt x$; on the lower bank, $z^{1/2}=-\sqrt x$, and the reversed
orientation makes the two contributions add. The circular arcs vanish, so
the contour integral tends to
\[
2I,
\qquad
I=\int_0^\infty\frac{\sqrt x}{(1+x)^2}\,dx.
\]

The only pole inside the contour is the double pole at $z=-1$. Since on our
branch $(-1)^{1/2}=i$,
\[
\operatorname{Res}_{z=-1}F
=\left.\frac{d}{dz}z^{1/2}\right|_{z=-1}
=\frac1{2i}=-\frac i2.
\]
Hence the residue theorem gives
\[
2I=2\pi i\left(-\frac i2\right)=\pi,
\]
and therefore
\[
\boxed{I=\frac\pi2}.
\]
:::
