---
schema: qual/card@1
id: P-2WRUJ
kind: problem
title: The identity $\sum_{m=k}^n\binom{m}{k}=\binom{n+1}{k+1}$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Combinatorics
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $k$ be a nonnegative integer.
Prove by mathematical induction that for all $n \geq k$ we have $$\sum_{m=k}^{n} \binom{m}{k} = \binom{n+1}{k+1}.$$
:::

::: solution
For $n=k$,
\[
\sum_{m=k}^{k}\binom{m}{k}=\binom{k}{k}=1=\binom{k+1}{k+1}.
\]
Assume
\[
\sum_{m=k}^{n}\binom{m}{k}=\binom{n+1}{k+1}.
\]
Then Pascal's identity gives
\[
\sum_{m=k}^{n+1}\binom{m}{k}
=\binom{n+1}{k+1}+\binom{n+1}{k}
=\binom{n+2}{k+1}.
\]
Thus the identity holds for all $n\ge k$ by induction.
:::
