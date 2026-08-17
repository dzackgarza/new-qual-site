---
schema: qual/card@1
id: P-TAPVD
kind: problem
title: "Write $f$ as $f(x,y)$, we are then given that $f_x, f_y \\in C_0(\\theset{0})$."
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
1. Write $f$ as $f(x,y)$, we are then given that $f_x, f_y \in C_0(\theset{0})$. It has the type
  $$
  f: \RR^2 \to \RR \\
  (x,y) \mapsto f(x,y)
  $$
   
   Definition:
$$
\vector u = \thevector{a, b} \implies D _ { \vector u } f = \lim _ { h \rightarrow 0 } \frac { f ( x + a h , y + b h ) - f ( x , y ) } { h }
$$
  Definition: 
$$
\dd{}{x}f(x,y) = f_x(x,y) = \lim_{h\to 0} \frac{f(x+h, y) - f(x,y)}{h}
$$

    We need to show that $D_{\vector u}f$ exists for arbitrary $\vector u$. Wlog, assume $\norm{\vector u} = 1$, and let $D_{\vector u}f$ denote the directional derivative of $f$ in the direction $\vector u$. Fix some $\vector p \in \RR^2$ and define the curve
$$
\gamma(t): \RR \to \RR^2 \\t \mapsto \vector p + t \vector u
$$

    Then define 
$$
g: \RR \to \RR \\ t \mapsto f(\gamma(t)) = f(\vector p + t\vector u).
$$

    Note that $g(0) = f(\vector p)$.

    **Since the partial derivatives of $f$ exist and are continuous**, $f$ is differentiable with derivative 
$$
Df = \sum_{i=1}^2 \dd{f}{x_i} \vector e_i \definedas \nabla f.
$$ 

    Thus by the multivariate chain rule, $g$ is differentiable as well and can be computed as 
$$
g'(t) = Df(\gamma(t)) ~ D\gamma(t) = \inner{\nabla f(\gamma(t))}{\gamma'(t)}.
$$ 

    Note that $\gamma(0) = \vector p$, and $\gamma$ is a linear function of $t$ that is differentiable, with derivative/tangent vector $\gamma'(t) = \vector u$.

    From this, we can compute 
$$
g'(0) = \inner{\nabla f(\vector p)}{\vector u}
$$ 
    in the above expression.

    Since $g$ is differentiable, we can write
$$\begin{align*}
g'(0) &= \restrictionof{g'(t)}{t=0} \\ 
&= \restrictionof{\lim_{h\to 0} \frac{g(t+h) - g(t)}{h}}{t=0} \\ 
&= \lim_{h\to 0} \frac{g(h) - g(0)}{h} \\
&\definedas \lim_{h\to 0} \frac{f(\vector p + h\vector u) - f(\vector p)}{h}
\end{align*}$$

    In particular, since $g'(0)$ exists, the limit in the last term does as well, and by definition is $D_{\vector u}(\vector p)$. Now letting $\vector p = \vector x$ be variable, we combine these to obtain 
$$
D_{\vector u}(\vector p) = \inner{\nabla f(\vector p)}{\vector u}
$$
  Since $\vector u$ was arbitrary, this shows that the directional derivative exists in any direction and is given by the above expression. $\qed$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f: \mathbb{R}^2 \to \mathbb{R}$ be a function whose first-order partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ exist and are continuous in a neighborhood of a point $\mathbf{p} = (x_0, y_0)$. Prove that the directional derivative $D_{\mathbf{u}} f(\mathbf{p})$ exists in any unit direction $\mathbf{u} = (u_1, u_2)$ and satisfies $D_{\mathbf{u}} f(\mathbf{p}) = \nabla f(\mathbf{p}) \cdot \mathbf{u}$.

<1>1. Definition of directional derivative: For a unit vector $\mathbf{u} = (u_1, u_2) \in \mathbb{R}^2$,
    $$D_{\mathbf{u}} f(\mathbf{p}) = \lim_{h \to 0} \frac{f(x_0 + h u_1, y_0 + h u_2) - f(x_0, y_0)}{h}.$$

<1>2. Since $f_x$ and $f_y$ are continuous in a neighborhood of $\mathbf{p}$, $f$ is (totally) differentiable at $\mathbf{p}$.
    Proof:
    <2>1. By the multivariable Mean Value Theorem on coordinate increments, for sufficiently small $h$:
        $$f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0) = \left[f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0 + hu_2)\right] + \left[f(x_0, y_0 + hu_2) - f(x_0, y_0)\right].$$
    <2>2. Applying the single-variable Mean Value Theorem to each bracketed term:
        $$f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0) = f_x(x_0 + \theta_1 hu_1, y_0 + hu_2)(h u_1) + f_y(x_0, y_0 + \theta_2 hu_2)(h u_2)$$
        for some $\theta_1, \theta_2 \in (0, 1)$.
    <2>3. By continuity of $f_x$ and $f_y$ at $(x_0, y_0)$:
        $$\lim_{h \to 0} f_x(x_0 + \theta_1 hu_1, y_0 + hu_2) = f_x(x_0, y_0), \qquad \lim_{h \to 0} f_y(x_0, y_0 + \theta_2 hu_2) = f_y(x_0, y_0).$$

<1>3. The directional derivative limit exists and equals $\nabla f(\mathbf{p}) \cdot \mathbf{u}$.
    Proof:
    <2>1. Dividing the expression in <1>2 by $h \neq 0$:
        $$\frac{f(\mathbf{p} + h\mathbf{u}) - f(\mathbf{p})}{h} = f_x(x_0 + \theta_1 hu_1, y_0 + hu_2) u_1 + f_y(x_0, y_0 + \theta_2 hu_2) u_2.$$
    <2>2. Taking the limit as $h \to 0$ and applying the limits established in <2>3:
        $$D_{\mathbf{u}} f(\mathbf{p}) = \lim_{h \to 0} \frac{f(\mathbf{p} + h\mathbf{u}) - f(\mathbf{p})}{h} = f_x(x_0, y_0) u_1 + f_y(x_0, y_0) u_2 = \nabla f(\mathbf{p}) \cdot \mathbf{u}.$$
    Since $\mathbf{u}$ was an arbitrary unit vector, $D_{\mathbf{u}} f(\mathbf{p})$ exists in all directions. Q.E.D.
:::
