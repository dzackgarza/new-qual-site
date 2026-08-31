---
schema: qual/card@1
id: FR-KEWV2
kind: proof
title: 'Proposition: $\sum \abs{f_n} \in L^1 \implies \sum \abs{f_n(x)} < \infty$
  a.e.'
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.proof}
Let $S(x) \da \sum_n \abs{f_n(x)}$, the pointwise sum of the nonnegative functions $\abs{f_n}$.
By the monotone convergence theorem applied to the partial sums $S_N(x) = \sum_{n=1}^N \abs{f_n(x)}$,
\[
\int_X S = \int_X \lim_N S_N = \lim_N \int_X S_N = \lim_N \sum_{n=1}^N \int_X \abs{f_n} = \sum_n \norm{f_n}_1 < \infty,
\]
where the last equality is the hypothesis $\sum \abs{f_n} \in L^1$.
An integrable function is finite almost everywhere: if $S(x) = \infty$ on a set of positive measure, then $\int_X S = \infty$, contradicting the computation above.
Therefore $S(x) = \sum_n \abs{f_n(x)} < \infty$ for almost every $x$.
:::
