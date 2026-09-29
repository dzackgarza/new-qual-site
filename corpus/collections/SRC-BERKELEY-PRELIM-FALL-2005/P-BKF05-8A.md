---
schema: qual/card@1
id: P-BKF05-8A
kind: problem
title: Smallest symmetric group containing an element of order 111
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained cycle-order argument. Since all cycle
    lengths divide 111, either a 111-cycle occurs or disjoint 3- and
    37-cycles are required, giving the sharp lower bound 40.
---

::: {.problem}
Find the smallest positive integer \(n\) for which \(S_n\) contains a cyclic subgroup of order \(111\).
:::

::: {.solution}

Since
$$
111=3\cdot37,
$$
the two prime factors are distinct.

::: pf

::: {.pf-step #S40-has-order-111-element}
The group $S_{40}$ contains an element of order $111$.

::: pf-proof
Take a $3$-cycle and a disjoint $37$-cycle in $S_{40}$, and let
$\sigma$ be their product. Disjoint cycles commute, and the order of
their product is the least common multiple of their lengths. Therefore
$$
\operatorname{ord}(\sigma)
=
\operatorname{lcm}(3,37)
=
111.
$$
Hence $\langle\sigma\rangle$ is a cyclic subgroup of $S_{40}$ of
order $111$.
:::

:::

::: {.pf-step #cycle-lengths-divide-111}
If $\sigma\in S_n$ has order $111$, then every cycle length in
the disjoint-cycle decomposition of $\sigma$ divides $111$.

::: pf-proof
The order of a permutation is the least common multiple of the lengths
of its disjoint cycles. If that least common multiple is $111$, each
cycle length divides $111$.
:::

:::

::: {.pf-step #moves-at-least-40}
Every permutation of order $111$ moves at least $40$ letters.

::: pf-proof
By step [](#cycle-lengths-divide-111){.pf-ref}, every nontrivial cycle length is one of
$$
3,\qquad37,\qquad111.
$$
If the permutation contains a $111$-cycle, then it already moves
$111>40$ letters.

Otherwise, the least common multiple of its cycle lengths can contain
the prime factor $3$ only if a $3$-cycle occurs, and it can contain the
prime factor $37$ only if a $37$-cycle occurs. These two cycles are
disjoint, so together they move
$$
3+37=40
$$
letters. Thus in every case $n\ge40$.
:::

:::

::: {.pf-step #smallest-n-40}
The smallest possible $n$ is
$$
\boxed{40}.
$$

::: pf-proof
Step [](#S40-has-order-111-element){.pf-ref} gives an order-$111$ cyclic subgroup in $S_{40}$, while step
[](#moves-at-least-40){.pf-ref} shows that no $S_n$ with $n<40$ can contain an element, and hence
a cyclic subgroup, of order $111$.
:::

:::

::: pf-qed
Step [](#smallest-n-40){.pf-ref} is the requested minimum.
:::

:::

:::
