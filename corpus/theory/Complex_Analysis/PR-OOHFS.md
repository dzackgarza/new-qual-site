---
schema: qual/card@1
id: PR-OOHFS
kind: proposition
title: Cayley transform from the upper half-plane onto the unit disc
slogan: 'The Cayley transform sends the upper half-plane to the unit disc and the first quadrant to the lower half-disc.'
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
Let $\HH\coloneqq\theset{z\in\CC\st\Im z>0}$ and $\DD\coloneqq\theset{w\in\CC\st\abs{w}<1}$.
The Cayley transform
$$
\Psi\colon\HH\to\DD,\qquad \Psi(z)=\frac{z-i}{z+i},
$$
is a [[D-TM4TE|biholomorphism]], with inverse $\Psi^{-1}(w)=i\,\frac{1+w}{1-w}$.
It restricts to a biholomorphism from the first quadrant $Q_1\coloneqq\theset{z\st\Re z>0,\ \Im z>0}$ onto the lower half-disc $\theset{w\in\DD\st\Im w<0}$.
:::

::: {.remark}
The real axis is mapped onto the unit circle minus $1$, and horizontal lines $\Im z=c>0$ are mapped onto circles in $\DD$ tangent to the unit circle at $1$:

![The Cayley map w = (z-i)/(z+i) sends the upper half-plane onto the unit disc: the real axis goes to the unit circle, and horizontal lines above it go to circles inside the disc tangent to the circle at 1.](../../assets/figures/2021-07-29_19-02-54.png)
:::
