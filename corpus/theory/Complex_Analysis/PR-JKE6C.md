---
schema: qual/card@1
id: PR-JKE6C
kind: proposition
title: Cauchy--Riemann implies holomorphic
slogan: '$C^1$ plus Cauchy--Riemann turns real differentiability into complex differentiability.'
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f = u+iv\colon\Omega\to\CC$, where $u,v\colon\Omega\to\RR$ are continuously differentiable as functions of $(x,y)$, $z=x+iy$.
If $u_x=v_y$ and $u_y=-v_x$ on $\Omega$, then $f$ is [[D-E7A5W|holomorphic]] on $\Omega$ and
$$
f'(z) = \del f(z) = u_x(z) + iv_x(z).
$$
:::
