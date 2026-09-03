---
schema: qual/card@1
id: E-SS3.PR-2
kind: problem
title: "Poisson's integral formula for the disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Mean Value Property
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
2. Let u be a harmonic function in the unit disc that is continuous on its closure.
   Deduce Poisson’s integral formula

$$
u (z _ {0}) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \frac {1 - | z _ {0} | ^ {2}}{| e ^ {i \theta} - z _ {0} | ^ {2}} u (e ^ {i \theta}) d \theta \quad \mathrm{for} | z _ {0} | <   1
$$

from the special case $z _ { 0 } = 0$ (the mean value theorem).
Show that if $z _ { 0 } = r e ^ { i \varphi }$ ， then

$$
\frac {1 - | z _ {0} | ^ {2}}{| e ^ {i \theta} - z _ {0} | ^ {2}} = \frac {1 - r ^ {2}}{1 - 2 r \cos (\theta - \varphi) + r ^ {2}} = P _ {r} (\theta - \varphi),
$$

and we recover the expression for the Poisson kernel derived in the exercises of the previous chapter.

[Hint: Set $u _ { 0 } ( z ) = u ( T ( z ) )$ where

$$
T (z) = \frac {z _ {0} - z}{1 - \overline {{z _ {0}}} z}.
$$

Prove that $u _ { 0 }$ is harmonic.
Then apply the mean value theorem to $u _ { 0 }$ , and make a change of variables in the integral.]
:::

::: {.solution}
<1>1. Let $T(z) = \frac{z_0 - z}{1 - \overline{z_0} z}$ and define $u_0(z) = u(T(z))$.
::: {.proof}
the hint.
:::

<1>2. $T$ is a holomorphic automorphism of the disk with $T(0) = z_0$ and $T(z_0) = 0$.
::: {.proof}
$T$ is a Blaschke factor (an involution of $\mathbb{D}$).
:::

<1>3. $u_0$ is harmonic.
::: {.proof}
$u_0 = u \circ T$ is the composition of a harmonic function with a holomorphic map, which is harmonic.
:::

<1>4. By the mean value theorem (the special case $z_0 = 0$), $u_0(0) = \frac{1}{2\pi}\int_0^{2\pi} u_0(e^{i\theta})\,d\theta$.
::: {.proof}
the mean value property of harmonic functions at the origin.
:::

<1>5. $u_0(0) = u(T(0)) = u(z_0)$.
::: {.proof}
<1>2.
:::

<1>6. Hence $u(z_0) = \frac{1}{2\pi}\int_0^{2\pi} u(T(e^{i\theta}))\,d\theta$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Make the change of variables $e^{i\varphi} = T(e^{i\theta})$; then $d\theta = \frac{1 - |z_0|^2}{|e^{i\theta} - z_0|^2}\,d\varphi$ (the Jacobian of the Blaschke factor on the circle).
::: {.proof}
the derivative of $T$ on the unit circle has modulus $\frac{1 - |z_0|^2}{|e^{i\theta} - z_0|^2}$.
:::

<1>8. Hence
$$u(z_0) = \frac{1}{2\pi}\int_0^{2\pi} \frac{1 - |z_0|^2}{|e^{i\theta} - z_0|^2} u(e^{i\theta})\,d\theta.$$
::: {.proof}
<1>6 and <1>7.
:::

<1>9. For $z_0 = re^{i\varphi}$, $\frac{1 - |z_0|^2}{|e^{i\theta} - z_0|^2} = \frac{1 - r^2}{1 - 2r\cos(\theta - \varphi) + r^2} = P_r(\theta - \varphi)$.
::: {.proof}
$|e^{i\theta} - re^{i\varphi}|^2 = 1 - 2r\cos(\theta - \varphi) + r^2$.
:::

<1>10. Q.E.D.
::: {.proof}
<1>8 and <1>9.
:::
:::
