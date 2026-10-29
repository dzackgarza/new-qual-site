---
schema: qual/card@1
id: E-TOZQJ
kind: problem
title: 'Residue from Laurent expansion: $1/(z - \sin(z))$'
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Laurent Series
  - Poles
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Use a direct Laurent expansion to show
$$
\Res_{z=0} {1\over z-\sin(z)} = {3! \over 5\cdot 4}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #denominator}
$z - \sin(z) = \frac{z^3}{3!}\left(1 - q(z)\right)$ with $q(z) \coloneqq \frac{z^2}{5\cdot 4} + \bigo(z^4)$.

::: pf-proof
From $\sin(z) = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots$,
$$
z-\sin(z) = \frac{z^3}{3!} - \frac{z^5}{5!} + \cdots = \frac{z^3}{3!}\left(1 - \frac{3!}{5!}z^2 + \bigo(z^4)\right),
$$
and $\frac{3!}{5!} = \frac{1}{5\cdot 4}$.
:::

:::

::: pf-step
$\frac{1}{z-\sin(z)} = \frac{3!}{z^3} + \frac{3!}{5\cdot 4}\cdot\frac1z + \bigo(z)$, so $\Res_{z=0}\frac{1}{z-\sin(z)} = \boxed{\frac{3!}{5\cdot 4} = \frac{3}{10}}$.

::: pf-proof
Near $0$, $\abs{q(z)}<1$, so by step [](#denominator){.pf-ref}
$$
\frac{1}{z-\sin(z)} = \frac{3!}{z^3}\left(1 + q(z) + q(z)^2 + \cdots\right) = \frac{3!}{z^3}\left(1 + \frac{z^2}{5\cdot 4} + \bigo(z^4)\right).
$$
:::

:::

:::

:::

::: {.remark}
A Laurent expansion is the natural route here because the order of the pole at $0$ is not visible in advance, so the number of derivatives the pole-order residue formula needs is not known before expanding.
:::
