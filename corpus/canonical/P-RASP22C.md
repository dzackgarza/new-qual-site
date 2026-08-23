---
schema: qual/card@1
id: P-RASP22C
kind: problem
title: "Exponential averaging in one variable kills L^1 functions"
classification:
  areas:
  - real-analysis
  topics:
  - Fubini Theorem
  - L1 Convergence
relations: []
review: draft
solved: false
---

::: problem
Let $f \in L^1((0, \infty) \times \mathbb{R})$ and for $n \in \mathbb{N}$ define $g_n : \mathbb{R} \to \mathbb{R}$ by the formula
$$
g_n(x) = \int_0^\infty e^{-\lambda} f(n\lambda, x) \, d\lambda.
$$
Prove that $g_n$ converges to $0$ almost-everywhere and in $L^1(\mathbb{R})$.
:::