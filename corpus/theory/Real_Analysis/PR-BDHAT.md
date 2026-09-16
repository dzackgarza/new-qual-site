---
schema: qual/card@1
id: PR-BDHAT
kind: proposition
title: Uniformly continuous $L^1$ functions vanish at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - L¹
  - Limits
relations: []
review: draft
---

::: {.proposition}
Let $f\colon\RR^n\to\CC$ be [[D-HHVPT|uniformly continuous]] with $f\in L^1(\RR^n)$.
Then $f(x) \to 0$ as $\abs{x}\to \infty$.
:::

::: {.proof}
Suppose not.
Then there exist $\varepsilon>0$ and points $x_k\in\RR^n$ with $\abs{x_k}\to\infty$ and $\abs{f(x_k)}\geq\varepsilon$ for all $k$.
By uniform continuity, choose $\delta>0$ such that $\abs{x-y}<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon/2$; then $\abs{f}\geq\varepsilon/2$ on each ball $B(x_k,\delta)$.
Passing to a subsequence, we may assume $\abs{x_{k+1}}\geq\abs{x_k}+2\delta$, so the balls $B(x_k,\delta)$ are pairwise disjoint.
Hence
$$
\int_{\RR^n}\abs{f}\geq\sum_{k}\int_{B(x_k,\delta)}\abs{f}\geq\sum_k\frac{\varepsilon}{2}\vol\qty{B(0,\delta)}=\infty,
$$
contradicting $f\in L^1(\RR^n)$.
:::
