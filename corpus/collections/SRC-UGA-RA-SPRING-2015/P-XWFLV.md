---
schema: qual/card@1
id: P-XWFLV
kind: problem
title: 'Sequential characterization of continuity between metric spaces'
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Continuity
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
  note: 'Split from P-4FH62, where it was part (d).'
---

::: {.problem}
Let $(X,d)$ and $(Y,\rho)$ be metric spaces, $f : X \to Y$, and $x_0 \in X$. Prove that the following statements are equivalent:

1. For every $\varepsilon > 0$ there is $\delta > 0$ such that $\rho(f(x), f(x_0)) < \varepsilon$ whenever $d(x, x_0) < \delta$.
2. The sequence $\theset{f(x_n)}_{n=1}^\infty \to f(x_0)$ for every sequence $\theset{x_n} \to x_0$ in $X$.
:::

::: {.solution}

::: pf

::: pf-step

$f$ is continuous at $x_0$ if and only if $f(x_n)\to f(x_0)$ for every sequence $x_n\to x_0$.

::: pf-proof

If $f$ is continuous at $x_0$ and $x_n\to x_0$, then given $\varepsilon > 0$ and its $\delta$, $d(x_n, x_0) < \delta$ for all large $n$, so $\rho(f(x_n), f(x_0)) < \varepsilon$ for all large $n$. Conversely, if continuity fails, there is $\varepsilon_0>0$ such that for every $n$ there is $x_n$ with $d(x_n,x_0)<1/n$ but $\rho(f(x_n),f(x_0))\ge\varepsilon_0$. Then $x_n\to x_0$ while $f(x_n)\not\to f(x_0)$.

:::

:::

:::

:::
