---
schema: qual/card@1
id: P-AMH-ALG-SG16-17
kind: problem
title: Ideals of $\mathbb Z$ containing relatively prime integers
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 1982) Prove that if an ideal $I$ of the ring $\mathbb{Z}$ contains two relatively prime integers, then $I=\mathbb{Z}$.
:::

::: {.solution}
Proof.
By hypothesis, there exist a,b∈I with gcd(a,b ) = 1. Thus, there are integers m,n∈ Z such thatma +nb = 1. But ma,nb∈I by the sticky property, so 1 = ma +nb∈I sinceI is closed under +. For any x∈ Z, then, we have x =x· 1∈I by the sticky property.
So I = Z QED
:::
