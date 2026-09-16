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
---

::: problem
Consider the sum a of $1 0 ^ { N }$ real numbers $a _ { k } , a = \sum _ { k = 1 } ^ { 1 0 ^ { N } } a _ { k }$ . Let $\tilde { a } _ { k }$ be an approximation of $a _ { k }$ with precision $1 0 ^ { - m }$ =1. Assume that the round-off errors $\delta _ { k } = a _ { k } - { \tilde { a } } _ { k }$ are distributed uniformly within the interval $( - 0 . 5 \cdot 1 0 ^ { - m } , \ 0 . 5 \cdot 1 0 ^ { - m } )$ . Compose the sum $\tilde { a } = \sum _ { k = 1 } ^ { 1 0 ^ { N } } \tilde { a } _ { k }$ and let $\delta = a - \tilde { a }$ be the total error of the approximation.
=1For the given values of N and m find - such that

$$
P ( | \delta | < \epsilon ) > 0 . 9 9 .\tag{52}
$$
:::
