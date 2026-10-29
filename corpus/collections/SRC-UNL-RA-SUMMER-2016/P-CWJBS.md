---
schema: qual/card@1
id: P-CWJBS
kind: problem
title: A compact metric space is complete and separable, and sequences with summable
  consecutive distances converge
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25

::: {.problem}
Assume $(X,d)$ is a compact metric space.

(a) Prove that $X$ is both complete and separable.

(b) Suppose $\{x_k\}_{k=1}^\infty \subseteq X$ is a sequence such that the series $\sum_{k=1}^\infty d(x_k, x_{k+1})$ converges.
Prove that the sequence $\{x_k\}_{k=1}^\infty$ converges in $X$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $X$ is complete and separable.

::: pf-proof

::: {.pf-step #complete}

$X$ is complete.

::: pf-proof

Let $(x_n)$ be a Cauchy sequence in $X$. A compact metric space is sequentially compact, so a subsequence $x_{n_k}$ converges to some $x \in X$. Given $\varepsilon > 0$, choose $N$ with $d(x_n, x_m) < \varepsilon/2$ for $n, m \ge N$, and choose $k$ with $n_k \ge N$ and $d(x_{n_k}, x) < \varepsilon/2$. Then $d(x_n, x) \le d(x_n, x_{n_k}) + d(x_{n_k}, x) < \varepsilon$ for $n \ge N$, so $x_n \to x$.

:::

:::

::: pf-step

$X$ is separable.

::: pf-proof

For each $m \in \NN$, the open cover $\{B(x, 1/m)\}_{x \in X}$ of the compact space $X$ has a finite subcover, with centres $x^{(m)}_1, \ldots, x^{(m)}_{N_m}$. The set $D = \bigcup_{m \in \NN}\{x^{(m)}_1, \ldots, x^{(m)}_{N_m}\}$ is a countable union of finite sets, hence countable. Given $x \in X$ and $\varepsilon > 0$, choose $m > 1/\varepsilon$ and $j$ with $x \in B(x^{(m)}_j, 1/m)$; then $d(x, x^{(m)}_j) < \varepsilon$. So $D$ is dense.

:::

:::

:::

:::

::: pf-step

(b) $(x_k)$ converges in $X$.

::: pf-proof

For $n < m$ the triangle inequality gives $d(x_n, x_m) \le \sum_{k=n}^{m-1} d(x_k, x_{k+1}) \le \sum_{k \ge n} d(x_k, x_{k+1})$. The right side is the tail of a convergent series, so it tends to $0$ as $n \to \infty$. Hence $(x_k)$ is Cauchy, and it converges because $X$ is complete by step [](#complete){.pf-ref}.

:::

:::

:::

:::
