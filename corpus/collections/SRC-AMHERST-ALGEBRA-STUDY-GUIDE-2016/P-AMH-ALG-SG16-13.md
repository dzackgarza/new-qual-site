---
schema: qual/card@1
id: P-AMH-ALG-SG16-13
kind: problem
title: Disjoint cycles, order and parity of $(4\ 2\ 1)(6\ 1\ 3\ 2)$
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
Let $\sigma$ be the permutation $(4\ 2\ 1)(6\ 1\ 3\ 2)$ in $S_6$.
(a) Write $\sigma$ as a product of disjoint cycles in $S_6$.
(b) Compute the order of $\sigma$.
(c) Is $\sigma$ an even or an odd permutation?
:::

::: {.solution}
Use the convention that the rightmost cycle acts first.

::: pf

::: {.pf-step #s1-1}
The disjoint-cycle decomposition is
$$
\boxed{\sigma=(1\ 3)(2\ 6\ 4)}.
$$

::: pf-proof
Compute the images under
$$
\sigma=(4\ 2\ 1)(6\ 1\ 3\ 2).
$$
One finds
$$
1\mapsto3\mapsto1,
$$
and
$$
2\mapsto6\mapsto4\mapsto2.
$$
The point $5$ is fixed. Hence the nontrivial disjoint cycles are exactly
$$
(1\ 3)
\qquad\text{and}\qquad
(2\ 6\ 4).
$$
:::

:::

::: pf-step
The order of $\sigma$ is
$$
\boxed{6}.
$$

::: pf-proof
Disjoint cycles commute, and the order of a product of disjoint cycles is the least common multiple of their lengths. By step [](#s1-1){.pf-ref},
$$
\operatorname{ord}(\sigma)
=\operatorname{lcm}(2,3)
=6.
$$
:::

:::

::: pf-step
The permutation $\sigma$ is odd.

::: pf-proof
A $2$-cycle is odd, while a $3$-cycle is even because it is a product of two transpositions. By step [](#s1-1){.pf-ref}, $\sigma$ is the product of one odd permutation and one even permutation, hence is odd.
:::

:::

:::

:::
