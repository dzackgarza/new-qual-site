---
schema: qual/card@1
id: P-Q7NED
kind: problem
title: $\int_0^\infty\frac{\sin x}{x(x^2+1)}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Calculate
\[
\int_0^\infty {\sin(x) \over x(x^2+1)}\, dx
.\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\int_0^\infty \frac{\sin x}{x(x^2+1)}\, dx = \frac{1}{2}\operatorname{Im}\int_{-\infty}^{\infty} \frac{e^{ix}}{x(x^2+1)}\, dx$.

::: pf-proof

the integrand is even, and $\sin x = \operatorname{Im}(e^{ix})$.

:::

:::

::: pf-step

The integrand $\frac{e^{iz}}{z(z^2+1)}$ has a simple pole at $z = 0$ and simple poles at $z = \pm i$.

::: pf-proof

factor the denominator.

:::

:::

::: pf-step

Indent the contour around $z = 0$ (small semicircle above) and close in the upper half-plane; the pole at $z = i$ is enclosed, and the pole at $z = 0$ contributes half its residue.

::: pf-proof

standard contour for such integrals.

:::

:::

::: pf-step

$\operatorname{Res}_{z=i}\frac{e^{iz}}{z(z^2+1)} = \frac{e^{i\cdot i}}{i(2i)} = \frac{e^{-1}}{-2} = -\frac{1}{2e}$.

::: pf-proof

residue at the simple pole $z = i$.

:::

:::

::: pf-step

$\operatorname{Res}_{z=0}\frac{e^{iz}}{z(z^2+1)} = \frac{e^{0}}{0^2+1} = 1$.

::: pf-proof

residue at the simple pole $z = 0$.

:::

:::

::: {.pf-step #s6}

By the residue theorem (with the indentation contributing $\pi i$ times the residue at $0$),
$$\int_{-\infty}^{\infty} \frac{e^{ix}}{x(x^2+1)}\, dx = 2\pi i \operatorname{Res}_{z=i} + \pi i \operatorname{Res}_{z=0} = 2\pi i\left(-\frac{1}{2e}\right) + \pi i(1) = \pi i\left(1 - \frac{1}{e}\right).$$

::: pf-proof

the principal value integral plus the half-residue at $0$.

:::

:::

::: {.pf-step #s7}

Hence $\int_0^\infty \frac{\sin x}{x(x^2+1)}\, dx = \frac{1}{2}\operatorname{Im}\left[\pi i\left(1 - \frac{1}{e}\right)\right] = \frac{\pi}{2}\left(1 - \frac{1}{e}\right)$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
