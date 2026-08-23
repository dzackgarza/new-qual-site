---
schema: qual/card@1
id: P-RASP13F
kind: problem
title: "Solving -Delta u + u = f via Fourier transform and the heat kernel representation"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Partial Differential Equations
  - Heat Kernel
  - Distributions
relations: []
review: draft
solved: false
---

::: problem
The problem concerns finding an explicit solution to the equation $-\Delta u + u = f$ for $f \in C_c^\infty(\mathbb{R}^n)$, using the Fourier transform.

(a) Assume that the solution $u$ and all its first-order and second-order partial derivatives are in $L^1(\mathbb{R}^n) \cap L^2(\mathbb{R}^n)$. Prove
$$
\hat{u}(z) = \frac{\hat{f}(z)}{1 + 4\pi^2 |z|^2}.
$$

(b) Prove, via the identity $(1 + 4\pi^2 |z|^2)^{-1} = \int_0^\infty e^{-t(1+4\pi^2|z|^2)} \, dt$, that
$$
u(x) = \int_0^\infty \frac{e^{-t}}{(4\pi t)^{n/2}} \int_{\mathbb{R}^n} e^{-\frac{|x-y|^2}{4t}} f(y) \, dm(y) \, dt.
$$
:::