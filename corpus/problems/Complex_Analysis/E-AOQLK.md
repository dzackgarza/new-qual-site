---
schema: qual/card@1
id: E-AOQLK
kind: problem
title: Residues of $z^3/(z^2+1)$ from its principal parts
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Principal Parts
  - Poles
relations: []
review: draft
---

::: {.exercise}
Find all residues of the following function by writing it as a sum of principal parts at its poles:
$$
f(z) = \frac{z^3}{z^2 + 1}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #parts}
$f(z) = z - \frac{1/2}{z+i} - \frac{1/2}{z-i}$, the sum of its principal parts at $\infty$, $-i$, and $i$.

::: pf-proof
Long division gives $z^3 = z(z^2+1) - z$, so $f(z) = z - \frac{z}{z^2 + 1}$.
Writing $\frac{z}{z^2 + 1} = \frac{a}{z+i} + \frac{b}{z-i}$ gives $a(z-i) + b(z+i) = z$; evaluating at $z=i$ gives $b=1/2$, and at $z=-i$ gives $a=1/2$.
:::

:::

::: pf-step
$\boxed{\Res_{z=i} f = -\tfrac12,\quad \Res_{z=-i} f = -\tfrac12,\quad \Res_{z=\infty} f = 1}$.

::: pf-proof
The finite residues are the coefficients of $(z\mp i)^{-1}$ in step [](#parts){.pf-ref}.
Expanding the same decomposition for large $\abs z$ gives $f(z)=z-\frac{1}{z}+O(z^{-3})$, so $\Res_{z=\infty}f=-(-1)=1$, the negative of the sum of the finite residues.
:::

:::

:::

:::
