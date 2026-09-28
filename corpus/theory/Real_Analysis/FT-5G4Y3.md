---
schema: qual/card@1
id: FT-5G4Y3
kind: theorem
title: Monotone convergence theorem
slogan: 'For an almost everywhere increasing sequence in $L^+$, the integral of the limit is the limit of the integrals.'
prompts:
- State the monotone convergence theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n$ for $n\geq1$ and $f$ belong to [[D-BF5L2|$L^+$]]. If $f_n\le f_{n+1}$ almost everywhere for every $n$ and $f_n\to f$ almost everywhere, then
$$
\lim_{n\to\infty} \int_X f_n \dmu = \int_X f \dmu .
$$
:::
