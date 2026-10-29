---
schema: qual/card@1
id: E-QCVGX
kind: problem
title: Laurent expansions of $\frac{1}{1+e^z}$ at $0$ and $i\pi$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Poles
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion for
$$
f(z) = {1\over 1 + e^z}
$$
about $z_0 = 0$ and $z_1 = i\pi$.
:::

::: {.solution}

::: pf

::: pf-step
Near $0$, $f$ is holomorphic and $\boxed{f(z) = \frac12 - \frac14 z + \frac1{48}z^3 + O(z^5)}$.

::: pf-proof
$1+e^0 = 2\neq0$, so $f$ is holomorphic near $0$.
Write $1+e^z = 2(1+p(z))$ with $p(z) \coloneqq \frac{z}{2} + \frac{z^2}{4} + \frac{z^3}{12} + \frac{z^4}{48} + O(z^5)$; for small $z$, $\abs{p(z)}<1$ and
$$
f(z) = \frac12\left(1 - p + p^2 - p^3 + p^4 - \cdots\right).
$$
Collecting coefficients: $z$ gives $-\frac12$; $z^2$ gives $-\frac14+\frac14 = 0$; $z^3$ gives $-\frac1{12} + 2\cdot\frac12\cdot\frac14 - \frac18 = \frac1{24}$; $z^4$ gives $-\frac1{48} + \left(\frac1{16}+2\cdot\frac12\cdot\frac1{12}\right) - 3\cdot\frac14\cdot\frac14 + \frac1{16} = 0$.
Multiplying by $\frac12$ gives the expansion.
:::

:::

::: pf-step
Near $i\pi$, with $\omega \coloneqq z - i\pi$, $f$ has a simple pole and $\boxed{f(z) = -\frac{1}{\omega} + \frac12 - \frac{1}{12}\omega + O(\omega^2)}$.

::: pf-proof
$e^z = e^{i\pi}e^{\omega} = -e^{\omega}$, so $f = \frac{1}{1-e^\omega}$.
Write $1-e^\omega = -\omega(1+q(\omega))$ with $q(\omega) \coloneqq \frac{\omega}{2} + \frac{\omega^2}{6} + O(\omega^3)$.
Then
$$
f = -\frac1\omega\left(1 - q + q^2 - \cdots\right) = -\frac1\omega\left(1 - \frac{\omega}{2} + \left(\frac14 - \frac16\right)\omega^2 + O(\omega^3)\right).
$$
:::

:::

:::

:::
