---
schema: qual/card@1
id: E-THK2Z
kind: problem
title: A real-valued holomorphic function is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source does not say the domain is connected; a real-valued holomorphic function on a disconnected open set need only be locally constant. The statement now takes a connected open set.
---

::: {.exercise}
Show that a real-valued holomorphic function on a connected open set must be constant.
:::

::: {.solution}
Let $f = u + iv$ be holomorphic and real-valued on a connected open set $\Omega$, so $v \equiv 0$.

::: pf

::: {.pf-step #cauchy-riemann-vanish}
$u_x = u_y = 0$ on $\Omega$.

::: pf-proof
The Cauchy–Riemann equations give $u_x = v_y = 0$ and $u_y = -v_x = 0$.
:::

:::

::: {.pf-step #u-constant}
$u$ is constant on $\Omega$.

::: pf-proof
By step [](#cauchy-riemann-vanish){.pf-ref} the gradient of $u$ vanishes. A connected open subset of the plane is path-connected by polygonal paths, and $u$ is constant along each segment of such a path, so $u(z) = u(z_0)$ for every $z\in\Omega$ and a fixed $z_0\in\Omega$.
:::

:::

::: pf-qed
$f = u$ is constant by step [](#u-constant){.pf-ref}.
:::

:::

:::

::: {.remark title="By the open mapping theorem"}
If $f$ were nonconstant, the [[FT-OEYLQ|open mapping theorem]] would make $f(\Omega)$ a nonempty open subset of $\CC$, but $f(\Omega)\subseteq\RR$ and $\RR$ contains no nonempty open subset of $\CC$.
:::
