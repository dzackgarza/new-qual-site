---
schema: qual/card@1
id: P-HGRO4
kind: problem
title: Abelian groups of order $27$
classification:
  areas: [algebra]
  topics: [Abelian Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, question on abelian groups of 27 elements.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Classify all abelian groups of order $27$.
Prove that the groups in your classification are pairwise nonisomorphic.
:::

::: solution
<1>1. Every abelian group of order $27=3^3$ is isomorphic to exactly one of
\[
C_{27},\qquad C_9\times C_3,\qquad C_3\times C_3\times C_3.
\]
::: proof
By the structure theorem for finite abelian groups, an abelian group of order
$3^3$ is a direct sum of cyclic $3$-power groups whose exponents correspond to
a partition of $3$. The partitions
\[
3,\qquad 2+1,\qquad 1+1+1
\]
give exactly the three displayed groups.
:::

<1>2. The three displayed groups are pairwise nonisomorphic.
::: proof
Their exponents are respectively
\[
27,\qquad 9,\qquad 3.
\]
The exponent of a finite group is preserved by isomorphism. Since these three
values are distinct, no two of the displayed groups are isomorphic.
:::
:::
