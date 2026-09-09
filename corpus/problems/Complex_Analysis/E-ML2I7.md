---
schema: qual/card@1
id: E-ML2I7
kind: problem
title: $f(z)= u(x,y) +i v(x,y)$ be analytic in a domain
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

::: exercise
a. Let $f(z) = u(x,y) + i v(x,y)$ be analytic in a domain $D \subset \mathbb{C}$.
Let $z_0 = (x_0, y_0) \in D$ be a point in the intersection of the level curves $u(x,y) = c_1$ and $v(x,y) = c_2$.
Suppose that $f'(z_0) \ne 0$.
Prove that the lines tangent to these curves at $z_0$ are perpendicular.

b. Let $f(z) = z^2$ on $\mathbb{C}$.
- Describe the level curves of $\operatorname{Re}(f)$ and of $\operatorname{Im}(f)$.
- What are the angles of intersection between the level curves $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f) = 0$? Is your answer in agreement with part (a)?
:::

::: solution
Write
\[
f=u+iv.
\]
At a point where $f'(z_0)\ne0$, neither $\nabla u(z_0)$ nor $\nabla v(z_0)$ vanishes. By the Cauchy--Riemann equations,
\[
\nabla u=(u_x,u_y),
\qquad
\nabla v=(v_x,v_y)=(-u_y,u_x).
\]
Therefore
\[
\nabla u\cdot\nabla v
=u_x(-u_y)+u_yu_x=0.
\]
The gradients are normal to the corresponding regular level curves, so their tangent lines are perpendicular.

For $f(z)=z^2$,
\[
u(x,y)=x^2-y^2,
\qquad
v(x,y)=2xy.
\]
Thus $u=c$ gives rectangular hyperbolas $x^2-y^2=c$; when $c=0$ this is the pair of lines $y=\pm x$. Likewise $v=c$ gives $2xy=c$; when $c=0$ this is the pair of coordinate axes.

At the origin, the zero level sets therefore meet in lines separated by angles $\pi/4$. This does not contradict part (a), because
\[
f'(0)=0,
\]
so the level sets are not regular there and the hypothesis of part (a) fails. At every noncritical intersection, the two level curves meet orthogonally.
:::
