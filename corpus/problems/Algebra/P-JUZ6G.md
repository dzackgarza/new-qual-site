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
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The statement left G undeclared; it now declares G as a group.
---

::: {.problem}
Let $G$ be a group. Show that
$$
Z(G)=\bigcap_{a\in G}C_G(a).
$$
:::

::: {.solution}

::: pf

::: pf-step

An element $x\in G$ lies in $\bigcap_{a\in G}C_G(a)$ if and only if $x\in Z(G)$.

::: pf-proof

By definition $C_G(a)=\{x\in G:xa=ax\}$, so $x$ lies in every $C_G(a)$ exactly when $xa=ax$ for every $a\in G$, which is the definition of $x\in Z(G)$.

:::

:::

:::

:::
