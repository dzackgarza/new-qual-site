---
schema: qual/card@1
id: P-AMH-ALG-SG16-20
kind: problem
title: Amherst algebra study guide problem 20
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
(March 2015) Let $R=\mathbb{Z}[x]$ be the ring of polynomials (in one variable) with integer coefficients.
Note that the constant polynomial $6$ and the degree one polynomial $x+1$ are both elements of $R$.
Define
\[
I=\{6f+(x+1)g\mid f,g\in R\}.
\]
Prove that $I$ is an ideal of $R$.
:::

::: {.solution}
Proof.
(Nonempty) Let f =g = 0∈R. Then 6f + (x + 1)g∈I, so I⁄= ∅. (Closed under−) Givena,b∈I, writea = 6f1+(x+1)g1 andb = 6f2+(x+1)g2 withf1,f 2,g 1,g 2∈R. Then a−b = 6f1 + (x + 1)g1− ( 6f2 + (x + 1)g2 ) = 6(f1−f2) + (x + 1)(g1−g2)∈I. (Sticky) Given a∈I and h∈R, write a = 6f + (x + 1)g with f,g ∈R. Then ah =ha =h ( 6f + (x + 1)g ) = 6(hf) + (x + 1)(hg)∈I QED

10 Quotient Rings Recall that an ideal I⊆R is a subgroup under addition, so the cosets of I are usually written I +r ={s +r|s∈I}, although sometimes you see r +I since addition is commutative.
The deﬁnition of ideal guarantees that the set of cosets R/I ={I +r|r∈R} becomes a ring, called the quotient ring, under the following operations: (I +a) + (I +b) =I + (a +b) and ( I +a)(I +b) =I +ab.
:::
