---
schema: qual/card@1
id: E-XFF7Q
kind: exercise
title: Uniform balls are not products of intervals
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Let $\bar{\rho}$ be the uniform metric on $\mathbb{R}^\omega$.
Given $\mathbf{x} = (x_1, x_2, \ldots) \in \mathbb{R}^\omega$ and given $0 < \epsilon < 1$, let

$$
U(\mathbf{x}, \epsilon) = (x_1 - \epsilon, x_1 + \epsilon) \times \dots \times (x_n - \epsilon, x_n + \epsilon) \times \dots.
$$

(a) Show that $U(\mathbf{x}, \epsilon)$ is not equal to the $\epsilon$-ball $B_{\bar{\rho}}(\mathbf{x}, \epsilon)$.

(b) Show that $U(\mathbf{x}, \epsilon)$ is not even open in the uniform topology.

(c) Show that

$$
B_{\bar{\rho}}(\mathbf{x}, \epsilon) = \bigcup_{\delta < \epsilon} U(\mathbf{x}, \delta).
$$
:::
