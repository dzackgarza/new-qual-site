---
schema: qual/card@1
id: P-TH3WN
kind: problem
title: Cauchy–Riemann equations in polar coordinates
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
that
$$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$
:::

::: {.solution}
<1>1. At the point $z=re^{i\theta}$, the Cartesian Cauchy--Riemann
equations are
$$
u_x=v_y,
\qquad
u_y=-v_x.
$$

::: {.proof}
The function is complex differentiable at $z$ and has continuous real
partial derivatives there, so the Cauchy--Riemann equations hold at that
point.
:::

<1>2. The polar derivatives satisfy
$$
\begin{aligned}
u_r&=u_x\cos\theta+u_y\sin\theta,\\
u_\theta&=-r u_x\sin\theta+r u_y\cos\theta,\\
v_r&=v_x\cos\theta+v_y\sin\theta,\\
v_\theta&=-r v_x\sin\theta+r v_y\cos\theta.
\end{aligned}
$$

::: {.proof}
Since
$$
x=r\cos\theta,
\qquad
y=r\sin\theta,
$$
the chain rule gives the four displayed formulas.
:::

<1>3. One has
$$
\boxed{u_r=\frac1r v_\theta}.
$$

::: {.proof}
By step <1>2 and then step <1>1,
$$
\frac1r v_\theta
=-v_x\sin\theta+v_y\cos\theta
=u_y\sin\theta+u_x\cos\theta
=u_r.
$$
The division by $r$ is valid because $r\ne0$.
:::

<1>4. One has
$$
\boxed{v_r=-\frac1r u_\theta}.
$$

::: {.proof}
Again using steps <1>2 and <1>1,
$$
-\frac1r u_\theta
=u_x\sin\theta-u_y\cos\theta
=v_y\sin\theta+v_x\cos\theta
=v_r.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 are exactly the two polar Cauchy--Riemann equations
required in the problem.
:::
:::
