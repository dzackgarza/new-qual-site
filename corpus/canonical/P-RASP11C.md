---
schema: qual/card@1
id: P-RASP11C
kind: problem
title: "Schur-type test: integral kernels bounded on pairings extend to bounded operators"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Schur Test
  - Holder Inequality
relations: []
review: draft
solved: false
---

::: problem
Let $1 \leq p, p' \leq \infty$ be fixed dual indices.
Suppose $K(x, y) \geq 0$ is a Lebesgue measurable function on $\mathbb{R}^n \times \mathbb{R}^n$ such that there exists a constant $0 \leq K_0 < \infty$ with
$$
\iint g(x) K(x, y) f(y) \, dx \, dy \leq K_0 \|g\|_{L^{p'}(\mathbb{R}^n)} \|f\|_{L^p(\mathbb{R}^n)}
$$
for all measurable $f, g \geq 0$ on $\mathbb{R}^n$.
Show that if $f \in L^p(\mathbb{R}^n)$, then the function $Kf(x) := \int_{\mathbb{R}^n} K(x, y) f(y) \, dy$ is well defined for (Lebesgue) a.e. $x \in \mathbb{R}^n$, and one has $\|Kf\|_{L^p(dx)} \leq K_0 \|f\|_{L^p(dx)}$.
:::
