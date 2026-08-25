---
schema: qual/card@1
id: P-RASP16F
kind: problem
title: "L^p boundedness plus L^1 convergence implies L^q convergence for q < p"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Interpolation
  - Uniform Integrability
relations: []
review: draft
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $1 < p < \infty$.
Suppose $f_k \in L^p(\mu)$ ($k = 1, 2, \ldots$) are such that $\sup_{k \geq 1} \|f_k\|_p < \infty$ and $f_k \to f$ in $L^1(\mu)$ for some $f \in L^1(\mu)$.
Prove that $f \in L^p(\mu)$ and $f_k \to f$ in $L^q(\mu)$ for any $q \in (1, p)$.
:::
