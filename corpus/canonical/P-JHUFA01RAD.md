---
schema: qual/card@1
id: P-JHUFA01RAD
kind: problem
title: Step function approximation converges in L1
classification:
  areas:
  - real-analysis
  topics: []
solved: false
relations: []
---

Let $f \in L^1([0,1])$.
For $k \in \mathbb{N}$, let $f_k$ be the step function defined on $[0,1]$ by

$$f_k(x) = k \int_{j/k}^{(j+1)/k} f(t) \, dt, \quad \text{for } \frac{j}{k} \leq x < \frac{j+1}{k}.$$

Show that $f_k$ tends to $f$ in $L^1$ norm as $k$ tends to $+\infty$.

Hint: Treat first the case where $f$ is continuous, and use approximation.
