---
schema: qual/card@1
id: P-UGAP13F-08
kind: problem
title: Compute a cube and all cube roots of $1+\sqrt3\,i$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
\[
z=1+\sqrt3\,i.
\]
Express $z^3$ and all cube roots of $z$ in the form $a+bi$.
:::

::: {.solution}
<1>1. The modulus and argument of
\[
z=1+\sqrt3,i
\]
are
\[
|z|=2
\]
and
\[
\arg z=\frac\pi3.
\]
Hence
\[
z
=
2e^{i\pi/3}.
\]

::: {.proof}
The modulus is
\[
|z|
=
\sqrt{1^2+(\sqrt3)^2}
=
\sqrt4
=
2.
\]
Since $z$ lies in the first quadrant and
\[
\tan\theta
=
\frac{\sqrt3}{1}
=
\sqrt3,
\]
one has
\[
\theta=\frac\pi3.
\]
:::

<1>2. One has
\[
\boxed{
z^3=-8.
}
\]

::: {.proof}
By De Moivre's formula,
\[
z^3
=
2^3e^{i\pi}
=
8(-1)
=
-8.
\]

Equivalently, a direct calculation gives
\[
\begin{aligned}
(1+\sqrt3,i)^2
&=
-2+2\sqrt3,i,
\end{aligned}
\]
and multiplying once more by
\[
1+\sqrt3,i
\]
gives $-8$.
:::

<1>3. If
\[
w^3=z,
\]
then
\[
|w|
=
2^{1/3}
\]
and its argument must satisfy
\[
3\theta
\equiv
\frac\pi3
\pmod{2\pi}.
\]

::: {.proof}
Taking moduli gives
\[
|w|^3=|z|=2,
\]
so
\[
|w|=2^{1/3}.
\]

Taking arguments gives
\[
3\theta
=
\frac\pi3+2\pi k
\]
for some integer $k$.
:::

<1>4. The three distinct arguments are
\[
\theta_k
=
\frac\pi9
+
\frac{2\pi k}{3},
\qquad
k=0,1,2.
\]

::: {.proof}
Divide the congruence from step <1>3 by $3$:
\[
\theta
=
\frac\pi9
+
\frac{2\pi k}{3}.
\]
Modulo $2\pi$, the values
\[
k=0,1,2
\]
give the three distinct cube roots.
:::

<1>5. Therefore the cube roots, in the form
\[
a+bi,
\]
are
\[
\boxed{
2^{1/3}
\left(
\cos\frac\pi9
+
i\sin\frac\pi9
\right),
}
\]
\[
\boxed{
2^{1/3}
\left(
\cos\frac{7\pi}{9}
+
i\sin\frac{7\pi}{9}
\right),
}
\]
and
\[
\boxed{
2^{1/3}
\left(
\cos\frac{13\pi}{9}
+
i\sin\frac{13\pi}{9}
\right).
}
\]

::: {.proof}
Substitute
\[
k=0,1,2
\]
into step <1>4 and convert each polar form
\[
re^{i\theta}
\]
to
\[
r\cos\theta
+
i r\sin\theta.
\]
Each displayed coefficient of $1$ and of $i$ is real, so these are
rectangular forms
\[
a+bi.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 gives $z^3$, and step <1>5 lists all three cube roots.
:::
:::
