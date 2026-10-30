---
schema: qual/card@1
id: E-UUBBS
kind: problem
title: Conformal map from the lune $\abs{z-i}<\sqrt2\cap\abs{z+i}<\sqrt2$ to $\DD$
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

Find a conformal map $L\to \DD$ where
$$
L\coloneqq \theset{\abs{z - i } < \sqrt 2} \intersect \theset{\abs{z+i} < \sqrt 2},
$$
i.e. a lune with vertices $-1$ and $1$.

:::

::: {.hint}
A Möbius map sending the two vertices of a lune to $0$ and $\infty$ sends the lune to a sector.
:::

::: {.solution}
![The lune with vertices -1 and 1 is mapped by (1+z)/(1-z) to the sector between the lines at angles -pi/4 and pi/4, rotated by e^{i pi/4} to the first quadrant, squared to the upper half-plane, and sent to the unit disc by (z-i)/(z+i).](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_22-01-04.png)

::: pf

::: {.pf-step #sector}
$T(z)=\frac{1+z}{1-z}$ maps $L$ conformally onto the sector $S=\theset{\abs{\Arg w}<\pi/4}$.

::: pf-proof
Both boundary circles pass through $\pm1$, since $\abs{1\mp i}=\abs{-1\mp i}=\sqrt2$.
$T$ sends $-1\mapsto0$ and $1\mapsto\infty$, so it sends each boundary circle to a line through $0$.
The circles have centers $\pm i$ and equal radii, so they are swapped by $z\mapsto\bar z$, which commutes with $T$; hence the image lines are symmetric about $\RR$.
At $z=1$ the radii $1-i$ and $1+i$ are perpendicular, so the circles meet at angle $\pi/2$, and the image lines meet at angle $\pi/2$.
Since $T(0)=1\in S$ and $0\in L$, $T(L)=S$.
:::

:::

::: {.pf-step #half-plane}
$w\mapsto i w^2$ maps $S$ conformally onto the upper half-plane $\HH$.

::: pf-proof
Squaring maps $\theset{\abs{\Arg w}<\pi/4}$ bijectively onto $\theset{\abs{\Arg u}<\pi/2}$, and multiplication by $i$ rotates that half-plane onto $\HH$.
:::

:::

::: pf-step
$$
\boxed{F(z)=\frac{i\qty(\frac{1+z}{1-z})^2-i}{i\qty(\frac{1+z}{1-z})^2+i}=\frac{(1+z)^2-(1-z)^2}{(1+z)^2+(1-z)^2}=\frac{2z}{1+z^2}}
$$
maps $L$ conformally onto $\DD$.

::: pf-proof
Compose steps [](#sector){.pf-ref} and [](#half-plane){.pf-ref} with the Cayley map $u\mapsto\frac{u-i}{u+i}$, which maps $\HH$ conformally onto $\DD$, and simplify.
:::

:::

:::

:::
