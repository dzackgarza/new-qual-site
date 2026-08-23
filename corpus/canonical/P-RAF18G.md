---
schema: qual/card@1
id: P-RAF18G
kind: problem
title: "Derivative of an integral involving min(x,y)"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $g \in L^1([0,1], m)$ and $h : [0,1] \to \mathbb{R}$ be a continuous function.

1. If $f : [0,1] \to \mathbb{R}$ is absolutely continuous and satisfies $f'(x) = h(x)$ for a.e. $x$, show $f'(x) = h(x)$ for all $x \in (0,1)$.

2. Now suppose that
$$
f(x) := \int_0^1 \min(x,y)\,g(y)\,dy.
$$
Show $f'(x) = \int_x^1 g(y)\,dy$ for all $x \in (0,1)$.
:::
