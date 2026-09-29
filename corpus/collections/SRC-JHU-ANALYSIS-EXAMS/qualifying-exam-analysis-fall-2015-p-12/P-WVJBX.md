---
schema: qual/card@1
id: P-WVJBX
kind: problem
title: 'A sequence converging to $0$ in $L^2$ has a subsequence converging almost everywhere'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations:
- kind: variant-of
  target: P-8XT26
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
1. Suppose $\{ f _ { n } \} _ { n = 1 } ^ { \infty } \subset L ^ { 2 } ( \mathbb { R } )$ is a sequence that converges to 0 in the $L ^ { 2 }$ norm; in other words,

$$
| | f _ { n } | | _ { L ^ { 2 } ( \mathbb { R } ) } = \left( \int _ { - \infty } ^ { \infty } | f _ { n } | ^ { 2 } \ d x \right) ^ { \frac { 1 } { 2 } } \to 0 .
$$

Prove that there exists a subsequence $\{ f _ { n _ { k } } \}$ such that $f _ { n _ { k } } \to 0$ almost everywhere.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a subsequence with $\sum_k\int\abs{f_{n_k}}^2<\infty$.

::: pf-proof

Since $\norm{f_n}_2\to0$, choose $n_1<n_2<\cdots$ with $\norm{f_{n_k}}_2\le2^{-k}$; then $\sum_k\norm{f_{n_k}}_2^2\le\sum_k4^{-k}<\infty$.

:::

:::

::: pf-qed

By the monotone convergence theorem and step [](#s1){.pf-ref}, $\int\sum_k\abs{f_{n_k}}^2=\sum_k\int\abs{f_{n_k}}^2<\infty$, so $\sum_k\abs{f_{n_k}(x)}^2<\infty$ for almost every $x$. For such $x$ the terms tend to $0$, so $f_{n_k}(x)\to0$.

:::

:::

:::
