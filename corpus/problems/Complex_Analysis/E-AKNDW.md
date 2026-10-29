---
schema: qual/card@1
id: E-AKNDW
kind: problem
title: $\int_\RR\frac{dx}{(1+x^2)^2}$
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
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source displays the formula with no instruction; the statement asks to show it.
---

::: {.exercise}
Show that
$$
\int_\RR \frac{1}{(1+x^2)^2}\dx = \frac{\pi}{2}.
$$
:::

::: {.solution}
Let $f(z)=\frac{1}{(1+z^2)^2}$, and for $R>1$ let $C_R$ be the positively oriented upper semicircle of radius $R$.

::: pf

::: {.pf-step #residue}
$\int_{-R}^R f(x)\,dx+\int_{C_R}f(z)\,dz=\frac{\pi}{2}$ for $R>1$.

::: pf-proof
The only enclosed pole is the double pole at $z=i$, with residue
$$
\Res_{z=i}f(z)
=\left.\frac{d}{dz}\frac{1}{(z+i)^2}\right|_{z=i}
=-\frac{2}{(2i)^3}
=\frac{1}{4i},
$$
and $2\pi i\cdot\frac1{4i}=\frac\pi2$ by the residue theorem.
:::

:::

::: {.pf-step #arc}
$\int_{C_R}f(z)\,dz\to0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{1+z^2}\ge R^2-1$, so the ML estimate bounds the integral by $\pi R/(R^2-1)^2$.
:::

:::

::: pf-step
$\int_{\RR}\frac{dx}{(1+x^2)^2}=\frac{\pi}{2}$.

::: pf-proof
Let $R\to\infty$ in step [](#residue){.pf-ref} and apply step [](#arc){.pf-ref}.
:::

:::

:::

:::
