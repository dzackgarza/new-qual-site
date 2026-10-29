---
schema: qual/card@1
id: E-YCHOS
kind: problem
title: A conformal map from the upper half-disc to the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from the upper half-disc to the upper half-plane.
:::

::: {.solution}
Write $\DD^+\coloneqq\DD\cap\HH$ and $Q\coloneqq\{u:\Re u>0,\ \Im u>0\}$.

::: pf

::: {.pf-step #quadrant}
$\varphi(z)\coloneqq\dfrac{1+z}{1-z}$ maps $\DD^+$ conformally onto $Q$.

::: pf-proof
For $z\in\DD$,
$$
\frac{1+z}{1-z} = \frac{1-\abs z^2 + 2i\Im z}{\abs{1-z}^2},
$$
so $\varphi(\DD^+)\subseteq Q$; the inverse Möbius map $u\mapsto\frac{u-1}{u+1}$ sends $Q$ into $\DD$, because $\abs{u-1}<\abs{u+1}$ when $\Re u>0$, and into $\HH$, because $\Im\frac{u-1}{u+1} = \frac{2\Im u}{\abs{u+1}^2}$.
:::

:::

::: pf-step
$\boxed{f(z)\coloneqq\qty(\dfrac{1+z}{1-z})^2}$ maps $\DD^+$ conformally onto $\HH$.

::: pf-proof
$u\mapsto u^2$ maps $Q$ bijectively and holomorphically onto $\HH$, doubling arguments in $(0,\pi/2)$ to $(0,\pi)$, with nonvanishing derivative on $Q$; compose with step [](#quadrant){.pf-ref}.
:::

:::

:::

:::
