---
schema: qual/card@1
id: P-HFGO7
kind: problem
title: Algebraic closure of a field
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

::: {.problem}
Define an algebraic closure of a field.
:::

::: {.solution}
An \dfn{algebraic closure} of a field $F$ is an extension field $\overline F/F$
such that

1. $\overline F$ is algebraic over $F$, and
2. $\overline F$ is algebraically closed.

Equivalently, every element of $\overline F$ is algebraic over $F$, and every
nonconstant polynomial in $\overline F[x]$ has a root in $\overline F$.

Algebraic closures exist for every field and are unique up to an
$F$-isomorphism, although not canonically unique.
:::

::: {.remark title="Example"}
$\CC$ is an algebraic closure of $\RR$ but not of $\QQ$.
$\CC$ is algebraically closed by the fundamental theorem of algebra, and $\CC=\RR(i)$ is algebraic over $\RR$.
Over $\QQ$, $\CC$ is not algebraic: the algebraic numbers form a countable set, while $\CC$ is uncountable.
:::
