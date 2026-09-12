---
schema: qual/card@1
id: P-CAF09E
kind: problem
title: "Evaluation of the integral of x/(x^4+1) via residue theory"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Evaluate the integral $\int_0^{\infty} \frac{x\,dx}{x^4 + 1}$ via residue theory.
It is not necessary to simplify your answer.
:::

::: solution
Integrate
\[
F(z)=\frac{z}{z^4+1}
\]
around the positively oriented boundary of the quarter-disk
$0\le \arg z\le \pi/2$, $|z|\le R$.

The only pole in the first quadrant is
\[
z_0=e^{i\pi/4},
\]
and it is simple. Its residue is
\[
\operatorname{Res}(F,z_0)
=\frac{z_0}{4z_0^3}
=\frac1{4z_0^2}
=\frac1{4i}
=-\frac{i}{4}.
\]
Hence the residue theorem gives, as $R\to\infty$,
\[
\oint F(z)\,dz\longrightarrow
2\pi i\left(-\frac{i}{4}\right)=\frac\pi2.
\]

The circular-arc contribution tends to $0$. The integral along the positive
real axis tends to
\[
I=\int_0^\infty\frac{x}{x^4+1}\,dx.
\]
On the positive imaginary axis write $z=iy$, traversed from $iR$ down to $0$.
Then
\[
\int_{iR}^{0}\frac{z}{z^4+1}\,dz
=\int_R^0\frac{iy}{y^4+1}i\,dy
=\int_0^R\frac{y}{y^4+1}\,dy,
\]
which also tends to $I$. Thus $2I=\pi/2$, and therefore
\[
\boxed{\displaystyle I=\frac\pi4.}
\]
:::
