---
schema: qual/card@1
id: P-LHC3M
kind: problem
title: The chain rule for $f(g(t))$ and perpendicularity of $\nabla f$ to the tangent
  of an implicit level curve
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
(a) Let $f(x, y)$ be a differentiable function from $\mathbb{R}^2$ to $\mathbb{R}$ and let $g(t) = (x(t), y(t))$ be a differentiable curve from $\mathbb{R}$ to $\mathbb{R}^2$.
State the multivariable **chain rule** for the derivative of the composite function $F(t) = (f \circ g)(t) = f(x(t), y(t))$.

(b) Let $f(x, y)$ be a continuously differentiable function on $\mathbb{R}^2$, and let $P = (x_0, y_0) \in \mathbb{R}^2$ be a point.
Assume that in a neighborhood of $P$, the level curve equation $f(x, y) = f(P)$ implicitly defines $y$ as a differentiable function of $x$, say $y = h(x)$ with $y_0 = h(x_0)$.
Show that the **tangent vector** to the graph of $y = h(x)$ at $P$ is **perpendicular (orthogonal)** to the **gradient vector** $\nabla f(P)$.
:::

::: solution
**Goal:** State the multivariable chain rule and prove that level curve tangent lines are orthogonal to the gradient vector $\nabla f(P)$.

<1>1. Part (a): Multivariable Chain Rule:
    *Proof:*
    <2>1. Let $f: \mathbb{R}^2 \to \mathbb{R}$ and $g: \mathbb{R} \to \mathbb{R}^2$ given by $g(t) = (x(t), y(t))$ be differentiable functions.
    <2>2. The derivative of the composite function $F(t) = (f \circ g)(t) = f(x(t), y(t))$ is given by:
        $$\frac{dF}{dt}(t) = \frac{\partial f}{\partial x}(x(t), y(t)) \frac{dx}{dt}(t) + \frac{\partial f}{\partial y}(x(t), y(t)) \frac{dy}{dt}(t).$$
    <2>3. In vector notation using the gradient vector $\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$ and velocity vector $g'(t) = (x'(t), y'(t))$:
        $$\frac{d}{dt}(f(g(t))) = \nabla f(g(t)) \cdot g'(t) = \langle \nabla f(g(t)), g'(t) \rangle.$$

<1>2. Part (b): Perpendicularity of $\nabla f(P)$ to the Tangent Line:
    *Proof:*
    <2>1. Parameterize the graph of the implicit function $y = h(x)$ as a smooth curve $\gamma: I \to \mathbb{R}^2$:
        $$\gamma(x) = (x, h(x)).$$
    <2>2. The point $P = (x_0, y_0) = \gamma(x_0)$.
    <2>3. The **tangent vector** to the graph at $P$ is given by the derivative:
        $$\mathbf{T} = \gamma'(x_0) = \left( 1, h'(x_0) \right).$$
    <2>4. Since the graph lies entirely on the level set $f(x, y) = f(P) = c$ for all $x$ in a neighborhood of $x_0$:
        $$f(\gamma(x)) = f(x, h(x)) = c \quad \text{for all } x \in I.$$
    <2>5. Differentiating both sides of the identity $f(\gamma(x)) = c$ with respect to $x$ using the Chain Rule from Part (a):
        $$\frac{d}{dx} [f(\gamma(x))] = \nabla f(\gamma(x)) \cdot \gamma'(x) = 0.$$
    <2>6. Evaluating at $x = x_0$ where $\gamma(x_0) = P$:
        $$\nabla f(P) \cdot \gamma'(x_0) = \nabla f(P) \cdot \mathbf{T} = 0.$$
    <2>7. Alternatively, by implicit differentiation:
        $$\frac{\partial f}{\partial x}(P) \cdot 1 + \frac{\partial f}{\partial y}(P) \cdot h'(x_0) = 0 \implies h'(x_0) = -\frac{f_x(P)}{f_y(P)} \quad (\text{if } f_y(P) \ne 0).$$
        Then:
        $$\nabla f(P) \cdot \mathbf{T} = (f_x(P), f_y(P)) \cdot \left( 1, -\frac{f_x(P)}{f_y(P)} \right) = f_x(P) - f_x(P) = 0.$$
    <2>8. Since the dot product $\nabla f(P) \cdot \mathbf{T} = 0$, the gradient $\nabla f(P)$ is **perpendicular (orthogonal)** to the tangent vector $\mathbf{T}$ of the level curve at $P$.

<1>3. Conclusion:
    The chain rule gives $\frac{d}{dt} f(g(t)) = \nabla f(g(t)) \cdot g'(t)$; differentiating the level curve identity $f(x, h(x)) = c$ yields $\nabla f(P) \cdot (1, h'(x_0)) = 0$. Q.E.D.
:::
