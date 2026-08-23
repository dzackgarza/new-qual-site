---
schema: qual/card@1
id: P-RASP17H
kind: problem
title: "Smoothness of the Fourier transform of a compactly supported L^2 function; Arzela-Ascoli extraction"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L2 Spaces
  - Arzela-Ascoli Theorem
relations: []
review: draft
solved: false
---

::: problem
Suppose that $f \in L^2(\mathbb{R}, m)$ is a function such that $f(x) = 0$ if $|x| \geq 1$.

1. Show $\hat{f} \in C^\infty(\mathbb{R}, \mathbb{C})$ and
$$
\sup_{k \in \mathbb{R}} |\hat{f}^{(\ell)}(k)| \leq \frac{1}{\sqrt{2\pi}} \sqrt{\frac{2}{2\ell + 1}} \|f\|_2 \quad \forall \ell = 0, 1, 2, \ldots
$$

2. Let $\{f_n\}_{n=1}^\infty \subset L^2(\mathbb{R}, m)$ satisfy $\|f_n\|_2 \leq 1$ and $f_n(x) = 0$ for $|x| \geq 1$.
   Show that for each $0 < M < \infty$ there exists $1 \leq n_1 < n_2 < n_3 < \ldots$ in $\mathbb{N}$ such that $\{\hat{f}_{n_k}\}_{k=1}^\infty$ is uniformly convergent on $[-M, M]$ to some $g \in C([-M, M], \mathbb{C})$.
:::
