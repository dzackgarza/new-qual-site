---
schema: qual/card@1
id: P-QNUFT
kind: problem
title: Paths with common endpoints in a simply connected space are homotopic
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - homotopy
relations: []
review: draft
solved: false
---

::: problem
1. **Main idea**: just algebraic manipulations using the $\pi_1$ functor and unravelling definitions.

Let $X$ be path connected and simply connected, and let $x,y \in X$ be two arbitrary points.
Then consider two paths, $\gamma: I \into X, \gamma(0) = x, \gamma(1) = y$ $\alpha: I \into X, \alpha(0) = x, \alpha(1) = y$.

We would like to show $\gamma \homotopic \alpha$.
Since $X$ is simply connected, we know that $\pi_1(X) = 0$.
This means that for any $a,b \in \pi_1(X), a = b = e$, the identity element in this group.

So we construct two loops: one as $\gamma \bar\alpha$, the other as $\alpha\bar\gamma$.
Apply the $\pi_1$ functor yields $[\gamma\bar\alpha] = e = [c_x] = [\alpha\bar\gamma]$, where $[c_x]$ is the equivalence class of the constant path at $x$, and equivalently the identity element in $\pi_1(X)$.
Lemma: If $f\homotopic g$, then $f\circ h \homotopic g \circ h$ for any $h$.

But this says $\gamma\bar\alpha \homotopic c_x$ and $\alpha\bar\gamma \homotopic c_x$.
But $\gamma \homotopic c_x \circ \gamma \homotopic (\alpha\bar\gamma) \circ \gamma \homotopic \alpha\circ (\bar\gamma \circ\gamma) \homotopic \alpha$, which is what we desired.
:::
