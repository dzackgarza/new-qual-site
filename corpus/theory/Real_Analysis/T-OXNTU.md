---
schema: qual/card@1
id: T-OXNTU
kind: theorem
title: Mean value theorem and Cauchy's mean value theorem
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Differentiation
relations: []
review: draft
---

::: {.theorem}
Let $a<b$ and let $f\colon [a, b] \to \RR$ be continuous on $[a,b]$ and differentiable on $(a, b)$.

1. There exists $\xi \in (a, b)$ such that
$$
f(b) - f(a) = f'(\xi)(b-a).
$$

2. If $g\colon [a,b]\to \RR$ is also continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $\xi\in(a,b)$ such that
$$
\qty{ f(b) - f(a) } g'(\xi) = \qty{g(b) - g(a)} f'(\xi).
$$
:::

::: {.remark}
Geometrically, (2) says that the plane curve $t\mapsto(f(t),g(t))$, $t\in[a,b]$, has a tangent vector $(f'(\xi),g'(\xi))$ at some interior parameter $\xi$ that is parallel to the chord from $(f(a),g(a))$ to $(f(b),g(b))$.

![](../../assets/figures/2021-11-09_22-20-24.png)
:::
