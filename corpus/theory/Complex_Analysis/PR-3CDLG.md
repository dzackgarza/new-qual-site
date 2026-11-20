---
schema: qual/card@1
id: PR-3CDLG
kind: proposition
title: Upper half-plane to horizontal strip
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
Let $S\coloneqq\theset{w\in\CC : 0<\Im w<\pi}=\RR\times i(0,\pi)$.
The [[D-4CSPM|principal branch]] $\Log$ of the logarithm restricts to a [[D-TM4TE|biholomorphism]]
$$
\begin{aligned}
F\colon \HH &\to S, \\
z &\mapsto \Log(z),
\end{aligned}
$$
with inverse $w\mapsto e^w$.

This is the same exponential correspondence of [@Ahl73, ch. 3, §4.1, The Use of Level Curves], which states that $\zeta=e^z$ maps the strip $-\pi/2<\Im z<\pi/2$ onto the half plane $\Re\zeta>0$; applying the rotation $z\mapsto e^{i\pi/2}z$ to the domain and the image brings that statement to $\Log\colon\HH\to\theset{0<\Im w<\pi}$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_18-09-31.png)
:::
