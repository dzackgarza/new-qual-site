---
schema: qual/card@1
id: P-3WZH2
kind: problem
title: Implicit function theorem for $f(s,t)=ps^3-6st+t^2$ at $(1,3)$, over $\RR$
  and $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $P = (1, 3)$ and define $f(s, t) = s^3 - 6st + t^2$ (with $f(1, 3) = 1 - 18 + 9 = -8$; or more generally at a zero of $f$, e.g., $f(s,t) = 0$).

a. State the conclusion of the Implicit Function Theorem concerning $f(s, t) = 0$ when $f$ is considered a function $\mathbb{R}^2\to\mathbb{R}$.

b. State the above conclusion when $f$ is considered a function $\mathbb{C}^2\to \mathbb{C}$.

c. Use the implicit function theorem for a function $\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$ to prove (b).
:::

::: solution
**Goal:** State the real and complex Implicit Function Theorems for $f(s, t) = 0$, and prove the complex case from the real case using the Cauchy–Riemann equations.

<1>1. Part (a): Real Implicit Function Theorem:
    *Proof:*
    <2>1. Let $f: \mathbb{R}^2 \to \mathbb{R}$ be of class $C^1$, and let $(s_0, t_0) \in \mathbb{R}^2$ be a point such that $f(s_0, t_0) = 0$.
    <2>2. If $\frac{\partial f}{\partial t}(s_0, t_0) \ne 0$, then:
        - There exists an open interval $U \subset \mathbb{R}$ containing $s_0$, an open interval $V \subset \mathbb{R}$ containing $t_0$, and a unique $C^1$ function $g: U \to V$ such that $g(s_0) = t_0$ and:
            $$f(s, g(s)) = 0 \quad \text{for all } s \in U.$$
        - The derivative of $g$ is given by:
            $$g'(s) = -\frac{\frac{\partial f}{\partial s}(s, g(s))}{\frac{\partial f}{\partial t}(s, g(s))}.$$

<1>2. Part (b): Complex Implicit Function Theorem:
    *Proof:*
    <2>1. Let $f: \mathbb{C}^2 \to \mathbb{C}$ be holomorphic, and $(s_0, t_0) \in \mathbb{C}^2$ satisfy $f(s_0, t_0) = 0$.
    <2>2. If $\frac{\partial f}{\partial t}(s_0, t_0) \ne 0$, then:
        - There exists an open disk $U \subset \mathbb{C}$ containing $s_0$, an open disk $V \subset \mathbb{C}$ containing $t_0$, and a unique **holomorphic** function $g: U \to V$ such that $g(s_0) = t_0$ and:
            $$f(s, g(s)) = 0 \quad \text{for all } s \in U.$$
        - The complex derivative is given by:
            $$g'(s) = -\frac{\frac{\partial f}{\partial s}(s, g(s))}{\frac{\partial f}{\partial t}(s, g(s))}.$$

<1>3. Part (c): Proof of (b) from the Real Implicit Function Theorem on $\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$:
    *Proof:*
    <2>1. Write $s = x_1 + i y_1 \in \mathbb{C} \cong \mathbb{R}^2$ and $t = x_2 + i y_2 \in \mathbb{C} \cong \mathbb{R}^2$.
    <2>2. Write $f(s, t) = u(x_1, y_1, x_2, y_2) + i v(x_1, y_1, x_2, y_2)$. Consider $F = (u, v): \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$.
    <2>3. Since $f$ is holomorphic, it is $C^\infty$ as a real mapping and satisfies the Cauchy–Riemann equations in each variable separately:
        $$u_{x_2} = v_{y_2}, \qquad u_{y_2} = -v_{x_2}.$$
    <2>4. The Jacobian matrix of $F$ with respect to the second variable $(x_2, y_2)$ is:
        $$J_t F = \begin{pmatrix} u_{x_2} & u_{y_2} \\ v_{x_2} & v_{y_2} \end{pmatrix} = \begin{pmatrix} u_{x_2} & -v_{x_2} \\ v_{x_2} & u_{x_2} \end{pmatrix}.$$
    <2>5. The determinant of this Jacobian is:
        $$\det(J_t F) = u_{x_2}^2 + v_{x_2}^2 = \left|\frac{\partial f}{\partial t}\right|^2.$$
    <2>6. Since $\frac{\partial f}{\partial t}(s_0, t_0) \ne 0$, $\det(J_t F)(s_0, t_0) = \left|\frac{\partial f}{\partial t}(s_0, t_0)\right|^2 > 0$, so $J_t F$ is invertible.
    <2>7. By the Real Implicit Function Theorem on $\mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}^2$, there exists a unique $C^1$ function $g = (g_1, g_2): U \to V$ from a neighborhood of $(x_1^0, y_1^0)$ to $(x_2^0, y_2^0)$ such that $F(x_1, y_1, g_1, g_2) = (0, 0)$.
    <2>8. **Holomorphicity of $g$:** Differentiating $F(s, g(s)) = 0$ with respect to $x_1$ and $y_1$ gives:
        $$J_s F + J_t F \cdot J g = 0 \implies J g = -(J_t F)^{-1} J_s F.$$
    <2>9. Both $J_t F$ and $J_s F$ are of the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ representing complex multiplication by $\frac{\partial f}{\partial t}$ and $\frac{\partial f}{\partial s}$.
    <2>10. Since the set of matrices of the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ is closed under matrix inversion and matrix multiplication (it is isomorphic to $\mathbb{C}$), the Jacobian $J g$ is also of the form $\begin{pmatrix} \alpha & -\beta \\ \beta & \alpha \end{pmatrix}$.
    <2>11. This means $g = g_1 + i g_2$ satisfies the Cauchy–Riemann equations, so $g$ is holomorphic on $U$.

<1>4. Conclusion:
    The complex Implicit Function Theorem follows directly from the real Implicit Function Theorem via Cauchy–Riemann structure of the Jacobian. Q.E.D.
:::
