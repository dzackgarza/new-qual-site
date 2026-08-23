---
schema: qual/card@1
id: P-RAF22C
kind: problem
title: "High-frequency parity oscillations integrate to zero against any L^1 function"
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Density Arguments
  - Oscillatory Integrals
relations: []
review: draft
solved: false
---

::: problem
Set $E = \bigcup_{m \in \mathbb{Z}} [2m, 2m+1)$ and $P = \chi_E - \chi_{\mathbb{R} \setminus E}$, so that $P(x)$ is $1$ if the greatest integer less than or equal to $x$ is even and is $-1$ if it is odd. Define $S_n(x) = P(10^n x)$. Prove that for every $f \in L^1(\mathbb{R})$
$$
\int_\mathbb{R} S_n(x) f(x) \, dx \to 0 \quad \text{as } n \to \infty.
$$
:::