---
schema: qual/card@1
id: P-HFGO23
kind: problem
title: Cardinality of an infinite field and its algebraic closure
classification:
  areas: [algebra]
  topics: [Field Theory]
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
Can passage from an infinite field to its algebraic closure increase its cardinality?
Justify your answer.
:::

::: solution
No. If $F$ is infinite and $\overline F$ is an algebraic closure, then
\[
|\overline F|=|F|.
\]

<1>1. The polynomial ring $F[x]$ has cardinality $|F|$.
::: proof
For each fixed degree $n$, the set of polynomials of degree at most $n$ is in
bijection with a subset of $F^{n+1}$, which has cardinality $|F|$ because $F$
is infinite. Since
\[
F[x]=\bigcup_{n\ge0}\{f:\deg f\le n\}
\]
is a countable union of sets of cardinality $|F|$, it also has cardinality
$|F|$.
:::

<1>2. There are at most $|F|$ elements algebraic over $F$ in any extension.
::: proof
Every algebraic element is a root of some nonzero polynomial in $F[x]$.
Each polynomial has finitely many roots in a field extension, and by <1>1 there
are only $|F|$ polynomials. Hence the union of all root sets has cardinality at
most
\[
|F|\cdot\aleph_0=|F|.
\]
:::

<1>3. Therefore $|\overline F|=|F|$.
::: proof
By <1>2,
\[
|\overline F|\le|F|.
\]
Since $F\subseteq\overline F$,
\[
|F|\le|\overline F|.
\]
The two inequalities give equality.
:::
:::
