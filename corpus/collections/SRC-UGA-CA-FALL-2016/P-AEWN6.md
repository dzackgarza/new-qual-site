---
schema: qual/card@1
id: P-AEWN6
kind: problem
title: 'The complex line integral, the bound $\abs{\int_\alpha f}\leq M\cdot\operatorname{length}(\alpha)$, and an estimate of $\int_{\abs z=R}\log z/z^2\,dz$'
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
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(a) Let $f: D\rightarrow {\CC}$ be a continuous function, where $D\subset {\CC}$ is a domain. Let $\alpha:[a,b]\rightarrow D$ be a smooth curve.
Give a precise definition of the *complex line integral* $$\int_{\alpha} f.$$

(b) Assume that there exists a constant $M$ such that $\abs{f(\tau)}\leq M$ for all $\tau\in\operatorname{Image}(\alpha)$. Prove that $$\abs{ \int_{\alpha} f }\leq M \times \operatorname{length}(\alpha).$$

(c) Let $C_R$ be the circle $\abs{z}=R$, described in the counterclockwise direction, where $R>1$.
Provide an upper bound for $\abs{ \int_{C_R} \dfrac{\log{(z)} }{z^2} },$ which depends [only]{.underline} on $R$ and other constants.
:::

::: {.solution}

::: pf

::: {.pf-step #def}

For a smooth curve $\alpha:[a,b]\to D$ and a continuous $f:D\to\CC$,
$$
\int_\alpha f\coloneqq\int_a^b f(\alpha(t))\,\alpha'(t)\,dt,
$$
where the integral of the continuous complex-valued function $g=f\circ\alpha\cdot\alpha'$ is $\int_a^b\operatorname{Re}g\,dt+i\int_a^b\operatorname{Im}g\,dt$.

:::

::: {.pf-step #ml}

$\abs{\int_\alpha f}\le M\cdot\operatorname{length}(\alpha)$, where $\operatorname{length}(\alpha)=\int_a^b\abs{\alpha'(t)}\,dt$.

::: pf-proof

Let $I=\int_\alpha f$. If $I=0$ there is nothing to prove. Otherwise write $I=\abs{I}e^{i\theta}$. By Step [](#def){.pf-ref} and linearity,
$$
\abs{I}=e^{-i\theta}I=\int_a^b e^{-i\theta}f(\alpha(t))\alpha'(t)\,dt.
$$
The left side is real, so it equals the real part of the right side:
$$
\abs{I}=\int_a^b\operatorname{Re}\bigl(e^{-i\theta}f(\alpha(t))\alpha'(t)\bigr)\,dt
\le\int_a^b\abs{f(\alpha(t))}\,\abs{\alpha'(t)}\,dt
\le M\int_a^b\abs{\alpha'(t)}\,dt.
$$

:::

:::

::: {.pf-step #bound}

With the principal branch $\log z=\ln\abs{z}+i\operatorname{Arg}z$, $\operatorname{Arg}z\in(-\pi,\pi]$,
$$
\abs{\int_{C_R}\frac{\log z}{z^2}\,dz}\le\frac{2\pi\sqrt{(\ln R)^2+\pi^2}}{R}.
$$

::: pf-proof

Parametrize $C_R$ by $\alpha(t)=Re^{it}$, $-\pi\le t\le\pi$. The integrand is continuous on $C_R$ except at $z=-R$, a single parameter value, so the integral exists and Step [](#ml){.pf-ref} applies to it. On $C_R$, $\abs{z^2}=R^2$ and $\abs{\log z}=\sqrt{(\ln R)^2+(\operatorname{Arg}z)^2}\le\sqrt{(\ln R)^2+\pi^2}$. The length of $C_R$ is $2\pi R$. Step [](#ml){.pf-ref} with $M=\sqrt{(\ln R)^2+\pi^2}/R^2$ gives the bound.

:::

:::

::: pf-qed

Steps [](#def){.pf-ref}, [](#ml){.pf-ref} and [](#bound){.pf-ref} answer (a), (b) and (c).

:::

:::

:::
