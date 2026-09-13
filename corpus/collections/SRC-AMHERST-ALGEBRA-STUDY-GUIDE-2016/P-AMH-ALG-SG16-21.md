---
schema: qual/card@1
id: P-AMH-ALG-SG16-21
kind: problem
title: Amherst algebra study guide problem 21
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
(January 2009) Let I⊆ R be an ideal of R, and suppose that xy−yx∈ I for every x,y ∈ R. Prove that the quotient ring R/I is commutative.
:::

::: {.solution}
Proof. GivenI +a,I +b∈R/I, our assumption on I implies that ab−ba∈I. By the coset relation,
we obtain I +ab =I +ba. Then
(I +a)(I +b) =I +ab =I +ba = (I +b)(I +a),
so R/I is commutative, as desired QED
:::
