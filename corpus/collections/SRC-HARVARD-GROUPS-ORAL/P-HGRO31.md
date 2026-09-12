---
schema: qual/card@1
id: P-HGRO31
kind: problem
title: Sylow theorems
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
State the Sylow theorems.
:::

::: solution
Let $G$ be a finite group and write
\[
|G|=p^n m,
\qquad p\nmid m,
\]
for a prime $p$.

<1>1. Existence.
::: proof
There exists a subgroup $P\le G$ of order $p^n$. Such a subgroup is called a
Sylow $p$-subgroup.
:::

<1>2. Containment and conjugacy.
::: proof
Every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup, and any two
Sylow $p$-subgroups of $G$ are conjugate in $G$.
:::

<1>3. Number of Sylow subgroups.
::: proof
If $n_p$ denotes the number of Sylow $p$-subgroups, then
\[
n_p\equiv1\pmod p
\qquad\text{and}\qquad
n_p\mid m.
\]
In particular, a Sylow $p$-subgroup is normal if and only if it is unique.
:::
:::
