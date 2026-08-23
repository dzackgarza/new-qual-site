---
schema: qual/card@1
id: P-RAF11C
kind: problem
title: "Uniform integrability and convergence in L^1"
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
(a) Let $(X, \mathcal{M}, \mu)$ be a finite measure space. Suppose that $f_n \in L^1(d\mu)$ is a sequence of functions with the property that for every $\epsilon > 0$ there exists a $\delta > 0$ such that for all $E \in \mathcal{M}$:
$$
|E| < \delta \implies \sup_n \int_E |f_n|\,d\mu < \epsilon.
$$
Suppose in addition that there exists $f$ with $f_n \to f$ $\mu$-a.e. Show that $f_n \to f$ in $L^1(d\mu)$.

(b) Give a simple example to show that if one drops the finite measure assumption but keeps all the other hypotheses above, the conclusion can fail.
:::
