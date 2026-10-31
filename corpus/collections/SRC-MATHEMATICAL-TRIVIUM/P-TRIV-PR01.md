---
schema: qual/card@1
id: P-TRIV-PR01
kind: problem
title: Probability that five randomly shelved volumes are in order
classification:
  areas: [prelim]
  topics:
  - Combinatorial Probability
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A collection of stories in 5 volumes is placed on a bookshelf in a random order.
What is the probability that the order is correct (direct or inverse)?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There are
$$
5!=120
$$
equally likely orders of the five distinct volumes.


::: pf-proof

A shelf order is a permutation of the five volumes. Under random ordering, each permutation has the same probability, and the number of permutations is $5!$.

:::

:::

::: {.pf-step #s1-2}

Exactly two orders are favorable.


::: pf-proof

The direct order is
$$
1,2,3,4,5,
$$
and the inverse order is
$$
5,4,3,2,1.
$$
No other permutation has the volumes in numerical order in either direction.

:::

:::

::: {.pf-step #s1-3}

Therefore the probability is
$$
\boxed{\frac{2}{5!}=\frac1{60}}.
$$


::: pf-proof

Divide the two favorable outcomes from step [](#s1-2){.pf-ref} by the $120$ equally likely outcomes from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested probability.

:::

:::

:::
