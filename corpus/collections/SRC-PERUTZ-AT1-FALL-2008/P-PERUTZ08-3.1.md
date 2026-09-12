---
schema: qual/card@1
id: P-PERUTZ08-3.1
kind: problem
title: Uniqueness of group pushouts
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.1 and Definition 3.3 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
---

::: {.problem}
Let $G_1\xleftarrow{f_1}H\xrightarrow{f_2}G_2$ be homomorphisms. A pushout is a group $P$ with homomorphisms $p_i:G_i\to P$ such that $p_1f_1=p_2f_2$ and with the following universal property: for every group $K$ and maps $k_i:G_i\to K$ satisfying $k_1f_1=k_2f_2$, there is a unique homomorphism $h:P\to K$ such that $k_i=hp_i$.

Prove that this universal property determines $P$ up to isomorphism. In what sense is the isomorphism unique?
:::
