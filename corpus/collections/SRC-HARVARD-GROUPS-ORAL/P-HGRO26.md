---
schema: qual/card@1
id: P-HGRO26
kind: problem
title: Subgroups of a given order in a cyclic group
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
Let $G$ be a finite cyclic group, and let $r$ divide $|G|$.
How many subgroups of order $r$ does $G$ have?
:::

::: solution
Exactly one.

Write $G=\langle g\rangle$ with $|G|=n$, and suppose $r\mid n$.

<1>1. The subgroup
\[
H=\left\langle g^{n/r}\right\rangle
\]
has order $r$.
::: proof
In a cyclic group of order $n$,
\[
|g^d|=\frac{n}{\gcd(n,d)}.
\]
For $d=n/r$, this gives
\[
\left|g^{n/r}\right|=\frac{n}{n/r}=r.
\]
:::

<1>2. Every subgroup of order $r$ equals $H$.
::: proof
Every subgroup of a cyclic group is cyclic. Let $K\le G$ have order $r$.
Then $K=\langle g^d\rangle$ for some divisor $d$ of $n$, and
\[
|K|=\frac nd=r.
\]
Hence $d=n/r$, so
\[
K=\left\langle g^{n/r}\right\rangle=H.
\]
:::

<1>3. Therefore a finite cyclic group has exactly one subgroup of each order
dividing its order.
::: proof
Existence is <1>1 and uniqueness is <1>2.
:::
:::
