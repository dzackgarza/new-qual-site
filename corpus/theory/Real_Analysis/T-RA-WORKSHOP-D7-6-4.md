---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-4
kind: theorem
title: Uniform convergence of derivatives and differentiability of the limit
slogan: 'If $(f_n^\prime)$ converges uniformly and $(f_n(x_0))$ converges, then $f_n\to f$ uniformly, $f$ is differentiable, and $f^\prime=\lim f_n^\prime$.'
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
Suppose that $\{f_n(x_0)\}$ converges for some $x_0\in[a,b]$ and that $\{f_n'\}$ converges [[D-YZC3C|uniformly]] on $[a,b]$.
Then $\{f_n\}$ converges uniformly on $[a,b]$ to a function $f\colon[a,b]\to\RR$, $f$ is differentiable on $[a,b]$, and
$$
f'(x)=\lim_{n\to\infty}f_n'(x)\qquad\text{for all }x\in[a,b].
$$
[@Rud76].
:::

::: {.remark title="Variations"}
Term-by-term differentiation of a series: if $f_n\colon[a,b]\to\RR$ are differentiable, $\sum_{n=1}^\infty f_n'$ converges uniformly on $[a,b]$ to $g$, and $\sum_{n=1}^\infty f_n(x_0)$ converges for some $x_0\in[a,b]$, then $\sum_{n=1}^\infty f_n$ converges uniformly on $[a,b]$ to a differentiable $f$ with $f'=g$ [@Abb16].
The theorem applies unchanged to the partial sums $S_N\coloneqq\sum_{n=1}^N f_n$, whose derivatives are $S_N'=\sum_{n=1}^N f_n'$.
:::
