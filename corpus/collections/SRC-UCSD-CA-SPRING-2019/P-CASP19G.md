---
schema: qual/card@1
id: P-CASP19G
kind: problem
title: "Poisson integral converges to the boundary value at points of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Poisson Kernel
  - Harmonic Functions
  - Boundary Values
relations: []
review: draft
---

::: problem
Let $f$ be a bounded, piecewise continuous function on $\partial \mathbb{D}$, and consider the harmonic function
$$
u(z) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it}) \, dt, \quad z = re^{i\theta},
$$
where $P_r(t) := \operatorname{Re} \frac{1 + re^{it}}{1 - re^{it}}$ is the Poisson kernel in $\mathbb{D}$.
Assume that $f$ is continuous at $a = e^{i\theta_0}$, and show that $\lim_{z \to a} u(z) = f(a)$.
:::
