---
schema: qual/card@1
id: P-1FPTH
kind: problem
title: '$\int_0^1 f^{1/n}\to m\{f>0\}$ for nonnegative integrable $f$'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Measure Theory
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
  note: 'Split from P-4FH62, where it was part (m).'
---

::: {.problem}
If $f$ is nonnegative and integrable on $[0,1]$, then $\lim_{n\to\infty} \int_0^1 \sqrt[n]{f} = m\theset{x \st f(x) > 0}$.
:::

::: {.solution}

::: pf

::: pf-step

For integrable $f\ge0$ on $[0,1]$, $\lim_{n\to\infty}\int_0^1 f^{1/n}=m\theset{f>0}$.

::: pf-proof

Pointwise, $f(x)^{1/n}\to\mathbf1_{\theset{f>0}}(x)$. Also $t^{1/n}\le1+t$ for $t\ge0$, so $f^{1/n}\le1+f\in L^1([0,1])$. The dominated convergence theorem gives
$$
\lim_{n\to\infty}\int_0^1 f(x)^{1/n}\,dx
=m\theset{x \st f(x)>0}.
$$

:::

:::

:::

:::
