---
schema: qual/card@1
id: E-AMD-KDSJ3FW4
kind: problem
title: Every proper ideal is contained in a maximal ideal
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
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Kept only the Zorn argument needed to obtain a maximal ideal over the given proper ideal.
---

::: {.exercise}
Show that every proper ideal in a commutative ring with identity is contained in a maximal ideal.
:::

::: {.solution}
Let $I\subsetneq R$ and consider
\[
\mathcal F=\{J\trianglelefteq R: I\subseteq J\subsetneq R\},
\]
ordered by inclusion. This set is nonempty since $I\in\mathcal F$.

If $\mathcal C\subseteq\mathcal F$ is a chain, then
\[
J=\bigcup_{L\in\mathcal C}L
\]
is an ideal: any two of its elements lie in a common member of the chain. It contains $I$. Moreover $J$ is proper, since $1\in J$ would imply $1\in L$ for some $L\in\mathcal C$, contradicting $L\ne R$. Hence every chain has an upper bound in $\mathcal F$.

By Zorn's lemma, $\mathcal F$ has a maximal element $\mathfrak m$. By definition, $\mathfrak m$ is a proper ideal containing $I$ and no larger proper ideal contains it. Therefore $\mathfrak m$ is maximal.
:::
