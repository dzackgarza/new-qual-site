---
schema: qual/card@1
id: E-3QAC4
kind: problem
title: If $f$ and $\bar f$ are holomorphic on a domain, then $f$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ and $\bar{f}$ are both holomorphic on a domain $\Omega$, then $f$ is constant on $\Omega$.

:::

::: {.hint}
Show that $f'=0$ on $\Omega$, and conclude by connectedness.
:::

::: {.solution}
Write $f = u + iv$, so that $\bar f = u - iv$.

::: pf

::: {.pf-step #partials}
$u_x=u_y=v_x=v_y=0$ on $\Omega$.

::: pf-proof
The Cauchy--Riemann equations for $f$ give $u_x = v_y$ and $u_y = -v_x$.
The Cauchy--Riemann equations for $\bar f=u+i(-v)$ give $u_x = -v_y$ and $u_y = v_x$.
Adding and subtracting the two pairs gives $u_x=v_y=0$ and $u_y=v_x=0$.
:::

:::

::: pf-step
$f$ is constant on $\Omega$.

::: pf-proof
Since $f$ is holomorphic, $f' = u_x + iv_x$, which vanishes by step [](#partials){.pf-ref}.
A holomorphic function with zero derivative on the connected open set $\Omega$ is constant.
:::

:::

:::

:::
