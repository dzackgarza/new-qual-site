---
schema: qual/card@1
id: P-AMH-ALG-SG16-26
kind: problem
title: Amherst algebra study guide problem 26
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
(January 2014) For the polynomial ring R = R[x], deﬁne I ={f∈R|f(2) =f(5) = 0}. Prove that I is an ideal of R.
:::

::: {.solution}
Proof. (Nonempty) Note that 0∈ R gives the constant polynomial 0 ∈R. Since 0(2) = 0(5) = 0, we
have 0∈I.
(Closed under−) Given f,g ∈I, we have f(2) =f(5) =g(2) =g(5) = 0. So
(f−g)(2) =f(2)−g(2) = 0− 0 = 0, and (f−g)(5) =f(5)−g(5) = 0− 0 = 0, and hence f−g∈I.
(Sticky) Given f∈I and g∈R, we have f(2) =f(5) = 0. So
(gf )(2) =g(2)f(2) =g(2)· 0 = 0, and (gf )(5) =g(5)f(5) =g(5)· 0 = 0. Thus, gf∈I.
Since R is commutative, we also have fg =gf∈I. QED

The Division Algorithm. Know the statement of the division algorithm in k[x]. Here is a problem that
uses the division algorithm.
:::
