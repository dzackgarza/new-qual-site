---
schema: qual/card@1
id: P-HFGO33
kind: problem
title: Define a cyclotomic extension
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define a cyclotomic extension.
:::

::: solution
A cyclotomic extension of a field $F$ is an extension obtained by adjoining a
root of unity. Concretely, for a positive integer $n$ and a primitive $n$th
root of unity $\zeta_n$, one considers
\[
F(\zeta_n)/F.
\]
When $F=\mathbb Q$, the field $\mathbb Q(\zeta_n)$ is called the $n$th
cyclotomic field.

Equivalently, when $\operatorname{char}F\nmid n$, $F(\zeta_n)$ is the splitting
field over $F$ of $T^n-1$: every $n$th root of unity is a power of a primitive
$n$th root.
:::
