---
schema: qual/card@1
id: T-J3AN3
kind: theorem
title: "Riesz-Fischer"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.theorem title="Riesz-Fischer"}
Let $U = \theset{u_{n}}_{n=1}^\infty$ be an orthonormal set (not necessarily a basis), then

1. There is an isometric surjection

\[
\mathcal{H} &\to \ell^2(\NN) \\
\vector x &\mapsto \theset{\inner{\vector x}{\vector u_{n}}}_{n=1}^\infty
\]

i.e. if $\theset{a_{n}} \in \ell^2(\NN)$, so $\sum \abs{a_{n}}^2 < \infty$, then there exists a $\vector x \in \mathcal{H}$ such that
$$
a_{n} = \inner{\vector x}{\vector u_{n}} \quad \forall n.
$$

2. $\vector x$ can be chosen such that
$$
\norm{\vector x}^2 = \sum \abs{a_{n}}^2
$$

> Note: the choice of $\vector x$ is unique $\iff$ $\theset{u_{n}}$ is **complete**, i.e. $\inner{\vector x}{\vector u_{n}} = 0$ for all $n$ implies $\vector x = \vector 0$.
:::
