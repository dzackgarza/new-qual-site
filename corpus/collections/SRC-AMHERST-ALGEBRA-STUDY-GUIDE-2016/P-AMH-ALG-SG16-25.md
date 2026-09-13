---
schema: qual/card@1
id: P-AMH-ALG-SG16-25
kind: problem
title: Amherst algebra study guide problem 25
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
(February 2013) Suppose that $R$ is commutative and has a multiplicative identity $1$.
Let $I\subseteq J\subseteq R$ be ideals, and suppose that the quotient ring $R/I$ is a field.
If $I\subsetneq J$, prove that $1\in J$.
[In fact, it is a Theorem from Math 350 that $J=R$ in this case, but you are only being asked to prove that $1\in J$. In particular, however, you may not quote the $J=R$ theorem.]
:::

::: {.solution}
Proof.
BecauseI ⊊J, there existsr∈J rI. By the coset relation, r /∈I impliesI +r⁄=I +0 = 0 R/I. Thus,I +r is nonzero.
By the deﬁnition of ﬁeld, every nonzero element of R/I has a multiplicative inverse.
Hence, there exists I +s∈R/I such that (I +r)(I +s) =I + 1. So I +rs =I + 1, and therefore 1−rs∈I⊆J by the coset relation.
Note that rs∈J, because J is an ideal of R and r∈J. Thus, since J is closed under addition, we have 1 = (1−rs) +rs∈J. QED
:::
