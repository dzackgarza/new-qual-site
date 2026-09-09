---
schema: qual/card@1
id: P-EMCA7
kind: problem
title: "Contour integral and Fourier-type integral"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Compute the integrals
$$
\int_{|z-2|=1} \frac{e^z}{z(z-1)^2}\,dz, \qquad \int_0^\infty \frac{\cos 2x}{x^2 + 2}\,dx.
$$
:::

::: solution
For the first integral, the circle $|z-2|=1$ encloses the double pole at
$z=1$ and excludes the pole at $z=0$. Thus
\[
\int_{|z-2|=1}\frac{e^z}{z(z-1)^2}\,dz
=2\pi i\operatorname{Res}_{z=1}\frac{e^z}{z(z-1)^2}.
\]
Since the pole is double,
\[
\operatorname{Res}_{z=1}\frac{e^z}{z(z-1)^2}
=\left.\frac{d}{dz}\left(\frac{e^z}{z}\right)\right|_{z=1}
=\left.e^z\frac{z-1}{z^2}\right|_{z=1}=0.
\]
Hence the first integral is
\[
\boxed{0}.
\]

For the second integral, integrate
\[
F(z)=\frac{e^{2iz}}{z^2+2}
\]
over the upper semicircle. The arc integral tends to $0$, and the only pole in
the upper half-plane is $z=i\sqrt2$. Its residue is
\[
\operatorname{Res}_{z=i\sqrt2}F
=\frac{e^{2i(i\sqrt2)}}{2i\sqrt2}
=\frac{e^{-2\sqrt2}}{2i\sqrt2}.
\]
Therefore
\[
\int_{-\infty}^{\infty}\frac{e^{2ix}}{x^2+2}\,dx
=2\pi i\frac{e^{-2\sqrt2}}{2i\sqrt2}
=\frac{\pi}{\sqrt2}e^{-2\sqrt2}.
\]
Taking real parts and using evenness gives
\[
\boxed{\displaystyle
\int_0^\infty\frac{\cos 2x}{x^2+2}\,dx
=\frac{\pi}{2\sqrt2}e^{-2\sqrt2}.}
\]
:::
