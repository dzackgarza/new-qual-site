---
title: The integral formula
order: 20
problems:
  topics:
  - Cauchy Integral Formula
  - Cauchy's Integral Formula
---

# The integral formula

The values of a holomorphic function inside a curve are determined by its values on the curve.
Every estimate in the chapter is this formula plus a bound on the integrand.

[[T-LA2UI]]

[[FT-5V4M2]]

[[FT-AK34G]]

:::{.proof}

![figures/image_2021-05-27-16-54-06.png](../../../../assets/assets/figures/image_2021-05-27-16-54-06.png)

:::

:::{.proof}

![figures/image_2021-05-27-16-56-39.png](../../../../assets/assets/figures/image_2021-05-27-16-56-39.png)

![figures/image_2021-05-27-16-56-52.png](../../../../assets/assets/figures/image_2021-05-27-16-56-52.png)

:::

:::{.proof title="Alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-49-17.png)

![](../../../../assets/assets/figures/2021-12-14_16-49-36.png)

:::

## The mean value property

Taking the curve to be a circle centered at the point turns the formula into an average, which is the form most arguments use.

[[T-5BLYU]]

:::{.proof title="Circle and area means"}
Parameterize $\abs{z-z_0}=r$ by $z=z_0+re^{i\theta}$.
The integral formula gives
\[
f(z_0)
= \frac{1}{2\pi i}\int_{\abs{z-z_0}=r}\frac{f(z)}{z-z_0}\,\dz
= \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(z_0+re^{i\theta})}{re^{i\theta}}\, r i e^{i\theta}\,\dtheta
= \frac{1}{2\pi}\int_0^{2\pi} f(z_0+re^{i\theta})\,\dtheta
.\]
For the area mean, integrate the circle identity in the radius: for $0<\rho<r$,
\[
\int_0^r \int_0^{2\pi} f(z_0+\rho e^{i\theta})\,\rho\,\dtheta\,\drho
= \int_0^r 2\pi f(z_0)\,\rho\,\drho
= \pi r^2 f(z_0)
,\]
so $f(z_0)=\frac{1}{\pi r^2}\iint_{D_r(z_0)} f(z)\,dA$.
The real-part claim is the same identity applied to $u=\Re f$.

:::

:::{.remark title="Where the mean value property is used"}
It is the hypothesis of the maximum principle: a value equal to the average of its neighbours cannot exceed all of them.
That is the whole proof of [[Complex_Analysis/cauchy-theory/maximum-modulus-and-open-mapping|maximum modulus]], and it is also what makes harmonic functions behave the same way.

:::

## Exercises

[[E-4F5TF]] [[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]]
[[E-ZVO5P]] [[E-5AKU5]] [[E-AZSMO]] [[E-DDKSS]]
