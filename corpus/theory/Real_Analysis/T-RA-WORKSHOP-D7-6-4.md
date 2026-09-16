---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-4
kind: theorem
title: Uniform convergence of derivatives and differentiability of the limit
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Differentiation
  - Convergence of Functions
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, and let $f_n\colon[a,b]\to\RR$ for $n\geq1$ be differentiable on $[a,b]$.
Suppose that $\{f_n(x_0)\}$ converges for some $x_0\in[a,b]$ and that $\{f_n'\}$ converges [[D-RA-WORKSHOP-D7-CONVERGENCE|uniformly]] on $[a,b]$.
Then $\{f_n\}$ converges uniformly on $[a,b]$ to a function $f\colon[a,b]\to\RR$, $f$ is differentiable on $[a,b]$, and
$$
f'(x)=\lim_{n\to\infty}f_n'(x)\qquad\text{for all }x\in[a,b].
$$
:::
