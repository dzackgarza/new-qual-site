---
schema: qual/card@1
id: P-RASP17D
kind: problem
title: "True or false: uniform boundedness variants and an L^2 membership criterion"
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Boundedness Principle
  - Banach-Steinhaus Theorem
  - L2 Spaces
  - Baire Category
relations: []
review: draft
solved: false
---

::: problem
Answer true or false.
For true statements give a brief justification; for false statements give a counterexample.

1. If $X$ is a Banach space and $\{\varphi_n\}_{n=1}^\infty \subset X^*$ satisfies $\sup_n |\varphi_n(x)| < \infty$ for all $x \in X$, then $\sup_n \sup_{\|x\|=1} |\varphi_n(x)| < \infty$.

2. If $X$ is a Banach space, $D$ is a dense subspace of $X$, and $\{\varphi_n\}_{n=1}^\infty \subset X^*$ satisfies $\sup_n |\varphi_n(x)| < \infty$ for all $x \in D$, then $\sup_n \sup_{\|x\|=1} |\varphi_n(x)| < \infty$.

3. Suppose $(\Omega, \mathcal{B}, \mu)$ is a measure space, $\Omega_n \in \mathcal{B}$ with $\Omega_n \uparrow \Omega$ and $\mu(\Omega_n) < \infty$ for all $n$.
   If $f : \Omega \to \mathbb{C}$ is measurable such that $\sup_{n \in \mathbb{N}} \int_{\Omega_n} f \mathbf{1}_{|f| \leq n} g \, d\mu < \infty$ for all $g \in L^2(\mu)$, then $f \in L^2(\mu)$.
:::
