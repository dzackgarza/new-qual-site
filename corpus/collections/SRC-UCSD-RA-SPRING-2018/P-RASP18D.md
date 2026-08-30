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
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
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

::: {.solution}
<1>1. Integrate by parts: $\int f\varphi'(\lambda x)dx = -\lambda^{-1}\int f'(x)\varphi(\lambda x)dx$.
Proof: $u=f$, $dv=\varphi'(\lambda x)dx$.

<1>2. Bound by $M\|f'\|_1/\lambda$.
Proof: $|\varphi|\le M$.

<1>3. For $L^1$, approximate by $C_c^1$ and use density.
Proof: $C_c^1$ dense in $L^1$, uniform bound.

<1>4. Hence limit $0$.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
