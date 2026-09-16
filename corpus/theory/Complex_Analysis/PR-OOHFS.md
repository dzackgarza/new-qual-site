---
schema: qual/card@1
id: PR-OOHFS
kind: proposition
title: Cayley transform from the upper half-plane onto the unit disc
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
Let $\HH\coloneqq\ts{z\in\CC\st\Im z>0}$ and $\DD\coloneqq\ts{w\in\CC\st\abs{w}<1}$.
The Cayley transform
$$
\Psi\colon\HH\to\DD,\qquad \Psi(z)=\frac{z-i}{z+i},
$$
is a [[D-TM4TE|biholomorphism]], with inverse $\Psi^{-1}(w)=i\,\frac{1+w}{1-w}$.
It restricts to a biholomorphism from the first quadrant $Q_1\coloneqq\ts{z\st\Re z>0,\ \Im z>0}$ onto the lower half-disc $\ts{w\in\DD\st\Im w<0}$.
:::

::: {.proof}
For $z\in\HH$, $\abs{z-i}^2-\abs{z+i}^2=-4\Im z<0$: every $z\in\HH$ is closer to $i$ than to $-i$, so $\abs{\Psi(z)}<1$.
Solving $w=\frac{z-i}{z+i}$ gives $z(1-w)=i(1+w)$, so $z=i\frac{1+w}{1-w}$; for $w\in\DD$ this is defined, and
$$
\Im\Big(i\,\frac{1+w}{1-w}\Big)=\Re\frac{(1+w)(1-\bar w)}{\abs{1-w}^2}=\frac{1-\abs{w}^2}{\abs{1-w}^2}>0,
$$
so the inverse formula maps $\DD$ into $\HH$, and the two maps are mutually inverse.

For $z\in\HH$, $\Im\Psi(z)=\Im\frac{(z-i)(\bar z-i)}{\abs{z+i}^2}=\frac{-2\Re z}{\abs{z+i}^2}$, since $(z-i)(\bar z-i)=\abs{z}^2-1-2i\Re z$.
So $\Psi(z)$ lies in the lower half-disc exactly when $\Re z>0$, and $\Psi(Q_1)=\ts{w\in\DD\st\Im w<0}$.
:::

::: {.remark}
The real axis is mapped onto the unit circle minus $1$, and horizontal lines $\Im z=c>0$ are mapped onto circles in $\DD$ tangent to the unit circle at $1$:

![](../../assets/figures/2021-07-29_19-02-54.png)
:::
