---
schema: qual/card@1
id: P-HFGO7
kind: problem
title: Define an algebraic closure
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
Define an algebraic closure of a field.
:::

::: solution
An **algebraic closure** of a field $F$ is an extension field $\overline F/F$
such that

1. $\overline F$ is algebraic over $F$, and
2. $\overline F$ is algebraically closed.

Equivalently, every element of $\overline F$ is algebraic over $F$, and every
nonconstant polynomial in $\overline F[x]$ has a root in $\overline F$.

Algebraic closures exist for every field and are unique up to an
$F$-isomorphism, although not canonically unique.
:::
