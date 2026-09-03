---
schema: qual/card@1
id: E-BGKED
kind: problem
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
**Goal:** Show that holomorphic implies Cauchy-Riemann, and conversely that Cauchy-Riemann (with $C^1$ hypothesis) implies holomorphic.

**Direction 1: Holomorphic $\implies$ CR.**

Suppose $f'(z_0)$ exists for some $z_0 = x_0 + iy_0 \in \Omega$. Since the limit
$$f'(z_0) = \lim_{h\to 0,\, h\in \CC} \frac{f(z_0 + h) - f(z_0)}{h}$$
exists, we may approach along the real and imaginary axes.

Along $h = t \in \RR$:
$$f'(z_0) = \lim_{t\to 0} \frac{f(x_0 + t, y_0) - f(x_0, y_0)}{t} = f_x(x_0, y_0).$$
Along $h = it$, $t \in \RR$:
$$f'(z_0) = \lim_{t\to 0} \frac{f(x_0, y_0 + t) - f(x_0, y_0)}{it} = \frac{1}{i} f_y(x_0, y_0).$$
Equating the two expressions for $f'(z_0)$ and writing $f = u + iv$:
$$f_x = \frac{1}{i} f_y \implies i(u_x + iv_x) = u_y + iv_y \implies -v_x + iu_x = u_y + iv_y.$$
Comparing real and imaginary parts: $u_x = v_y$ and $u_y = -v_x$.

**Direction 2: CR $\implies$ holomorphic.**

Suppose $u, v \in C^1(\Omega)$ satisfy $u_x = v_y$ and $u_y = -v_x$ on $\Omega$. Write $h = \Delta x + i\Delta y$. By the multivariable Taylor theorem (since $u, v$ are $C^1$):
$$u(x_0 + \Delta x, y_0 + \Delta y) - u(x_0, y_0) = u_x \Delta x + u_y \Delta y + o(|h|),$$
$$v(x_0 + \Delta x, y_0 + \Delta y) - v(x_0, y_0) = v_x \Delta x + v_y \Delta y + o(|h|),$$
where the partial derivatives are evaluated at $(x_0, y_0)$. Using the CR equations $u_y = -v_x$ and $v_y = u_x$:
$$f(z_0 + h) - f(z_0) = (u_x \Delta x - v_x \Delta y) + i(v_x \Delta x + u_x \Delta y) + o(|h|).$$
The first two terms factor as $(u_x + iv_x)(\Delta x + i\Delta y) = (u_x + iv_x) h$, so:
$$\frac{f(z_0 + h) - f(z_0)}{h} = (u_x + iv_x) + \frac{o(|h|)}{h}.$$
Since $|o(|h|)/h| \to 0$ as $h \to 0$, the limit exists and $f'(z_0) = u_x + iv_x = u_x - iu_y$.

:::

