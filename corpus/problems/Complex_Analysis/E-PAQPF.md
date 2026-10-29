---
schema: qual/card@1
id: E-PAQPF
kind: problem
title: Cauchy--Riemann equations in polar coordinates
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.exercise}
Let $\Omega\subseteq\CC\sm\theset{0}$ be open and let $f=u+iv$ be [[D-E7A5W|holomorphic]] on $\Omega$, with $u,v$ real-valued. Writing $u$ and $v$ as functions of $(r,\theta)$ through $z=re^{i\theta}$, $r>0$, show that the Cauchy--Riemann equations take the form
$$
\frac{\partial u}{\partial r}=\frac{1}{r} \frac{\partial v}{\partial \theta} \quad \text { and } \quad \frac{1}{r} \frac{\partial u}{\partial \theta}=-\frac{\partial v}{\partial r}.
$$
:::

::: {.solution}

Let $u$ and $v$ be differentiable and satisfy $u_x=v_y$ and $u_y=-v_x$, and write $x=r\cos(\theta)$, $y=r\sin(\theta)$ with $r>0$.

::: pf

::: {.pf-step #chain}
For $w\in\{u,v\}$, $w_r = \cos(\theta)\,w_x + \sin(\theta)\,w_y$ and $w_\theta = -r\sin(\theta)\,w_x + r\cos(\theta)\,w_y$.

::: pf-proof
This is the chain rule with $x_r=\cos(\theta)$, $y_r=\sin(\theta)$, $x_\theta=-r\sin(\theta)$, $y_\theta=r\cos(\theta)$.
:::

:::

::: pf-step
$u_r = \frac1r v_\theta$.

::: pf-proof
By step [](#chain){.pf-ref} and the Cauchy--Riemann equations, $v_\theta = -r\sin(\theta)\,v_x + r\cos(\theta)\,v_y = r\sin(\theta)\,u_y + r\cos(\theta)\,u_x = r\,u_r$.
:::

:::

::: pf-step
$\frac1r u_\theta = -v_r$.

::: pf-proof
By step [](#chain){.pf-ref} and the Cauchy--Riemann equations, $v_r = \cos(\theta)\,v_x + \sin(\theta)\,v_y = -\cos(\theta)\,u_y + \sin(\theta)\,u_x = -\frac1r u_\theta$.
:::

:::

:::

:::
