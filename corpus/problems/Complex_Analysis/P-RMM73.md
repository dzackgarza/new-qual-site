---
schema: qual/card@1
id: P-RMM73
kind: problem
title: Cauchy's estimate and the mean value property on a closed disk
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $f$ be holomorphic in a neighborhood of the closed disk $\overline{D}_r(z_0)$.
Prove Cauchy's estimate for derivatives:
$$|f^{(n)}(z_0)| \le \frac{n!}{r^n} \max_{|z-z_0| = r} |f(z)|$$
and the Mean Value Property:
$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + r e^{i\theta}) \, d\theta.$$
:::

::: {.solution}
Write $M_r\coloneqq\max_{\abs{z-z_0}=r}\abs{f(z)}$.

::: pf

::: {.pf-step #cif}

$\displaystyle f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_{\abs{z-z_0}=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz$ for every $n\ge0$.

::: pf-proof

This is Cauchy's integral formula for derivatives, which applies because $f$ is holomorphic on a neighborhood of $\overline D_r(z_0)$.

:::

:::

::: pf-step

$\abs{f^{(n)}(z_0)}\le\dfrac{n!}{r^n}M_r$.

::: pf-proof

On the circle the integrand in step [](#cif){.pf-ref} has modulus at most $M_r/r^{n+1}$, and the circle has length $2\pi r$, so
$$
\abs{f^{(n)}(z_0)}\le\frac{n!}{2\pi}\cdot\frac{M_r}{r^{n+1}}\cdot2\pi r=\frac{n!}{r^n}M_r.
$$

:::

:::

::: pf-step

$f(z_0)=\dfrac1{2\pi}\displaystyle\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta$.

::: pf-proof

Take $n=0$ in step [](#cif){.pf-ref} and parametrize $z=z_0+re^{i\theta}$, $dz=ire^{i\theta}\,d\theta$:
$$
f(z_0)=\frac1{2\pi i}\int_0^{2\pi}\frac{f(z_0+re^{i\theta})}{re^{i\theta}}\,ire^{i\theta}\,d\theta=\frac1{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta.
$$

:::

:::

:::

:::
