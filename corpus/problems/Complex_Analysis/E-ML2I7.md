---
schema: qual/card@1
id: E-ML2I7
kind: problem
title: Level curves of $\Re f$ and $\Im f$ are orthogonal where $f'\neq0$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Cauchy-Riemann
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
(a) Let $f(z) = u(x,y) + i v(x,y)$ be analytic in a domain $D \subset \CC$.
Let $z_0 = (x_0, y_0) \in D$ be a point in the intersection of the level curves $u(x,y) = c_1$ and $v(x,y) = c_2$.
Suppose that $f'(z_0) \ne 0$.
Prove that the lines tangent to these curves at $z_0$ are perpendicular.

(b) Let $f(z) = z^2$ on $\CC$.

- Describe the level curves of $\operatorname{Re}(f)$ and of $\operatorname{Im}(f)$.
- What are the angles of intersection between the level curves $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f) = 0$? Is your answer in agreement with part (a)?
:::

::: {.solution}
::: pf

::: pf-step
(a) The tangent lines at $z_0$ are perpendicular.

::: pf-proof
$f'(z_0)=u_x+iv_x\neq0$ at $z_0$, and by the Cauchy--Riemann equations $\nabla u=(u_x,u_y)$ and $\nabla v=(v_x,v_y)=(-u_y,u_x)$, so both gradients are nonzero at $z_0$ and $\nabla u\cdot\nabla v=-u_xu_y+u_yu_x=0$. By the implicit function theorem both level sets are smooth curves near $z_0$ with normals $\nabla u(z_0)$ and $\nabla v(z_0)$; orthogonal normals give orthogonal tangent lines.
:::

:::

::: {.pf-step #level-sets}
(b) For $f(z)=z^2$, $u=x^2-y^2$ and $v=2xy$. For $c\neq0$ the level curves $u=c$ and $v=c$ are rectangular hyperbolas; $u=0$ is the pair of lines $y=\pm x$ and $v=0$ is the pair of coordinate axes.

::: pf-proof
Expand $(x+iy)^2=x^2-y^2+2ixy$.
:::

:::

::: pf-step
(b) The curves $u=0$ and $v=0$ meet only at $0$, where their lines meet at angles $\frac\pi4$. This agrees with part (a), whose hypothesis fails there.

::: pf-proof
By step [](#level-sets){.pf-ref} the lines $y=\pm x$ make angle $\frac\pi4$ with each axis, and they meet the axes only at $0$. There $f'(0)=0$, so part (a) does not apply.
:::

:::

:::

:::
