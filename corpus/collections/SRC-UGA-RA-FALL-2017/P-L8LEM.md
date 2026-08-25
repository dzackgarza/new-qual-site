---
schema: qual/card@1
id: P-L8LEM
kind: problem
title: $C_{\mathbb{R}}(X)$ is complete in the maximum norm when $X$ is compact metric
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Completeness
  - Norms
relations: []
review: draft
---

::: problem
Let $X$ be a compact metric space and equip the space $C_{\mathbb{R}}(X)$ of continuous functions from $X$ to $\mathbb{R}$ with the maximum norm
$$
\|f\|:=\max\{|f(x)|:x\in X\}.
$$
Prove that this norm is complete.
:::

::: {.solution}
The maximum exists for each $f\in C_{\mathbb{R}}(X)$ because $X$ is compact and $x\mapsto |f(x)|$ is continuous, so the expression is a genuine norm.

Let $\{f_n\}$ be Cauchy in this norm.
For each $x\in X$, $\{f_n(x)\}$ is Cauchy in $\mathbb{R}$, hence converges; define $f(x):=\lim_n f_n(x)$.
Given $\varepsilon>0$, choose $N$ so that $\|f_n-f_m\|<\varepsilon$ for all $n,m\ge N$.
Fixing $n\ge N$ and sending $m\to\infty$ yields $|f_n(x)-f(x)|\le\varepsilon$ for every $x$, so $\|f_n-f\|\to 0$.
Thus $f_n\to f$ uniformly, $f$ is continuous, and $f_n\to f$ in $C_{\mathbb{R}}(X)$.
:::
