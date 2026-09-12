---
schema: qual/card@1
id: P-HFGO13
kind: problem
title: Define a splitting field
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
Define the splitting field of a polynomial over a field.
:::

::: solution
Let $f(x)\in F[x]$. A **splitting field** of $f$ over $F$ is an extension
$K/F$ such that

1. $f$ splits completely into linear factors over $K$, and
2. $K$ is generated over $F$ by the roots of $f$.

Equivalently, if $\alpha_1,\ldots,\alpha_r$ are the distinct roots of $f$ in an
algebraic closure of $F$, then a splitting field is
\[
K=F(\alpha_1,\ldots,\alpha_r).
\]
The second condition is the minimality condition: no proper intermediate field
between $F$ and $K$ contains all roots of $f$.

Splitting fields exist and are unique up to an $F$-isomorphism.
:::
