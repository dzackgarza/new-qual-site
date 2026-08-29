---
schema: qual/card@1
id: T-RA-WORKSHOP-D4-3-1
kind: theorem
title: 'Proposition 3.1: Equivalent characterizations of continuity'
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Euclidean Spaces
relations: []
review: draft
---

::: {.theorem}
For a function $f:E\subset\mathbb R^n\to\mathbb R^m$ the following are equivalent:

1. $f$ is continuous on $E$.

2. For any $x\in E$ and $\epsilon>0$ there exists some $\delta>0$ such that $\lVert f(y)-f(x)\rVert<\epsilon$ for all $y\in E$ with $\lVert x-y\rVert<\delta$.

3. For every convergent sequence $\{x_n\}\subset E$ with $\lim_{n\to\infty}x_n=x\in E$, $\lim_{n\to\infty}f(x_n)=f(x)$.

4. For every open set $G\subset\mathbb R^m$ the set $f^{-1}(G)$ is open in $E$ (with the subspace topology).
:::
