---
schema: qual/card@1
id: P-HCAO16
kind: problem
title: Define a Dedekind domain
classification:
  areas:
  - algebra
  topics:
  - Dedekind Domains
  - Noetherian Rings
  - Integral Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define a Dedekind domain.
:::

::: solution
A Dedekind domain is an integral domain $R$ satisfying the following three
conditions:

1. $R$ is Noetherian;
2. $R$ is integrally closed in its fraction field;
3. every nonzero prime ideal of $R$ is maximal.

For a Dedekind domain that is not a field, the third condition is equivalent to
\[
\dim R=1.
\]
Some conventions exclude fields by requiring Krull dimension exactly $1$;
others allow fields, in which case the formulation using nonzero prime ideals
is convenient.
:::
