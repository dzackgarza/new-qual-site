---
schema: qual/card@1
id: P-HGRO21
kind: problem
title: Every group of order 12 has a normal subgroup
classification:
  areas: [algebra]
  topics: [Sylow Theory]
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
Prove that every group of order $12$ has a nontrivial proper normal subgroup.
:::

::: solution
Let $n_3$ be the number of Sylow $3$-subgroups. Sylow's theorem gives
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid4,
\]
so $n_3=1$ or $4$.

<1>1. If $n_3=1$, the unique Sylow $3$-subgroup is a nontrivial proper normal
subgroup.
::: proof
It has order $3$, and uniqueness makes it normal.
:::

<1>2. If $n_3=4$, then the Sylow $2$-subgroup is unique and hence normal.
::: proof
Four distinct subgroups of order $3$ intersect pairwise only in the identity,
so their nonidentity elements account for
\[
4(3-1)=8
\]
elements of $G$. Thus exactly three nonidentity elements remain outside all
Sylow $3$-subgroups.

Every Sylow $2$-subgroup has order $4$, so its three nonidentity elements have
orders powers of $2$ and therefore lie among those same three remaining
elements. Hence every Sylow $2$-subgroup consists of the identity together with
those three elements. There is therefore only one Sylow $2$-subgroup, and it is
normal.
:::

<1>3. Hence $G$ always has a nontrivial proper normal subgroup.
::: proof
This follows from <1>1 and <1>2.
:::
:::
