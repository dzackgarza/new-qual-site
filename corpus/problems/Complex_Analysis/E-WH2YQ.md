---
schema: qual/card@1
id: E-WH2YQ
kind: problem
title: "The locus $\\Arg\\qty{z-a\\over z-b}=\\theta$: circular arcs through $a$ and $b$"
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Fix $a,b\in \CC$ and $\theta$, and describe the locus
$$
\theset{z\st \Arg\qty{z-a\over z-b} = \theta}.
$$

:::

::: {.solution}
![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-16_00-02-51.png)

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-16_00-06-08.png)

![](../../assets/Complex_Analysis/999_Quals/figures/ArcCapable.gif)

Assume $a\neq b$, take $\Arg$ with values in $(-\pi,\pi]$, and let $L_\theta$ denote the locus; it excludes $a$ and $b$.

::: pf

::: {.pf-step #mobius}
$L_\theta = T^{-1}(R_\theta)$, where $T(z) = \frac{z-a}{z-b}$ and $R_\theta = \theset{re^{i\theta} \st r>0}$ is the open ray at angle $\theta$.

::: pf-proof
This is the definition of $\Arg$.
:::

:::

::: {.pf-step #circle}
$L_\theta$ is an open arc of a circle or line through $a$ and $b$, with endpoints $a$ and $b$.

::: pf-proof
$T$ is a Möbius map with $T(a) = 0$ and $T(b) = \infty$, so $T^{-1}$ maps the line through $0$ containing $R_\theta$ to a circle or line $C$ through $a$ and $b$, and maps the ray $R_\theta$, one of the two arcs of that line between $0$ and $\infty$, onto one of the two arcs of $C$ between $a$ and $b$.
:::

:::

::: pf-step
The locus is as follows.

- For $\theta = \pi$: the open segment from $a$ to $b$.
- For $\theta = 0$: the line through $a$ and $b$ with the closed segment $[a,b]$ removed.
- For $0<\abs\theta<\pi$: the open arc from $a$ to $b$ of the circle through $a$ and $b$ on which the chord $[a,b]$ subtends the angle $\abs\theta$ at every point, lying to the right of the directed line from $a$ to $b$ when $\theta>0$ and to the left when $\theta<0$.

::: pf-proof
By step [](#circle){.pf-ref} it suffices to identify the arc.
$\Arg\frac{z-a}{z-b}$ is the oriented angle at $z$ from the vector $b - z$ to the vector $a - z$; its absolute value is the angle that the chord $[a,b]$ subtends at $z$.
This angle is $\pi$ exactly on the open segment and $0$ exactly on the rest of the line minus the segment.
For $0<\abs\theta<\pi$ the arc is therefore not on the line, and the inscribed angle theorem identifies the circle: its center $O$ satisfies $\angle aOb = 2\abs\theta$.
The sign of the oriented angle is constant on each side of the line through $a$ and $b$; at $a=-1$, $b=1$, $z=i$ one computes $\frac{i+1}{i-1} = -i$, of argument $-\pi/2$, which fixes the side.
:::

:::

:::

:::
