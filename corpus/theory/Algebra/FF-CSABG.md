---
schema: qual/card@1
id: FF-CSABG
kind: fact
title: The Artin--Rees lemma
prompts:
- What is the Artin-Rees lemma?
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Modules
  - Ideals
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative [[D-TZXBO|Noetherian]] ring, let $I\subseteq R$ be an [[D-GOFWL|ideal]], let $M$ be a finitely generated $R$-module, and let $N\subseteq M$ be a submodule.
Then there is an integer $c\ge0$ such that for every $n\ge c$,
$$
I^nM\cap N=I^{n-c}\qty{I^cM\cap N}.
$$
:::
