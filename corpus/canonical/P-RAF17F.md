---
schema: qual/card@1
id: P-RAF17F
kind: problem
title: "Triple convolution equation implies vanishing"
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
Suppose $\lambda \in \mathbb{C}$ and $f \in L^1(m) = L^1(\mathbb{R}, m)$ satisfies $f * f * f(x) = \lambda f * f(x)$ for $m$-a.e. $x$. Show $f(x) = 0$ for $m$-a.e. $x$.

Recall that $\|f * g\|_{L^1(m)} \leq \|f\|_{L^1(m)} \|g\|_{L^1(m)}$ for all $f, g \in L^1(m)$ and therefore $f * f$ and $f * f * f$ are still in $L^1(m)$.
:::
