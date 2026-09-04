---
schema: qual/card@1
id: P-SFDLG
kind: problem
title: Cauchy-Riemann equations in polar coordinates and the holomorphicity and discontinuity
  of $\Log z$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Complex Logarithm
  - Holomorphic Functions
relations: []
review: draft
---

:::{.problem}
\envlist

a. Show that in polar coordinates, the Cauchy-Riemann equations take the form
\[
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \text { and } \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}
.\]

b. Use (a) to show that the logarithm function, defined as 
\[
\Log z=\log r+i \theta \text { where } z=r e^{i \theta} \text { with }-\pi<\theta<\pi
.\]
is holomorphic on the region $r> 0, -\pi < \theta < \pi$.

Show also that this branch cannot be extended continuously across the negative
real axis to all of $\CC\setminus\{0\}$.

:::

::: {.solution}
For (a), write $x=r\cos\theta$ and $y=r\sin\theta$. Then
\[
u_r&=u_x\cos\theta+u_y\sin\theta
=v_y\cos\theta-v_x\sin\theta
={1\over r}v_\theta,\\
v_r&=v_x\cos\theta+v_y\sin\theta
=-u_y\cos\theta+u_x\sin\theta
=-{1\over r}u_\theta,
\]
using the Cartesian Cauchy--Riemann equations $u_x=v_y$ and $u_y=-v_x$.

For (b), take
\[
u(r,\theta)=\log r,
\qquad
v(r,\theta)=\theta.
\]
Then
\[
u_r={1\over r}={1\over r}v_\theta,
\qquad
v_r=0=-{1\over r}u_\theta,
\]
so the principal branch $\Log z=\log r+i\theta$ is holomorphic on
\[
\CC\setminus(-\infty,0]
=\{re^{i\theta}:r>0,\ -\pi<\theta<\pi\}.
\]
In particular it is continuous on that domain.

It cannot be extended continuously across the negative real axis. Indeed,
\[
z_k^+=e^{i(\pi-1/k)},
\qquad
z_k^-=e^{-i(\pi-1/k)}
\]
both tend to $-1$, while
\[
\Log z_k^+=i(\pi-1/k)\to i\pi,
\qquad
\Log z_k^-=-i(\pi-1/k)\to-i\pi.
\]
The two one-sided limits disagree, so no continuous extension to $-1$, and
hence no continuous extension of this branch to all of $\CC^\times$, exists.
:::
