---
schema: qual/card@1
id: P-RASP22A
kind: problem
title: "True/false on integral inequalities, L^2 convergence, and Radon measures"
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
Determine if each of the following statements is true or false.

1. If $f, g : \mathbb{R} \to \mathbb{R}$ belong to $L^1(\mathbb{R})$ and satisfy $\int_{-\infty}^{x} f(t)\,dt \leq \int_{-\infty}^{x} g(t)\,dt$ for all $x \in \mathbb{R}$, then $f \leq g$ almost everywhere.

2. Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and let $f_n \in L^2(X)$ be a sequence.
   If $\sup_{n \in \mathbb{N}} \|f_n\|_2 < \infty$ and $f_n \to f$ almost everywhere, then $\int_X f_n\,d\mu \to \int_X f\,d\mu$.

3. Let $\mu$ be a Radon measure on an LCH space $X$ and let $A$ be an open subset of $X$.
   Define $\mu_A(E) = \mu(A \cap E)$.
   Then $\mu_A$ is a Radon measure.
:::
