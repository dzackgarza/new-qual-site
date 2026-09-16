---
schema: qual/card@1
id: FF-3IKZZ
kind: fact
title: ML estimate for contour integrals
prompts:
- State the maximum length (ML) estimate for a contour integral.
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations:
- kind: variant-of
  target: T-SFXI7
review: draft
---

::: {.fact}
Let $\gamma\colon[a,b]\to\CC$ be a piecewise $C^1$ curve with length $\ell(\gamma)\coloneqq\int_a^b\abs{\gamma'(t)}\dt$, and let $f$ be continuous on $\gamma([a,b])$.
Then
$$
\abs{\int_\gamma f\dz}\le\sup_{z\in\gamma([a,b])}\abs{f(z)}\cdot\ell(\gamma).
$$
:::

::: {.proof}
By the definition of the [[D-6DAXB|contour integral]],
$$
\abs{\int_\gamma f\dz}=\abs{\int_a^bf(\gamma(t))\gamma'(t)\dt}\le\int_a^b\abs{f(\gamma(t))}\,\abs{\gamma'(t)}\dt\le\sup_{z\in\gamma([a,b])}\abs{f(z)}\int_a^b\abs{\gamma'(t)}\dt.
$$
:::
