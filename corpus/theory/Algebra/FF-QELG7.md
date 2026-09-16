---
schema: qual/card@1
id: FF-QELG7
kind: fact
title: Krull's theorem on maximal ideals
prompts:
- What is Krull's theorem?
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

::: {.fact}
Let $R$ be a commutative ring.
Every proper [[D-GOFWL|ideal]] $I\subsetneq R$ is contained in a [[D-7XH2R|maximal ideal]] of $R$.
In particular, applying this to $I=0$, every nonzero commutative ring has a maximal ideal.
:::

::: {.proof}
Let $P$ be the set of proper ideals of $R$ containing $I$, ordered by inclusion; it contains $I$.
The union of a nonempty chain in $P$ is an ideal containing $I$, and it is proper because it does not contain $1$, so it is an upper bound in $P$; the empty chain has the upper bound $I$.
By [[FT-PUVIQ|Zorn's lemma]], $P$ has a maximal element, which is a maximal ideal of $R$ containing $I$.
:::
