---
schema: qual/card@1
id: E-SPIVX
kind: problem
title: $\int_0^\infty \frac{\cos x}{x^2+b^2}\,dx$
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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source prints the identity with no instruction and no hypothesis on $b$; the statement now asks to show it for $b>0$.
---

::: {.exercise}
Show that for $b>0$,
$$
I \coloneqq \int_{0}^{\infty} \frac{\cos x}{x^{2}+b^{2}} \dx=\frac{\pi e^{-b}}{2 b}.
$$
:::

::: {.solution}
Let $f(z) \coloneqq \frac{e^{iz}}{(z+ib)(z-ib)}$ and $\tilde I \coloneqq \int_\RR f(x)\dx$. For $R>b$ let $\gamma_R$ be the segment $[-R,R]$ followed by the upper semicircle $C_R$ of radius $R$.

![figures/2021-07-29_18-42-38.png](../../assets/figures/2021-07-29_18-42-38.png)

::: pf

::: {.pf-step #even}
$I = \frac12\Re\tilde I$.

::: pf-proof
The integrand of $I$ is even, so $2I = \int_\RR \frac{\cos x}{x^2+b^2}\dx = \Re\tilde I$.
:::

:::

::: {.pf-step #arc}
$\int_{C_R} f\to 0$ as $R\to\infty$.

::: pf-proof
For $\Im z\geq 0$, $\abs{e^{iz}} = e^{-\Im z}\leq 1$, and on $C_R$, $\abs{z^2+b^2}\geq R^2-b^2$. So $\abs{\int_{C_R} f}\leq \pi R/(R^2-b^2)\to 0$.
:::

:::

::: {.pf-step #tilde}
$\tilde I = \frac{\pi e^{-b}}{b}$.

::: pf-proof
For $R>b$ only the simple pole $ib$ lies inside $\gamma_R$, and
$$
\int_{\gamma_R} f = 2\pi i\Res_{z=ib} f = 2\pi i\,\frac{e^{i\cdot ib}}{2ib} = \frac{\pi e^{-b}}{b}.
$$
Let $R\to\infty$ and apply step [](#arc){.pf-ref}.
:::

:::

::: pf-step
$I = \boxed{\frac{\pi e^{-b}}{2b}}$.

::: pf-proof
Combine steps [](#even){.pf-ref} and [](#tilde){.pf-ref}.
:::

:::

:::

:::
