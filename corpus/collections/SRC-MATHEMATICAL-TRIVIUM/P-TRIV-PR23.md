---
schema: qual/card@1
id: P-TRIV-PR23
kind: problem
title: Central limit estimate of accumulated round-off error
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost epsilon and removed stray residue against Probability Problem 23 on page 30 of the source PDF.
---

::: {.problem}
Consider the sum $a$ of $10^N$ real numbers $a_k$, $a = \sum_{k=1}^{10^N} a_k$.
Let $\tilde{a}_k$ be an approximation of $a_k$ with precision $10^{-m}$.
Assume that the round-off errors $\delta_k = a_k - \tilde{a}_k$ are distributed uniformly within the interval $(-0.5 \cdot 10^{-m},\ 0.5 \cdot 10^{-m})$.
Compose the sum $\tilde{a} = \sum_{k=1}^{10^N} \tilde{a}_k$ and let $\delta = a - \tilde{a}$ be the total error of the approximation.
For the given values of $N$ and $m$ find $\epsilon$ such that
$$
P(|\delta| < \epsilon) > 0.99.
\tag{52}
$$
:::
