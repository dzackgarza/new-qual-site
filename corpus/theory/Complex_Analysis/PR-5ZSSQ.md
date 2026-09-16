---
schema: qual/card@1
id: PR-5ZSSQ
kind: proposition
title: Contraction mapping principle
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Metric Spaces
  - Completeness
relations: []
review: draft
---

::: {.proposition}
Let $(X,d)$ be a nonempty complete metric space, and let $f\colon X\to X$ be a map for which there exists $c\in[0,1)$ with
$$
d(f(x),f(y)) \leq c\, d(x,y) \quad\text{for all } x, y\in X.
$$
Then $f$ has a unique fixed point: there is exactly one $x_0\in X$ with $f(x_0) = x_0$.
:::

::: {.proof}
Fix $x\in X$ and set $x_k\coloneqq f^k(x)$.
By induction $d(x_{k+1},x_k)\le c^kd(x_1,x_0)$, so for $m>k$ the triangle inequality gives $d(x_m,x_k)\le\frac{c^k}{1-c}d(x_1,x_0)$, and $(x_k)$ is Cauchy.
By completeness $x_k\to x^*$ for some $x^*\in X$; since $f$ is continuous, $f(x^*)=\lim_k f(x_k)=\lim_kx_{k+1}=x^*$.
If $f(y)=y$ as well, then $d(x^*,y)=d(f(x^*),f(y))\le c\,d(x^*,y)$ with $c<1$, so $d(x^*,y)=0$ and $y=x^*$.
:::
