---
schema: qual/card@1
id: P-CASP17A
kind: problem
title: "Residue computation of the integral of cos(x)/(1+x^2)^2 from 0 to 1"
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
relations: []
review: draft
---

::: {.problem}
Using the calculus of residues, compute
$$
\int_0^\infty \frac{\cos x}{(1 + x^2)^2} \, dx.
$$
:::

::: {.remark}
The local transcription previously had upper limit $1$. The official Spring
2017 UCSD exam has upper limit $\infty$.
:::

::: {.solution}
Integrate
\[
F(z)=\frac{e^{iz}}{(1+z^2)^2}
\]
over the upper semicircle. The arc contribution tends to $0$ by Jordan's
lemma (or directly from $|e^{iz}|=e^{-\operatorname{Im}z}$). The only pole in
the upper half-plane is the double pole at $z=i$. Since
\[
F(z)=\frac{e^{iz}}{(z-i)^2(z+i)^2},
\]
\[
\operatorname{Res}_{z=i}F
=\left.\frac{d}{dz}\frac{e^{iz}}{(z+i)^2}\right|_{z=i}
=-\frac{i}{2e}.
\]
Hence
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{(1+x^2)^2}\,dx
=2\pi i\left(-\frac{i}{2e}\right)=\frac\pi e.
\]
Taking real parts and using evenness gives
\[
\boxed{\displaystyle \int_0^\infty\frac{\cos x}{(1+x^2)^2}\,dx
=\frac{\pi}{2e}.}
\]
:::
