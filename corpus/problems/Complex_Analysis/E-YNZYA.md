---
schema: qual/card@1
id: E-YNZYA
kind: problem
title: Residues of $1/(z^2+1)$ at $\pm i$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.exercise}
Use the rational function formula to compute the residues at $z=\pm i$ of
$$
f(z) \coloneqq \frac{1}{z^2 + 1}.
$$
:::

::: {.solution}

::: pf

::: pf-step
$\operatorname{Res}_{z=i}f = \boxed{-\dfrac i2}$ and $\operatorname{Res}_{z=-i}f = \boxed{\dfrac i2}$.

::: pf-proof
At a simple zero $z_0$ of $q$ with $p(z_0)\neq0$, the rational function formula gives $\operatorname{Res}_{z=z_0}\frac{p}{q} = \frac{p(z_0)}{q'(z_0)}$.
Here $p=1$, $q = z^2+1$ has simple zeros at $\pm i$, and $q'(z) = 2z$, so the residues are $\frac{1}{2i} = -\frac i2$ and $\frac{1}{-2i} = \frac i2$.
:::

:::

:::

:::
