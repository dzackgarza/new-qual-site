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
solved: true
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

::: {.solution}
> **AI-Generated Solution**

<1>1. By Plancherel, $\|f_n\|_{L^2} = \|\hat f_n\|_{\ell^2}$ (up to the convention constant), where $\hat f_n(\xi) = \int_0^1 f_n(x)e^{2\pi i \xi x}\,dx$, $\xi \in \ZZ$.
    Proof: Plancherel's identity on $L^2([0,1])$ with the exponentials $\{e^{2\pi i \xi x}\}_{\xi \in \ZZ}$ an orthonormal basis.

<1>2. The supports of $\hat f_n$ and $\hat f_m$ are disjoint for $|n - m| \ge 2$; for $|n - m| = 1$ they meet only at the common endpoint $\xi = 2^{n+1}$.
    Proof: the intervals $[2^n, 2^{n+1}]$ and $[2^m, 2^{m+1}]$ are disjoint for $|n - m| \ge 2$, and adjacent intervals share exactly the endpoint.

<1>3. For $|n - m| \ge 2$: $\langle \hat f_n, \hat f_m\rangle = 0$; for adjacent indices, $|\langle \hat f_n, \hat f_{n+1}\rangle| \le \|\hat f_n\|_2\|\hat f_{n+1}\|_2$.
    Proof: disjoint supports give a vanishing inner product by <1>2; the adjacent bound is Cauchy–Schwarz.

<1>4. For $N < M$: $\left\|\sum_{n=N}^{M} f_n\right\|_2^2 = \sum_{n=N}^{M}\|\hat f_n\|_2^2 + 2\sum_{n=N}^{M-1}\mathrm{Re}\langle \hat f_n, \hat f_{n+1}\rangle \le \sum_{n=N}^{M}\|f_n\|_2^2 + 2\sum_{n=N}^{M-1}\|f_n\|_2\|f_{n+1}\|_2$.
    Proof: expand the squared norm via Plancherel (<1>1); cross terms between non-adjacent indices vanish by <1>3, and the adjacent cross terms are bounded by <1>3.

<1>5. The tails of both sums tend to $0$ as $N \to \infty$.
    <2>1. $\sum_{n=N}^{\infty}\|f_n\|_2^2 \le \sum_{n=N}^{\infty} n^{-51/50} \to 0$.
        Proof: $\|f_n\|_2 \le n^{-51/100}$, and $\sum_n n^{-51/50} < \infty$ since $51/50 > 1$.
    <2>2. $\sum_{n=N}^{\infty}\|f_n\|_2\|f_{n+1}\|_2 \le \sum_{n=N}^{\infty} n^{-51/100}(n+1)^{-51/100} \le \sum_{n=N}^{\infty} n^{-51/50} \to 0$.
        Proof: $(n+1)^{-51/100} \le n^{-51/100}$, and <2>1.

<1>6. Q.E.D.
    Proof: <1>4 and <1>5 show $\left\|\sum_{n=N}^{M}f_n\right\|_2^2 \to 0$ as $N \to \infty$ uniformly in $M > N$, i.e. the partial sums are Cauchy in the complete space $L^2([0,1])$; hence $\sum_n f_n$ converges in $L^2$.
:::
