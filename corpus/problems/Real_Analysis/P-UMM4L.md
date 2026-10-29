---
schema: qual/card@1
id: P-UMM4L
kind: problem
title: 'A uniformly convergent series of step functions that fails the Weierstrass M-test'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Counterexamples
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
  note: 'Split from P-4FH62, where it was part (f).'
---

::: {.problem}
Let
$$
f_n(x) = \begin{cases} \frac{1}{n} & x \in \left(\frac{1}{2^{n+1}}, \frac{1}{2^n}\right] \\ 0 & \text{otherwise.} \end{cases}
$$
Show that $\sum_{n=1}^\infty f_n$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on $\RR$.
:::

::: {.solution}

::: pf

::: pf-step

$\sum_n\norm{f_n}_\infty=\infty$, but $\sum_n f_n$ converges uniformly on $\RR$.

::: pf-proof

$\norm{f_n}_\infty=1/n$ and $\sum_n1/n=\infty$, so the M-test does not apply. The supports are pairwise disjoint, so at each $x$ at most one term is nonzero. Therefore
$$
\sup_x\abs{\sum_{n>N}f_n(x)}\le\frac1{N+1}\to0,
$$
so the series converges uniformly.

:::

:::

:::

:::
