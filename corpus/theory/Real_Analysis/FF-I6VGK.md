---
schema: qual/card@1
id: FF-I6VGK
kind: fact
title: Implications among uniform, pointwise, almost everywhere, and $L^p$ convergence
prompts:
- How do uniform, pointwise, a.e. and norm convergence compare in strength?
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
relations: []
review: draft
---

::: {.fact}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1\leq p<\infty$, and let $f_n, f\colon X\to\CC$ be measurable.

1. If $f_n\to f$ [[D-YZC3C|uniformly]] on $X$, then $f_n\to f$ [[D-IYDZU|pointwise]] on $X$; if $f_n\to f$ pointwise on $X$, then $f_n\to f$ almost everywhere.

2. If $\mu(X)<\infty$, $f_n, f\in L^p(\mu)$, and $f_n\to f$ uniformly on $X$, then $f_n\to f$ in $L^p(\mu)$.

3. If $f_n\to f$ in $L^p(\mu)$, then some subsequence $(f_{n_k})$ converges to $f$ almost everywhere.
:::

::: {.example}
Without $\mu(X)<\infty$, uniform convergence does not imply $L^1$ convergence: $\frac1n\chi_{[0,n]}\to 0$ uniformly on $\RR$ with $\int_\RR\frac1n\chi_{[0,n]} = 1$ ([[FE-3RPMC]]).
Almost everywhere convergence does not imply $L^1$ convergence: $n\chi_{[0,1/n]}\to 0$ almost everywhere on $\RR$ with integral $1$ ([[FE-VT5N3]]).
:::

::: {.example}
$L^1$ convergence does not imply almost everywhere convergence.
Write each $n\geq 1$ uniquely as $n = 2^k + j$ with $k\geq 0$ and $0\leq j<2^k$, and let $f_n\coloneqq\chi_{[j2^{-k},\,(j+1)2^{-k}]}$ on $[0,1]$.
Then $\norm{f_n}_1 = 2^{-k}\to 0$, but for every $x\in[0,1]$ and every $k$ some $f_n$ with $2^k\leq n<2^{k+1}$ has $f_n(x) = 1$, and for $k\geq 2$ another has $f_n(x) = 0$, so $(f_n(x))$ diverges at every $x\in[0,1]$.
:::
