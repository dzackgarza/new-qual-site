---
schema: qual/card@1
id: P-H6WQ2
kind: problem
title: $\int_{\partial T}f(z)\,dz=0$ for a $C^1$ function on a triangle, by Green's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Theorem
  - Cauchy-Riemann
relations: []
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source required only the interior of T to lie in Omega; then the boundary integral need not be defined. The statement now requires the closed triangle T to lie in Omega.
---

::: {.problem}
Suppose $f$ is continuously complex differentiable on $\Omega$, and $T$ is
a closed triangle, together with its interior, contained in $\Omega$. Use Green's theorem to
prove $\int_{\partial T}f(z)\,dz=0$.
:::

::: {.solution}
Write $f=u+iv$ with $u,v$ real. Since $f$ is continuously complex differentiable, $u$ and $v$ are $C^1$ on $\Omega$ and satisfy the Cauchy–Riemann equations $u_x=v_y$, $u_y=-v_x$.

::: pf

::: {.pf-step #split}
$\displaystyle\int_{\partial T}f(z)\,dz=\int_{\partial T}(u\,dx-v\,dy)+i\int_{\partial T}(v\,dx+u\,dy)$.

::: pf-proof
Expand $(u+iv)(dx+i\,dy)$ into real and imaginary parts.
:::

:::

::: pf-step
$\int_{\partial T}f(z)\,dz=0$.

::: pf-proof
Green's theorem applies because $u,v$ are $C^1$ on a neighborhood of the closed triangle. It turns the two integrals of step [](#split){.pf-ref} into
$$
\iint_T(-v_x-u_y)\,dx\,dy
\qquad\text{and}\qquad
\iint_T(u_x-v_y)\,dx\,dy,
$$
and both integrands vanish by the Cauchy–Riemann equations.
:::

:::

:::

:::
