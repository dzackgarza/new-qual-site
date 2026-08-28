---
order: 15
---

# The mean value theorem

[[T-5BLYU]]

:::{.proof title="Circle and area means"}
Parameterize $\abs{z-z_0}=r$ by $z=z_0+re^{i\theta}$.
Cauchy's integral formula gives
\[
f(z_0)
= \frac{1}{2\pi i}\int_{\abs{z-z_0}=r}\frac{f(z)}{z-z_0}\,\dz
= \frac{1}{2\pi i}\int_0^{2\pi}\frac{f(z_0+re^{i\theta})}{re^{i\theta}}\, r i e^{i\theta}\,\dtheta
= \frac{1}{2\pi}\int_0^{2\pi} f(z_0+re^{i\theta})\,\dtheta
.\]
For the area mean, integrate the circle identity in the radius: if $0<\rho<r$ then
\[
\int_0^r \int_0^{2\pi} f(z_0+\rho e^{i\theta})\,\rho\,\dtheta\,\d\rho
= \int_0^r 2\pi f(z_0)\,\rho\,\d\rho
= \pi r^2 f(z_0)
,\]
so $f(z_0)=\frac{1}{\pi r^2}\iint_{D_r(z_0)} f(z)\,dA$.
The real-part claim is the same identities applied to $u=\Re f$, or the observation that both sides of the circle identity have matching real parts.

:::

The exercises for this section live on [[999 Exercises]].
