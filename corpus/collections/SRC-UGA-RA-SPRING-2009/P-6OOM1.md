---
schema: qual/card@1
id: P-6OOM1
kind: problem
title: '$\lim_{k\to\infty}\int_0^1 kx^{k-1}f(x)\,dx=f(1)$ for continuous $f$'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Approximations to the Identity
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
  note: 'Split from P-4FH62, where it was part (o).'
---

::: {.problem}
Let $f : [0,1] \to \RR$ be continuous. Evaluate
$$
\lim_{k\to\infty} \int_0^1 kx^{k-1}f(x)\,dx.
$$
:::

::: {.solution}

::: pf

::: pf-step

The limit is $\boxed{f(1)}$.

::: pf-proof

Since $\int_0^1kx^{k-1}\,dx=1$,
$$
k\int_0^1x^{k-1}f(x)\,dx-f(1)
=k\int_0^1x^{k-1}(f(x)-f(1))\,dx.
$$
Given $\varepsilon>0$, choose $a<1$ so that $\abs{f(x)-f(1)}<\varepsilon$ on $[a,1]$. The contribution from $[a,1]$ is at most $\varepsilon$. On $[0,a]$ it is at most $2\norm{f}_\infty a^k$, which tends to $0$.

:::

:::

:::

:::
