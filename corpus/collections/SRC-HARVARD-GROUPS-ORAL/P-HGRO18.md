---
schema: qual/card@1
id: P-HGRO18
kind: problem
title: A normal subgroup of order 11 in a group of order 99
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
Let $G$ be a group of order $99$.
Must $G$ have a normal subgroup of order $11$?
Justify your answer.
:::

::: solution
Yes.

Let $n_{11}$ be the number of Sylow $11$-subgroups of $G$. Since
\[
|G|=99=3^2\cdot11,
\]
Sylow's theorem gives
\[
n_{11}\equiv1\pmod{11}
\qquad\text{and}\qquad
n_{11}\mid9.
\]
The only positive divisor of $9$ congruent to $1$ modulo $11$ is $1$.
Therefore the Sylow $11$-subgroup is unique, hence normal, and has order $11$.
:::
