---
schema: qual/card@1
id: E-SNRS5
kind: problem
title: The integral of $1/(1+x^2)^2$ over $\RR$
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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source prints the integral with no instruction; the statement now asks to compute it.
---

::: {.exercise}
Compute
$$
\int_\RR {1 \over (1+x^2)^2} \dx.
$$
:::

::: {.solution}
Let $f(z) \coloneqq (1+z^2)^{-2} = (z-i)^{-2}(z+i)^{-2}$, with poles of order $2$ at $\pm i$. For $R>1$ let $\gamma_R$ be the segment $[-R,R]$ followed by the upper semicircle $C_R$ of radius $R$.

::: pf

::: {.pf-step #arc}
$\int_{C_R} f \to 0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{1+z^2}\geq R^2-1$, so $\abs{\int_{C_R} f}\leq \pi R/(R^2-1)^2\to 0$.
:::

:::

::: {.pf-step #residue}
$\Res_{z=i} f = \frac{1}{4i}$.

::: pf-proof
For a pole of order $2$,
$$
\Res_{z=i} f = \lim_{z\to i} \frac{d}{dz}\left[(z-i)^2 f(z)\right] = \lim_{z\to i} \frac{-2}{(z+i)^3} = \frac{-2}{(2i)^3} = \frac{1}{4i}.
$$
:::

:::

::: pf-step
$\int_\RR {1 \over (1+x^2)^2} \dx = \boxed{\frac{\pi}{2}}$.

::: pf-proof
For $R>1$, only the pole $i$ lies inside $\gamma_R$, so $\int_{-R}^R f + \int_{C_R} f = 2\pi i\cdot\frac{1}{4i} = \frac{\pi}{2}$ by the residue theorem and step [](#residue){.pf-ref}. Let $R\to\infty$ and apply step [](#arc){.pf-ref}.
:::

:::

:::

:::
