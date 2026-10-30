---
schema: qual/card@1
id: P-RASP07A
kind: problem
title: "Chebyshev's inequality"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Prove Chebyshev's Inequality: If $f \in L^p(X, \mu)$, with $0 < p < \infty$, then for any positive number $r$,
$$
\mu(\{x : \abs{f(x)} > r\}) \leq \left[\frac{\norm{f}_p}{r}\right]^p.
$$
:::

::: {.solution}

::: pf

::: pf-step

Integrate the pointwise lower bound on the superlevel set.

::: pf-proof

Let
$$
E_r:=\{x\in X:\abs{f(x)}>r\}.
$$
On $E_r$,
$$
\abs{f(x)}^p\ge r^p.
$$
Therefore
$$
\norm{f}_p^p
=\int_X\abs{f}^p\,d\mu
\ge\int_{E_r}\abs{f}^p\,d\mu
\ge r^p\mu(E_r).
$$
Dividing by $r^p$ gives
$$
\boxed{
\mu(\{\abs{f}>r\})
\le \frac{\norm{f}_p^p}{r^p}
=\left(\frac{\norm{f}_p}{r}\right)^p.}
$$

:::

:::

:::

:::
