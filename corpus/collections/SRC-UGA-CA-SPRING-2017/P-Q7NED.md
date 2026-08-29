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

:::{.problem}
Calculate
\[
\int_0^\infty {\sin(x) \over x(x^2+1)}\, dx
.\]
:::

::: {.solution}
<1>1. $\int_0^\infty \frac{\sin x}{x(x^2+1)}\, dx = \frac{1}{2}\operatorname{Im}\int_{-\infty}^{\infty} \frac{e^{ix}}{x(x^2+1)}\, dx$.
Proof: the integrand is even, and $\sin x = \operatorname{Im}(e^{ix})$.

<1>2. The integrand $\frac{e^{iz}}{z(z^2+1)}$ has a simple pole at $z = 0$ and simple poles at $z = \pm i$.
Proof: factor the denominator.

<1>3. Indent the contour around $z = 0$ (small semicircle above) and close in the upper half-plane; the pole at $z = i$ is enclosed, and the pole at $z = 0$ contributes half its residue.
Proof: standard contour for such integrals.

<1>4. $\operatorname{Res}_{z=i}\frac{e^{iz}}{z(z^2+1)} = \frac{e^{i\cdot i}}{i(2i)} = \frac{e^{-1}}{-2} = -\frac{1}{2e}$.
Proof: residue at the simple pole $z = i$.

<1>5. $\operatorname{Res}_{z=0}\frac{e^{iz}}{z(z^2+1)} = \frac{e^{0}}{0^2+1} = 1$.
Proof: residue at the simple pole $z = 0$.

<1>6. By the residue theorem (with the indentation contributing $\pi i$ times the residue at $0$),
$$\int_{-\infty}^{\infty} \frac{e^{ix}}{x(x^2+1)}\, dx = 2\pi i \operatorname{Res}_{z=i} + \pi i \operatorname{Res}_{z=0} = 2\pi i\left(-\frac{1}{2e}\right) + \pi i(1) = \pi i\left(1 - \frac{1}{e}\right).$$
Proof: the principal value integral plus the half-residue at $0$.

<1>7. Hence $\int_0^\infty \frac{\sin x}{x(x^2+1)}\, dx = \frac{1}{2}\operatorname{Im}\left[\pi i\left(1 - \frac{1}{e}\right)\right] = \frac{\pi}{2}\left(1 - \frac{1}{e}\right)$.
Proof: <1>1 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::

