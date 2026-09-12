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

::: problem
Prove Chebyshev's Inequality: If $f \in L^p(X, \mu)$, with $0 < p < \infty$, then for any positive number $r$,
$$
\mu(\{x : |f(x)| > r\}) \leq \left[\frac{\|f\|_p}{r}\right]^p.
$$
:::

::: solution
<1>1. Integrate the pointwise lower bound on the superlevel set.
::: proof
Let
\[
E_r:=\{x\in X:|f(x)|>r\}.
\]
On $E_r$,
\[
|f(x)|^p\ge r^p.
\]
Therefore
\[
\|f\|_p^p
=\int_X|f|^p\,d\mu
\ge\int_{E_r}|f|^p\,d\mu
\ge r^p\mu(E_r).
\]
Dividing by $r^p$ gives
\[
\boxed{
\mu(\{|f|>r\})
\le \frac{\|f\|_p^p}{r^p}
=\left(\frac{\|f\|_p}{r}\right)^p.}
\]
:::
:::
