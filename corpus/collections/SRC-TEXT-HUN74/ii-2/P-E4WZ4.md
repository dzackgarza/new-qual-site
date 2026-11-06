---
schema: qual/card@1
id: P-E4WZ4
kind: problem
title: Abelian groups of orders $64$ and $96$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford II.2.12(b) in a scanned copy of Algebra and an independent course guide reproducing the exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section II.2,
    exercise 12(b), book page 82: "Determine up to isomorphism all abelian
    groups of order 64; do the same for order 96." The card states exactly this
    and answers the part it names. Both lists were read to the end and checked
    against the partitions. Order 64 = 2^6 has p(6) = 11 partitions, and the
    displayed types are 6, 5+1, 4+2, 4+1+1, 3+3, 3+2+1, 3+1+1+1, 2+2+2,
    2+2+1+1, 2+1+1+1+1, 1+1+1+1+1+1, in that order and with no repetition:
    Z_64, Z_32⊕Z_2, Z_16⊕Z_4, Z_16⊕Z_2^2, Z_8^2, Z_8⊕Z_4⊕Z_2, Z_8⊕Z_2^3,
    Z_4^3, Z_4^2⊕Z_2^2, Z_4⊕Z_2^4, Z_2^6. Order 96 = 2^5·3 has Sylow 3 of
    order 3, hence Z_3, and p(5) = 7 partitions for the Sylow 2-subgroup, and
    the displayed seven are 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
    with Z_3 adjoined. Both counts and both lists are right. Distinctness is by
    uniqueness of the elementary divisors, and completeness by the primary
    decomposition, so no case is missing. Complete; no defect. Part (a) and
    part (c) of the same numbered exercise are other cards' business and are
    not claimed here.
---

::: {.problem}
Determine (up to isomorphism) all abelian groups of order 64; do the same for order 96.
:::

::: {.solution}
By the classification of finite abelian groups, a finite abelian group is the
direct sum of its Sylow subgroups, and an abelian group of order $p^n$ is
determined up to isomorphism by the partition $n=a_1+\cdots+a_r$ with
$G\cong\ZZ_{p^{a_1}}\oplus\cdots\oplus\ZZ_{p^{a_r}}$.

::: pf

::: pf-step

There are exactly eleven abelian groups of order $64=2^6$:
$$
\begin{aligned}
&\ZZ_{64},\\
&\ZZ_{32}\oplus\ZZ_2,\\
&\ZZ_{16}\oplus\ZZ_4,\\
&\ZZ_{16}\oplus\ZZ_2\oplus\ZZ_2,\\
&\ZZ_8\oplus\ZZ_8,\\
&\ZZ_8\oplus\ZZ_4\oplus\ZZ_2,\\
&\ZZ_8\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_2,\\
&\ZZ_4\oplus\ZZ_4\oplus\ZZ_4,\\
&\ZZ_4\oplus\ZZ_4\oplus\ZZ_2\oplus\ZZ_2,\\
&\ZZ_4\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_2,\\
&\ZZ_2^{\oplus6}.
\end{aligned}
$$

::: pf-proof

An abelian group of order $2^6$ is uniquely determined by a partition of $6$:
$$
6,\ 5+1,\ 4+2,\ 4+1+1,\ 3+3,\ 3+2+1,\ 3+1+1+1,
$$
$$
2+2+2,\ 2+2+1+1,\ 2+1+1+1+1,\ 1+1+1+1+1+1.
$$
Replacing each part $a$ by a cyclic summand $\ZZ_{2^a}$ gives exactly the
displayed list. Distinct partitions give nonisomorphic groups by uniqueness in
the classification theorem.

:::

:::

::: pf-step

There are exactly seven abelian groups of order $96=2^5\cdot3$:
$$
\begin{aligned}
&\ZZ_{32}\oplus\ZZ_3,\\
&\ZZ_{16}\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_8\oplus\ZZ_4\oplus\ZZ_3,\\
&\ZZ_8\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_4\oplus\ZZ_4\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_4\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_2^{\oplus5}\oplus\ZZ_3.
\end{aligned}
$$

::: pf-proof

The Sylow $3$-subgroup has order $3$, hence is necessarily $\ZZ_3$. The Sylow
$2$-subgroup has order $2^5$, and the partitions
$$
5,\ 4+1,\ 3+2,\ 3+1+1,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1
$$
give its seven possible isomorphism types. Taking the direct sum with $\ZZ_3$
gives the displayed list. Uniqueness of the primary decomposition shows that no
two groups on the list are isomorphic and that no further cases occur.

:::

:::

:::

:::
