---
schema: qual/card@1
id: E-TZJKN
kind: problem
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

::: {.exercise}
Let $\Omega\subseteq\CC$ be open and let $f = u+iv$ be [[D-E7A5W|holomorphic]] on $\Omega$, with $u,v$ real-valued. Show that $u$ and $v$ are [[D-CFBSA|harmonic]] on $\Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #smooth}
$u$ and $v$ are $C^\infty$, and $u_x = v_y$, $u_y = -v_x$.

::: pf-proof
A holomorphic function is infinitely complex differentiable, so its real and imaginary parts are $C^\infty$. The equations are the Cauchy–Riemann equations.
:::

:::

::: pf-step
$u_{xx} + u_{yy} = 0$ and $v_{xx} + v_{yy} = 0$.

::: pf-proof
Differentiating the equations of step [](#smooth){.pf-ref} gives $u_{xx} = v_{yx}$, $u_{yy} = -v_{xy}$, $v_{xx} = -u_{yx}$ and $v_{yy} = u_{xy}$. Since $u$ and $v$ are $C^2$, mixed partials commute (Clairaut), so $u_{xx}+u_{yy} = v_{yx}-v_{xy} = 0$ and $v_{xx}+v_{yy} = u_{xy}-u_{yx} = 0$.
:::

:::

:::

:::
