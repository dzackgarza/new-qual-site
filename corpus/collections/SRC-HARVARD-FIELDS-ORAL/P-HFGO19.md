---
schema: qual/card@1
id: P-HFGO19
kind: problem
title: Solvability by radicals for a product of cyclic Galois groups
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
Let $p(x)\in\mathbb Q[x]$ have Galois group $\mathbb Z/4\mathbb Z\times\mathbb Z/4\mathbb Z$.
What can be said about the solvability of $p(x)$ by radicals?
:::

::: solution
The polynomial is solvable by radicals.

<1>1. Its Galois group is solvable.
::: proof
By hypothesis,
\[
G\cong \mathbb Z/4\mathbb Z\times\mathbb Z/4\mathbb Z.
\]
This group is abelian. Every abelian group is solvable: its commutator subgroup
is trivial, so its derived series terminates after one step.
:::

<1>2. A polynomial over $\mathbb Q$ is solvable by radicals if and only if its
Galois group is solvable.
::: proof
This is the Galois criterion for solvability by radicals in characteristic
zero. Applying it to <1>1 gives the conclusion.
:::

Hence the roots of $p(x)$ can be expressed using a finite tower of radical
extensions over $\mathbb Q$.
:::
