---
schema: qual/card@1
id: E-WOS95
kind: problem
title: Induced homomorphisms up to base-point change
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Show that if $X$ is path connected, the homomorphism induced by a continuous map is independent of base point, up to isomorphisms of the groups involved.
More precisely, let $h: X \to Y$ be continuous, with $h(x_0) = y_0$ and $h(x_1) = y_1$.
Let $\alpha$ be a path in $X$ from $x_0$ to $x_1$, and let $\beta = h \circ \alpha$.
Show that

$$
\hat{\beta} \circ (h_{x_0})_* = (h_{x_1})_* \circ \hat{\alpha}.
$$

This equation expresses the fact that the following diagram of maps "commutes."

$$
\begin{array}{c}
\pi_1(X, x_0) \xrightarrow{\ (h_{x_0})_*\ } \pi_1(Y, y_0) \\
\Biggl\downarrow \hat{\alpha} \qquad\qquad\qquad\quad \Biggl\downarrow \hat{\beta} \\
\pi_1(X, x_1) \xrightarrow{\ (h_{x_1})_*\ } \pi_1(Y, y_1)
\end{array}
$$
:::
