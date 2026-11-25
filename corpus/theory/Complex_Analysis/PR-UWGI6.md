---
schema: qual/card@1
id: PR-UWGI6
kind: proposition
title: Mean value property for harmonic functions
slogan: 'A harmonic function equals both its circular average and its disc average at the center.'
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
Let $\Omega\subseteq\CC$ be open, let $u$ be [[D-CFBSA|harmonic]] on $\Omega$, and let $z_0=x_0+iy_0\in\Omega$ and $r>0$ satisfy $\overline{\DD_r(z_0)}\subseteq\Omega$.
Then
$$
u(z_0)=\frac{1}{2\pi r}\oint_{\bd \DD_r(z_0)}u\,ds=\frac{1}{\pi r^2}\iint_{\DD_r(z_0)}u(x,y)\dx\dy,
$$
where $ds$ is arc length on the circle $\bd \DD_r(z_0)$ [@SS03, ch. 3, Corollary 7.3].

The circular average is that corollary; the disc average is an addition here, obtained from the circular one by integrating over $0\leq s\leq r$ in polar coordinates.
:::
