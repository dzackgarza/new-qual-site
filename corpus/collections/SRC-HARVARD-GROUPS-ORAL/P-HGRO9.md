---
schema: qual/card@1
id: P-HGRO9
kind: problem
title: The converse of Lagrange's theorem
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Is the converse of Lagrange's theorem true?
Justify your answer.
:::

::: solution
No. The group $A_4$ gives a counterexample: $6$ divides $|A_4|=12$, but
$A_4$ has no subgroup of order $6$.

<1>1. Any subgroup $H\le A_4$ of order $6$ would be normal.
::: proof
Such a subgroup would have index $2$, and every subgroup of index $2$ is
normal.
:::

<1>2. No normal subgroup of order $6$ exists in $A_4$.
::: proof
A group of order $6$ has a Sylow $3$-subgroup. If $H\trianglelefteq A_4$ has
order $6$ and $P\le H$ has order $3$, then every conjugate $gPg^{-1}$ also lies
in $H$.

But $A_4$ has four Sylow $3$-subgroups: its eight $3$-cycles split into four
subgroups, each containing two nonidentity elements. Thus $H$ would contain all
eight $3$-cycles, impossible because $|H|=6$.
:::

<1>3. Therefore the converse of Lagrange's theorem is false.
::: proof
Lagrange's theorem gives a necessary divisibility condition on subgroup orders,
but <1>1--<1>2 show that the divisor $6$ of $12$ is not realized as a subgroup
order in $A_4$.
:::
:::
