---
schema: qual/card@1
id: P-MMAQ-TLAEWGH2QZ
kind: problem
title: Let $(X, \mathcal M, \mu)$ be a measure space. For $f\in L^1(\mu)$…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - l1
relations: []
review: draft
---

::: problem
Let $(X, \mathcal M, \mu)$ be a measure space. For $f\in L^1(\mu)$ and $\lambda > 0$, define
$$
\phi(\lambda)=\mu(\{x \in X | f(x)>\lambda\}) 
\quad \text { and } \quad 
\psi(\lambda)=\mu(\{x \in X | f(x)<-\lambda\})
$$

Show that $\phi, \psi$ are Borel measurable and
$$
\int_{X}|f| ~d \mu=\int_{0}^{\infty}[\phi(\lambda)+\psi(\lambda)] ~d \lambda
$$
:::
