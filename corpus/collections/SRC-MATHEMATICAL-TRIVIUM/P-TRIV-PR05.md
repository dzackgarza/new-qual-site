---
schema: qual/card@1
id: P-TRIV-PR05
kind: problem
title: Probability of a derangement of five presents
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
5 people decide to have a party with presents.
Everyone prepares one present and brings it to the party, where the presents are mixed.
Then everyone takes one random present.
What is the probability that nobody gets his own present?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There are $5!=120$ equally likely assignments of the five presents to the five people.


::: pf-proof

An assignment is a permutation of the five distinct presents among the five recipients. Random drawing without replacement makes every permutation equally likely.

:::

:::

::: {.pf-step #s1-2}

By inclusion--exclusion, the number of assignments with no fixed point is
$$
!5
=5!\sum_{k=0}^{5}\frac{(-1)^k}{k!}.
$$


::: pf-proof

For each person $i$, let $A_i$ be the event that person $i$ receives their own present. If a specified set of $k$ people are fixed, the remaining presents can be assigned in $(5-k)!$ ways. Inclusion--exclusion therefore gives
$$
!5=\sum_{k=0}^{5}(-1)^k\binom5k(5-k)!
=5!\sum_{k=0}^{5}\frac{(-1)^k}{k!}.
$$

:::

:::

::: {.pf-step #s1-3}

Evaluating the sum gives
$$
!5=120-120+60-20+5-1=44.
$$


::: pf-proof

Substitute $k=0,1,\ldots,5$ into the inclusion--exclusion sum in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Hence the required probability is
$$
\boxed{\frac{44}{120}=\frac{11}{30}}.
$$


::: pf-proof

Divide the $44$ favorable derangements from step [](#s1-3){.pf-ref} by the $120$ equally likely assignments from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested probability.

:::

:::

:::
