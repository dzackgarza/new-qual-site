---
schema: qual/card@1
id: PR-V4MOK
kind: proposition
title: Differentiation under the integral sign
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]], let $I\subseteq\RR$ be an open interval, and let $f\colon X\times I\to\CC$ be such that $x\mapsto f(x,t)$ is [[D-R5DL3|integrable]] for each $t\in I$.
Put $F(t)\coloneqq\int_X f(x,t)\dmu(x)$.
Suppose $\frac{\partial f}{\partial t}(x,t)$ exists for all $x\in X$ and $t\in I$, and there is $g\in L^1(\mu)$ with $\abs{\frac{\partial f}{\partial t}(x,t)}\leq g(x)$ for all $x\in X$ and $t\in I$.
Then $F$ is differentiable on $I$ and
$$
F'(t) = \int_X \frac{\partial f}{\partial t}(x, t) \dmu(x)
$$
[@Fol13, Theorem 2.27].
:::
