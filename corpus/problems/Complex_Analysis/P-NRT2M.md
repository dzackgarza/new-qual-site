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
$$
\dd{u}{r} = {1\over r}\dd{v}{\theta} \qquad \dd{v}{r} = -{1\over r}\dd{u}{\theta}.
$$
:::

::: {.solution}
Write $x=r\cos\theta$ and $y=r\sin\theta$. Since $f$ is complex differentiable, $u$ and $v$ are real differentiable and satisfy the Cauchy--Riemann equations $u_x=v_y$, $u_y=-v_x$.

::: pf

::: {.pf-step #chain-rule}
$u_r=u_x\cos\theta+u_y\sin\theta$, $u_\theta=-ru_x\sin\theta+ru_y\cos\theta$, and the same formulas hold with $v$ in place of $u$.

::: pf-proof
This is the chain rule, with $x_r=\cos\theta$, $y_r=\sin\theta$, $x_\theta=-r\sin\theta$, $y_\theta=r\cos\theta$.
:::

:::

::: pf-step
$u_r=\frac1r v_\theta$.

::: pf-proof
By step [](#chain-rule){.pf-ref} and the Cauchy--Riemann equations, $v_\theta=-rv_x\sin\theta+rv_y\cos\theta=ru_y\sin\theta+ru_x\cos\theta=ru_r$, and $r\neq0$.
:::

:::

::: pf-step
$v_r=-\frac1r u_\theta$.

::: pf-proof
By step [](#chain-rule){.pf-ref} and the Cauchy--Riemann equations, $u_\theta=-ru_x\sin\theta+ru_y\cos\theta=-rv_y\sin\theta-rv_x\cos\theta=-rv_r$, and $r\neq0$.
:::

:::

:::
:::
