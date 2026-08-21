---
schema: qual/card@1
id: P-TIRTE
kind: problem
title: Contractible if and only if the identity is nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
solved: false
---

::: problem
4. $\Leftarrow$: **Main Idea**: Projection and inclusion are homotopy inverses.
   One composition is equality, the other is just equality *up to homotopy*, but that's all we need!

Suppose $\id_X$ is nullhomotopic.

Then there exists some constant map $g: X \into \theset{x_0}$ for some $x_0 \in X$ where $g(x) = x_0$ and $g \homotopic \id_X$.

This means there is some homotopy $F: X \cross I \into X$ such that $F(x,0) = \id_X(x) = x$ and $F(x,1) = g(x) = x_0$ for all $x \in X$.

So let $p:X \into \theset{x_0}$ be the projection map sending every point to $x_0$, and $\iota: \theset{x_0} \into X$ be the inclusion.
We will show that the two compositions are homotopy inverses, from which it follows that $X \homotopic \theset{x_0}$.
This means that $X$ is homotopy-equivalent to a point, and thus by definition contractible.

Then $(p\circ \iota): \theset{x_0} \to \theset{x_0}$ is given by $p(\iota(x_0)) = p(x_0) = x_0$, so this is the identity on the target space $\theset{x_0}$.

Similarly, $(\iota \circ p): X \to X$ is given by $\iota(p(x)) = \iota(x_0) = x_0$, so this is the constant map on $X$ mapping every point from $X$ to $x_0$.
But then this map is exactly $g$, and by assumption this is homotopic to the identity on $X$

But then we have $p\circ \iota \homotopic \id_{\theset{x_0}}$ and $\iota \circ p \homotopic \id_X$, so they are homotopy inverses.

$\Rightarrow$: **Main Idea**: One of the homotopy inverses *is* just a constant map.

Suppose $X \homotopic \theset{x_0}$, then there exist a pair of homotopy inverses

$f: X \into \theset{x_0}$ and $g: \theset{x_0} \into X$ such that $f\circ g \homotopic \id_{\theset{x_0}}$ and $g\circ f \homotopic \id_X$.

Since $\theset{x_0}$ is a single point space, $f$ is necessarily a constant map (i.e. $f(x) = x_0$ for every $x\in X$.)
But then $(g\circ f)(x) = g(x_0) = y_0$ for some constant $y_0 \in X$, so $g\circ f$ is a constant map.
By assumption, $g\circ f \homotopic \id_X$, so the identity is homotopic to a constant map.
:::
