---
schema: qual/card@1
id: P-AGH441GRADEDRINGWEIERSTRASS
kind: problem
title: The section ring $\bigoplus_n H^0(\OO_X(nP))$ of an elliptic curve is a Weierstrass ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Linear Systems
  - Embeddings
relations: []
review: draft
---

::: {.problem}
Let $X$ be an elliptic curve over $k$, with $\characteristic k \neq 2$, let $P \in X$ be a point, and let $R$ be the graded ring $R=\bigoplus_{n \geq 0} H^0(X, \OO_X(nP))$.
Show that for suitable choice of $t, x, y$
$$
R \cong k[t, x, y] /\left(y^2-x\left(x-t^2\right)\left(x-\lambda t^2\right)\right),
$$
as a graded ring, where $k[t, x, y]$ is graded by setting $\deg t=1$, $\deg x=2$, $\deg y=3$.
:::
