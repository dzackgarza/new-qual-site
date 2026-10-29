---
schema: qual/card@1
id: E-BGKED
kind: problem
title: A $C^1$ function satisfies the Cauchy--Riemann equations if and only if it is
  holomorphic
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
  note: 'The source reads "Show that f = u+iv with u, v in C^1(R) satisfying the Cauchy-Riemann equations on Omega, then f is holomorphic on Omega with f''(z) = df/dx = (1/i) df/dy = (1/2)(u_x + i v_x)". The statement takes u, v in C^1(Omega), supplies "if", and drops the factor 1/2, which belongs to the Wirtinger derivative and makes the last equality false.'
---

::: {.exercise}
Let $\Omega\subseteq\CC$ be open. Show that if $f = u+iv$ with $u, v\in C^1(\Omega)$ satisfying the Cauchy-Riemann equations on $\Omega$, then $f$ is holomorphic on $\Omega$ with
$$
f'(z) = \dd{f}{x} = \frac{1}{i} \dd{f}{y} = u_x + iv_x.
$$
Conversely, show that if $f$ is holomorphic, then $f$ satisfies the Cauchy-Riemann equations.
:::

::: {.solution}
Fix $z_0 = x_0 + iy_0 \in \Omega$, write $h=\Delta x+i\Delta y$, and evaluate all partial derivatives at $(x_0,y_0)$.

::: pf

::: {.pf-step #axes}
If $f'(z_0)$ exists, then $f'(z_0)=f_x=\frac1i f_y$.

::: pf-proof
The limit $f'(z_0) = \lim_{h\to 0} \frac{f(z_0 + h) - f(z_0)}{h}$ may be taken along $h = t\in\RR$, giving $f_x(x_0,y_0)$, and along $h = it$ with $t\in\RR$, giving $\frac1i f_y(x_0,y_0)$.
:::

:::

::: pf-step
If $f$ is holomorphic, then $u_x = v_y$ and $u_y = -v_x$.

::: pf-proof
By step [](#axes){.pf-ref}, $i(u_x + iv_x) = u_y + iv_y$, that is, $-v_x + iu_x = u_y + iv_y$.
Compare real and imaginary parts.
:::

:::

::: pf-step
If $u,v\in C^1(\Omega)$ satisfy the Cauchy--Riemann equations, then $f$ is holomorphic with $f'=\dd fx=\frac1i\dd fy=u_x+iv_x$.

::: pf-proof
Since $u$ and $v$ are $C^1$, they are differentiable at $(x_0,y_0)$:
$$
\begin{aligned}
u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0) &= u_x \Delta x + u_y \Delta y + o(\abs h),\\
v(x_0 + \Delta x, y_0 + \Delta y) - v(x_0, y_0) &= v_x \Delta x + v_y \Delta y + o(\abs h).
\end{aligned}
$$
Substituting $u_y = -v_x$ and $v_y = u_x$,
$$
f(z_0 + h) - f(z_0) = (u_x \Delta x - v_x \Delta y) + i(v_x \Delta x + u_x \Delta y) + o(\abs h) = (u_x + iv_x)h + o(\abs h).
$$
Dividing by $h$ and letting $h\to0$ gives $f'(z_0) = u_x + iv_x=\dd fx$, and step [](#axes){.pf-ref} gives $\dd fx=\frac1i\dd fy$.
:::

:::

:::

:::
