---
schema: qual/card@1
id: P-HH4R3
kind: problem
title: "Let $\\gamma$ be a piecewise smooth simple closed curve with interior\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-integral-formula
  - contour-integration
relations: []
review: draft
solved: false
---

::: problem
Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f'$ exists in an open set containing $\gamma$ and $\Omega_2$ with $\lim_{z\to \infty} f(z) = A$.
Show that
\[
\frac{1}{2 \pi i} \int_{\gamma} \frac{f(\xi)}{\xi-z} d \xi=\left\{\begin{array}{ll}
A, & \text { if } z \in \Omega_{1} \\
-f(z)+A, & \text { if } z \in \Omega_{2}
\end{array}\right.
.\]
:::
