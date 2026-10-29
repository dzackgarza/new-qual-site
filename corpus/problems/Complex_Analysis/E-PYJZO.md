---
schema: qual/card@1
id: E-PYJZO
kind: problem
title: Sector to disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from the sector $\theset{\Arg(z) \in (0, \alpha)} \to \DD$.
:::

::: {.solution}

![The sector, its image $\HH$ under $z^{\pi/\alpha}$, and the disc.](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_22-13-13.png)

Let $S\coloneqq\theset{\Arg(z) \in (0, \alpha)}$ with $0<\alpha\leq\pi$.

::: pf

::: {.pf-step #power}
$p(z)\coloneqq \exp\left(\frac{\pi}{\alpha}\Log z\right)$, with $\Log$ the principal branch, maps $S$ conformally onto $\HH$.

::: pf-proof
$\Log$ is holomorphic on $S$, which avoids $(-\infty,0]$.
For $z=re^{i\theta}$ with $r>0$ and $0<\theta<\alpha$, $p(z) = r^{\pi/\alpha}e^{i\pi\theta/\alpha}$; the map $(r,\theta)\mapsto(r^{\pi/\alpha},\pi\theta/\alpha)$ is a bijection of $(0,\infty)\times(0,\alpha)$ onto $(0,\infty)\times(0,\pi)$.
:::

:::

::: pf-step
$\boxed{z\mapsto\frac{p(z)-i}{p(z)+i}}$ maps $S$ conformally onto $\DD$.

::: pf-proof
The Cayley map $w\mapsto\frac{w-i}{w+i}$ maps $\HH$ conformally onto $\DD$; compose with step [](#power){.pf-ref}.
:::

:::

:::

:::
