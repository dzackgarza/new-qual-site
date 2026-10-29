---
schema: qual/card@1
id: E-VS4XE
kind: problem
title: Conformal map from $\DD\setminus\theset{\abs{z-\frac12}\le\frac12}$ to $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
  - Complex Logarithm
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source removes only the circle |z-1/2| = 1/2, which leaves a disconnected set with no conformal map onto D; the statement removes the closed disk, the crescent the solution maps.
---

::: {.exercise}
Find a conformal map:
$$
\DD \sm \theset{\abs{z - {1\over 2}} \leq {1\over 2} } \to \DD.
$$

:::

::: {.hint}
Send the point of tangency of the two circles to $\infty$; the crescent becomes a strip.
:::

::: {.solution}
![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_23-07-02.png)

Let $\Omega = \DD \sm \theset{\abs{z - \frac12} \leq \frac12}$.

::: pf

::: {.pf-step #strip}
$T(z) = \frac{1+z}{1-z}$ maps $\Omega$ conformally onto the strip $S = \theset{0 < \Re w < 1}$.

::: pf-proof
$T$ sends $-1\mapsto0$, $0\mapsto1$, $1\mapsto\infty$, and commutes with $z\mapsto\bar z$.
Both boundary circles pass through $1$, so their images are lines; being symmetric about $\RR$, they are vertical.
The unit circle passes through $-1$, so its image is $\Re w = 0$; the circle $\abs{z-\frac12}=\frac12$ passes through $0$, so its image is $\Re w = 1$.
Since $T(-\frac12) = \frac13$, $T(\Omega) = S$.
:::

:::

::: {.pf-step #half-plane}
$w \mapsto e^{i\pi w}$ maps $S$ conformally onto the upper half-plane $\HH$.

::: pf-proof
Multiplication by $i\pi$ maps $S$ onto $\theset{0 < \Im u < \pi}$, which $\exp$ maps bijectively onto $\HH$.
:::

:::

::: pf-step
$$
\boxed{F(z) = \frac{e^{i\pi\frac{1+z}{1-z}} - i}{e^{i\pi\frac{1+z}{1-z}} + i}}
$$
maps $\Omega$ conformally onto $\DD$.

::: pf-proof
Compose steps [](#strip){.pf-ref} and [](#half-plane){.pf-ref} with the Cayley map $u\mapsto\frac{u-i}{u+i}$ from $\HH$ onto $\DD$.
:::

:::

:::

:::
