---
schema: qual/card@1
id: E-BGKED
kind: exercise
title: Cauchy-Riemann iff holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

:::{.exercise}
Show that $f = u+iv$ with $u, v\in C^1(\RR)$ satisfying the Cauchy-Riemann equations on $\Omega$, then $f$ is holomorphic on $\Omega$ with
\[
f'(z) = \dd{f}{x} = {1\over i} \dd{f}{y} = {1\over 2}\qty{u_x + iv_x}
.\]
Conversely, show that if $f$ is holomorphic, then $f$ satisfies the Cauchy-Riemann equations.
:::

:::{.solution}
Holomorphic $\implies$ CR:

Suppose $f'(z_0)$ exists for all $z_0\in \CC$, so the following limit exists:
\[
f'(z_0) \da \lim_{h\to 0, h\in \CC} {f(z_0 + h) - f(z_0) \over h}
.\]
Approach along $\ts{t + 0i \st t\in \RR}$:
\[
f'(z_0) = f'(x_0, y_0) = \lim_{t\to 0, t\in \RR} {f(x_0 + t, y_0) - f(x_0, y_0) \over t} \da f_x(x_0, y_0)
.\]
Approach along $\ts{0 + ti \st t\in \RR}$:
\[
f'(z_0) = f'(x_0, y_0) = \lim_{t\to 0, t\in \RR} {f(x_0, y_0 + t) - f(x_0, y_0) \over it} \da {1\over i} f_y(x_0, y_0)
.\]
Thus
\[
if_x = f_y \implies i(u_x + i v_x) = u_y + i v_y \\ 
\implies -v_x + iu_x = u_y + iv_y \\ 
\implies u_x = v_y,\, u_y = -v_x
.\]


CR $\implies$ holomorphic:
A straightforward but messy calculation, not likely to be useful for quals!

:::

