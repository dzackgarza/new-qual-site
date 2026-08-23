---
schema: qual/card@1
id: P-RAF17B
kind: problem
title: "True/false on convergence in L^p and pointwise convergence"
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
Let $(\Omega, \mathcal{B}, \mu)$ be a measure space and $f_n, f : \Omega \to \mathbb{C}$ be measurable functions. Determine which of the following statements are true. For the true statements give a brief reason and for the false statements give a counterexample.

1. If $f_n \to f$ in $L^2(\mu)$, then $\lim_{n \to \infty} f_n(\omega) = f(\omega)$ for $\mu$-a.e. $\omega$.

2. Suppose that $\omega_0 \in \Omega$ is a point such that $\{\omega_0\} \in \mathcal{B}$ and $0 < \mu(\{\omega_0\}) < \infty$. If $f_n \to f$ in $L^2(\mu)$, then $f(\omega_0) = \lim_{n \to \infty} f_n(\omega_0)$.

3. If $f(\omega) = \lim_{n \to \infty} f_n(\omega)$ for $\mu$-a.e. $\omega$, then $f_n \to f$ in measure, i.e. $\lim_{n \to \infty} \mu(|f - f_n| \geq \varepsilon) = 0$ for all $\varepsilon > 0$.

4. If $\mu(\Omega) < \infty$ and $f_n \to f$ in $L^3(\mu)$, then $f_n \to f$ in $L^1(\mu)$.
:::
