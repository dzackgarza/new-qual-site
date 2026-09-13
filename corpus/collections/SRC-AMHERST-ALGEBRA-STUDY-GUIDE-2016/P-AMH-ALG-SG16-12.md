---
schema: qual/card@1
id: P-AMH-ALG-SG16-12
kind: problem
title: Amherst algebra study guide problem 12
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
(January 1997) Suppose that $\sigma$ is a permutation in the alternating group $A_{10}$ given by
\[
\begin{pmatrix}
1&2&3&4&5&6&7&8&9&10\\
4&7&2&6&10&1&5&?&?&3
\end{pmatrix},
\]
where the images of $8$ and $9$ have been lost.
Determine the images of $8$ and $9$ under $\sigma$.
What is the order of $\sigma$?
:::

::: {.solution}
Solution.
The two missing outputs are also 8 and 9. If σ(8) = 9, then we must have σ(9) = 8, which would give σ = (1 4 6)(2 7 5 10 3)(8 9). However, since 3-cycles and 5-cycles are even, and 2-cycles are odd, that would make σ an odd permutation.
But we were told σ∈A10, meaning that σ is even.
Contradiction!
Therefore σ is not the permutation above, and therefore σ(8)⁄= 9. So we must have σ(8) = 8, and hence σ(9) = 9. Thus, σ = (1 4 6)(2 7 5 10 3). The order of σ is the lcm of the orders of the individual (disjoint) cycles in the above decomposition.
So the order of σ is o(σ) = lcm(3, 5) = 15.
:::
