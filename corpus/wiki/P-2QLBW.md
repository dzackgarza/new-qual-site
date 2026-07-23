---
schema: qual/card@1
id: P-2QLBW
kind: problem
title: "1. Definitions:"
classification:
  areas: []
  topics: []
relations: []
review: draft
---
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

