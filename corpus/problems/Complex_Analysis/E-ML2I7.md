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
**Goal:** Prove orthogonality of level curves of conjugate harmonic functions when $f'(z_0) \ne 0$, and analyze $f(z) = z^2$.

<1>1. Part (a): Perpendicularity of tangent lines:
    *Proof:*
    <2>1. The normal vector to the level curve $u(x, y) = c_1$ at $(x_0, y_0)$ is the gradient:
        $$\nabla u(x_0, y_0) = (u_x, u_y).$$
    <2>2. The normal vector to the level curve $v(x, y) = c_2$ at $(x_0, y_0)$ is the gradient:
        $$\nabla v(x_0, y_0) = (v_x, v_y).$$
    <2>3. Because $f'(z_0) = u_x + i v_x \ne 0$, we have $(u_x, u_y) \ne (0, 0)$ and $(v_x, v_y) \ne (0, 0)$, so both gradients are non-zero normal vectors.
    <2>4. Compute the standard dot product in $\mathbb{R}^2$:
        $$\nabla u \cdot \nabla v = u_x v_x + u_y v_y.$$
    <2>5. By the Cauchy–Riemann equations ($u_x = v_y$ and $u_y = -v_x$):
        $$\nabla u \cdot \nabla v = (v_y) v_x + (-v_x) v_y = v_y v_x - v_x v_y = 0.$$
    <2>6. Since the gradient normal vectors are non-zero and orthogonal ($\nabla u \cdot \nabla v = 0$), the tangent lines to the level curves $u = c_1$ and $v = c_2$ at $z_0$ are perpendicular.

<1>2. Part (b): Level curves of $f(z) = z^2$:
    *Proof:*
    <2>1. Write $z = x + iy$. Then $f(z) = (x + iy)^2 = (x^2 - y^2) + i(2xy)$.
    <2>2. **Level curves of $\operatorname{Re}(f) = x^2 - y^2 = c_1$:**
        - For $c_1 > 0$: rectangular hyperbolas opening horizontally along the $x$-axis.
        - For $c_1 < 0$: rectangular hyperbolas opening vertically along the $y$-axis.
        - For $c_1 = 0$: the pair of orthogonal lines $y = x$ and $y = -x$.
    <2>3. **Level curves of $\operatorname{Im}(f) = 2xy = c_2$:**
        - For $c_2 \ne 0$: rectangular hyperbolas with the coordinate axes as asymptotes (in quadrants 1 & 3 for $c_2 > 0$, quadrants 2 & 4 for $c_2 < 0$).
        - For $c_2 = 0$: the pair of coordinate axes $x = 0$ (the $y$-axis) and $y = 0$ (the $x$-axis).
    <2>4. **Intersection of $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f) = 0$:**
        - The curves intersect at the origin $z_0 = 0$.
        - $\operatorname{Re}(f) = 0$ consists of the lines $y = \pm x$ (angles $\pi/4$ and $3\pi/4$).
        - $\operatorname{Im}(f) = 0$ consists of the lines $x = 0$ and $y = 0$ (angles $0$ and $\pi/2$).
        - The angle between the line $y = 0$ and the line $y = x$ is $\pi/4$ ($45^\circ$).
    <2>5. **Agreement with part (a):**
        - At $z_0 = 0$, $f'(0) = 2(0) = 0$.
        - The hypothesis of part (a) requires $f'(z_0) \ne 0$.
        - Since $f'(0) = 0$, part (a) does not apply at the origin. The angle doubling map $z \mapsto z^2$ doubles angles between curves at the origin (from $45^\circ$ in the $z$-plane to $90^\circ$ in the $w$-plane), which is why the angle is $\pi/4$ instead of $\pi/2$.
        - At every point $z_0 \ne 0$ where $f'(z_0) \ne 0$, the level curves intersect at right angles ($\pi/2$), in complete agreement with part (a).

<1>3. Conclusion:
    Gradients are orthogonal by Cauchy–Riemann equations whenever $f'(z_0) \ne 0$. For $f(z) = z^2$, level curves are orthogonal hyperbolas everywhere except at the critical point $z = 0$ where angles are halved. Q.E.D.
:::
