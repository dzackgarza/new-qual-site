---
schema: qual/card@1
id: D-CREQS
kind: definition
title: Cauchy--Riemann equations
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $f=u+iv$ be a complex-valued function on an open set $\Omega$ and let $z_0=x_0+iy_0\in\Omega$.
Then $f$ \dfn{satisfies the Cauchy--Riemann equations} at $z_0$ if the partial derivatives of $u$ and $v$ exist there and
$$
u_x(z_0)=v_y(z_0),\qquad u_y(z_0)=-v_x(z_0).
$$
For a real differentiable $f$ this is the single equation $\delbar f(z_0)=0$ in the [[D-OAFF5|Wirtinger operators]] ([[PR-TVPCM]]).

This is [@Ahl73, ch. 2, §1.2, Analytic Functions], where the two equations are obtained as the real form of the existence of the complex derivative.
:::
