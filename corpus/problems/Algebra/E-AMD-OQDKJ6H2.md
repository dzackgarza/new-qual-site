---
schema: qual/card@1
id: E-AMD-OQDKJ6H2
kind: problem
title: $Z(G)=\bigcap_{a\in G}C_G(a)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the identity to its defining equivalence.
---

::: {.exercise}
Show that
\[
Z(G)=\bigcap_{a\in G}C_G(a).
\]
:::

::: {.solution}
An element $z\in G$ lies in the center exactly when it commutes with every element of $G$:
\[
z\in Z(G)
\iff za=az\text{ for all }a\in G
\iff z\in C_G(a)\text{ for all }a\in G.
\]
The last condition is precisely
\[
z\in\bigcap_{a\in G}C_G(a).
\]
Hence the two subgroups are equal.
:::
