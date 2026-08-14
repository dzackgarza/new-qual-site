---
schema: qual/card@1
id: P-BBI5H
kind: problem
title: "3. $\\Rightarrow$ Let $[\\alpha] \\in \\pi_1(X\\cross Y, (x_0, y_0))$ be an\u2026"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - product-topology
relations: []
review: draft
---
3. $\Rightarrow$ Let $[\alpha] \in \pi_1(X\cross Y, (x_0, y_0))$ be an arbitrary loop in $X \cross Y$. Then $\alpha$ is equivalently a map $S^1 \into X \cross Y$. Considering $S^1$ to be a subset of $\RR^2$, we can parameterize $\alpha$ as $\alpha(z) = \alpha(x+iy) = (\alpha_x(x), \alpha_y(y))$ in components. In particular, since $\alpha$ is continuous, so are $\alpha_x, \alpha_y$. Moreover, since $\alpha(0) = \alpha(0 + i0) = (x_0, y_0)$, we have $\alpha_x(0) = x_0, \alpha_y(0) = y_0$.
(Note: alternatively, given the product, we have projections $p_X, p_y$, so we can define the map $\alpha \mapsto (p_X \circ \alpha, p_Y \circ \alpha)$)

But then $\alpha_x: S^1 \into X$ and $\alpha_y: S^1 \into Y$ are loops entirely in $X, Y$ at the respective base points, and so we can define the map
$F: \pi_1(X\cross Y, (x_0, y_0)) \into \pi_1(X, x_0) \cross \pi_1(Y, y_0)$ by
$[\alpha] = [(\alpha_x, \alpha_y)] \mapsto ([\alpha_x], [\alpha_y])$

This is injective, since $([a],[b]) = ([c],[d])$ on the RHS means that $[a] = [c], [b] = [d]$ in the fundamental groups, and thus $a\homotopic c, b\homotopic d$ in the spaces. We want to show that $[(a,b)] = [(c,d)]$, which would follow if $\alpha(x+iy) = (a(x),b(y)) \homotopic \beta(x+iy) = (c(x),d(y))$ in $X\ \cross Y$. ...?

This is surjective, because if $([a], [b])$ are elements in the right-hand side, then $a(0) = a(1) = x_0$ and $b(0) = b(1) = y_0$, so we can consider $(a,b): I \into X \cross Y$ where $(a,b)(z) = (a,b)(x+iy) = (a(x), b(y))$. This is then a loop in $X\cross Y$, since $(a,b)(0) = (a(0), b(0)) = (0,0) = (x_0, y_0)$ and similarly $(a,b)(1) = (a(1), b(1)) = (x_0, y_0)$. So this is actually a map $(a,b): S^1 \into X \cross Y$, or in other words, a loop in $X\times Y$ based at $(x_0, y_0)$, which lifts to an element of the fundamental group on the LHS.

Maps in both directions are continuous, since a vector function is continuous iff its component functions are continuous.

This is well-defined, due to the fact that if $a \homotopic b$, then $p_X \circ a \homotopic p_X\circ b$, and $F = (f_x, f_y)$ is a homotopy iff its components functions are homotopies.
