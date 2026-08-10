---
schema: qual/card@1
id: D-RA-WORKSHOP-D7-CONVERGENCE
kind: definition
title: 'Pointwise and uniform convergence of function sequences and series'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.definition title="Convergence of function sequences and series"}
For a sequence of functions $\{f_n\}$ where $f_n,f:E\to\mathbb R$ for all $n$:

1. $f_n\to f$ pointwise if $\lim_{n\to\infty}f_n(x)=f(x)$ for each $x\in E$.

2. $f_n\to f$ uniformly if for every $\epsilon>0$ there exists $N\in\mathbb N$ such that $|f_n(x)-f(x)|<\epsilon$ for all $n\ge N$ and all $x\in E$.
   That is, $f_n\to f$ uniformly provided $\|f_n-f\|_\infty\to0$.

3. $\sum_{n=1}^{\infty}f_n(x)\to f(x)$ provided the partial sums $\sum_{n=1}^{N}f_n(x)$ converge pointwise to $f$ as $N\to\infty$.

4. $\sum_{n=1}^{\infty}f_n(x)\to f(x)$ uniformly provided the partial sums $\sum_{n=1}^{N}f_n(x)$ converge uniformly to $f$ as $N\to\infty$.
:::
