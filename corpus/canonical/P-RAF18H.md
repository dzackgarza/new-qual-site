---
schema: qual/card@1
id: P-RAF18H
kind: problem
title: "Precompactness from Fourier decay"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $-\infty < a < b < \infty$, $C([a,b], \mathbb{R})$ be the Banach space of continuous functions on $[a,b]$ equipped with the supremum norm,
$$
\mathcal{F} := \left\{f \in L^1(\mathbb{R}, m) \cap C(\mathbb{R}, \mathbb{R}) : \int_{\mathbb{R}} (1 + |k|)\,|\hat{f}(k)|\,dk \leq 1\right\},
$$
and
$$
\mathcal{F}_{[a,b]} := \{f|_{[a,b]} : f \in \mathcal{F}\}.
$$
Show $\mathcal{F}_{[a,b]}$ is a precompact subset of $C([a,b], \mathbb{R})$.
:::
