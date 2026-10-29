---
schema: qual/card@1
id: E-P2PEF
kind: problem
title: Holomorphic iff $\bar\partial f = 0$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Show that f is holomorphic iff delbar f = 0" with no hypothesis on f; the partial derivatives in delbar f need not exist and their vanishing at a point does not give complex differentiability without real differentiability, so the statement assumes f is real-differentiable on an open set.'
---

::: {.exercise}
Let $f = u+iv$ be real-differentiable on an open set $\Omega\subseteq\CC$.
Show that $f$ is holomorphic on $\Omega$ iff $\delbar f = 0$ on $\Omega$.
:::

::: {.solution}

Write $z=x+iy$ and $\delbar \coloneqq \frac12(\del_x + i\del_y)$.

::: pf

::: {.pf-step #delbar-cr}
$\delbar f = 0$ at a point iff $u$ and $v$ satisfy the Cauchy--Riemann equations $u_x=v_y$, $u_y=-v_x$ there.

::: pf-proof
$$
2\delbar f = (\del_x + i \del_y) (u+iv) = (u_x - v_y) + i(u_y + v_x),
$$
whose real and imaginary parts vanish exactly when the Cauchy--Riemann equations hold.
:::

:::

::: pf-step
$f$ is holomorphic on $\Omega$ iff $\delbar f = 0$ on $\Omega$.

::: pf-proof
A real-differentiable $f$ is complex differentiable at a point iff its real derivative there, the matrix $\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}$, is multiplication by a complex number, that is, iff the Cauchy--Riemann equations hold there.
By step [](#delbar-cr){.pf-ref}, this holds at every point of $\Omega$ iff $\delbar f=0$ on $\Omega$.
:::

:::

:::

:::
