---
schema: qual/card@1
id: E-THK2Z
kind: exercise
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
---

::: {.exercise}
Show that a real-valued holomorphic function must be constant.
:::

::: {.solution}
**Goal:** Show that a real-valued holomorphic function on a domain must be constant.

<1>1. Write $f = u + iv$ with $v \equiv 0$; the Cauchy–Riemann equations give $u_x = v_y = 0$ and $u_y = -v_x = 0$.
::: {.proof}
If $f$ is holomorphic, the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$ hold.
:::
Since $f$ is real-valued, $v \equiv 0$, so $v_x = v_y = 0$; hence $u_x = u_y = 0$ on the domain.

<1>2. $u$ is constant on the domain.
::: {.proof}
<1>1 shows both partial derivatives of $u$ vanish.
:::
On a connected (path-connected) domain, fix $z_0$; any other point joins to $z_0$ by a path, and along the path $u$ is constant (vanishing directional derivative), so $u(z) = u(z_0)$ everywhere.

<1>3. Q.E.D.
::: {.proof}
$f = u$ (as $v \equiv 0$) is constant by <1>2.
:::
:::
