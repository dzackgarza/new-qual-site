---
schema: qual/card@1
id: PR-37QA5
kind: proposition
title: Complex differentiable implies Cauchy--Riemann
slogan: 'A complex derivative has the same directional limit along the real and imaginary axes, forcing the Cauchy--Riemann equations.'
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

The equations are [@SS03, ch. 1, Proposition 2.3], which states that a function holomorphic at $z_0$ has $\partial f/\partial\overline z(z_0)=0$ with $f'(z_0)=\partial f/\partial z(z_0)$, the Cauchy--Riemann equations being the real and imaginary parts of $\partial f/\partial\overline z=0$ displayed in that section; with the two operators there, $\partial f/\partial z=\frac12\qty{f_x+\frac1i f_y}$ and $\partial f/\partial\overline z=0$ give $f'(z_0)=f_x(z_0)=\frac1i f_y(z_0)$.
:::
