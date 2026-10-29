---
schema: qual/card@1
id: P-R4WQK
kind: problem
title: Distinct $z_1,z_2,z_3$ form an equilateral triangle iff $z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that distinct complex numbers $z_1,z_2,z_3$ are the vertices of an
equilateral triangle if and only if
$$
z_1^2+z_2^2+z_3^2=z_1z_2+z_2z_3+z_3z_1.
$$
:::

::: {.solution}
Let $\omega=e^{2\pi i/3}$, so $1+\omega+\omega^2=0$.

::: pf

::: {.pf-step #factor}

$z_1^2+z_2^2+z_3^2-z_1z_2-z_2z_3-z_3z_1=(z_1+\omega z_2+\omega^2z_3)(z_1+\omega^2z_2+\omega z_3)$.

::: pf-proof

Expanding the right side, the coefficient of each product $z_jz_k$ with $j\ne k$ is $\omega+\omega^2=-1$.

:::

:::

::: {.pf-step #rotate}

$z_1+\omega z_2+\omega^2z_3=0$ if and only if $z_1-z_3=e^{-i\pi/3}(z_2-z_3)$, and $z_1+\omega^2z_2+\omega z_3=0$ if and only if $z_1-z_3=e^{i\pi/3}(z_2-z_3)$.

::: pf-proof

Using $\omega^2=-1-\omega$, the first factor equals $(z_1-z_3)+\omega(z_2-z_3)$, and $-\omega=e^{-i\pi/3}$. The second case is the same with $\omega$ and $\omega^2$ exchanged, and $-\omega^2=e^{i\pi/3}$.

:::

:::

::: pf-step

$z_1,z_2,z_3$ are the vertices of an equilateral triangle if and only if the identity holds.

::: pf-proof

The distinct points $z_1,z_2,z_3$ form an equilateral triangle exactly when the sides issuing from $z_3$ have equal length and meet at angle $\pi/3$, that is, when $z_1-z_3=e^{\pm i\pi/3}(z_2-z_3)$. By step [](#rotate){.pf-ref} this happens exactly when one factor in step [](#factor){.pf-ref} vanishes, that is, when the identity holds.

:::

:::

:::

:::
