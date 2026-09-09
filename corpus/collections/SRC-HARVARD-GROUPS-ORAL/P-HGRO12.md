---
schema: qual/card@1
id: P-HGRO12
kind: problem
title: No surjection from A4 to the cyclic group of order two
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
Can $A_4$ be mapped homomorphically onto $\mathbb Z/2\mathbb Z$?
Justify your answer.
:::

::: solution
No.

<1>1. A surjection $f:A_4\to \ZZ/2\ZZ$ would have a normal kernel of order
$6$.
::: proof
By the first isomorphism theorem,
\[
|A_4:\ker f|=|\operatorname{im}f|=2,
\]
so $|\ker f|=12/2=6$. Every kernel is normal.
:::

<1>2. The group $A_4$ has no normal subgroup of order $6$.
::: proof
Suppose $N\trianglelefteq A_4$ and $|N|=6$. By Sylow's theorem, $N$ contains a
subgroup $P$ of order $3$. Since $N$ is normal, it contains every $A_4$-conjugate
of $P$.

The group $A_4$ has four Sylow $3$-subgroups, accounting for all eight
$3$-cycles. Hence $N$ would contain those eight nonidentity elements, contradicting
$|N|=6$.
:::

<1>3. Therefore no surjection $A_4\to\ZZ/2\ZZ$ exists.
::: proof
This follows from <1>1 and <1>2.
:::
:::
