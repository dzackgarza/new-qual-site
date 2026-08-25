---
schema: qual/card@1
id: P-JHUFA10RA1
kind: problem
title: L2 convergence with Gaussian weight
classification:
  areas:
  - real-analysis
  topics:
  - L^p Spaces
relations: []
review: draft
---

Suppose that $f_j \in L^2(\mathbb{R}^n)$, $j = 1, 2, 3, \ldots$ and that $f_j \to f$ in $L^2$.
Suppose further that there is a constant $M < \infty$ so that

$$\int e^{100|x|^2} |f_j(x)|^2 \, dx \leq M, \quad j = 1, 2, 3, \ldots.$$

Is it true that $\int e^{99|x|^2} |f(x)|^2 \, dx < \infty$?
Give a proof or counterexample.
