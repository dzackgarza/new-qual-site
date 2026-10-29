---
schema: qual/card@1
id: E-3B2YA
kind: problem
title: Integrals over circles by Cauchy's integral formula
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Contour Integration
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints the six integrals in one unaligned display with no orientation; the statement labels them (a)-(f) and orients each circle positively.
---

::: {.exercise}
Evaluate the following integrals using Cauchy's integral formula, each circle positively oriented.

(a) $\displaystyle\int_{S^1} \frac{\cos(z)}{z} \dz$

(b) $\displaystyle\int_{S^1} \frac{\sin(z)}{z}\dz$

(c) $\displaystyle\int_{\abs z = 2} \frac{z^2}{z-1} \dz$

(d) $\displaystyle\int_{S^1} \frac{e^z}{z^2} \dz$

(e) $\displaystyle\int_{\abs z = 2} \frac{z^2 - 1}{z^2 + 1}\dz$

(f) $\displaystyle\int_{\abs z = 2} \frac{1}{z^2 + z + 1}\dz$

:::

::: {.solution}
Let $\zeta_3=e^{2\pi i/3}=-\frac12+i\frac{\sqrt3}2$, so that $\zeta_3+\bar\zeta_3=-1$, $\zeta_3\bar\zeta_3=1$, and $z^2+z+1=(z-\zeta_3)(z-\bar\zeta_3)$.
For (e) and (f), the circle $\abs z=2$ is the sum, in homology of the plane minus the poles, of small circles around each enclosed pole, and Cauchy's integral formula applies on each.

::: pf

::: pf-step
(a) $\displaystyle\int_{S^1} \frac{\cos(z)}{z} \dz=\boxed{2\pi i}$.

::: pf-proof
By Cauchy's integral formula the integral is $2\pi i\cos(0)=2\pi i$.
:::

:::

::: pf-step
(b) $\displaystyle\int_{S^1} \frac{\sin(z)}{z}\dz=\boxed{0}$.

::: pf-proof
By Cauchy's integral formula the integral is $2\pi i\sin(0)=0$.
:::

:::

::: pf-step
(c) $\displaystyle\int_{\abs z = 2} \frac{z^2}{z-1} \dz=\boxed{2\pi i}$.

::: pf-proof
The point $1$ lies inside $\abs z=2$, so the integral is $2\pi i\cdot 1^2=2\pi i$.
:::

:::

::: pf-step
(d) $\displaystyle\int_{S^1} \frac{e^z}{z^2} \dz=\boxed{2\pi i}$.

::: pf-proof
By Cauchy's integral formula for the first derivative, the integral is $2\pi i\,\frac{d}{dz}e^z\big|_{z=0}=2\pi i$.
:::

:::

::: pf-step
(e) $\displaystyle\int_{\abs z = 2} \frac{z^2 - 1}{z^2 + 1}\dz=\boxed{0}$.

::: pf-proof
Both poles $\pm i$ lie inside $\abs z=2$. Applying Cauchy's integral formula to $(z^2-1)/(z+i)$ at $i$ and to $(z^2-1)/(z-i)$ at $-i$ gives
$$
2\pi i\,\frac{-2}{2i}+2\pi i\,\frac{-2}{-2i}=-2\pi+2\pi=0.
$$
:::

:::

::: pf-step
(f) $\displaystyle\int_{\abs z = 2} \frac{1}{z^2 + z + 1}\dz=\boxed{0}$.

::: pf-proof
Both roots $\zeta_3,\bar\zeta_3$ have modulus $1$ and lie inside $\abs z=2$. Applying Cauchy's integral formula to $1/(z-\zeta_3)$ at $\bar\zeta_3$ and to $1/(z-\bar\zeta_3)$ at $\zeta_3$ gives
$$
2\pi i\left(\frac{1}{\bar\zeta_3-\zeta_3}+\frac{1}{\zeta_3-\bar\zeta_3}\right)=0.
$$
:::

:::

:::

:::
