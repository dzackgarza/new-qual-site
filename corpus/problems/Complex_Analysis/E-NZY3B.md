---
schema: qual/card@1
id: E-NZY3B
kind: problem
title: Complement of a segment
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Map C minus [-1, 1] to D". That domain is not simply connected, so it has no conformal map onto D; the statement asks for the complement of the segment in the Riemann sphere.'
---

::: {.exercise}
Find a conformal map of $(\CC\cup\{\infty\})\sm[-1, 1]$ onto $\DD$.
:::

::: {.solution}

Write $\sqrt{\cdot}$ for the principal branch of the square root on $\CC\setminus(-\infty,0]$.

::: pf

::: {.pf-step #mobius}
$T(z) \coloneqq \frac{z+1}{z-1}$ maps $\CC\sm[-1,1]$ conformally onto $\CC\setminus(-\infty,0]$.

::: pf-proof
$T$ is a Möbius transformation with $T(-1)=0$, $T(1)=\infty$, $T(\infty)=1$, so it maps the circle $\RR\cup\{\infty\}$ to itself and the arc $[-1,1]$ through $T(0)=-1$ onto the arc $[-\infty,0]$ through $-1$.
Hence $T$ maps $(\CC\cup\{\infty\})\sm[-1,1]$ bijectively onto $(\CC\cup\{\infty\})\setminus[-\infty,0]$, and $\infty\mapsto 1$, so it maps $\CC\sm[-1,1]$ onto $\CC\setminus\big((-\infty,0]\cup\{1\}\big)$.
:::

:::

::: {.pf-step #root}
$\sqrt{\cdot}$ maps $\CC\setminus(-\infty,0]$ conformally onto the right half-plane $H \coloneqq \{\operatorname{Re} w > 0\}$, and $C(w) \coloneqq \frac{w-1}{w+1}$ maps $H$ conformally onto $\DD$.

::: pf-proof
The principal square root halves the argument, mapping $-\pi<\Arg<\pi$ onto $-\pi/2<\Arg<\pi/2$, with inverse $w\mapsto w^2$.
For $\operatorname{Re}w>0$, $w$ is closer to $1$ than to $-1$, so $\abs{C(w)}<1$; $C$ is a Möbius transformation with inverse $\zeta\mapsto\frac{1+\zeta}{1-\zeta}$, which maps $\DD$ into $H$.
:::

:::

::: pf-step
The map
$$
\boxed{\varphi(z) \coloneqq \frac{\sqrt{T(z)}-1}{\sqrt{T(z)}+1}}
$$
is a conformal map of $\CC\sm[-1,1]$ onto $\DD\setminus\{0\}$, and setting $\varphi(\infty)=0$ makes it a conformal map of $(\CC\cup\{\infty\})\sm[-1,1]$ onto $\DD$.
Its inverse is $\zeta\mapsto\frac12\left(\zeta+\frac1\zeta\right)$.

::: pf-proof
By steps [](#mobius){.pf-ref} and [](#root){.pf-ref}, $\varphi = C\circ\sqrt{\cdot}\circ T$ is conformal and injective, its image omits only $C(\sqrt{T(\infty)}) = C(1) = 0$, and it extends to $\infty$ by $\varphi(\infty)=0$.
Solving $\zeta = C(\sqrt{T(z)})$ gives $\sqrt{T(z)} = \frac{1+\zeta}{1-\zeta}$, so
$$
\frac{z+1}{z-1} = \frac{(1+\zeta)^2}{(1-\zeta)^2}, \qquad\text{hence}\qquad z = \frac{(1+\zeta)^2+(1-\zeta)^2}{(1+\zeta)^2-(1-\zeta)^2} = \frac{1+\zeta^2}{2\zeta}.
$$
:::

:::

:::

:::
