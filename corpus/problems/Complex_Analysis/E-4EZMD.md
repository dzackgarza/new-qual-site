---
schema: qual/card@1
id: E-4EZMD
kind: problem
title: A conformal equivalence from the quarter-disc to the first quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source leaves Delta undeclared; the statement declares it the open unit disk.
---

::: {.problem}
Let $\Delta$ be the open unit disk and define $A \definedas \theset{\Re(z) > 0, \Im(z) > 0}$.
Find a conformal equivalence $\Delta \intersect A \to A$.
:::

::: {.solution}
Let $J(z)=\frac12(z+z^{-1})$ be the Joukowski map.

::: pf

::: {.pf-step #square}
$z\mapsto z^2$ maps $\Delta\intersect A$ conformally onto $\DD\intersect\HH$.

::: pf-proof
In polar form $re^{i\theta}\mapsto r^2e^{2i\theta}$ is a bijection from $\theset{0<r<1,\ 0<\theta<\pi/2}$ onto $\theset{0<r<1,\ 0<\theta<\pi}$, with nonzero derivative $2z$.
:::

:::

::: {.pf-step #joukowski}
$z\mapsto -J(z)$ maps $\DD\intersect\HH$ conformally onto $\HH$.

::: pf-proof
$J$ is injective on $\DD\setminus\theset0$, because $J(z)=J(w)$ with $z\ne w$ forces $zw=1$, and it maps $\DD\setminus\theset0$ onto $\CC\setminus[-1,1]$.
For $z=re^{i\theta}$ with $0<r<1$, $\Im J(z)=\frac12(r-r^{-1})\sin\theta$, which has the sign of $-\sin\theta$.
So $J$ maps $\DD\intersect\HH$ onto the lower half-plane, and $-J$ maps it onto $\HH$.
:::

:::

::: {.pf-step #root}
The principal branch of $z\mapsto z^{1/2}$ maps $\HH$ conformally onto $A$.

::: pf-proof
In polar form it is $re^{i\theta}\mapsto r^{1/2}e^{i\theta/2}$, a bijection from $0<\theta<\pi$ onto $0<\theta<\pi/2$, holomorphic with nonzero derivative on $\HH$.
:::

:::

::: pf-step
$z\mapsto \qty{-J(z^2)}^{1/2}$ is a conformal equivalence $\Delta\intersect A\to A$.

::: pf-proof
It is the composite of the maps of steps [](#square){.pf-ref}, [](#joukowski){.pf-ref} and [](#root){.pf-ref}.
:::

:::

:::

:::
