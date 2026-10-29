---
schema: qual/card@1
id: P-NY56Z
kind: problem
title: $\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$ for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: {.problem}
Let $a>0$ and calculate
$$
\int_0^\infty {\cos(x) \over (x^2 + a^2)^2}\, dx.
$$
:::

::: {.solution}
For $a>0$ let $I(a)\definedas\int_0^\infty\frac{\cos x}{x^2+a^2}\,dx$.

::: pf

::: {.pf-step #first-integral}
$I(a)=\frac{\pi}{2a}e^{-a}$.

::: pf-proof
Integrate $h(z)=\frac{e^{iz}}{z^2+a^2}$ over the boundary of the upper half-disk of radius $R>a$. The only pole inside is $ia$, with residue $\frac{e^{-a}}{2ia}$, so the contour integral is $\frac{\pi e^{-a}}{a}$. On the arc $\abs{e^{iz}}\le1$, so the arc integral is at most $\frac{\pi R}{R^2-a^2}\to0$. Hence $\int_{-\infty}^\infty\frac{e^{ix}}{x^2+a^2}\,dx=\frac{\pi e^{-a}}{a}$; taking real parts and using that the integrand $\frac{\cos x}{x^2+a^2}$ is even gives the claim.
:::

:::

::: {.pf-step #differentiate}
$I'(a)=-2a\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx$.

::: pf-proof
For $a$ in a compact interval $[\delta,A]\subset(0,\infty)$, $\abs{\frac{\partial}{\partial a}\frac{\cos x}{x^2+a^2}}=\frac{2a\abs{\cos x}}{(x^2+a^2)^2}\le\frac{2A}{(x^2+\delta^2)^2}$, which is integrable on $[0,\infty)$, so differentiation under the integral sign is justified.
:::

:::

::: pf-step
$\int_0^\infty\frac{\cos x}{(x^2+a^2)^2}\,dx=\boxed{\frac{\pi e^{-a}(a+1)}{4a^3}}$.

::: pf-proof
By step [](#first-integral){.pf-ref}, $I'(a)=-\frac{\pi e^{-a}}{2a^2}-\frac{\pi e^{-a}}{2a}=-\frac{\pi e^{-a}(a+1)}{2a^2}$. Divide by $-2a$ and use step [](#differentiate){.pf-ref}.
:::

:::

:::
:::
