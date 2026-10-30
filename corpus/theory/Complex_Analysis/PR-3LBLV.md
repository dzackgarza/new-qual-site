---
schema: qual/card@1
id: PR-3LBLV
kind: proposition
title: Centered vertical half-strip to upper half-plane by $\sin$
slogan: 'On the centered vertical half-strip, $\sin$ is a biholomorphism onto the upper half-plane.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: {.proposition}
Let $S\coloneqq\theset{z\in\CC : -\pi/2<\Re z<\pi/2,\ \Im z>0}$.
Then $\sin$ restricts to a [[D-TM4TE|biholomorphism]] $S\to\HH$, and its inverse $\arcsin\colon\HH\to S$ is a biholomorphism from the upper half-plane onto the vertical half-strip.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-31_23-01-11.png)
:::

::: {.remark}
The boundary of $S$ maps onto $\RR$: the segment $[-\pi/2,\pi/2]$ maps onto $[-1,1]$, the ray $\pi/2+it$ ($t\ge0$) maps to $\sin(\pi/2+it)=\cosh t$, tracing $[1,\infty)$, and the ray $-\pi/2+it$ maps to $-\cosh t$, tracing $(-\infty,-1]$.
The imaginary axis $it$ ($t>0$) maps to $\sin(it)=i\sinh t$, the positive imaginary axis.
:::
