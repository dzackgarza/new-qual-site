---
schema: qual/card@1
id: PR-2CZUM
kind: proposition
title: Continuity and differentiation under the integral sign
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $I=[a,b]\subseteq\RR$ with $a<b$, and let $f\colon X\times I \to \CC$ be such that $x\mapsto f(x,t)$ is [[D-R5DL3|integrable]] for each $t\in I$.
Put
$$
F(t)\coloneqq\int_X f(x, t) \dmu(x), \qquad t\in I .
$$

1. Suppose there exists $g\in L^1(X,\mu)$ with $\abs{f(x, t)} \leq g(x)$ for all $x\in X$ and $t\in I$.
If $t_0\in I$ and $\lim_{t\to t_0}f(x,t)=f(x,t_0)$ for every $x\in X$, then $\lim_{t\to t_0}F(t)=F(t_0)$.
In particular, if $t\mapsto f(x,t)$ is continuous on $I$ for every $x\in X$, then $F$ is continuous on $I$.

2. Suppose the partial derivative $\frac{\partial f}{\partial t}(x,t)$ exists for all $x\in X$ and $t\in I$, and there exists $g\in L^1(X,\mu)$ with $\abs{\frac{\partial f}{\partial t}(x, t)} \leq g(x)$ for all $x\in X$ and $t\in I$.
Then $F$ is differentiable on $I$ and
$$
F'(t) = \int_X \frac{\partial f}{\partial t}(x, t) \dmu(x) .
$$
:::
