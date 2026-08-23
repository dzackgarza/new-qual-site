---
schema: qual/card@1
id: P-RAF06E
kind: problem
title: "Laplace transform operator: Schur's test bound on L^p and L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Schur Test
  - Laplace Transform
  - Holder Inequality
relations: []
review: draft
solved: false
---

::: problem
Consider the linear operator
$$
(Tf)(y) := \int_0^\infty e^{-xy} f(x) \, dx, \quad y > 0.
$$

(a) Let $1 < p < \infty$, $\frac{1}{p} + \frac{1}{q} = 1$, and show that for nonnegative measurable functions $f, g : (0, \infty) \to [0, \infty)$,
$$
\int_0^\infty \int_0^\infty e^{-xy} f(x) g(y) \, dx \, dy \leq C_p \left(\int_0^\infty f(x)^p x^{-2} \, dx\right)^{1/p} \left(\int_0^\infty g(y)^q y^{-2} \, dy\right)^{1/q}
$$
with an explicit constant $C_p$.

(b) Show that the operator $T$ is bounded on $L^2((0, \infty))$ and $\|Tf\|_2 \leq C_2 \|f\|_2$, where $C_2$ is the constant in (a) with $p = 2$.
:::