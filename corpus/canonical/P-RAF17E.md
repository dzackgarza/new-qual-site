---
schema: qual/card@1
id: P-RAF17E
kind: problem
title: "Convolution with essentially bounded kernel is continuous"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $g : \mathbb{R}^d \to \mathbb{R}^d$ be a measurable function which is essentially bounded, i.e. there exists $M < \infty$ such that $|g(x)| \leq M$ for $m$-a.e. $x \in \mathbb{R}^d$.
For $f \in L^1(m) := L^1(\mathbb{R}^d, m)$, let
$$
(f * g)(x) = \int_{\mathbb{R}^d} f(x-y)g(y)\,dy.
$$

1. Show $(f * g)(x)$ is well defined (i.e. the integral exists) and $|(f * g)(x)| \leq M\|f\|_1$ for all $x \in \mathbb{R}^d$.

2. Show $(f * g)(x)$ may also be written as
$$
(f * g)(x) = \int_{\mathbb{R}^d} f(y)g(x - y)\,dy.
$$

3. Verify $(f_n * g)(x)$ is continuous in $x$ for any $f_n \in C_c(\mathbb{R}^d)$.

4. Show, for $f \in L^1(m)$, that $f * g$ may be written as a uniformly convergent limit of continuous functions and hence $(f * g)(x)$ is continuous in $x$.
:::
