---
schema: qual/card@1
id: P-RAF22A
kind: problem
title: "True or false: sigma-finite mutual absolute continuity, local L^2, Fourier transform of translates"
classification:
  areas:
  - real-analysis
  topics:
  - Sigma-Finite Measures
  - Absolute Continuity
  - L2 Spaces
  - Tempered Distributions
  - Fourier Transform
relations: []
review: draft
solved: false
---

::: problem
Determine if each of the following statements is true or false. If true, give a brief proof. If false, give a counterexample or prove your assertion.

1. If $(X, \mathcal{M}, \mu)$ is a $\sigma$-finite measure space, then there exists a finite measure $\nu$ on $\mathcal{M}$ such that $\nu \ll \mu$ and $\mu \ll \nu$.

2. Let $m$ denote Lebesgue measure on $\mathbb{R}$. If $f \in L^1(\mathbb{R}, m)$ and $\int_a^{a+1} |f(x)|^2 \, dx < \infty$ for every $a \in \mathbb{R}$, then $f \in L^2(\mathbb{R}, m)$.

3. Let $f$ be a tempered distribution on $\mathbb{R}^n$, with Fourier transform defined by $\langle \hat{f}, \varphi \rangle = \langle f, \hat{\varphi} \rangle$ for $\varphi \in \mathcal{S}$. Recall that for a distribution, $\langle \tau_y^\vee f, \varphi \rangle = \langle f, \tau_{-y} \varphi \rangle$. Then it must hold
$$
\widehat{(\tau_y f)}(\xi) = e^{-2\pi i \langle \xi, y \rangle} \hat{f}(\xi), \quad \forall y \in \mathbb{R}^n.
$$
:::