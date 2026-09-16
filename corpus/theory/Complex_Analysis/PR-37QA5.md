---
schema: qual/card@1
id: PR-37QA5
kind: proposition
title: Complex differentiable implies Cauchy--Riemann
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be open, let $f=u+iv\colon\Omega\to\CC$ with $u,v$ real-valued, and regard $f$, $u$, $v$ as functions of $(x,y)$ where $z=x+iy$.
If $f$ is [[D-E7A5W|complex differentiable]] at $z_0=x_0+iy_0\in\Omega$, then the partial derivatives of $u$ and $v$ exist at $(x_0,y_0)$,
$$
f'(z_0)=\dd{f}{x}(x_0,y_0)={1\over i}\dd{f}{y}(x_0,y_0),
$$
and at $(x_0,y_0)$
$$
\dd{u}{x} = \dd{v}{y}, \qquad \dd{u}{y} = -\dd{v}{x}.
$$
:::

::: {.proof}
The limit $f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}$ exists, so it may be computed along any direction.
Along real $h=h_1\in\RR$,
$$
f'(z_0) =
\lim_{h_1\to 0} { f(x_0+h_1, y_0) - f(x_0, y_0) \over h_1}
= \dd{f}{x}(x_0, y_0).
$$
Along purely imaginary $h=ih_2$ with $h_2\in\RR$,
$$
f'(z_0)
= \lim_{h_2\to 0} { f(x_0, y_0+h_2) - f(x_0, y_0) \over ih_2 } = {1\over i} \dd{f}{y}(x_0, y_0).
$$
Taking real and imaginary parts of these limits shows that the partial derivatives of $u$ and $v$ exist.
Writing $1/i=-i$,
$$
\begin{aligned}
\dd{f}{x} &= \dd{u}{x} + i \dd{v}{x}, \\
{1\over i} \dd{f}{y} &= -i \qty{ \dd{u}{y} + i \dd{v}{y}} = \dd{v}{y} - i\dd{u}{y}.
\end{aligned}
$$
Equating real and imaginary parts of the two expressions for $f'(z_0)$ gives $\dd{u}{x} = \dd{v}{y}$ and $\dd{v}{x} = -\dd{u}{y}$.
:::
