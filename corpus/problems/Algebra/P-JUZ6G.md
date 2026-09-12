---
schema: qual/card@1
id: P-JUZ6G
kind: problem
title: $Z(G) = \bigcap_{a \in G} C_G(a)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
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
Show that
\[
Z(G)=\bigcap_{a\in G}C_G(a).
\]
:::

::: {.solution}
By definition,
\[
Z(G)=\{x\in G:xa=ax\text{ for every }a\in G\}.
\]
For a fixed $a\in G$,
\[
C_G(a)=\{x\in G:xa=ax\}.
\]
Therefore an element $x$ lies in every $C_G(a)$ exactly when it commutes with every element of $G$. Hence
\[
\bigcap_{a\in G}C_G(a)
=\{x\in G:xa=ax\text{ for all }a\in G\}
=Z(G).
\]
:::
