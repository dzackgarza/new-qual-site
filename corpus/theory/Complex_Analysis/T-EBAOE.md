---
schema: qual/card@1
id: T-EBAOE
kind: theorem
title: Argument principle as a winding number
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Winding Number
relations:
- kind: variant-of
  target: T-52HK6
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-7DFVJ|meromorphic]] on $\Omega$, and let $\gamma\colon[a,b]\to\Omega$ be a piecewise smooth closed curve on which $f$ has no [[D-65VIK|zeros]] or [[D-AUD6K|poles]].
Then
$$
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\dz=\Index_{w=0}(f\circ\gamma),
$$
the [[D-PJ7JM|winding number]] of the closed curve $f\circ\gamma$ about $0$.
:::

::: {.proof}
The curve $f\circ\gamma$ is closed, piecewise smooth, and avoids $0$.
Substituting $w=f(\gamma(t))$, so that $\dw=f'(\gamma(t))\gamma'(t)\dt$, gives
$$
\Index_{w=0}(f\circ\gamma)=\frac{1}{2\pi i}\int_{f\circ\gamma}\frac{\dw}{w}=\frac{1}{2\pi i}\int_a^b\frac{f'(\gamma(t))}{f(\gamma(t))}\gamma'(t)\dt=\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\dz.
$$
:::
