---
schema: qual/card@1
id: P-EEUV6
kind: problem
title: An injective conformal map from $\{\abs{z}<1\}\setminus\{\abs{z-1/4}\le 1/4\}$ onto
  an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $\Omega$ be the region inside the unit circle $\abs{z} = 1$ and outside the circle $\abs{z-{1\over 4}} = {1\over 4}$.

Find an injective conformal map from $\Omega$ onto some annulus $\theset{r < \abs{z} < 1}$ for constant $r$.
:::

::: {.solution}

Let $\alpha\coloneqq2-\sqrt3$ and $\beta\coloneqq2+\sqrt3$, so $\alpha\beta=1$ and $\alpha+\beta=4$, and let $T(z)\coloneqq\frac{z-\alpha}{z-\beta}$.

::: pf

::: {.pf-step #symmetric}
$\alpha$ and $\beta$ are symmetric with respect to both boundary circles.

::: pf-proof
Both lie on the real line through the centers.
For $\abs{z}=1$: $\alpha\beta=1$.
For $\abs{z-1/4}=1/4$: $(\alpha-\tfrac14)(\beta-\tfrac14)=\alpha\beta-\tfrac{\alpha+\beta}4+\tfrac1{16}=\tfrac1{16}$.
:::

:::

::: {.pf-step #image}
$T(\Omega)=\{\alpha^2<\abs{w}<\alpha\}$.

::: pf-proof
A Möbius map sends a pair of points symmetric in a circle to a pair symmetric in the image circle; $T$ sends $\alpha,\beta$ to $0,\infty$, so by step [](#symmetric){.pf-ref} it sends each boundary circle to a circle centered at $0$.
The radii are $\abs{T(1)}=\frac{\sqrt3-1}{\sqrt3+1}=2-\sqrt3=\alpha$ and $\abs{T(1/2)}=\frac{\sqrt3-3/2}{\sqrt3+3/2}=\alpha^2$.
$\Omega$ lies between the two circles and $T(-1/2)=\frac{1/2+\alpha}{1/2+\beta}\approx0.18$ lies between $\alpha^2\approx0.072$ and $\alpha\approx0.27$.
:::

:::

::: pf-step
$\Phi(z)\coloneqq\frac1\alpha\frac{z-\alpha}{z-\beta}$ maps $\Omega$ injectively and conformally onto $\{\alpha<\abs{w}<1\}$, so $\boxed{r=2-\sqrt3}$.

::: pf-proof
$\beta>1$ lies outside $\Omega$, so $\Phi$ is holomorphic and injective on $\Omega$; scale step [](#image){.pf-ref} by $1/\alpha$.
:::

:::

:::

:::
