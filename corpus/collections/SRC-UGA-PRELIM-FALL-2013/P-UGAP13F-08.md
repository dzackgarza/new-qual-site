---
schema: qual/card@1
id: P-UGAP13F-08
kind: problem
title: Compute a cube and all cube roots of $1+\sqrt3\,i$
classification:
  areas: [prelim]
  topics:
  - Roots of Unity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
$$
z=1+\sqrt3\,i.
$$
Express $z^3$ and all cube roots of $z$ in the form $a+bi$.
:::

::: {.solution}

::: pf

::: pf-step

The modulus and argument of
$$
z=1+\sqrt3\,i
$$
are
$$
\abs{z}=2
$$
and
$$
\arg z=\frac\pi3.
$$
Hence
$$
z
=
2e^{i\pi/3}.
$$


::: pf-proof

The modulus is
$$
\abs{z}
=
\sqrt{1^2+(\sqrt3)^2}
=
\sqrt4
=
2.
$$
Since $z$ lies in the first quadrant and
$$
\tan\theta
=
\frac{\sqrt3}{1}
=
\sqrt3,
$$
one has
$$
\theta=\frac\pi3.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
z^3=-8.
}
$$


::: pf-proof

By De Moivre's formula,
$$
z^3
=
2^3e^{i\pi}
=
8(-1)
=
-8.
$$

Equivalently, a direct calculation gives
$$
\begin{aligned}
(1+\sqrt3\,i)^2
&=
-2+2\sqrt3\,i,
\end{aligned}
$$
and multiplying once more by
$$
1+\sqrt3\,i
$$
gives $-8$.

:::

:::

::: {.pf-step #s1-3}

If
$$
w^3=z,
$$
then
$$
\abs{w}
=
2^{1/3}
$$
and its argument must satisfy
$$
3\theta
\equiv
\frac\pi3
\pmod{2\pi}.
$$


::: pf-proof

Taking moduli gives
$$
\abs{w}^3=\abs{z}=2,
$$
so
$$
\abs{w}=2^{1/3}.
$$

Taking arguments gives
$$
3\theta
=
\frac\pi3+2\pi k
$$
for some integer $k$.

:::

:::

::: {.pf-step #s1-4}

The three distinct arguments are
$$
\theta_k
=
\frac\pi9
+
\frac{2\pi k}{3},
\qquad
k=0,1,2.
$$


::: pf-proof

Divide the congruence from step [](#s1-3){.pf-ref} by $3$:
$$
\theta
=
\frac\pi9
+
\frac{2\pi k}{3}.
$$
Modulo $2\pi$, the values
$$
k=0,1,2
$$
give the three distinct cube roots.

:::

:::

::: {.pf-step #s1-5}

Therefore the cube roots, in the form
$$
a+bi,
$$
are
$$
\boxed{
2^{1/3}
\left(
\cos\frac\pi9
+
i\sin\frac\pi9
\right),
}
$$
$$
\boxed{
2^{1/3}
\left(
\cos\frac{7\pi}{9}
+
i\sin\frac{7\pi}{9}
\right),
}
$$
and
$$
\boxed{
2^{1/3}
\left(
\cos\frac{13\pi}{9}
+
i\sin\frac{13\pi}{9}
\right).
}
$$


::: pf-proof

Substitute
$$
k=0,1,2
$$
into step [](#s1-4){.pf-ref} and convert each polar form
$$
re^{i\theta}
$$
to
$$
r\cos\theta
+
i r\sin\theta.
$$
Each displayed coefficient of $1$ and of $i$ is real, so these are
rectangular forms
$$
a+bi.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives $z^3$, and step [](#s1-5){.pf-ref} lists all three cube roots.

:::

:::

:::
