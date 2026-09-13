---
schema: qual/card@1
id: P-AMH-ALG-SG16-10
kind: problem
title: Amherst algebra study guide problem 10
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
(March 2015) Let G1,G 2 be groups, let H2⊆ G2 be a subgroup, and let φ : G1→ G2 be a homomorphism. Deﬁne H1 ={x∈G1|φ(x)∈H2}. It is a fact, which you may assume, that H1 is a subgroup of G1. Prove that for any x,y ∈ G1, H1x =H1y if and only if H2φ(x) =H2φ(y).
:::

::: {.solution}
Proof. (=⇒) Given x,y ∈G1 such that H1x =H1y, we have xy−1∈H1 [by the right coset relation
for H1]. So φ(x)φ(y)−1 =φ
(
xy−1)
∈H2, by deﬁnition of H1. Thus, [by the right coset relation for
H2], we have H2φ(x) =H2φ(y).
(⇐=) Given x,y ∈ G1 such that H2φ(x) = H2φ(y), we have φ(x)φ(y)−1∈ H2 [by the right coset
relation for H2]. Thus,
φ
(
xy−1)
=φ(x)φ(y)−1∈H2,
and therefore xy−1∈ H1, by deﬁnition of H1. Thus, [by the right coset relation for H1], we have
H1x =H1y. QED
:::
