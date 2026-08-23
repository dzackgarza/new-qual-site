---
schema: qual/card@1
id: P-RASP11E
kind: problem
title: "Carleson's theorem: Fourier partial sums converge a.e."
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
Let $f \in L^2([0, 2\pi])$, and set $S_N f(x) = \sum_{n=-N}^{N} \hat{f}(n) e^{inx}$ to be the $N$th symmetric partial sum of its Fourier series.
Here $\hat{f}(n) = (2\pi)^{-1} \int_0^{2\pi} e^{-inx} f(x)\,dx$.
Show that there exists a subsequence $N_k \to \infty$ so that $S_{N_k} f \to f$ a.e. with respect to Lebesgue measure on $[0, 2\pi]$.
:::
