---
schema: qual/card@1
id: P-DUKEBA14-11
kind: problem
title: Taylor expansion separates two logarithmic series
classification:
  areas: [real-analysis]
  topics: [Series, Taylor Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 5 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Use Taylor's theorem to prove that
$$
\sum_{k=1}^\infty \log(1+k^{-2/3})
$$
diverges, while
$$
\sum_{k=1}^\infty
\left[\log(1+k^{-2/3})-k^{-2/3}\right]
$$
converges. You may use standard convergence tests.
:::

::: {.solution}

::: pf

::: {.pf-step #taylor}

For $x \ge 0$, $0 \le x - \log(1+x) \le \frac{x^2}{2}$.

::: pf-proof

Taylor's theorem with the Lagrange remainder for $\log(1+x)$ at $0$ gives $\log(1+x) = x - \frac{x^2}{2(1+\xi)^2}$ for some $\xi \in [0,x]$, and $0 < \frac{1}{(1+\xi)^2} \le 1$.

:::

:::

::: pf-step

$\sum_{k\ge1}\log(1+k^{-2/3})$ diverges.

::: pf-proof

By step [](#taylor){.pf-ref}, $\log(1+x) \ge x - \frac{x^2}{2} \ge \frac{x}{2}$ for $0 \le x \le 1$. With $x = k^{-2/3} \le 1$ this gives $\log(1+k^{-2/3}) \ge \frac12 k^{-2/3}$, and $\sum k^{-2/3}$ diverges by the $p$-test, so the series diverges by comparison.

:::

:::

::: pf-step

$\sum_{k\ge1}\left[\log(1+k^{-2/3})-k^{-2/3}\right]$ converges.

::: pf-proof

By step [](#taylor){.pf-ref}, $\abs{\log(1+k^{-2/3})-k^{-2/3}} \le \frac12 k^{-4/3}$, and $\sum k^{-4/3}$ converges by the $p$-test, so the series converges absolutely.

:::

:::

:::

:::
