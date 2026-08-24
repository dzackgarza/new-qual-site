---
schema: qual/card@1
id: P-RASP26F
kind: problem
title: "Compactness of uniformly tight L^2 sequences via Fourier concentration"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $f_k \in L^2(\mathbb{R}^n)$ and $\|f_k\|_2 \leq 1$ for each $k = 1, 2, \ldots$, and assume that
$$
\lim_{R \to \infty} \sup_{k \geq 1} \int_{\mathbb{R}^n \setminus B_R(0)} (|f_k(x)|^2 + |\hat{f}_k(x)|^2)\,dx = 0
$$
with $B_R(0)$ the ball of radius $R$ centered at the origin.
Show that $\{f_k\}_{k \geq 1}$ has a convergent subsequence in $L^2(\mathbb{R}^n)$.
:::
