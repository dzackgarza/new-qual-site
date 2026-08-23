---
schema: qual/card@1
id: P-RAF18A
kind: problem
title: "L^1 convergence from a.e. convergence with uniformly bounded running maxima"
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
Let $\{f_n\}_n \subset L^1(\mathbb{R}, m)$ be a sequence of functions such that $f_n \to 0$, $m$-almost everywhere.
Assume that there exists $M < \infty$ such that
$$
\int_{\mathbb{R}} \max(|f_1|, |f_2|, \ldots, |f_n|)\,dm \leq M, \quad \text{for every } n \geq 1.
$$
Prove that $\lim_{n \to \infty} \|f_n\|_1 = 0$.
:::
