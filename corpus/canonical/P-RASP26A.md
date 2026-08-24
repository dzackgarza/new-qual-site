---
schema: qual/card@1
id: P-RASP26A
kind: problem
title: "Equi-integrability and strong L^1 convergence"
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
Let $(\Omega, \mathcal{M}, \mu)$ be a measure space. A sequence $(f_n)_n \subset L^1(\Omega, \mu)$ is equi-integrable if:

(a) for every $\epsilon > 0$ there is a $\delta > 0$ such that $\sup_n \int_E |f_n|\,d\mu < \epsilon$ for all $E \in \mathcal{M}$ with $\mu(E) < \delta$;

(b) for every $\epsilon > 0$ there is $A_\epsilon \in \mathcal{M}$ with $\mu(A_\epsilon) < +\infty$ and $\sup_n \int_{\Omega \setminus A_\epsilon} |f_n|\,d\mu < \epsilon$.

(1) Show that if $(f_n)_n$ is equi-integrable and $f_n \to f$ $\mu$-a.e., then $f \in L^1(\Omega, \mu)$ and $f_n \to f$ strongly in $L^1$.

(2) Show that if $(f_n)_n$ converges strongly in $L^1$ then condition (a) holds.
:::
