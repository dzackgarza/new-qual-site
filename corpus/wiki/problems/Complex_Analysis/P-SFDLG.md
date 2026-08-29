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

Also show that this function is not continuous in $r>0$.

:::

:::{.solution}
**Part 1:**

Write 
\[
x &= r\cos \theta \implies \grad_{r, \theta} x = \tv{\cos \theta, -r\sin \theta} \\
y & =r\sin \theta \implies \grad_{r, \theta} y = \tv{\sin \theta, r\cos \theta}
.\]
Then
\[
u_r 
&= u_x x_r + u_y y_r \\
&= u_x \cos \theta + u_y \sin \theta \\
&= v_y \cos \theta - v_x \sin \theta \\
&= r\inv \qty{v_y \cdot r\cos\theta - u_y \cdot r \sin \theta} \\
&= r\inv \qty{v_y y_\theta + u_y x_\theta} \\
&= r\inv v_\theta
.\]
Similarly
\[
v_r
&= v_x x_r + v_y y_r \\
&= v_x \cos \theta + v_y \sin \theta \\
&= -u_y \cos \theta + u_x \sin \theta \\
&= -r\inv\qty{u_y \cdot r\cos\theta i u_x \cdot r\sin \theta } \\
&= -r\inv \qty{u_x x_\theta + u_y y_\theta} \\
&= -r\inv u_\theta
.\]

**Part 2:**

Define $u(r, \theta) = \log(r)$ and $v(r, \theta) = \theta$ to write $\Log(z) = u+iv$.
Then check
\[
u_r &= r\inv, \quad v_\theta = 1 \implies u_r = r\inv v_\theta \\
v_r &= 0, \quad u_\theta = 0 \implies v_r = -r\inv u_\theta
,\]
provided $r>0$ so that $u_r$ is defined.

That this function is not continuous: let $w_k = 1\cdot e^{i(2\pi - 1/k)}$, noting that these are two sequences converging to 1.
If $\Log(z)$ were continuous, we would have
\[
\lim_{k\to\infty} \Log(w_k)
= \Log(1) 
\da \log(1) + i\cdot 0
= 0
,\]
Thus for any $\eps$ we could choose $k\gg 1$ so that 
\[
\abs{\log(z_k) - 0}, \abs{\log(w_k) - 0 } < \eps
.\]
However,
\[
\log(w_k) = \log(1) + i(2\pi - 1/k) = i(2\pi - 1/k) = 2\pi i - {1\over k} > \eps
,\]
for arbitrarily large $k$, provided we choose $\eps$ small.
:::
