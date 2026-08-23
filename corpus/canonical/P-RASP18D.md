---
schema: qual/card@1
id: P-RASP18D
kind: problem
title: "Riemann-Lebesgue lemma for derivatives of dilated functions"
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
Let $\varphi : \mathbb{R} \to \mathbb{R}$ be a $C^1$-function such that $M := \sup_{x \in \mathbb{R}} [|\varphi(x)| + |\varphi'(x)|] < \infty$.

1. If $f \in C_c^1(\mathbb{R})$, show
$$
\left|\int_{\mathbb{R}} f(x) \varphi'(\lambda x)\,dx\right| \leq M \cdot \|f'\|_{L^1(\mathbb{R}, m)} |\lambda|^{-1} \quad \text{for all } \lambda > 0.
$$

2. If $f \in L^1(\mathbb{R}, m)$, show
$$
\lim_{\lambda \to \infty} \int_{\mathbb{R}} f(x) \varphi'(\lambda x)\,dx = 0.
$$
:::
