---
schema: qual/card@1
id: P-2QLBW
kind: problem
title: Gradient is orthogonal to level curves
classification:
  areas:
  - prelim
  topics:
  - multivariable-calculus
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
1. Definitions:
  - $f: \RR^2 \to \RR, \quad (x,y) \mapsto z = f(x,y)$
  - Level curves are given by $f(x, y) = c$; 
  - $\nabla f: \RR^2 \to \RR^2, \quad \nabla f(\vector p) = \thevector{f_x(\vector p), f_y(\vector p)}$
  - $\gamma(t): \RR \to \RR^2, \quad \gamma(t) = \thevector{x(t), y(t)}, \quad \gamma_t(t) = \thevector{x_t(t), y_t(t)}$
  - $g(t) = f \circ \gamma:\RR \to \RR, \quad (f \circ \gamma)(t) = f(x(t), y(t)), \quad g_t(t) = f_t(\gamma(t))\cdot \gamma_t(t)$
  - A vector $v$ is perpendicular to a surface at a point $p$ iff $v$ is perpendicular to the tangent vector of every curve passing through $p$.

  - Proof of actual statement
    - Let $\vector p = \thevector{x_0, y_0}$ be a point on the level surface, so $f(\vector p) = c$ for some constant.

    - Let $\gamma(t) = \thevector{x(t), y(t)}$ be a curve on the level surface, so $\gamma(t_0) = \vector p$ for some $t_0$. Let $\gamma'(t)$ be its tangent vector.

    - Let $g(t) = f(x(t), y(t)) = (f \circ \gamma)(t)$, and note that for some $\vector x$ on the level surface, and so we have $g(t_0) = f(\vector x) = c$ and thus $\dd{g}{t}(t) = 0$.

    - By the chain rule, compute 
    $$\begin{align*}
    \dd{g}{t}(t)
    &= \left(\dd{f}{x}\dd{x}{t} + \dd{f}{y}\dd{y}{t}\right)(t) \\
    &= \inner{ \thevector{\dd{f}{x}(x(t), y(t)), \dd{f}{y}(x(t), y(t))} } { \thevector{\dd{x}{t}(t), \dd{y}{t}(t)} } \\ 
    &= \inner{\nabla f(\gamma(t))}{\dd{\gamma}{t} (t)}.
    \end{align*}$$ 

    From above, we know that this is zero. Now note that we have 
    $$ 
    \dd{g}{t}(t_0) =  \inner{\nabla f(\gamma(t_0))}{\dd{\gamma}{t}(t_0)} = \inner{\nabla f(\vector p)}{\gamma'(t_0)}
    $$
    but by the previous statement, $\dd{g}{t}(t_0) = 0$, which exacty says that the gradient of $f$ is orthogonal to $\gamma$ at $\vector p$. But $\vector p$ was an arbitrary point on the level surface, and $\gamma$ was an arbitrary curve through it. So $\nabla f$ is orthogonal to *every* level curve through $\vector p$, and this orthogonal to the tangent plane at $\vector p$, and thus normal to the surface at $\vector p$. Since $\vector p$ was an arbitrary point on the level curve, this holds everywhere on the level curve, and for arbitrary level curves. Thus $\nabla f$ is orthogonal to every level curve. $\qed$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that for a continuously differentiable function $f: \mathbb{R}^2 \to \mathbb{R}$, the gradient vector $\nabla f(\mathbf{p})$ at any point $\mathbf{p}$ on a level curve $C = \{(x,y) \in \mathbb{R}^2 \mid f(x,y) = c\}$ is orthogonal to the tangent vector of every smooth curve in $C$ passing through $\mathbf{p}$.

<1>1. Let $\mathbf{p} = (x_0, y_0) \in C$ such that $f(\mathbf{p}) = c$. Let $\gamma: (-\varepsilon, \varepsilon) \to \mathbb{R}^2$ be a differentiable parametrized curve such that $\gamma(0) = \mathbf{p}$ and $\gamma(t) \in C$ for all $t \in (-\varepsilon, \varepsilon)$.
    Proof: By definition of a smooth curve on the level set $C$.

<1>2. The composite function $g(t) = (f \circ \gamma)(t) = f(\gamma(t))$ is constant on $(-\varepsilon, \varepsilon)$ with value $c$.
    Proof: Since $\gamma(t) \in C$ for all $t$, $f(\gamma(t)) = c$ identically.

<1>3. $g'(0) = 0$.
    Proof: The derivative of a constant function is identically zero.

<1>4. By the multivariable Chain Rule, $g'(0) = \nabla f(\gamma(0)) \cdot \gamma'(0) = \nabla f(\mathbf{p}) \cdot \gamma'(0)$.
    Proof: Since $f$ is continuously differentiable and $\gamma$ is differentiable at $t=0$, the chain rule applies:
    $$g'(0) = \left.\frac{d}{dt} f(x(t), y(t))\right|_{t=0} = \frac{\partial f}{\partial x}(\mathbf{p}) x'(0) + \frac{\partial f}{\partial y}(\mathbf{p}) y'(0) = \nabla f(\mathbf{p}) \cdot \gamma'(0).$$

<1>5. $\nabla f(\mathbf{p}) \cdot \gamma'(0) = 0$.
    Proof: Combining <1>3 and <1>4 gives $\nabla f(\mathbf{p}) \cdot \gamma'(0) = g'(0) = 0$.

<1>6. Conclusion: $\nabla f(\mathbf{p})$ is orthogonal to the tangent vector $\gamma'(0)$ of any curve lying on the level set through $\mathbf{p}$.
    Proof: Since two vectors with zero dot product are orthogonal by definition, and $\gamma$ was arbitrary. Q.E.D.
:::
