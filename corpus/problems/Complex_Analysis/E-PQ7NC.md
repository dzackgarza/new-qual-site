---
schema: qual/card@1
id: E-PQ7NC
kind: problem
title: Complement of the disc to $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.exercise}
Find a conformal map $\DD^c\cap\HH\to\HH$, where $\DD^c=\{z:\abs{z}>1\}$.
:::

::: {.solution}

Let $J(z)\coloneqq z+\frac1z$ and $\Omega\coloneqq\DD^c\cap\HH$.
For $z=re^{i\theta}$, $\Im J(z) = \left(r-r^{-1}\right)\sin\theta$.

::: pf

::: {.pf-step #into}
$J(\Omega)\subseteq\HH$.

::: pf-proof
For $z\in\Omega$, $r>1$ and $0<\theta<\pi$, so $\Im J(z)>0$.
:::

:::

::: {.pf-step #injective}
$J$ is injective on $\Omega$.

::: pf-proof
$J(z_1)-J(z_2) = (z_1-z_2)\left(1-\frac{1}{z_1z_2}\right)$, and $\abs{z_1z_2}>1$ for $z_1,z_2\in\Omega$, so the second factor does not vanish.
:::

:::

::: {.pf-step #onto}
$J(\Omega)=\HH$.

::: pf-proof
Let $w\in\HH$.
The roots of $z^2-wz+1=0$ are the solutions of $J(z)=w$, and their product is $1$.
Neither root has modulus $1$, because $J(e^{i\theta}) = 2\cos\theta\in\RR$, so exactly one root $z$ has $\abs{z}>1$.
Then $\Im w = \left(\abs{z}-\abs{z}^{-1}\right)\sin(\arg z)>0$ forces $\sin(\arg z)>0$, so $z\in\Omega$.
:::

:::

::: pf-step
$\boxed{J(z)=z+\frac1z}$ is a conformal map of $\Omega$ onto $\HH$.

::: pf-proof
$J$ is holomorphic on $\Omega$, and by steps [](#into){.pf-ref}, [](#injective){.pf-ref} and [](#onto){.pf-ref} it is a bijection onto $\HH$; an injective holomorphic map is biholomorphic onto its image.
:::

:::

:::

:::

::: {.remark title="Variations"}
One version asks for the map to be built with cross-ratios.
:::
