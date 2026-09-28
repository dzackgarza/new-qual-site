---
schema: qual/card@1
id: E-BPSOU
kind: problem
title: Entire $O(|z|^p)$ functions are polynomials of degree at most $\lfloor p\rfloor$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise} 
Show that if $f$ is entire and $\abs{f(z)} \in \bigo(\abs{z}^p)$ for $\abs{z}$ sufficiently large, then $f$ is a polynomial of degree at most $\floor{p}$.

:::

::: {.solution}
Write $f(z)=\sum_{k\geq0}c_kz^k$, and choose $C$ and $R_0$ with $\abs{f(\xi)}\le C\abs\xi^p$ for $\abs\xi\ge R_0$. For $R\ge R_0$, Cauchy's integral formula for $c_k=f^{(k)}(0)/k!$ gives
\[
\abs{c_k} 
&\leq {1\over 2\pi}\int_{\abs{\xi} = R} {\abs{f(\xi)} \over \abs{\xi}^{k+1}}\abs{\dxi}\\
&\leq {1 \over 2\pi}\int_{\abs \xi = R}{ C\abs{\xi}^{p} \over \abs{\xi}^{k+1} }\abs{\dxi} \\
&= {C \over 2\pi} {1\over R^{k+1-p}} \cdot 2\pi R \\
&= C R^{p-k}
,\]
which converges to $0$ as $R\to \infty$ provided that $k>p$.
So every coefficient $c_k$ with $k> p$, that is, $k\geq \floor{p}+1$, vanishes, and $f$ is a polynomial of degree at most $\floor p$.
:::
