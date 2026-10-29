---
schema: qual/card@1
id: E-JPAJE
kind: problem
title: Möbius transformations as cross-ratios
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source omits the hypothesis ad-bc != 0, without which f is constant or undefined and is not a Möbius transformation; the statement adds it.
---

::: {.exercise}
Write a Möbius transformation $f(z) = {az+b\over cz + d}$, where $ad-bc\neq0$, as a cross-ratio.

:::

::: {.solution}
For distinct $z_1,z_2,z_3$ in the Riemann sphere $\hat\CC$, write
$$
(z;z_1,z_2,z_3)\coloneqq\frac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)},
$$
with the usual conventions when one of the points is $\infty$; it is the unique Möbius transformation sending $z_1,z_2,z_3$ to $0,1,\infty$.

::: pf

::: {.pf-step #preimages}
The preimages of $0$, $1$, $\infty$ under $f$ are $z_1=-\frac ba$, $z_2=\frac{d-b}{a-c}$, $z_3=-\frac dc$, read as $\infty$ when the denominator vanishes, and they are distinct.

::: pf-proof
$az+b=0$ at $z_1$, $az+b=cz+d$ at $z_2$, and $cz+d=0$ at $z_3$; for instance $a=0$ gives $f(\infty)=0$, and $a=c$ gives $f(\infty)=1$. They are distinct because $f$ is a bijection of $\hat\CC$ when $ad-bc\neq0$.
:::

:::

::: pf-step
$f(z)=\boxed{\qty(z;\,-\tfrac ba,\,\tfrac{d-b}{a-c},\,-\tfrac dc)}$.

::: pf-proof
Both sides are Möbius transformations that send the three distinct points of step [](#preimages){.pf-ref} to $0,1,\infty$. A Möbius transformation is determined by the images of three distinct points, so they are equal.
:::

:::

:::

:::
