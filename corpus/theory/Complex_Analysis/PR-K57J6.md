---
schema: qual/card@1
id: PR-K57J6
kind: proposition
title: Holomorphic functions have harmonic components
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f(z) = u(x, y) + iv(x, y)$ be [[D-E7A5W|holomorphic]] on $\Omega$, with $u,v$ real-valued and $z=x+iy$.
Then $u$ and $v$ are [[D-CFBSA|harmonic]] on $\Omega$.
:::

::: {.proof}
The derivative of a holomorphic function is holomorphic, so $f$ is infinitely differentiable and $u,v$ have continuous partial derivatives of all orders.
By the Cauchy--Riemann equations $u_x=v_y$ and $u_y=-v_x$, so $u_{xx}=v_{yx}=v_{xy}=-u_{yy}$ and $v_{xx}=-u_{yx}=-u_{xy}=-v_{yy}$, using equality of mixed partials.
Hence $\Delta u=\Delta v=0$.
:::
