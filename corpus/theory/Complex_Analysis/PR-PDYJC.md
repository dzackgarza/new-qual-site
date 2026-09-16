---
schema: qual/card@1
id: PR-PDYJC
kind: proposition
title: Power maps between sectors
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
For $0<\beta\le2\pi$ let $S_\beta\coloneqq\ts{re^{i\theta}\st r>0,\ 0<\theta<\beta}$ be the open sector of opening $\beta$, so that $S_\pi=\HH$.
Let $0<\alpha<2$, and on $S_{2\pi}=\CC\sm[0,\infty)$ define $z^\alpha\coloneqq r^\alpha e^{i\alpha\theta}$ for $z=re^{i\theta}$, $0<\theta<2\pi$.
Then
$$
F_\alpha\colon\HH\to S_{\alpha\pi},\qquad F_\alpha(z)=z^\alpha,
$$
is a [[D-TM4TE|biholomorphism]], with inverse $w\mapsto w^{1/\alpha}$ defined by the same choice of argument in $(0,2\pi)$.
Equivalently, for $0<\beta<2\pi$ the map $z\mapsto z^{\pi/\beta}$ is a biholomorphism $S_\beta\to\HH$.
:::

::: {.proof}
With the argument taken in $(0,2\pi)$, $z\mapsto z^\alpha=e^{\alpha(\ln r+i\theta)}$ is holomorphic on $S_{2\pi}$.
It maps $re^{i\theta}$ with $0<\theta<\pi$ to $r^\alpha e^{i\alpha\theta}$ with $0<\alpha\theta<\alpha\pi<2\pi$; since $r\mapsto r^\alpha$ is a bijection of $(0,\infty)$ and $\theta\mapsto\alpha\theta$ is a bijection $(0,\pi)\to(0,\alpha\pi)$, the map is a bijection $\HH\to S_{\alpha\pi}$ with inverse $\rho e^{i\varphi}\mapsto\rho^{1/\alpha}e^{i\varphi/\alpha}$, which is also holomorphic.
The second statement is the first with $\alpha=\beta/\pi$, inverted.
:::

::: {.remark}
The formula $z^\alpha$ extends continuously to the boundary of $\HH$.
As $x$ increases from $0$ to $\infty$ along the positive real axis, $x^\alpha$ increases from $0$ to $\infty$ along the positive real axis.
As $x$ increases from $-\infty$ to $0$ along the negative real axis, $x^\alpha=\abs{x}^\alpha e^{i\alpha\pi}$ moves from $\infty$ to $0$ along the ray $\ts{te^{i\alpha\pi}\st t>0}$.
:::
