---
schema: qual/card@1
id: P-3JNFF
kind: problem
title: Normal subgroups of $A_4$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Find all normal subgroups of $A_4$.
:::

::: {.solution}

::: pf

::: {.pf-step #classes}

The conjugacy classes of $A_4$ are $\{e\}$, the class $\{(12)(34),(13)(24),(14)(23)\}$ of size $3$, and two classes of size $4$ consisting of $3$-cycles.

::: pf-proof

The double transpositions form one class: conjugating $(12)(34)$ by $(123)$ gives $(23)(14)$, and by $(132)$ gives $(31)(24)$. The centralizer of $(123)$ in $A_4$ is $\langle(123)\rangle$, of order $3$, so its class has size $12/3=4$. The eight $3$-cycles therefore split into two classes of size $4$.

:::

:::

::: {.pf-step #unions}

A normal subgroup of $A_4$ has order $1$, $4$ or $12$, and is $\{e\}$, $V_4=\{e,(12)(34),(13)(24),(14)(23)\}$ or $A_4$.

::: pf-proof

A normal subgroup is a union of conjugacy classes containing $\{e\}$, and its order divides $12$. By step [](#classes){.pf-ref}, the possible orders of such unions are $1$, $4$, $5$, $8$, $9$ and $12$; of these only $1$, $4$, $12$ divide $12$. The only union of order $4$ is $V_4$, since a class of size $4$ together with $\{e\}$ has order $5$.

:::

:::

::: pf-step

The normal subgroups of $A_4$ are exactly $\boxed{\{e\},\ V_4,\ A_4}$.

::: pf-proof

Each of the three sets in step [](#unions){.pf-ref} is a subgroup: $V_4$ is closed under multiplication, since the product of two distinct nonidentity elements of $V_4$ is the third. Each is a union of conjugacy classes, hence normal.

:::

:::

:::

:::
