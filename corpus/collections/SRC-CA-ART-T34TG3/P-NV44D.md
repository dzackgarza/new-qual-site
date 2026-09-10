---
schema: qual/card@1
id: P-NV44D
kind: problem
title: For $a> 0$, evaluate
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

::: problem
For $a> 0$, evaluate
\[
\int_0^{\pi/2} \frac{d\theta}{a + \sin^2 \theta}
\]
:::

::: solution
Set $t=\tan\theta$. Then
\[
\sin^2\theta=\frac{t^2}{1+t^2},
\qquad
d\theta=\frac{dt}{1+t^2}.
\]
Hence
\[
\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}
=\int_0^\infty\frac{dt}{a+(a+1)t^2}.
\]
After $u=t\sqrt{(a+1)/a}$,
\[
\int_0^\infty\frac{dt}{a+(a+1)t^2}
=\frac1{\sqrt{a(a+1)}}\int_0^\infty\frac{du}{1+u^2}.
\]
Therefore
\[
\boxed{
\int_0^{\pi/2}\frac{d\theta}{a+\sin^2\theta}
=\frac{\pi}{2\sqrt{a(a+1)}}.}
\]
:::
