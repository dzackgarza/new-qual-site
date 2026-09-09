---
schema: qual/card@1
id: P-BIFDZ
kind: problem
title: Non-isomorphic groups can have isomorphic automorphism groups
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Counterexamples
  - Classification
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
- Find two groups $G\not\cong H$ where $\Aut G\cong \Aut H$.
:::


::: {.solution}
Take
\[
G=C_3,
\qquad
H=C_4.
\]
Then $G\not\cong H$ because they have different orders. On the other hand,
\[
\Aut(C_n)\cong (\ZZ/n\ZZ)^\times.
\]
Therefore
\[
\Aut(C_3)\cong (\ZZ/3\ZZ)^\times\cong C_2
\]
and
\[
\Aut(C_4)\cong (\ZZ/4\ZZ)^\times\cong C_2.
\]
Hence
\[
\Aut(G)\cong\Aut(H)
\]
even though $G\not\cong H$.
:::
