---
schema: qual/card@1
id: P-CASP18B
kind: problem
title: "Residue evaluation of the integral of dt/(t^3 + 1) from 0 to infinity"
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Improper Integrals
relations: []
review: draft
---

::: {.problem}
Use the method of residues to evaluate
$$
\int_0^\infty \frac{dt}{t^3 + 1}.
$$
:::

::: {.solution}
Integrate
\[
F(z)=\frac1{1+z^3}
\]
over the boundary of the sector $0\le\arg z\le2\pi/3$, truncated at radius
$R$. The circular arc tends to $0$ because $F(z)=O(R^{-3})$ while its length
is $O(R)$.

Let
\[
I=\int_0^\infty\frac{dt}{1+t^3}.
\]
The integral on the lower ray tends to $I$. On the upper ray, parametrized in
the reverse direction by $z=t e^{2\pi i/3}$,
\[
\int_{\text{upper ray}}F(z)\,dz
=-e^{2\pi i/3}I.
\]
The only pole in the sector is
\[
z_0=e^{i\pi/3},
\]
and
\[
\operatorname{Res}_{z=z_0}F
=\frac1{3z_0^2}=\frac{e^{-2\pi i/3}}3.
\]
Thus
\[
(1-e^{2\pi i/3})I
=\frac{2\pi i}{3}e^{-2\pi i/3}.
\]
Simplifying gives
\[
\boxed{I=\frac{2\pi}{3\sqrt3}}.
\]
:::
