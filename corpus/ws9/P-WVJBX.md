---
schema: qual/card@1
id: P-WVJBX
kind: problem
title: Suppose $\{f_n\}_{n=1}^\infty \subset L^2(\mathbb{R})$ is a sequence t…
classification:
  areas:
  - real-analysis
  topics:
  - l2
  - convergence-of-functions
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose $\{f_n\}_{n=1}^\infty \subset L^2(\mathbb{R})$ is a sequence that converges to $0$ in the $L^2$ norm; in other words, $$\|f_n\|_{L^2(\mathbb{R})} = \left(\int_{-\infty}^\infty |f_n|^2 dx\right)^{1/2} \to 0.$$ Prove that there exists a subsequence $\{f_{n_k}\}$ such that $f_{n_k} \to 0$ almost everywhere.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $\|f_n\|_{L^2} \to 0$ implies there is a subsequence with $f_{n_k} \to 0$ almost everywhere.

<1>1. Choose a subsequence with $\|f_{n_k}\|_{L^2} \le 2^{-k}$.
Proof: $\|f_n\|_2 \to 0$, so for each $k$ pick $n_k > n_{k-1}$ with $\|f_{n_k}\|_2 < 2^{-k}$.

<1>2. $\sum_k \|f_{n_k}\|_{L^2}^2 \le \sum_k 2^{-2k} < \infty$.
Proof: <1>1: geometric series.

<1>3. $\sum_k |f_{n_k}(x)|^2 < \infty$ for almost every $x$.
Proof: by the Monotone Convergence Theorem, $\int \sum_k |f_{n_k}|^2 = \sum_k \int |f_{n_k}|^2 = \sum_k \|f_{n_k}\|_2^2 < \infty$; hence the nonnegative integrand $\sum_k|f_{n_k}(x)|^2$ is finite a.e.

<1>4. $f_{n_k}(x) \to 0$ for almost every $x$.
Proof: <1>3: the terms of the convergent series $\sum_k |f_{n_k}(x)|^2$ tend to $0$, so $|f_{n_k}(x)|^2 \to 0$ (hence $f_{n_k}(x) \to 0$) for a.e. $x$.

<1>5. Q.E.D. Proof: <1>1–<1>4 prove the claim (the standard "convergence in $L^p$ implies a.e. convergence along a subsequence" via the Borel–Cantelli/MCT route).
:::
