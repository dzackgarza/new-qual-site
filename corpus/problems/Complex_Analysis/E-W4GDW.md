---
schema: qual/card@1
id: E-W4GDW
kind: problem
title: A conformal map from $\HH$ onto $\{-\pi/2<\Re w<\pi/2,\,\Im w>0\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Find the conformal map that takes the upper half-plane conformally onto the half-strip
$$
\theset{w=x+iy \st -\pi/2 < x < \pi/2,\, y>0}.
$$
:::

::: {.solution}
![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_23-37-00.png)

Let $S = \theset{-\pi/2<\Re w < \pi/2,\ \Im w > 0}$.

::: pf

::: {.pf-step #sine}
$\sin$ maps $S$ conformally onto $\HH$.

::: pf-proof
For $w = x+iy\in S$, $\sin w = \sin x\cosh y + i\cos x\sinh y$ has positive imaginary part, so $\sin(S)\subseteq\HH$.
$\sin$ is injective on $S$: $\sin w_1 = \sin w_2$ forces $w_1 = w_2 + 2\pi k$ or $w_1 = \pi - w_2 + 2\pi k$, and in $S$ the first gives $k=0$ while the second gives $\Re(w_1+w_2) = \pi(2k+1)$, impossible since $\abs{\Re(w_1+w_2)}<\pi$.
For surjectivity, let $u\in\HH$. With $\zeta = e^{iw}$ the equation $\sin w = u$ becomes $\zeta^2 - 2iu\zeta - 1 = 0$, whose roots satisfy $\zeta_1\zeta_2 = -1$ and $\zeta_1+\zeta_2 = 2iu$.
If $\abs{\zeta_1} = 1$ then $\zeta_2 = -\bar\zeta_1$ and $2iu = \zeta_1 - \bar\zeta_1 = 2i\Im\zeta_1$, so $u\in\RR$, which is false; hence one root, say $\zeta_1$, has $0<\abs{\zeta_1}<1$.
Take $w = x+iy$ with $e^{iw} = \zeta_1$ and $x\in(-\pi,\pi]$. Then $y = -\log\abs{\zeta_1} > 0$, and $0 < \Im u = \cos x\sinh y$ forces $\cos x > 0$, so $w\in S$.
:::

:::

::: pf-step
$\boxed{z\mapsto\arcsin z}$, the inverse of $\sin|_S$, maps $\HH$ conformally onto $S$.

::: pf-proof
The inverse of the bijective holomorphic map of step [](#sine){.pf-ref} is holomorphic.
:::

:::

:::

:::
