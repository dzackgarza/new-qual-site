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

::: {.problem}
(a) Show that in polar coordinates, the Cauchy-Riemann equations take the form
$$
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \text { and } \frac{\partial v}{\partial r}=-\frac{1}{r} \frac{\partial u}{\partial \theta}
.$$

(b) Use (a) to show that the logarithm function, defined as 
$$
\Log z=\log r+i \theta \text { where } z=r e^{i \theta} \text { with }-\pi<\theta<\pi
.$$
is holomorphic on the region $r> 0, -\pi < \theta < \pi$.

Show also that this branch cannot be extended continuously across the negative
real axis to all of $\CC\setminus\{0\}$.
:::

::: {.solution title="(a)"}
Write $x=r\cos\theta$, $y=r\sin\theta$ with $r>0$.

::: pf

::: {.pf-step #chain}

$u_r=u_x\cos\theta+u_y\sin\theta$, $\frac1ru_\theta=-u_x\sin\theta+u_y\cos\theta$, and likewise for $v$.

::: pf-proof

This is the chain rule, using $x_r=\cos\theta$, $y_r=\sin\theta$, $x_\theta=-r\sin\theta$, $y_\theta=r\cos\theta$.

:::

:::

::: pf-step

The equations $u_x=v_y$, $u_y=-v_x$ hold if and only if $u_r=\frac1rv_\theta$ and $v_r=-\frac1ru_\theta$.

::: pf-proof

By step [](#chain){.pf-ref},
$$
\begin{aligned}
u_r-\tfrac1rv_\theta&=(u_x-v_y)\cos\theta+(u_y+v_x)\sin\theta,\\
v_r+\tfrac1ru_\theta&=-(u_x-v_y)\sin\theta+(u_y+v_x)\cos\theta.
\end{aligned}
$$
The coefficient matrix is a rotation, hence invertible, so the left sides vanish exactly when $u_x-v_y$ and $u_y+v_x$ vanish.

:::

:::

:::

:::

::: {.solution title="(b)"}
On the region $\Omega\coloneqq\theset{re^{i\theta}: r>0,\ -\pi<\theta<\pi}=\CC\setminus(-\infty,0]$, take $u(r,\theta)=\log r$ and $v(r,\theta)=\theta$.

::: pf

::: pf-step

$\Log$ is holomorphic on $\Omega$.

::: pf-proof

The functions $u,v$ are smooth on $\Omega$, so $\Log$ is real differentiable there, and
$$
u_r=\frac1r=\frac1rv_\theta,
\qquad
v_r=0=-\frac1ru_\theta.
$$
By part (a), the Cauchy--Riemann equations hold on $\Omega$, so $\Log$ is holomorphic there.

:::

:::

::: pf-step

$\Log$ has no continuous extension to $\CC\setminus\{0\}$.

::: pf-proof

The points $z_k^\pm=e^{\pm i(\pi-1/k)}$ lie in $\Omega$ and tend to $-1$, while
$$
\Log z_k^\pm=\pm i(\pi-1/k)\longrightarrow\pm i\pi.
$$
The two limits differ, so $\Log$ has no continuous extension to $-1$.

:::

:::

:::

:::
