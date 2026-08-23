---
schema: qual/card@1
id: P-CAF11E
kind: problem
title: "A continuous function harmonic on the punctured disk is harmonic on the full disk"
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
Let $u$ be a real-valued continuous function on $\overline{\mathbb{D}}$, and assume that $u$ is harmonic in $\mathbb{D} \setminus \{0\}$.
Prove that $u$ is harmonic in $\mathbb{D}$.

Hint: Consider $v(r) := \int_{-\pi}^{\pi} u(re^{i\theta})\,d\theta$.
You may use without proof Laplace's equation in polar coordinates: $$r\frac{\partial}{\partial r}\!\left(r\frac{\partial U}{\partial r}\right) + \frac{\partial^2 U}{\partial \theta^2} = 0,$$ where $U(r, \theta) = u(re^{i\theta})$.
You may also use without proof the fact that a harmonic function in $\mathbb{D} \setminus \{0\}$ that depends only on $|z|$ is necessarily of the form $u(z) = a\log|z| + b$, where $a$ and $b$ are real constants.
:::
