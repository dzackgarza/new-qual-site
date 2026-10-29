---
schema: qual/card@1
id: P-OIP5P
kind: problem
title: $\int_0^\infty\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{2b}$
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
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states the identity without a hypothesis on b; it is false for b<0 and undefined for b=0, so the statement adds b>0.'
---

::: {.problem}
Let $b>0$. Show that
$$
\int_0^{\infty} {\cos(x) \over x^2 + b^2}\,dx = {\pi e^{-b} \over 2b}.
$$
:::

::: {.solution}
Let $f(z)=\frac{e^{iz}}{z^2+b^2}$. For $R>b$ let $\Gamma_R$ be the segment $[-R,R]$ followed by the upper semicircle $C_R$ of radius $R$.

::: pf

::: {.pf-step #residue}
$\oint_{\Gamma_R}f(z)\,dz=\frac{\pi e^{-b}}{b}$.

::: pf-proof
$z^2+b^2=(z-ib)(z+ib)$, so the only pole inside $\Gamma_R$ is the simple pole $ib$, with residue $\frac{e^{i(ib)}}{2ib}=\frac{e^{-b}}{2ib}$. Multiply by $2\pi i$.
:::

:::

::: {.pf-step #arc}
$\int_{C_R}f(z)\,dz\to0$ as $R\to\infty$.

::: pf-proof
For $\Im z\ge0$, $\abs{e^{iz}}=e^{-\Im z}\le1$, and on $C_R$, $\abs{z^2+b^2}\ge R^2-b^2$. So $\abs{\int_{C_R}f}\le\frac{\pi R}{R^2-b^2}\to0$.
:::

:::

::: pf-step
$\int_0^\infty\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{2b}$.

::: pf-proof
By steps [](#residue){.pf-ref} and [](#arc){.pf-ref}, $\int_{-\infty}^\infty\frac{e^{ix}}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{b}$. Taking real parts gives $\int_{-\infty}^\infty\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{b}$, and the integrand is even.
:::

:::

:::
:::
