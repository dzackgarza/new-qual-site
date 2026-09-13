---
schema: qual/card@1
id: P-AMH-ALG-SG16-13
kind: problem
title: Amherst algebra study guide problem 13
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
(January 2010) Let $\sigma$ be the permutation $(4\ 2\ 1)(6\ 1\ 3\ 2)$ in $S_6$.
(a) Write $\sigma$ as a product of disjoint cycles in $S_6$.
(b) Compute the order of $\sigma$.
(c) Is $\sigma$ an even or an odd permutation?
:::

::: {.solution}
Solution.
(a) σ = (1 3)(2 6 4). (b) The order of σ is the lcm of the orders of each individual cycle in its decomposition into disjoint cycles.
Since the order of an n-cycle is n, we obtain o(σ) = lcm(3, 2) = 6. (c)σ is a product of a 2-cycle and a 3-cycle.
The 2-cycle is an odd permutation (since 2 is even), and the 3-cycle is even (since 3 is odd), so σ is even + odd = odd.
:::
