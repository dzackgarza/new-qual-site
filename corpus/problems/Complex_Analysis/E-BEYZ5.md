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
Let $f=u+iv$, which is holomorphic because $u$ and $v$ satisfy the Cauchy--Riemann equations.

::: pf

::: pf-step
$u^2-v^2$ and $uv$ are harmonic.

::: pf-proof
$f^2 = u^2 - v^2 + 2i\,uv$ is holomorphic, so its real part $u^2-v^2$ and its imaginary part $2uv$ are harmonic.
:::

:::

::: pf-step
$u_x$ is harmonic.

::: pf-proof
$f' = u_x + iv_x$ is holomorphic, so its real part $u_x$ is harmonic.
:::

:::

:::

:::

::: {.solution title="Direct computation for $uv$"}

::: pf

::: pf-step
$\laplacian(uv)=0$.

::: pf-proof
By the product rule,
$$
\laplacian(uv) = \laplacian(u)\,v + \laplacian(v)\,u + 2(u_xv_x + u_yv_y).
$$
The first two terms vanish because $u$ and $v$ are harmonic, and the Cauchy--Riemann equations $v_x = -u_y$, $v_y = u_x$ give $u_xv_x + u_yv_y = -u_xu_y + u_yu_x = 0$.
:::

:::

:::

:::
