---
schema: qual/card@1
id: PR-XCDL5
kind: proposition
title: Logarithm from the upper half-plane to a horizontal strip
slogan: 'The principal logarithm unwraps the upper half-plane into the strip $0<\Im w<\pi$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
---

::: {.proposition}
Let $\Log$ be the [[D-4CSPM|principal branch]] of the logarithm.
The map
$$
F\colon\HH=\theset{z\st\Im z>0}\to\theset{w\st0<\Im w<\pi},\qquad F(z)=\Log z,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto e^w$.
:::

::: {.remark}
The map extends continuously to the boundary of $\HH$ minus $0$, with the argument $\pi$ on the negative real axis.
As $x$ increases from $-\infty$ to $0$, $F(x)=\ln\abs x+i\pi$ moves from $+\infty+i\pi$ to $-\infty+i\pi$ along the line $\Im w=\pi$.
As $x$ increases from $0$ to $\infty$, $F(x)=\ln x$ moves from $-\infty$ to $+\infty$ along $\RR$.
:::
