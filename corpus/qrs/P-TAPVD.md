---
schema: qual/card@1
id: P-TAPVD
kind: problem
title: "Write $f$ as $f(x,y)$, we are then given that $f_x, f_y \\in C_0(\\theset{0})$."
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
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

