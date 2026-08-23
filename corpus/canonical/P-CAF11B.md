---
schema: qual/card@1
id: P-CAF11B
kind: problem
title: "Construction of a metric from a sequence of metrics and convergence characterization"
classification:
  areas:
  - complex-analysis
  topics:
  - Metric Spaces
relations: []
review: draft
solved: false
---

::: problem
Let $X$ be a set and $\{\rho_n\}$ a sequence of metrics on $X$.
Define $\rho$ on $X \times X$ by $$\rho(x, y) := \sum_{n=1}^{\infty} \frac{1}{n^2} \cdot \frac{\rho_n(x, y)}{1 + \rho_n(x, y)}.$$

(a) Show that $\rho(x, y) < \infty$ for all $x, y \in X$ and prove that $\rho$ is a metric on $X$.

(b) Let $\{x_j\}$ be a sequence in $X$, and $x \in X$.
Prove that $\lim_{j \to \infty} \rho(x_j, x) = 0$ if and only if $\lim_{j \to \infty} \rho_n(x_j, x) = 0$ for all $n \geq 1$.
:::
