---
schema: qual/card@1
id: D-V6UQJ
kind: definition
title: Analytic function
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $f\colon\Omega\to\CC$, and let $z_0\in\Omega$.
The function $f$ is \dfn{analytic} at $z_0$ if there exist a power series $\sum_{n\ge0}a_n(z-z_0)^n$ with radius of convergence $R>0$ and an open neighborhood $U\subseteq\Omega$ of $z_0$ with $\abs{z-z_0}<R$ for all $z\in U$, such that
$$
f(z)=\sum_{n\ge0}a_n(z-z_0)^n\qquad\text{for all } z\in U.
$$
The function $f$ is analytic on $\Omega$ if it is analytic at every point of $\Omega$.
:::
