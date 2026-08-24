---
schema: qual/card@1
id: P-RASP20E
kind: problem
title: "Absolute convergence of Fourier series of C^1 function"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $f \in C^1(\mathbb{T})$.
Let $\hat{f}(k)$ ($k \in \mathbb{Z}$) be the Fourier coefficients of $f$.
Prove that
$$
\sum_{k=-\infty}^{\infty} |\hat{f}(k)| \leq \|f\|_{L^1(\mathbb{T})} + \frac{1}{\sqrt{2}\pi}\|f'\|_{L^2(\mathbb{T})} \sqrt{\sum_{k=1}^{\infty} \frac{1}{k^2}}.
$$
:::
