---
schema: qual/card@1
id: P-BKF18-5A
kind: problem
title: Conformal map from a crescent to the disk
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Describe a conformal map from
$$
\{z:\abs{z-4i}<4\}\cap\{z:\abs{z-i}>1\}
$$
onto the open unit disk.
:::

::: {.solution}

The map
$$
F(z)=\frac{w-i}{w+i},\qquad w=\exp\!\left(\frac{8\pi}{3}\Big(\frac1z+\frac i2\Big)\right),
$$
is a conformal map of $\Omega=\{\abs{z-4i}<4\}\cap\{\abs{z-i}>1\}$ onto the unit disk.

::: pf

::: {.pf-step #s1}

$z\mapsto 1/z$ maps $\Omega$ conformally onto the strip $\{-\tfrac12<\operatorname{Im}u<-\tfrac18\}$.

::: pf-proof

Both boundary circles pass through $0$, so $1/z$ maps them to lines. For $u=1/z$, $\abs{z-4i}<4$ is $\abs{z}^2<8\operatorname{Im}z$, that is $1<-8\operatorname{Im}u$, since $\operatorname{Im}(1/z)=-\operatorname{Im}z/\abs{z}^2$. In the same way $\abs{z-i}>1$ is $\abs{z}^2>2\operatorname{Im}z$, that is $\operatorname{Im}u>-\tfrac12$. The point $0$ is not in $\Omega$, so $1/z$ is a biholomorphism of $\Omega$ onto the strip.

:::

:::

::: {.pf-step #s2}

$u\mapsto \tfrac{8\pi}{3}(u+\tfrac i2)$ maps the strip onto $\{0<\operatorname{Im}v<\pi\}$, and $\exp$ maps that strip conformally onto the upper half-plane.

::: pf-proof

The translation by $i/2$ gives $0<\operatorname{Im}<\tfrac38$, and the dilation by $\tfrac{8\pi}{3}$ gives $0<\operatorname{Im}<\pi$. On this strip $\exp(x+iy)=e^xe^{iy}$ is injective and takes every value with argument in $(0,\pi)$.

:::

:::

::: {.pf-step #s3}

$w\mapsto (w-i)/(w+i)$ maps the upper half-plane conformally onto the unit disk.

::: pf-proof

For $\operatorname{Im}w>0$, $w$ is nearer to $i$ than to $-i$, so $\abs{w-i}<\abs{w+i}$. The Möbius map is injective, and its inverse $\zeta\mapsto i(1+\zeta)/(1-\zeta)$ maps the disk into the upper half-plane.

:::

:::

::: pf-qed

$F$ is the composite of the maps in steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::
