---
schema: qual/card@1
id: P-UMNCP-S09-03
kind: problem
title: Conformally map a crescent region to the upper half-plane
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2009, 3 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Find an explicit conformal equivalence from the region bounded by the circles
\[
\left|z-\frac{i}{2}\right|=\frac12
\qquad\text{and}\qquad
|z-i|=1
\]
onto the upper half-plane.
The intended region is the part inside \(|z-i|<1\) and outside \(|z-i/2|\le 1/2\).
:::

::: {.solution}
Let
$$
\Omega
\coloneqq
\left\{
z:
|z-i|<1,
\quad
\left|z-\frac i2\right|>\frac12
\right\}.
$$
Both boundary circles pass through $0$, which is not contained in $\Omega$.

<1>1. For $a>0$, the circle
$$
|z-ia|=a
$$
is mapped by
$$
w=\frac1z
$$
to the horizontal line
$$
\operatorname{Im}w=-\frac1{2a}.
$$

::: {.proof}
The circle equation expands to
$$
|z|^2
-2a\operatorname{Im}z
=0.
$$
Write
$$
w=u+iv
$$
and
$$
z=\frac1w
=
\frac{u-iv}{|w|^2}.
$$
Then
$$
|z|^2=\frac1{|w|^2},
\qquad
\operatorname{Im}z
=
-\frac{v}{|w|^2}.
$$
Substituting and multiplying by $|w|^2$ gives
$$
1+2av=0,
$$
so
$$
v=-\frac1{2a}.
$$
:::

<1>2. Under $w=1/z$, the two boundary circles become
$$
\operatorname{Im}w=-1
$$
and
$$
\operatorname{Im}w=-\frac12,
$$
respectively.

::: {.proof}
Apply step <1>1 with
$$
a=\frac12
$$
for the circle
$$
\left|z-\frac i2\right|=\frac12,
$$
and with
$$
a=1
$$
for
$$
|z-i|=1.
$$
:::

<1>3. The map
$$
z\longmapsto\frac1z
$$
sends $\Omega$ biholomorphically onto the strip
$$
\boxed{
S
=
\left\{
w:
-1<\operatorname{Im}w<-rac12
\right\}}.
$$

::: {.proof}
The reciprocal map is a Möbius transformation, hence biholomorphic away from $0$. By step <1>2, it sends the two boundary circles to the two boundary lines of $S$.

To determine which component is the image, take
$$
z=\frac{3i}{2}.
$$
Then
$$
|z-i|=\frac12<1
$$
and
$$
\left|z-\frac i2\right|=1>\frac12,
$$
so $z\in\Omega$. Its reciprocal is
$$
\frac1z
=
-\frac{2i}{3},
$$
whose imaginary part lies strictly between $-1$ and $-1/2$. Hence the image component is exactly $S$.
:::

<1>4. The exponential map
$$
E(w)=e^{2\pi w}
$$
maps $S$ into the upper half-plane
$$
\mathbb H
=
\{\zeta:\operatorname{Im}\zeta>0\}.
$$

::: {.proof}
Write
$$
w=u+iv,
\qquad
-1<v<-rac12.
$$
Then
$$
E(w)
=
e^{2\pi u}e^{2\pi iv}.
$$
Its argument lies in
$$
(-2\pi,-\pi),
$$
which modulo $2\pi$ is the interval
$$
(0,\pi).
$$
Therefore
$$
\operatorname{Im}E(w)>0.
$$
:::

<1>5. The map $E:S\to\mathbb H$ is injective.

::: {.proof}
If
$$
e^{2\pi w_1}
=
e^{2\pi w_2},
$$
then
$$
2\pi(w_1-w_2)
=
2\pi i k
$$
for some
$$
k\in\ZZ,
$$
so
$$
w_1-w_2=ik.
$$
But the imaginary parts of two points of $S$ differ by strictly less than $1/2$, whereas a nonzero integer $k$ has
$$
|k|\ge1.
$$
Thus $k=0$ and $w_1=w_2$.
:::

<1>6. The map $E:S\to\mathbb H$ is surjective.

::: {.proof}
Let
$$
\zeta\in\mathbb H.
$$
Write
$$
\zeta
=
\rho e^{i\theta},
\qquad
\rho>0,
\quad
0<\theta<\pi.
$$
Set
$$
w
=
\frac{\log\rho}{2\pi}
+i\left(
\frac{\theta}{2\pi}-1
\right).
$$
Then
$$
-1
<
\frac{\theta}{2\pi}-1
<
-\frac12,
$$
so $w\in S$. Moreover,
$$
e^{2\pi w}
=
e^{\log\rho}
e^{i(\theta-2\pi)}
=
\rho e^{i\theta}
=
\zeta.
$$
:::

<1>7. An explicit conformal equivalence is
$$
\boxed{
F(z)
=
\exp\!\left(\frac{2\pi}{z}\right)}.
$$

::: {.proof}
By step <1>3,
$$
z\mapsto1/z
$$
is a biholomorphism from $\Omega$ to $S$. By steps <1>4--<1>6,
$$
w\mapsto e^{2\pi w}
$$
is a biholomorphism from $S$ to $\mathbb H$. Their composition is the displayed map.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives the requested explicit conformal equivalence.
:::
:::
