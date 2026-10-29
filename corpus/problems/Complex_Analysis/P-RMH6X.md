---
schema: qual/card@1
id: P-RMH6X
kind: problem
title: A conformal map from the horizontal strip $\{0<\Im z<1\}$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Find a conformal map from the strip $\theset{z\in \CC \suchthat 0 < \Im(z) < 1}$ to $\HH$.
:::

::: {.solution}
Write $S\coloneqq\theset{0<\Im z<1}$ and $S_\pi\coloneqq\theset{0<\Im z<\pi}$.

::: pf

::: {.pf-step #dilate}

$z\mapsto\pi z$ maps $S$ biholomorphically onto $S_\pi$.

::: pf-proof

It is an invertible linear map that multiplies imaginary parts by $\pi$.

:::

:::

::: {.pf-step #exp}

$z\mapsto e^z$ maps $S_\pi$ biholomorphically onto $\HH$.

::: pf-proof

The principal logarithm $\Log w=\ln\abs w+i\Arg w$ is holomorphic on $\HH$. Writing $w=re^{i\theta}$ with $r>0$ and $0<\theta<\pi$, we get $\Log w=\ln r+i\theta$, and $\ln r$ takes every real value, so $\Log$ maps $\HH$ onto $S_\pi$. It is a two-sided inverse of $e^z$ there.

:::

:::

::: pf-step

$\boxed{z\mapsto e^{\pi z}}$ maps $S$ conformally onto $\HH$.

::: pf-proof

Compose the maps in steps [](#dilate){.pf-ref} and [](#exp){.pf-ref}.

:::

:::

:::

:::
