---
schema: qual/card@1
id: P-ZDWLN
kind: problem
title: Real differentiability of $f:\RR^2\to\RR$ via linear maps, the inverse function
  theorem, and the Cauchy–Riemann criterion for complex differentiability
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f:\mathbb{R}^2\to \mathbb{R}^2$ (or $\mathbb{R}^2 \to \mathbb{R}$).

a. Define in terms of linear transformations what it means for $f$ to be differentiable at a point $(a, b) \in \mathbb{R}^2$.

b. State a version of the inverse function theorem in this setting.

c. Identify $\mathbb{R}^2$ with $\mathbb{C}$ and give a necessary and sufficient condition for a real-differentiable function at $(a, b)$ to be complex differentiable at the point $a+ib$.
:::

::: solution
**Goal:** Define Fréchet differentiability, state the Inverse Function Theorem on $\mathbb{R}^2$, and derive the Cauchy–Riemann criterion for complex differentiability.

<1>1. Part (a): Definition of real differentiability via linear transformations:
    *Proof:*
    <2>1. Let $U \subseteq \mathbb{R}^2$ be an open neighborhood of $p = (a, b)$, and $f: U \to \mathbb{R}^2$.
    <2>2. $f$ is **differentiable at $p$** if there exists a linear transformation $L: \mathbb{R}^2 \to \mathbb{R}^2$ (the total derivative or Fréchet derivative $Df(p)$) such that:
        $$\lim_{h \to 0} \frac{\|f(p + h) - f(p) - L(h)\|}{\|h\|} = 0.$$
    <2>3. In matrix form with respect to the standard basis, $L$ is represented by the Jacobian matrix:
        $$J_f(a, b) = \begin{pmatrix} \frac{\partial f_1}{\partial x}(a,b) & \frac{\partial f_1}{\partial y}(a,b) \\ \frac{\partial f_2}{\partial x}(a,b) & \frac{\partial f_2}{\partial y}(a,b) \end{pmatrix}.$$

<1>2. Part (b): Inverse Function Theorem:
    *Proof:*
    <2>1. **Theorem (Inverse Function Theorem):** Let $U \subseteq \mathbb{R}^2$ be open, $p = (a, b) \in U$, and let $f: U \to \mathbb{R}^2$ be of class $C^1$ (continuously differentiable).
    <2>2. If the derivative $Df(p): \mathbb{R}^2 \to \mathbb{R}^2$ is invertible (i.e. $\det J_f(p) \ne 0$), then:
        - There exists an open neighborhood $V \subseteq U$ of $p$ and an open neighborhood $W \subseteq \mathbb{R}^2$ of $f(p)$ such that $f|_V: V \to W$ is a bijection.
        - The inverse function $g = (f|_V)^{-1}: W \to V$ is also of class $C^1$.
        - The derivative of the inverse is given by the matrix inverse of the derivative:
            $$Dg(f(p)) = (Df(p))^{-1}, \quad \text{i.e.} \quad J_g(f(p)) = (J_f(p))^{-1}.$$

<1>3. Part (c): Condition for complex differentiability (Cauchy–Riemann equations):
    *Proof:*
    <2>1. Identify $\mathbb{R}^2 \cong \mathbb{C}$ via $(x, y) \leftrightarrow x + iy$. Write $f(x, y) = u(x, y) + i v(x, y)$.
    <2>2. Real differentiability means $Df(a,b)$ acts as $\mathbb{R}$-linear map on $\mathbb{R}^2 \cong \mathbb{C}$.
    <2>3. Complex differentiability at $z_0 = a + ib$ means there exists a complex number $f'(z_0) = \alpha + i\beta \in \mathbb{C}$ such that $Df(a, b)$ acts by multiplication by $f'(z_0)$ over $\mathbb{C}$.
    <2>4. Multiplication by $\alpha + i\beta$ on $\mathbb{C} \cong \mathbb{R}^2$ corresponds to the $2 \times 2$ real matrix:
        $$\begin{pmatrix} \alpha & -\beta \\ \beta & \alpha \end{pmatrix}.$$
    <2>5. Setting this equal to the Jacobian matrix $J_f(a, b) = \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix}$:
        $$u_x = v_y = \alpha \quad \text{and} \quad u_y = -v_x = -\beta.$$
    <2>6. Thus, a real-differentiable function $f = u + iv$ at $(a, b)$ is complex differentiable at $a + ib$ if and only if the **Cauchy–Riemann equations** hold at $(a, b)$:
        $$\frac{\partial u}{\partial x}(a, b) = \frac{\partial v}{\partial y}(a, b) \quad \text{and} \quad \frac{\partial u}{\partial y}(a, b) = -\frac{\partial v}{\partial x}(a, b).$$

<1>4. Conclusion:
    The Fréchet derivative, Inverse Function Theorem, and Cauchy–Riemann criterion have been fully stated and derived. Q.E.D.
:::
