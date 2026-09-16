---
schema: qual/card@1
id: PR-UWGI6
kind: proposition
title: Mean value property for harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Harmonic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be open, let $u$ be [[D-CFBSA|harmonic]] on $\Omega$, and let $z_0=x_0+iy_0\in\Omega$ and $r>0$ satisfy $\overline{D_r(z_0)}\subseteq\Omega$.
Then
$$
u(z_0)=\frac{1}{2\pi r}\oint_{\bd D_r(z_0)}u\ds=\frac{1}{\pi r^2}\iint_{D_r(z_0)}u(x,y)\dx\dy,
$$
where $ds$ is arc length on the circle $\bd D_r(z_0)$.
:::
