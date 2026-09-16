---
schema: qual/card@1
id: T-F2THV
kind: theorem
title: Uniform boundedness principle
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a [[D-BG455|Banach space]], let $Y$ be a normed vector space, and let $(T_\alpha)_{\alpha\in A}$ be a family of bounded linear operators $T_\alpha\colon X\to Y$.
Suppose the family is pointwise bounded: for every $x\in X$ there exists $C_x\geq0$ such that
$$
\norm{T_{\alpha}x} \leq C_x \quad\text{for all } \alpha\in A .
$$
Then the family is uniformly bounded in operator norm: there exists $C\geq0$ such that
$$
\norm{T_\alpha x}\leq C\norm{x} \quad\text{for all } \alpha\in A \text{ and all } x\in X,
$$
that is, $\sup_{\alpha\in A}\norm{T_\alpha}<\infty$ [@Fol13].
:::
