---
schema: qual/card@1
id: P-ULPU3
kind: problem
title: The Poisson kernel for $0\le \rho<1$ is the $2\pi$-periodic function o…
classification:
  areas:
  - real-analysis
  topics:
  - harmonic-functions
  - measure-theory
  - integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
The Poisson kernel for $0\le \rho<1$ is the $2\pi$-periodic function on $\mathbb{R}$ defined by $$P_\rho(\theta) = \text{Re}\left(\frac{1+\rho e^{i\theta}}{1-\rho e^{i\theta}}\right).$$ For functions $h$ continuous on and harmonic inside the closed disc of radius $R$ about the origin one has $$h(re^{i\eta}) = \frac{1}{2\pi}\int_0^{2\pi} P_{r/R}(\eta-\theta) h(Re^{i\theta})\,d\theta.$$ Assume that $h$ is harmonic and positive on $\mathbb{D}$.
Prove that there exists a positive Borel measure $\mu$ on $[0,2\pi]$ such that for all $re^{i\nu}\in\mathbb{D}$ one has $$h(re^{i\nu}) = \int_0^{2\pi} P_r(\eta-\theta)\,d\mu(\theta).$$
:::
