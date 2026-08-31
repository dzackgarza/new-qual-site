---
schema: qual/card@1
id: FR-6AHGM
kind: proof
title: 'Proposition: $\int \abs{f} = 0 \implies f = 0$ a.e.'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proof}
Suppose $f$ is measurable with $\int \abs{f} = 0$.
For each $n \ge 1$ define $E_n \da \ts{x \st \abs{f(x)} \ge \frac1n}$.
On $E_n$ we have $\abs{f} \ge \frac1n$, so
\[
0 = \int \abs{f} \ge \int_{E_n} \abs{f} \ge \int_{E_n} \frac1n = \frac1n \mu(E_n),
\]
which forces $\mu(E_n) = 0$ for every $n$.
Now $\ts{x \st f(x) \neq 0} = \ts{x \st \abs{f(x)} > 0} = \bigcup_{n \ge 1} E_n$ is a countable union of null sets, hence null.
Therefore $f = 0$ almost everywhere.
:::
