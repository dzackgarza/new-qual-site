---
schema: qual/card@1
id: P-AMH-ALG-SG16-14
kind: problem
title: Amherst algebra study guide problem 14
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2008) Recall that Sn denotes the group of permutations on n symbols. (a) Find an element of S10 of order 21. (b) Prove that no element of S10 has order 11.
:::

::: {.solution}
Solution. (a) The order of σ is the lcm of the orders of each individual disjoint cycle comprising σ
(and the order of an n-cycle is n). Since 21 = lcm(3 , 7), the element σ = (1 2 3)(4 5 6 7 8 9 10) has
order 21.
(b) Suppose S10 has a permutation σ of order 11. Then σ must have a disjoint cycle structure such
that the lcm of the cycle lengths is 11. If the disjoint cycles making up σ have lengths𝓁1,...,𝓁 k, then
11 =o(σ) = lcm(𝓁1,...,𝓁 k).
Thus each 𝓁i divides 11. Since 11 is prime, each 𝓁i = 1 or 11. But an 11-cycle requires 11 distinct
symbols, which can’t happen since we are in S10. So 𝓁i = 1 for all i, which means that σ is the
identity. Yet it has order 11. This contradiction shows that no element of S10 has order 11.
Here is a more abstract problem.
:::
