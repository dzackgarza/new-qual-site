---
schema: qual/card@1
id: P-HLAG5
kind: problem
title: Images of circles $|z|=r$ and rays $\arg z=\theta_0$ under $z+1/z$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $f(z)=z+1 / z$.
Describe the images of both the circle $|z|=r$ of radius $r(r \neq 0)$ and the ray $\arg z=\theta_{0}$ under $f$ in terms of well known curves.
:::

::: {.solution}
Write $w = f(z) = x+iy$.

::: pf

::: pf-step
For $r\neq 1$ the circle $\abs z=r$ maps onto the ellipse $\boxed{\dfrac{x^2}{(r+r^{-1})^2}+\dfrac{y^2}{(r-r^{-1})^2}=1}$ with foci $\pm 2$; for $r=1$ it maps onto the segment $[-2,2]$.

::: pf-proof
For $z=re^{i\theta}$, $\theta\in[0,2\pi)$,
$$
w = \qty(r+\frac1r)\cos\theta + i\qty(r-\frac1r)\sin\theta,
$$
which traces the stated ellipse once. Its foci are at $\pm c$ with $c^2=(r+r^{-1})^2-(r-r^{-1})^2=4$. For $r=1$, $w=2\cos\theta$ runs over $[-2,2]$.
:::

:::

::: pf-step
If $\sin\theta_0\cos\theta_0\neq 0$, the ray $\arg z=\theta_0$ maps onto the branch of the hyperbola $\boxed{\dfrac{x^2}{4\cos^2\theta_0}-\dfrac{y^2}{4\sin^2\theta_0}=1}$ on which $x$ has the sign of $\cos\theta_0$; its foci are $\pm 2$.

::: pf-proof
For $z=\rho e^{i\theta_0}$, $\rho>0$, we get $x=(\rho+\rho^{-1})\cos\theta_0$ and $y=(\rho-\rho^{-1})\sin\theta_0$. Since $(\rho+\rho^{-1})^2-(\rho-\rho^{-1})^2=4$, the point lies on the stated hyperbola, and $x$ has the sign of $\cos\theta_0$. As $\rho$ runs over $(0,\infty)$, $\rho-\rho^{-1}$ runs over $\RR$, so $y$ takes every real value and the whole branch is covered. The foci are at $\pm c$ with $c^2 = 4\cos^2\theta_0+4\sin^2\theta_0=4$.
:::

:::

::: pf-step
The ray $\theta_0=0$ maps onto $[2,\infty)$, the ray $\theta_0=\pi$ onto $(-\infty,-2]$, and the rays $\theta_0=\pm\pi/2$ onto the imaginary axis.

::: pf-proof
For $\theta_0=0$ or $\pi$, $w=\pm(\rho+\rho^{-1})$ and $\rho+\rho^{-1}$ runs over $[2,\infty)$. For $\theta_0=\pm\pi/2$, $w=\pm i(\rho-\rho^{-1})$ and $\rho-\rho^{-1}$ runs over $\RR$.
:::

:::

:::

:::
