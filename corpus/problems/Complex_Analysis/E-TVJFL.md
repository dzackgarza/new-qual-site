---
schema: qual/card@1
id: E-TVJFL
kind: problem
title: Zero derivative implies constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy-Riemann
  - Connectedness
relations: []
review: draft
---

::: {.exercise}
Show that if $f' = 0$ on a domain $\Omega$, then $f$ is constant on $\Omega$.
:::

::: {.solution}
Write $f = u + iv$ on the connected open set $\Omega$.

::: pf

::: {.pf-step #gradients}
$\nabla u = \nabla v = 0$ on $\Omega$.

::: pf-proof
For holomorphic $f$, $f' = u_x + iv_x = v_y - iu_y$. So $f'=0$ gives $u_x = v_x = 0$ and $u_y = v_y = 0$.
:::

:::

::: {.pf-step #segments}
$f$ is constant on every line segment contained in $\Omega$.

::: pf-proof
On a segment from $p$ to $q$, the derivative of $t\mapsto u(p+t(q-p))$ is $\nabla u\cdot(q-p) = 0$ by step [](#gradients){.pf-ref}, so $u(p) = u(q)$; likewise $v(p) = v(q)$.
:::

:::

::: pf-step
$f$ is constant on $\Omega$.

::: pf-proof
A connected open subset of the plane is connected by polygonal paths. Fix $z_0\in\Omega$; for $z\in\Omega$, applying step [](#segments){.pf-ref} to each segment of a polygonal path from $z_0$ to $z$ gives $f(z) = f(z_0)$.
:::

:::

:::

:::
