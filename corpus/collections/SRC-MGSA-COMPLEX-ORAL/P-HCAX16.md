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

::: {.problem}
Let $u$ be a continuous real-valued function on a region $\Omega$.
Show that if $u$ has the mean-value property, then $u$ is harmonic.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own mollifier argument follows, with smoothing, the $C^{2}$ conclusion and the Laplacian identity as separate steps.

Let $u$ be continuous on the region $\Omega$ with the mean-value property: $u(z)=\frac{1}{2\pi}\int_{0}^{2\pi}u(z+re^{i\theta})d\theta$ whenever $\overline{D(z,r)}\subseteq\Omega$.

::: pf

::: {.pf-step #smooth}
$u$ is $C^{\infty}$ on $\Omega$.

::: pf-proof
Fix a disc $\overline{D(a,R)}\subseteq\Omega$ and a radial mollifier $\varphi_{\varepsilon}$ supported in $D(0,\varepsilon)$ with $\int\varphi_{\varepsilon}=1$, $\varepsilon<R$. In polar coordinates,
$(u*\varphi_{\varepsilon})(z)=\int_{0}^{\varepsilon}\psi_{\varepsilon}(r)\Big(\int_{0}^{2\pi}u(z-re^{i\theta})r\,d\theta\Big)dr=u(z)\int_{\CC}\varphi_{\varepsilon}$, the inner integral being $2\pi r\,u(z)$ by the mean-value property; so $u*\varphi_{\varepsilon}=u$ on $D(a,R-\varepsilon)$. A convolution with a smooth compactly supported function is smooth, so $u$ is $C^{\infty}$ there; as $a,R$ were arbitrary, on $\Omega$.
:::

:::

::: {.pf-step #laplacian}
For $C^{2}$ functions, $\Delta u(z)=\lim_{r\to0}\dfrac{4}{r^{2}}\Big(\dfrac{1}{2\pi}\int_{0}^{2\pi}u(z+re^{i\theta})d\theta-u(z)\Big)$.

::: pf-proof
Taylor's formula gives $\frac{1}{2\pi}\int_{0}^{2\pi}u(z+re^{i\theta})d\theta=u(z)+\frac{r^{2}}{4}\Delta u(z)+o(r^{2})$: the linear terms integrate to zero and the average of the quadratic terms is $\frac{r^{2}}{4}(u_{xx}+u_{yy})$. Rearranging and letting $r\to0$ gives the identity.
:::

:::

::: {.pf-step #harmonic}
$\Delta u=0$ on $\Omega$.

::: pf-proof
By step [](#smooth){.pf-ref} $u$ is $C^{2}$, so the identity of step [](#laplacian){.pf-ref} applies at each $z\in\Omega$ for all small $r$. The bracket is zero for every $r$ by the mean-value property, so the limit is $0$, that is $\Delta u(z)=0$.
:::

:::

::: {.pf-qed}
By step [](#harmonic){.pf-ref} $u$ is $C^{2}$ with $\Delta u=0$ on the region $\Omega$, which is the definition of harmonicity.
:::

:::

:::
