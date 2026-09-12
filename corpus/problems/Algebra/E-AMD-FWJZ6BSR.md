---
schema: qual/card@1
id: E-AMD-FWJZ6BSR
kind: problem
title: Every ring has a proper maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every non-zero ring with identity has a proper maximal ideal.
:::

::: {.solution}
Let $R\ne0$ be a ring with identity, and let $\mathcal P$ be the set of proper ideals of $R$, ordered by inclusion. Since $(0)$ is proper, $\mathcal P$ is nonempty.

Let $\mathcal C\subseteq\mathcal P$ be a chain and set
\[
J=\bigcup_{I\in\mathcal C} I.
\]
Because $\mathcal C$ is totally ordered by inclusion, $J$ is an ideal: any two of its elements lie together in one member of the chain, and absorption by elements of $R$ is inherited from that member. Also $J$ is proper, since $1\in J$ would imply $1\in I$ for some $I\in\mathcal C$, contradicting $I\ne R$.

Thus every chain in $\mathcal P$ has an upper bound in $\mathcal P$. By Zorn's lemma, $\mathcal P$ has a maximal element, which is precisely a proper maximal ideal of $R$.
:::
