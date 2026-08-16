---
schema: qual/card@1
id: P-Y4YM6
kind: problem
title: "Let \\( f_n \\in L^2([0, 1]) \\) for \\( n\\in \\NN \\), and assume that \\( \\norm{f_n}_2 \\leq n^{-51 \\over 100} \\) for all \\( n\\in \\NN \\), $\\hat{f}_n$ is supported in the\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - l2
  - hilbert-spaces
  - series-of-functions
relations: []
review: draft
---

::: problem
Let \( f_n \in L^2([0, 1]) \) for \( n\in \NN \), and assume that 

- \( \norm{f_n}_2 \leq n^{-51 \over 100} \)  for all \( n\in \NN \),

- $\hat{f}_n$ is supported in the interval $[2^n, 2^{n+1}]$, so
\[
\hat{f}_n(\xi) \da \int_0^1 f_n(x) e^{2\pi i \xi \cdot x} \dx = 0 && \text{for } \xi \not\in [2^n, 2^{n+1}]
.\]

Prove that \( \sum_{n\in \NN} f_n \) converges in the Hilbert space \( L^2([0, 1]) \).

> Hint: Plancherel's identity may be helpful.
:::
