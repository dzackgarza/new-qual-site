---
schema: qual/card@1
id: P-JHUSP02CAB
kind: problem
title: Evaluating $\int_0^{2\pi}(a^2+\cos^2x)^{-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the integrand, full-period limits and hypothesis a>1 with Spring 2002 Complex Analysis question 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Reduced cos squared to a single cosine, evaluated the resulting period integral by a unit-circle residue, located the unique interior quadratic root, and simplified using a>1."
---

2. Evaluate the integral

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d x } { a ^ { 2 } + \cos ^ { 2 } x } } .
$$

Where $a > 1$


::: solution
The value is
$$
\boxed{\frac{2\pi}{a\sqrt{a^2+1}}}.
$$

<1>1. Reduce the problem to the standard integral $\int_0^{2\pi}(c+\cos t)^{-1}dt$.
::: proof
Using $\cos^2x=(1+\cos2x)/2$ and setting
$$
c=2a^2+1>1,
$$
we obtain
$$
\frac1{a^2+\cos^2x}=\frac{2}{c+\cos2x}.
$$
Hence, with $t=2x$,
$$
\int_0^{2\pi}\frac{dx}{a^2+\cos^2x}
=\int_0^{4\pi}\frac{dt}{c+\cos t}
=2\int_0^{2\pi}\frac{dt}{c+\cos t},
$$
because the last integrand is $2\pi$-periodic.
:::

<1>2. The unit-circle contour gives
$\int_0^{2\pi}(c+\cos t)^{-1}dt=2\pi/\sqrt{c^2-1}$.
::: proof
Put $z=e^{it}$. Then $dt=dz/(iz)$ and
$\cos t=(z+z^{-1})/2$, so
$$
\int_0^{2\pi}\frac{dt}{c+\cos t}
=\frac{2}{i}\int_{|z|=1}\frac{dz}{z^2+2cz+1}.
$$
The two roots of the denominator are
$$
z_\pm=-c\pm\sqrt{c^2-1}.
$$
Since $c>1$, $z_-<-1$. Moreover
$$
|z_+|=c-\sqrt{c^2-1}
=\frac1{c+\sqrt{c^2-1}}<1,
$$
so exactly $z_+$ lies inside the unit circle. It is simple, and the residue of
$2/[i(z^2+2cz+1)]$ there is
$$
\frac{2}{i(2z_++2c)}
=\frac1{i\sqrt{c^2-1}}.
$$
The residue theorem therefore yields
$$
\int_0^{2\pi}\frac{dt}{c+\cos t}
=2\pi i\frac1{i\sqrt{c^2-1}}
=\frac{2\pi}{\sqrt{c^2-1}}.
$$
:::

<1>3. Substitute $c=2a^2+1$.
::: proof
By steps <1>1 and <1>2,
$$
\int_0^{2\pi}\frac{dx}{a^2+\cos^2x}
=\frac{4\pi}{\sqrt{(2a^2+1)^2-1}}
=\frac{4\pi}{\sqrt{4a^2(a^2+1)}}.
$$
Since $a>1$, the square root is $2a\sqrt{a^2+1}$, giving
$$
\frac{2\pi}{a\sqrt{a^2+1}}.
$$
:::
:::
