---
schema: qual/card@1
id: P-BKF09-3A
kind: problem
title: Contour integral of $1/\cos z$ over $\abs{ z}=2$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Find
$$
\int_{\abs{z}=2}\frac{1}{\cos z}\,dz,
$$
where the integral is taken with respect to the counterclockwise (positively oriented) parameterization of the circle $\abs{z}=2$.
:::

::: {.solution}

The argument is the card's own: the integral vanishes for want of symmetry, and the residue computation confirms it.

::: pf

::: {.pf-step #even}

$\sec z=1/\cos z$ is even, and the contour $\abs{z}=2$ is invariant under $z\mapsto-z$ with reversed orientation.

::: pf-proof

$\cos(-z)=\cos z$ gives $\sec(-z)=\sec z$, since $\cos$ is an even entire function with no zeros on $\abs{z}=2$ (the zeros of $\cos$ are $\pm\pi/2+2\pi k$, of modulus $1$ or more — exactly $\pi/2\approx1.571<2$, so $\pm\pi/2$ lie inside the circle but not on it). The substitution $z=-w$ maps $\abs{z}=2$ onto $\abs{w}=2$ and reverses the direction of travel, so $\int_{\abs{z}=2}\sec z\,dz=-\int_{\abs{w}=2}\sec w\,dw$.

:::

:::

::: {.pf-step #residues}

$\operatorname{Res}_{\pi/2}\sec z=-1$ and $\operatorname{Res}_{-\pi/2}\sec z=1$.

::: pf-proof

$\cos z$ has simple zeros at $\pm\pi/2$, so $\sec$ has simple poles there with residue $1/\cos'(z)=-1/\sin(z)$ evaluated at the pole: at $z=\pi/2$ this is $-1/\sin(\pi/2)=-1$, and at $z=-\pi/2$ it is $-1/\sin(-\pi/2)=1$.

:::

:::

::: {.pf-step #evaluate}

$\displaystyle\int_{\abs{z}=2}\frac{dz}{\cos z}=2\pi i(-1+1)=0$.

::: pf-proof

The poles of $\sec$ inside $\abs{z}=2$ are exactly $\pm\pi/2$: the zeros of $\cos$ are $\pm\pi/2+2\pi k$, and $\abs{\pm\pi/2+2\pi k}\ge\pi/2$ with equality only for $k=0$, while $\pi/2<2$. The residue theorem then gives the integral as $2\pi i$ times the sum of the residues, which is
$$
\boxed{\int_{\abs{z}=2}\frac{dz}{\cos z}=0.}
$$
This agrees with step [](#even){.pf-ref}: the integral equals its own negative.

:::

:::

:::

:::
