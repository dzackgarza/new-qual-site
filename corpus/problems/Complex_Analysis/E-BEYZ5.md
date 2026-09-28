---
schema: qual/card@1
id: E-BEYZ5
kind: problem
title: $u^2-v^2$, $uv$ and $u_x$ are harmonic for harmonic conjugates $u,v$
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

::: {.exercise}
Show that if $u,v$ are harmonic conjugates, then

- $u^2-v^2$ is harmonic
- $uv$ is harmonic.
- $u_x$ is harmonic.

:::

::: {.solution}
Write $f=u+iv$, which is analytic.

- $f^2$ is analytic, and $f^2 = (u+iv)^2 = u^2 - v^2 + i (2uv)$, which necessarily has harmonic components.

- The imaginary part of $f^2$ is $2uv$, so $uv$ is harmonic.

- $f'$ is analytic and $f' = u_x + iv_x$, which has harmonic components.

Alternatively, $uv$ is in the kernel of the Laplacian:
\[
\laplacian(uv) 
&= (uv)_{xx} + (uv)_{yy} \\
&= (u_{xx}v + uv_{xx} + 2u_x v_x) + (u_{yy}v + uv_{yy} + 2u_y v_y) \\
&= (u_{xx} + u_{yy}) v + (v_{xx} + v_{yy}) u + 2(u_xv_x + u_yv_y) \\
&= (u_{xx} + u_{yy}) v + (v_{xx} + v_{yy}) u + 2(-u_x u_y + u_y u_x) && v_x = -u_y,\, v_y = u_x \\
&= (u_{xx} + u_{yy}) v + (v_{xx} + v_{yy})u  \\
&= \laplacian(u)v + \laplacian(v)u \\
&= 0
.\]
:::
