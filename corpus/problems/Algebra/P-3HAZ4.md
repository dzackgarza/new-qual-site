---
schema: qual/card@1
id: P-3HAZ4
kind: problem
title: $C_G(G)=Z(G)$
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
- Show that $C_G(G) = Z(G)$.
:::


::: {.solution}
<1>1. By definition,
\[
C_G(G)=\{g\in G:gx=xg\text{ for every }x\in G\}.
\]
::: {.proof}
The centralizer $C_G(S)$ of a subset $S\subseteq G$ consists of the elements of $G$ commuting with every element of $S$. Taking $S=G$ gives the displayed set.
:::

<1>2. By definition,
\[
Z(G)=\{g\in G:gx=xg\text{ for every }x\in G\}.
\]
::: {.proof}
This is the definition of the center of a group.
:::

<1>3. Therefore $C_G(G)=Z(G)$.
::: {.proof}
The two subsets described in <1>1 and <1>2 have exactly the same membership condition.
:::
:::
