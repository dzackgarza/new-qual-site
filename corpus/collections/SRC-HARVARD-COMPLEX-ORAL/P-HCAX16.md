---
schema: qual/card@1
id: P-HCAX16
kind: problem
title: Continuous functions with the mean-value property are harmonic
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Mean Value Property
relations: []
review: draft
---

::: problem
Let $u$ be a continuous real-valued function on a region $\Omega$.
Show that if $u$ has the mean-value property, then $u$ is harmonic.
:::

::: solution
Fix a closed disk $\overline{D(a,R)}\subset\Omega$. Let $\varphi_\varepsilon$ be a smooth nonnegative radial mollifier supported in $D(0,\varepsilon)$, where $0<\varepsilon<R$. For $z\in D(a,R-\varepsilon)$, write $\varphi_\varepsilon(w)=\psi_\varepsilon(|w|)$. Polar coordinates and the mean-value property give
\[
(u*\varphi_\varepsilon)(z)
=\int_0^\varepsilon \psi_\varepsilon(r)
   \left(\int_0^{2\pi}u(z-re^{i\theta})\,r\,d\theta\right)dr
=u(z)\int_{\mathbb C}\varphi_\varepsilon(w)\,dA(w)
=u(z).
\]
Hence $u$ agrees locally with a smooth convolution, so $u\in C^\infty(\Omega)$.

Now fix $z\in\Omega$. For sufficiently small $r$, Taylor expansion of the smooth function $u$ around $z$ and averaging over the circle yield
\[
\frac1{2\pi}\int_0^{2\pi}u(z+re^{i\theta})\,d\theta
=u(z)+\frac{r^2}{4}\Delta u(z)+o(r^2),
\qquad r\to0.
\]
The left-hand side equals $u(z)$ by the mean-value property. Dividing by $r^2$ and letting $r\to0$ gives $\Delta u(z)=0$.

Thus $u$ is $C^2$ and satisfies $\Delta u=0$ throughout $\Omega$, so $u$ is harmonic.
:::
