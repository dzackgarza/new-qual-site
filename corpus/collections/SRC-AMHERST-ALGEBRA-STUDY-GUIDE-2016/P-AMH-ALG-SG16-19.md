---
schema: qual/card@1
id: P-AMH-ALG-SG16-19
kind: problem
title: Amherst algebra study guide problem 19
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
(January 2010) Let R be a commutative ring and S⊆R a subset of R. Deﬁne the annihilator of S in R to be Ann(S) ={r∈R|rs = 0 for every s∈S}. Prove that Ann(S) is an ideal of R.
:::

::: {.solution}
Proof. (Nonempty) We have 0∈ Ann(S), since 0s = 0∀s∈S. So Ann(S)⁄= ∅.
(Closed under−) Given a,b ∈ Ann(S) and s∈ S, we have (a−b)s = as−bs = 0− 0 = 0, so that
a−b∈ Ann(S).
(Sticky) Given r∈ R and x∈ Ann(S), and given any s∈ S, we have ( rx)s = r(xs) = r(0) = 0.
Thus,rx∈ Ann(S). Since R is commutative, xr =rx∈ Ann(S). QED
:::
