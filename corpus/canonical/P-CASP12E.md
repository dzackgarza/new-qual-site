---
schema: qual/card@1
id: P-CASP12E
kind: problem
title: "Boundary behavior of the Poisson integral on arcs of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
solved: false
---

::: problem
Let $f(e^{it})$ be a piecewise continuous, real-valued function on $\mathbb{T}$, and consider the harmonic function in the unit disk $\mathbb{D}$ given by $$u(z) := \frac{1}{2\pi}\int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it})\,dt,$$ where $P_r(\theta)$ denotes the Poisson kernel and $z = re^{i\theta}$.
Suppose that $A \subset \mathbb{T}$ is an open sub-arc on which $f$ is continuous.
Show that $$\lim_{z \to a} u(z) = f(a)$$ for every $a = e^{i\theta} \in A$.
:::
