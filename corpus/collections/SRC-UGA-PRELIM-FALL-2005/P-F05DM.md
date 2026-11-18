---
schema: qual/card@1
id: P-F05DM
kind: problem
title: 'De Morgan: complement of an intersection is the union of complements'
classification:
  areas:
  - prelim
  topics:
  - Set Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $Z$ be a set and let $X_1, X_2, \dots$ be subsets of $Z$.
Prove the formula $\bigl(\bigcap_i X_i\bigr)^c = \bigcup_i X_i^c$, where $(\cdot)^c$ denotes complement.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own elementwise argument follows, with the two implications as separate steps.

Let $Z$ be a set, $\theset{X_{i}}$ a family of subsets of $Z$, and $(\cdot)^{c}$ complement in $Z$.

::: pf

::: {.pf-step #left-in-right}
Every element of $\big(\bigcap_{i}X_{i}\big)^{c}$ lies in $\bigcup_{i}X_{i}^{c}$.

::: pf-proof
Let $z\in\big(\bigcap_{i}X_{i}\big)^{c}$, that is $z\notin\bigcap_{i}X_{i}$. By the definition of intersection, $z$ fails to belong to at least one $X_{i}$: there is an index $i$ with $z\notin X_{i}$, that is $z\in X_{i}^{c}$, and hence $z\in\bigcup_{i}X_{i}^{c}$.
:::

:::

::: {.pf-step #right-in-left}
Every element of $\bigcup_{i}X_{i}^{c}$ lies in $\big(\bigcap_{i}X_{i}\big)^{c}$.

::: pf-proof
Let $z\in\bigcup_{i}X_{i}^{c}$: there is $i$ with $z\in X_{i}^{c}$, that is $z\notin X_{i}$. Then $z$ is not in the intersection of all the $X_{i}$, because membership in the intersection requires membership in every one of them; so $z\in\big(\bigcap_{i}X_{i}\big)^{c}$.
:::

:::

::: {.pf-qed}
The two inclusions of steps [](#left-in-right){.pf-ref} and [](#right-in-left){.pf-ref} give $\big(\bigcap_{i}X_{i}\big)^{c}=\bigcup_{i}X_{i}^{c}$. Nothing in the argument uses countability of the index set, so the identity holds for an arbitrary family.
:::

:::

:::
