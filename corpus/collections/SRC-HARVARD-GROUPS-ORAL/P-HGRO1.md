---
schema: qual/card@1
id: P-HGRO1
kind: problem
title: Classification of finitely generated abelian groups
classification:
  areas: [algebra]
  topics: [Abelian Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, first question.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
State the classification theorem for finitely generated abelian groups.
:::

::: solution
<1>1. Let $G$ be a finitely generated abelian group. Then there is a unique
integer $r\ge0$ and unique integers
\[
1<d_1\mid d_2\mid\cdots\mid d_t
\]
such that
\[
G\cong \ZZ^r\oplus
\ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_t\ZZ.
\]
::: proof
This is the invariant-factor form of the structure theorem. The integer $r$ is
the rank of the free part, and the finite direct sum is the torsion subgroup
$G_{\mathrm{tors}}$.
:::

<1>2. Equivalently, the torsion subgroup has a unique elementary-divisor
decomposition
\[
G_{\mathrm{tors}}
\cong
\bigoplus_p\bigoplus_{j=1}^{m_p}\ZZ/p^{e_{p,j}}\ZZ,
\]
where $p$ runs over finitely many primes and, for each $p$, the positive
integers $e_{p,j}$ are uniquely determined up to order.
::: proof
Factoring each invariant factor $d_i$ into prime powers and applying the
Chinese remainder theorem gives the elementary-divisor form. Conversely,
grouping the prime-power cyclic factors by increasing exponent recovers the
invariant factors. Thus the two formulations are equivalent and both are
unique up to isomorphism and reordering of direct summands.
:::
:::
