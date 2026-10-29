---
schema: qual/card@1
id: P-A6PQA
kind: problem
title: A conformal map from $\CC\setminus[1,\infty)$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from $\CC\setminus\theset{x\in \RR\suchthat x\geq 1}$ to $\DD$.
:::

::: {.solution}
Let $\sqrt{\cdot}$ denote the principal square root on $\CC\setminus(-\infty,0]$.

::: pf

::: {.pf-step #flip}
$z\mapsto 1-z$ maps $\CC\setminus[1,\infty)$ biholomorphically onto $\CC\setminus(-\infty,0]$.

::: pf-proof
It is an affine bijection of $\CC$ sending $[1,\infty)$ onto $(-\infty,0]$.
:::

:::

::: {.pf-step #root}
$\sqrt{\cdot}$ maps $\CC\setminus(-\infty,0]$ biholomorphically onto the right half-plane $\theset{\Re w>0}$.

::: pf-proof
In polar form $re^{i\theta}$ with $r>0$ and $\abs\theta<\pi$, it is $\sqrt r\,e^{i\theta/2}$, which has argument in $(-\pi/2,\pi/2)$; squaring is its holomorphic inverse.
:::

:::

::: {.pf-step #cayley}
$w\mapsto\frac{w-1}{w+1}$ maps $\theset{\Re w>0}$ biholomorphically onto $\DD$.

::: pf-proof
$\abs{w-1}<\abs{w+1}$ exactly when $w$ is closer to $1$ than to $-1$, that is, when $\Re w>0$; the map is a Möbius transformation, so it is a bijection onto its image, and its inverse $\zeta\mapsto\frac{1+\zeta}{1-\zeta}$ sends $\DD$ into $\theset{\Re w>0}$.
:::

:::

::: pf-step
A conformal map from $\CC\setminus[1,\infty)$ onto $\DD$ is
$$
\boxed{F(z)=\frac{\sqrt{1-z}-1}{\sqrt{1-z}+1}}.
$$

::: pf-proof
$F$ is the composition of the maps of steps [](#flip){.pf-ref}, [](#root){.pf-ref} and [](#cayley){.pf-ref}.
:::

:::

:::

:::
