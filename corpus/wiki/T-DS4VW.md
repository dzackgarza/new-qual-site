---
schema: qual/card@1
id: T-DS4VW
kind: theorem
title: Term by Term Differentiability Theorem
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Differentiation
  - Uniform Convergence
relations: []
review: draft
---

:::{.theorem title="Term by Term Differentiability Theorem"}
If $\ts{f_n}$ is a sequence of functions where

- each $f_n$ is differentiable, 
- there is some $G$ such that $\norm{ \sum_{n\leq N} f_n' - G}_\infty \convergesto{N\to\infty} 0$, and 
- there exists at least *one point*[^pointwise_works_too] $x_0$ such that $\sum f_n(x)$ converges (pointwise), 

then there exists an $F$ such that 
[^theorem_referfence_6.4.3_Abbott]
\[
\norm{ \sum_{n\leq N} f_n - F}_\infty \convergesto{N\to\infty} 0 && F' = g
.\]

:::

[^pointwise_works_too]: So this implicitly holds if $f$ is the pointwise limit of $f_n$.

[^theorem_referfence_6.4.3_Abbott]: See Abbott theorem 6.4.3, pp 168.
