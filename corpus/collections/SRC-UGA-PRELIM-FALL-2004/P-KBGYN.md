---
schema: qual/card@1
id: P-KBGYN
kind: problem
title: $\sum_{k=0}^{n-1}a^k=(a^n-1)/(a-1)$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $a$ be a real number other than 1. Use induction to show that for each positive integer $n$, $$\sum_{k=0}^{n-1} a^k = (a^n-1)/(a-1).$$
:::

::: {.solution}
For $n=1$,
\[
\sum_{k=0}^{0}a^k=1=\frac{a-1}{a-1}.
\]
Assume
\[
\sum_{k=0}^{n-1}a^k=\frac{a^n-1}{a-1}.
\]
Then
\[
\sum_{k=0}^{n}a^k
=\frac{a^n-1}{a-1}+a^n
=\frac{a^{n+1}-1}{a-1}.
\]
Thus the formula holds for all positive integers $n$ by induction.
:::
