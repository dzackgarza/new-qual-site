---
schema: qual/card@1
id: P-TRIV-PR31
kind: problem
title: Sample size for testing coin-matching probability $2/3$ against $1/2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
One may naively argue that in one toss of two coins the probability to have two heads or tails equals $2 / 3$ . Indeed, if we use the scheme with three elementary events (it fell two heads, or two tails, or one head and one tail), the probability that the coins fall equally may seem to be $2 / 3$ . The correct scheme, however, must contain four different events (head-head, tail-tail, head-tail, tail-head) with the probabilities equally distributed among them, and it gives the correct answer $1 / 2$ An experiment can be conducted to overcome the doubts about which scheme is more reasonable.
Let the first hypothesis claim that the correct value is $2 / 3$ and the second - that it is $1 / 2$ . Find how many coins tosses one should make to eliminate the first hypothesis with type I error 0.05 (probability to reject the second hypothesis when it is true) and type II error 0.05 (probability to accept the first hypothesis when it is false).
:::
