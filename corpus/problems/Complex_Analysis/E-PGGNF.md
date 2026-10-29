---
schema: qual/card@1
id: E-PGGNF
kind: problem
title: Half disc to full disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from $\theset{z\in \CC \st \abs{z} < 1, \Im(z) > 0} = \DD \intersect \HH$ to $\DD$.
:::

::: {.solution}

Let $Q_1\coloneqq\{w : \operatorname{Re} w>0,\ \Im w>0\}$.
The square $z\mapsto z^2$ alone maps $\DD\intersect\HH$ onto $\DD\setminus[0,1)$, not onto $\DD$.

::: pf

::: {.pf-step #to-quadrant}
$T(z)\coloneqq\frac{1+z}{1-z}$ maps $\DD\intersect\HH$ conformally onto $Q_1$.

::: pf-proof
$T$ is a Möbius transformation that maps $\DD$ onto the right half-plane and preserves $\RR\cup\{\infty\}$, with $T(0)=1$.
It maps the arc of $\partial\DD$ in $\HH$ onto the positive imaginary axis and $(-1,1)$ onto $(0,\infty)$, so it maps $\DD\intersect\HH$ onto the component of the right half-plane minus $(0,\infty)$ containing $T(i/2)=\frac{3+4i}{5}$, which is $Q_1$.
:::

:::

::: pf-step
$\boxed{z\mapsto \frac{T(z)^2-i}{T(z)^2+i}}$ maps $\DD\intersect\HH$ conformally onto $\DD$.

::: pf-proof
$w\mapsto w^2$ maps $Q_1$ conformally onto $\HH$, and the Cayley map $w\mapsto\frac{w-i}{w+i}$ maps $\HH$ conformally onto $\DD$; compose with step [](#to-quadrant){.pf-ref}.
:::

:::

:::

:::

::: {.solution title="Using Joukowski maps"}

::: pf

::: {.pf-step #outside}
$z\mapsto -1/z$ maps $\DD\intersect\HH$ conformally onto $\HH\setminus\overline{\DD}$.

::: pf-proof
$-1/z$ has modulus $1/\abs{z}$ and argument $\pi-\arg z$, so it maps $\{0<\abs{z}<1,\ 0<\arg z<\pi\}$ bijectively onto $\{\abs{w}>1,\ 0<\arg w<\pi\}$.
:::

:::

::: {.pf-step #joukowski}
$J(w)\coloneqq\frac12\left(w+\frac1w\right)$ maps $\HH\setminus\overline{\DD}$ conformally onto $\HH$.

::: pf-proof
For $w=\rho e^{i\theta}$ with $\rho>1$ and $0<\theta<\pi$, $\Im J(w) = \frac12\left(\rho-\frac1\rho\right)\sin\theta>0$.
$J(w)=c$ means $w^2-2cw+1=0$, whose two roots have product $1$; for $c\in\HH$ neither root is real or of modulus $1$, so exactly one root lies outside $\overline{\DD}$, and it lies in $\HH$ because $J$ maps the lower half-plane outside $\overline\DD$ into the lower half-plane.
:::

:::

::: pf-step
$\boxed{z\mapsto \frac{J(-1/z)-i}{J(-1/z)+i}}$ maps $\DD\intersect\HH$ conformally onto $\DD$.

::: pf-proof
Compose steps [](#outside){.pf-ref} and [](#joukowski){.pf-ref} with the Cayley map $w\mapsto\frac{w-i}{w+i}$ of $\HH$ onto $\DD$.
:::

:::

:::

:::
