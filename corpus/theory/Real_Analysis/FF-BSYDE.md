---
schema: qual/card@1
id: FF-BSYDE
kind: fact
title: Compact operators
prompts:
- What is a compact operator?
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Compactness
relations: []
review: draft
---

::: {.fact}
Let $X$ and $Y$ be normed vector spaces.
A linear map $T\colon X\to Y$ is \dfn{compact} if $T(B)$ has compact closure in $Y$ for every bounded subset $B\subseteq X$.
:::

::: {.fact}
Every compact linear map $T\colon X\to Y$ between normed vector spaces is bounded.
:::

::: {.proof}
The closure of $T(\theset{x\in X\suchthat\norm{x}\leq 1})$ is compact, hence bounded, so $\sup_{\norm{x}\leq 1}\norm{Tx}<\infty$.
:::

::: {.fact}
Let $H$ be a [[D-7QQUO|Hilbert space]].
The set of compact operators $H\to H$ is the closure, in the operator norm, of the set of bounded operators $H\to H$ of finite rank.
:::
