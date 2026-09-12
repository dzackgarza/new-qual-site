---
schema: qual/card@1
id: P-HGRO30
kind: problem
title: A group with every subgroup normal need not be abelian
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
If every subgroup of a group is normal, must the group be abelian?
Prove the claim or give a counterexample.
:::

::: solution
No. The quaternion group
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\}
\]
is nonabelian, but every subgroup of $Q_8$ is normal.

<1>1. The group $Q_8$ is nonabelian.
::: proof
Its defining multiplication gives
\[
ij=k,
\qquad
ji=-k,
\]
so $ij\ne ji$.
:::

<1>2. Every subgroup of $Q_8$ is normal.
::: proof
The subgroups are
\[
\{1\},\quad \{\pm1\},\quad
\langle i\rangle,\quad \langle j\rangle,\quad \langle k\rangle,\quad Q_8.
\]
The three subgroups of order $4$ have index $2$, hence are normal. The subgroup
$\{\pm1\}$ lies in the center, and the trivial subgroup and whole group are
normal.
:::

<1>3. Hence normality of every subgroup does not imply commutativity.
::: proof
Combine <1>1 and <1>2.
:::
:::
