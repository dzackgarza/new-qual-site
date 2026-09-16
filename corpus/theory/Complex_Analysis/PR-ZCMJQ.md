---
schema: qual/card@1
id: PR-ZCMJQ
kind: proposition
title: ML estimate for contour integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.proposition}
Let $\gamma\colon[a,b]\to\CC$ be a piecewise $C^1$ curve with length $L\coloneqq\int_a^b\abs{\gamma'(t)}\dt$, and let $f$ be continuous on the image of $\gamma$.
With $M\coloneqq\max_{z\in\gamma}\abs{f(z)}$,
$$
\abs{\int_\gamma f(z)\dz}\le ML.
$$
:::

::: {.proof}
By the definition of the [[D-6DAXB|contour integral]],
$$
\abs{\int_\gamma f(z)\dz}=\abs{\int_a^bf(\gamma(t))\gamma'(t)\dt}\le\int_a^b\abs{f(\gamma(t))}\abs{\gamma'(t)}\dt\le M\int_a^b\abs{\gamma'(t)}\dt=ML.
$$
:::
