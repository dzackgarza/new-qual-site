---
title: The integral formula
order: 20
topics:
- Cauchy Integral Formula

---

# The integral formula

The values of a holomorphic function inside a curve are determined by its values on the curve.

[[T-LA2UI]]

[[FT-5V4M2]]

[[FT-AK34G]]

::: {.proof}

![figures/image_2021-05-27-16-54-06.png](../../../../assets/assets/figures/image_2021-05-27-16-54-06.png)

:::

::: {.proof}

![figures/image_2021-05-27-16-56-39.png](../../../../assets/assets/figures/image_2021-05-27-16-56-39.png)

![figures/image_2021-05-27-16-56-52.png](../../../../assets/assets/figures/image_2021-05-27-16-56-52.png)

:::

::: {.proof title="Alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-49-17.png)

![](../../../../assets/assets/figures/2021-12-14_16-49-36.png)

:::

## The mean value property

For a circle centered at the point, the integral formula expresses $f$ at the center as the average of $f$ over the circle.

[[T-5BLYU]]

::: {.proof title="Circle and area means"}
Parameterize $\abs{z-z_0}=r$ by $z=z_0+re^{i\theta}$.
The integral formula gives
$$
f(z_0)
= \frac{1}{2\pi i}\int_{\abs{z-z_0}=r}\frac{f(z)}{z-z_0}\,\dz
= \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(z_0+re^{i\theta})}{re^{i\theta}}\, r i e^{i\theta}\,\dtheta
= \frac{1}{2\pi}\int_0^{2\pi} f(z_0+re^{i\theta})\,\dtheta
.$$
For the area mean, multiply the circle identity for radius $\rho\in(0,r)$ by $\rho$ and integrate over $\rho$:
$$
\int_0^r \int_0^{2\pi} f(z_0+\rho e^{i\theta})\,\rho\,\dtheta\,\drho
= \int_0^r 2\pi f(z_0)\,\rho\,\drho
= \pi r^2 f(z_0)
,$$
so $f(z_0)=\frac{1}{\pi r^2}\iint_{D_r(z_0)} f(z)\,dA$.
The real-part claim is the same identity applied to $u=\Re f$.

:::

::: {.remark title="Mean value property and the maximum principle"}
If $\abs f$ has a local maximum at $z_0$, then for small $r$
$$
\abs{f(z_0)} \leq \frac{1}{2\pi}\int_0^{2\pi}\abs{f(z_0+re^{i\theta})}\dtheta \leq \abs{f(z_0)}
,$$
and since $\abs f$ is continuous, $\abs f = \abs{f(z_0)}$ on every small circle about $z_0$.
This is the argument for the [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|maximum modulus principle]], and the same argument, with the mean value property of a real harmonic function $u$ in place of that of $f$, proves the maximum principle for $u$.

:::

## Exercises

[[E-4F5TF]] [[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]]
[[E-ZVO5P]] [[E-5AKU5]] [[E-AZSMO]] [[E-DDKSS]]
