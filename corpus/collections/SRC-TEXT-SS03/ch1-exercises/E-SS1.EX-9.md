---
schema: qual/card@1
id: E-SS1.EX-9
kind: problem
title: "SS 1.9: The Cauchy-Riemann equations in polar coordinates"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
9. Show that in polar coordinates, the Cauchy-Riemann equations take the form

$$
{\frac {\partial u}{\partial r}} = {\frac {1}{r}} {\frac {\partial v}{\partial \theta}} \quad {\mathrm{and}} \quad {\frac {1}{r}} {\frac {\partial u}{\partial \theta}} = - {\frac {\partial v}{\partial r}}.
$$

Use these equations to show that the logarithm function defined by

$$
\log z = \log r + i \theta \quad \mathrm{where} z = r e ^ {i \theta} \mathrm{with} - \pi <   \theta <   \pi
$$

is holomorphic in the region $r > 0$ and $- \pi < \theta < \pi$
:::

::: {.solution}
Let $z=x+iy=re^{i\theta}$, so
\[
x=r\cos\theta,
\qquad
y=r\sin\theta.
\]
For $f=u+iv$, the ordinary chain rule gives
\[
u_r=u_x\cos\theta+u_y\sin\theta,
\qquad
u_\theta=-r u_x\sin\theta+r u_y\cos\theta,
\]
and similarly for $v$. If the Cartesian Cauchy--Riemann equations $u_x=v_y$ and $u_y=-v_x$ hold, then
\[
\frac1r v_\theta
=-v_x\sin\theta+v_y\cos\theta
=u_y\sin\theta+u_x\cos\theta
=u_r,
\]
and
\[
v_r=v_x\cos\theta+v_y\sin\theta
=-u_y\cos\theta+u_x\sin\theta
=-\frac1r u_\theta.
\]
Thus
\[
u_r=\frac1r v_\theta,
\qquad
\frac1r u_\theta=-v_r.
\]
Conversely, reversing the calculation gives the Cartesian Cauchy--Riemann equations, so these are the polar form for $r>0$.

For the principal logarithm,
\[
u(r,\theta)=\log r,
\qquad
v(r,\theta)=\theta.
\]
Hence
\[
u_r=\frac1r,
\quad u_\theta=0,
\quad v_r=0,
\quad v_\theta=1,
\]
so the polar Cauchy--Riemann equations hold throughout
\[
r>0,\qquad -\pi<\theta<\pi.
\]
Therefore the principal branch $\log z=\log r+i\theta$ is holomorphic on that region.
:::
