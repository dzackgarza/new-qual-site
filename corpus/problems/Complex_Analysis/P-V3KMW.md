---
schema: qual/card@1
id: P-V3KMW
kind: problem
title: The $ML$ estimate for contour integrals and $\abs{\int_{\abs{z}=R}\frac{\log z}{z^2}\,dz}$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Let $f:D\to\CC$ be continuous and let $\alpha:[a,b]\to D$ be a smooth
curve.

(a) Define $\int_\alpha f$.

(b) If $\abs{f}\le M$ on the image of $\alpha$, prove
$$
\abs{\int_\alpha f}\le M\,\operatorname{length}(\alpha).
$$

(c) For $C_R:\abs{z}=R$, $R>1$, give an upper bound for
$$
\abs{\int_{C_R}\frac{\log z}{z^2}\,dz},
$$
after fixing a continuous determination of the logarithm along the
parametrized circle.
:::

::: {.solution}

::: pf

::: pf-step

(a) $\displaystyle\int_\alpha f(z)\,dz \coloneqq \int_a^b f(\alpha(t))\,\alpha'(t)\,dt$.

::: pf-proof

This is the definition of the contour integral along a smooth curve; the integrand $t \mapsto f(\alpha(t))\alpha'(t)$ is continuous on $[a, b]$.

:::

:::

::: {.pf-step #ml}

(b) $\abs{\int_\alpha f}\le M\,\operatorname{length}(\alpha)$.

::: pf-proof

The modulus of an integral is at most the integral of the modulus, so
$$
\abs{\int_\alpha f}
\le\int_a^b\abs{f(\alpha(t))}\,\abs{\alpha'(t)}\,dt
\le M\int_a^b\abs{\alpha'(t)}\,dt = M\,\operatorname{length}(\alpha).
$$

:::

:::

::: pf-step

(c) With the determination $\log(Re^{it}) = \log R + it$ for $0 \leq t \leq 2\pi$,
$$
\abs{\int_{C_R}\frac{\log z}{z^2}\,dz}
\le \boxed{\frac{2\pi}{R}(\log R+2\pi)}.
$$

::: pf-proof

Parametrize $C_R$ by $z=Re^{it}$, $0\le t\le2\pi$. Along it, $\abs{\log R + it}\le\log R+2\pi$ and $\abs{z^2} = R^2$, so the integrand is bounded by $(\log R + 2\pi)/R^2$. The length of $C_R$ is $2\pi R$, and step [](#ml){.pf-ref} gives the bound.

:::

:::

:::

:::

::: {.remark}
No holomorphic logarithm is single-valued on a neighborhood of the whole circle $C_R$, so the integral in (c) depends on the chosen determination along the parametrized contour.
:::
