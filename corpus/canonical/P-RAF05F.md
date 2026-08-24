---
schema: qual/card@1
id: P-RAF05F
kind: problem
title: "Distribution function convergence and integral representation for monotone limits"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Distribution Functions
  - Monotone Convergence
  - Layer Cake Representation
relations: []
review: draft
solved: false
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and $0 \leq f_1 \leq f_2 \leq \cdots \leq f$ be nonnegative measurable functions on $X$ with $\lim f_j(x) = f(x)$ for almost every $x \in X$.

(a) Prove that $\mu(f_j^{-1}((r, \infty])) \to \mu(f^{-1}((r, \infty)))$ as $j \to \infty$ for every $r \geq 0$, $r \in \mathbb{R}$.

(b) Prove that $\int_X f \, d\mu = \int_0^\infty \mu(f^{-1}((r, \infty))) \, dr$.
:::
