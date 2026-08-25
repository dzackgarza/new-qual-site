---
schema: qual/card@1
id: P-RAF22B
kind: problem
title: "In L^p on a finite measure space, pointwise convergence gives: norm convergence iff norms converge"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Pointwise Convergence
  - Vitali Convergence Theorem
relations: []
review: draft
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $1 \leq p < \infty$, let $f, f_n \in L^p(X, \mu)$ for $n \in \mathbb{N}$, and assume that $f_n \to f$ pointwise $\mu$-almost-everywhere.
Prove that $\|f_n - f\|_p \to 0$ if and only if $\|f_n\|_p \to \|f\|_p$.

(Note: You are not allowed to use the generalized Dominated Convergence Theorem unless you prove it.)
:::
