---
schema: qual/card@1
id: P-PQOTX
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+\cos\theta)^2}=\frac{2\pi a}{(a^2-1)^{3/2}}$
  for $a>1$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Poles
relations: []
review: draft
---

::: problem
Show that
\[
\int_{0}^{2 \pi} \frac{d \theta}{(a+\cos \theta)^{2}}=\frac{2 \pi a}{\left(a^{2}-1\right)^{3 / 2}}, \quad \text { whenever } a>1
.\]
:::

::: solution
First evaluate
\[
J(a)=\int_0^{2\pi}\frac{d\theta}{a+\cos\theta},
\qquad a>1.
\]
With $z=e^{i\theta}$,
\[
\cos\theta=\frac12\left(z+\frac1z\right),
\qquad
d\theta=\frac{dz}{iz},
\]
so
\[
J(a)
=\frac2i\int_{|z|=1}
\frac{dz}{z^2+2az+1}.
\]
The roots of the denominator are
\[
z_\pm=-a\pm\sqrt{a^2-1}.
\]
For $a>1$, one has
\[
|z_+|<1<|z_-|,
\]
so only $z_+$ lies inside the unit circle. Its residue is
\[
\operatorname{Res}_{z=z_+}
\frac1{z^2+2az+1}
=\frac1{2(z_++a)}
=\frac1{2\sqrt{a^2-1}}.
\]
Hence
\[
J(a)
=\frac2i\cdot2\pi i\cdot
\frac1{2\sqrt{a^2-1}}
=\frac{2\pi}{\sqrt{a^2-1}}.
\]

Since $a>1$, the denominator $a+\cos\theta$ is bounded away from zero, so differentiation under the integral sign is valid. Therefore
\[
J'(a)
=-\int_0^{2\pi}
\frac{d\theta}{(a+\cos\theta)^2}.
\]
Differentiating the explicit expression for $J$ gives
\[
J'(a)
=-\frac{2\pi a}{(a^2-1)^{3/2}}.
\]
Thus
\[
\boxed{
\int_0^{2\pi}
\frac{d\theta}{(a+\cos\theta)^2}
=\frac{2\pi a}{(a^2-1)^{3/2}}.}
\]
:::
