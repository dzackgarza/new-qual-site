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
---

::: {.problem}
Determine (up to isomorphism) all abelian groups of order 64; do the same for order 96.
:::

::: solution
Use the classification of finite abelian groups by their primary cyclic
decomposition.

<1>1. There are exactly eleven abelian groups of order $64=2^6$:
\[
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
\]
::: proof
An abelian group of order $2^6$ is uniquely determined by a partition of $6$:
\[
6,\ 5+1,\ 4+2,\ 4+1+1,\ 3+3,\ 3+2+1,\ 3+1+1+1,
\]
\[
2+2+2,\ 2+2+1+1,\ 2+1+1+1+1,\ 1+1+1+1+1+1.
\]
Replacing each part $a$ by a cyclic summand $\ZZ_{2^a}$ gives exactly the
displayed list. Distinct partitions give nonisomorphic groups by uniqueness in
the classification theorem.
:::

<1>2. There are exactly seven abelian groups of order $96=2^5\cdot3$:
\[
\begin{aligned}
&\ZZ_{32}\oplus\ZZ_3,\\
&\ZZ_{16}\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_8\oplus\ZZ_4\oplus\ZZ_3,\\
&\ZZ_8\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_4\oplus\ZZ_4\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_4\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_2\oplus\ZZ_3,\\
&\ZZ_2^{\oplus5}\oplus\ZZ_3.
\end{aligned}
\]
::: proof
The Sylow $3$-subgroup has order $3$, hence is necessarily $\ZZ_3$. The Sylow
$2$-subgroup has order $2^5$, and the partitions
\[
5,\ 4+1,\ 3+2,\ 3+1+1,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1
\]
give its seven possible isomorphism types. Taking the direct sum with $\ZZ_3$
gives the displayed list. Uniqueness of the primary decomposition shows that no
two groups on the list are isomorphic and that no further cases occur.
:::
:::
