---
schema: qual/card@1
id: P-CASP11E
kind: problem
title: "Vanishing of the contour integral of e^{iz}/log(z) over a quarter circle"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: problem
For $R > 1$ let $C_R$ be the quarter circle parametrized by $z = Re^{i\theta}$, $0 \leq \theta \leq \pi/2$.
Prove that $$\lim_{R \to \infty} \int_{C_R} \frac{e^{iz}}{\log z}\,dz = 0,$$ where $\log z$ is the principal branch of the logarithm.

Hint: You may use the inequality $\sin\theta \geq c\theta$ for $0 \leq \theta \leq \pi/2$, with some constant $c > 0$.
Then evaluate an appropriate integral.
:::
