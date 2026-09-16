---
schema: qual/card@1
id: FT-PUVIQ
kind: theorem
title: Zorn's lemma
prompts:
- State Zorn's lemma.
classification:
  areas:
  - algebra
  topics:
  - Zorn's Lemma
relations: []
review: draft
---

::: {.theorem}
Let $(P,\le)$ be a partially ordered set in which every [[D-P6XOT|chain]] has an upper bound in $P$.
Then $P$ has a maximal element: an element $m\in P$ such that $m\le x$ with $x\in P$ implies $x=m$.
:::

::: {.remark}
The empty chain is a chain, so the hypothesis forces $P$ to be nonempty.
:::
