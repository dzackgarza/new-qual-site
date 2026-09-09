---
schema: qual/card@1
id: P-IQPLX
kind: problem
title: An $m$-cycle is odd iff $m$ is even
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that an $m$-cycle is an odd permutation iff $m$ is even.
:::


::: {.solution}
An $m$-cycle can be written as a product of $m-1$ transpositions:
\[
(a_1\ a_2\ \cdots\ a_m)
=
(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2).
\]
Therefore its sign is
\[
(-1)^{m-1}.
\]
This equals $-1$ exactly when $m-1$ is odd, equivalently when $m$ is even. Hence an $m$-cycle is odd iff $m$ is even.
:::
