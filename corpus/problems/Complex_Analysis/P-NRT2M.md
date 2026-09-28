---
schema: qual/card@1
id: P-NRT2M
kind: problem
title: Cauchy-Riemann equations in polar coordinates
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.problem}
Let $f = u+iv$ be complex-differentiable with continuous partial derivatives at a point $z = re^{i\theta}$ with $r\neq 0$.
Show that
\[  
\dd{u}{r} = {1\over r}\dd{v}{\theta} \qquad \dd{v}{r} = -{1\over r}\dd{u}{\theta}
.\]
:::

::: {.solution}
With $x=r\cos\theta$ and $y=r\sin\theta$, the chain rule gives
\[
u_r=u_x\cos\theta+u_y\sin\theta,
\qquad
u_\theta=-r u_x\sin\theta+r u_y\cos\theta,
\]
and similarly
\[
v_r=v_x\cos\theta+v_y\sin\theta,
\qquad
v_\theta=-r v_x\sin\theta+r v_y\cos\theta.
\]
Using the Cauchy--Riemann equations $u_x=v_y$ and $u_y=-v_x$,
\[
v_\theta
=r u_y\sin\theta+r u_x\cos\theta
=r u_r,
\]
so
\[
u_r=\frac1r v_\theta.
\]
Likewise,
\[
u_\theta
=-r v_y\sin\theta-r v_x\cos\theta
=-r v_r,
\]
and therefore
\[
v_r=-\frac1r u_\theta.
\]
:::
