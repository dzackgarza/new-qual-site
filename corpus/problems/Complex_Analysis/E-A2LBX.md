---
schema: qual/card@1
id: E-A2LBX
kind: problem
title: Complex line integrals and the ML bound for $\log(z)/z^2$ on $\abs z=R$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Part (a) of the source reads "f: D -> C be a continuous function" with no "Let"; the statement supplies it.'
---

::: {.exercise}
(a) Let $f: D\to \CC$ be a continuous function, where $D\subset \CC$ is a domain. Let $\alpha:[a,b]\to D$ be a smooth curve.
Give a precise definition of the *complex line integral* $$\int_{\alpha} f.$$

(b) Assume that there exists a constant $M$ such that $\abs{f(\tau)}\leq M$ for all $\tau\in \operatorname{Image}(\alpha)$. Prove that $$\abs{\int_{\alpha} f}\leq M \times \operatorname{length}(\alpha).$$

(c) Let $C_R$ be the circle $\abs{z}=R$, described in the counterclockwise direction, where $R>1$.
Using the parametrization $z=Re^{it}$ for $0\le t\le2\pi$ and the pathwise determination $\log(Re^{it})=\log R+it$, provide an upper bound for $\abs{\int_{C_R} \frac{\log z}{z^2}\,dz}$ depending only on $R$ and universal constants.
:::

::: {.solution}

::: pf

::: pf-step
(a) $\int_\alpha f(z)\,dz\coloneqq\int_a^b f(\alpha(t))\,\alpha'(t)\,dt$.

::: pf-proof
The right-hand side is the integral of the continuous complex-valued function $t\mapsto f(\alpha(t))\alpha'(t)$ on $[a,b]$, defined as the integral of its real part plus $i$ times the integral of its imaginary part.
:::

:::

::: {.pf-step #ml-bound}
(b) $\abs{\int_\alpha f(z)\,dz}\le M\operatorname{length}(\alpha)$.

::: pf-proof
Since $\abs{\int_a^b g}\le\int_a^b\abs g$ for complex-valued continuous $g$,
$$
\abs{\int_\alpha f(z)\,dz}
\le\int_a^b\abs{f(\alpha(t))}\,\abs{\alpha'(t)}\,dt
\le M\int_a^b\abs{\alpha'(t)}\,dt
=M\operatorname{length}(\alpha).
$$
:::

:::

::: pf-step
(c) $\abs{\int_{C_R}\frac{\log z}{z^2}\,dz}\le\boxed{\frac{2\pi(\log R+2\pi)}{R}}$.

::: pf-proof
No continuous branch of $\log z$ exists on all of $C_R$, which winds once around $0$, so the integral is taken along $\alpha(t)=Re^{it}$, $0\le t\le2\pi$, with $\log(\alpha(t))=\log R+it$.
Then $\abs{\log(\alpha(t))}\le\log R+2\pi$, so
$$
\abs{\frac{\log(\alpha(t))}{\alpha(t)^2}}
\le\frac{\log R+2\pi}{R^2}.
$$
Since $\operatorname{length}(C_R)=2\pi R$, step [](#ml-bound){.pf-ref} gives the bound.
:::

:::

:::

:::
