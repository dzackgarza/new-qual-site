---
schema: qual/card@1
id: P-JHUU45RA1
kind: problem
title: Convergence of step-function approximations in L1
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

Let $I = [0,1]$ and for $n \in \mathbb{N}$, consider $0 \leq j \leq 2^n - 1$.
Define

$$I_{nj} = [j 2^{-n}, (j+1) 2^{-n}].$$

Let $f \in L^1(I)$ and define

$$E_n(f)(x) = \sum_{j=0}^{2^n - 1} \left( 2^n \int_{I_{nj}} f \, dt \right) \chi_{I_{nj}}(x).$$

Prove that $\lim_{n \to \infty} E_n(f)(x) = f(x)$ a.e. in $I$.
