---
schema: qual/card@1
id: PR-UTFSY
kind: proposition
title: Existence of maximal ideals
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a [[D-GURUB|ring]] and $I\subsetneq R$ a proper [[D-GOFWL|ideal]].
Then $I$ is contained in a [[D-7XH2R|maximal ideal]] of $R$.
:::

::: {.proof}
Let $\mathcal S$ be the set of proper ideals of $R$ containing $I$, ordered by inclusion; it is nonempty since $I\in\mathcal S$.
If $\mathcal C\subseteq\mathcal S$ is a nonempty chain, then $J\coloneqq\bigcup_{J'\in\mathcal C}J'$ is an ideal containing $I$, and $1\notin J$ because $1$ lies in no proper ideal, so $J\in\mathcal S$ is an upper bound for $\mathcal C$.
By Zorn's lemma $\mathcal S$ has a maximal element $\mathfrak m$.
Any ideal strictly containing $\mathfrak m$ contains $I$ and is not in $\mathcal S$, so it equals $R$; thus $\mathfrak m$ is a maximal ideal.
:::
