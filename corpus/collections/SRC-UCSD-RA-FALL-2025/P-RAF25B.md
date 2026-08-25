---
schema: qual/card@1
id: P-RAF25B
kind: problem
title: "Level sets of the distance function have Lebesgue measure zero"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Measure
  - Lebesgue Differentiation Theorem
  - Distance Functions
relations: []
review: draft
---

::: problem
Let $K \subset \mathbb{R}^2$ be compact.
Given $\delta > 0$, consider the set
$$
K_\delta := \{x \in \mathbb{R}^2 : d(x, K) := \inf_{y \in K} |x - y| = \delta\},
$$
that is, the collection of points at distance $\delta$ from $K$.

(1) Prove that $K_\delta$ is closed and that the distance is always realized, that is, for every $x \in K_\delta$ there is $y_x \in K$ such that $|y_x - x| = \delta$.

(2) Given $x \in K_\delta$ and $\epsilon \in (0, \delta)$, show that
$$
L^2(B_\epsilon(x) \cap K_\delta^c) \geq \frac{\pi \epsilon^2}{4},
$$
where $L^2$ is the Lebesgue measure on $\mathbb{R}^2$, $B_\epsilon(x)$ is the ball of radius $\epsilon$ centered at $x$ and $K_\delta^c = \mathbb{R}^2 \setminus K_\delta$.

(3) Using the Lebesgue differentiation theorem show that $L^2(K_\delta) = 0$.
:::
