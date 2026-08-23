---
schema: qual/card@1
id: P-RASP20E
kind: problem
title: "Absolute Fourier coefficient bound via integration by parts"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Series
  - Cauchy-Schwarz Inequality
  - Integration by Parts
relations: []
review: draft
solved: false
---

::: problem
Let $f \in C^1(\mathbb{T})$.
Let $\hat{f}(k)$ ($k \in \mathbb{Z}$) be the Fourier coefficients of $f$.
Prove that
$$
\sum_{k=-\infty}^\infty |\hat{f}(k)| \leq \|f\|_{L^1(\mathbb{T})} + \frac{1}{\sqrt{2\pi}} \left( \sum_{k=1}^\infty \frac{1}{k^2} \right)^{1/2} \|f'\|_{L^2(\mathbb{T})}.
$$
:::
