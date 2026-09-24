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

<1>1. The group $S_{40}$ contains an element of order $111$.

::: {.proof}
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

<1>2. If $\sigma\in S_n$ has order $111$, then every cycle length in
the disjoint-cycle decomposition of $\sigma$ divides $111$.

::: {.proof}
The order of a permutation is the least common multiple of the lengths
of its disjoint cycles. If that least common multiple is $111$, each
cycle length divides $111$.
:::

<1>3. Every permutation of order $111$ moves at least $40$ letters.

::: {.proof}
By step <1>2, every nontrivial cycle length is one of
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

<1>4. The smallest possible $n$ is
$$
\boxed{40}.
$$

::: {.proof}
Step <1>1 gives an order-$111$ cyclic subgroup in $S_{40}$, while step
<1>3 shows that no $S_n$ with $n<40$ can contain an element, and hence
a cyclic subgroup, of order $111$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested minimum.
:::
:::
