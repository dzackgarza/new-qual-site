---
schema: qual/card@1
id: P-G7GOP
kind: problem
title: '$\sum_k x^k/(1+x^k)$ converges uniformly on each $[0,a]$, $a<1$, to a differentiable function'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (g).'
---

::: {.problem}
Let $f_n : [0,1) \to \RR$ be the function defined by
$$
f_n(x) \coloneqq \sum_{k=1}^n \frac{x^k}{1+x^k}.
$$

1. Prove that $f_n$ converges to a function $f : [0,1) \to \RR$.

2. Prove that for every $0 < a < 1$ the convergence is uniform on $[0,a]$.

3. Prove that $f$ is differentiable on $(0,1)$.
:::

::: {.solution}

::: pf

::: pf-step

$\sum_{k\ge1}x^k/(1+x^k)$ converges on $[0,1)$, uniformly on each $[0,a]$ with $a<1$, and its sum is differentiable on $(0,1)$.

::: pf-proof

For fixed $x<1$,
$$
0\le \frac{x^k}{1+x^k}\le x^k,
$$
so the series converges. On every $[0,a]$ with $a<1$, the bound by $a^k$ gives uniform convergence by the M-test. Moreover
$$
\left(\frac{x^k}{1+x^k}\right)'=\frac{kx^{k-1}}{(1+x^k)^2},
$$
and on $[0,a]$ this is bounded by $ka^{k-1}$, whose series converges. So the series of derivatives converges uniformly on each $[0,a]$, termwise differentiation is valid there, and the sum is differentiable on $(0,1)$.

:::

:::

:::

:::
