---
schema: qual/card@1
id: P-RAF17D
kind: problem
title: "L^p integrability from weak-type boundedness"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Suppose that $(\Omega, \mathcal{B}, \mu)$ is a measure space, $\Omega_n \in \mathcal{B}$ with $\Omega_n \uparrow \Omega$ and $\mu(\Omega_n) < \infty$ for all $n \in \mathbb{N}$.
If $f : \Omega \to \mathbb{C}$ is a measurable function such that
$$
\int_\Omega |fg|\,d\mu < \infty \quad \text{for all } g \in L^{3/2}(\mu),
$$
show $f \in L^3(\mu)$, i.e. $\int_\Omega |f|^3\,d\mu < \infty$.

Hint: consider $f_n := \mathbf{1}_{\Omega_n} f \cdot \mathbf{1}_{|f| \leq n} \in L^3(\mu)$ for $n \in \mathbb{N}$ and recall $L^3(\mu) \cong L^{3/2}(\mu)^*$.
:::
