---
schema: qual/card@1
id: PR-L5UH3
kind: proposition
title: Biholomorphism from the right half-plane onto the unit disc
slogan: 'The Cayley map $\frac{1-z}{1+z}$ turns the right half-plane into the unit disc.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.proposition}
Let $\HH_R\coloneqq\theset{z\in\CC \st \Re z>0}$ be the right half-plane and $\DD\coloneqq\theset{w\in\CC \st \abs{w}<1}$ the unit disc.
The map
$$
\varphi\colon\HH_R\to\DD,\qquad \varphi(z)=\frac{1-z}{1+z},
$$
is a [[D-TM4TE|biholomorphism]], with inverse $\varphi^{-1}\colon\DD\to\HH_R$, $\varphi^{-1}(w)=\frac{1-w}{1+w}$.
:::

::: {.remark}
The formula $\frac{1-z}{1+z}$ also maps the imaginary axis into the unit circle: for $t\in\RR$, the numbers $1-it$ and $1+it$ are complex conjugates, so $\abs{\frac{1-it}{1+it}}=1$.
:::
