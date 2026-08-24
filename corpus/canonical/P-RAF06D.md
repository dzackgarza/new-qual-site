---
schema: qual/card@1
id: P-RAF06D
kind: problem
title: "Characterizations of convex functions: secant slopes and monotone derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Convex Functions
  - Absolute Continuity
  - Monotone Derivatives
relations: []
review: draft
---

::: problem
Recall that a function $f : (a, b) \to \mathbb{R}$ (with $-\infty \leq a < b \leq \infty$) is called convex if
$$
f((1-\lambda)x + \lambda y) \leq (1-\lambda)f(x) + \lambda f(y), \quad \forall \lambda \in (0, 1), x, y \in (a, b).
$$

(a) Show that $f$ is convex if and only if for all $x, y, x', y' \in (a, b)$ with $x \leq x' < y'$ and $x < y \leq y'$,
$$
\frac{f(y) - f(x)}{y - x} \leq \frac{f(y') - f(x')}{y' - x'}.
$$

(b) Show that $f$ is convex if and only if $f$ is absolutely continuous on every compact subinterval $[c, d]$ of $(a, b)$ and $f'$ is increasing a.e.
:::
