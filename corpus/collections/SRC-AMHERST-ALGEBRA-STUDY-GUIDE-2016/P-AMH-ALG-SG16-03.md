---
schema: qual/card@1
id: P-AMH-ALG-SG16-03
kind: problem
title: Elements commuting with the cosets of a subgroup form a subgroup
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
(January 2016) Let $G$ be a group, let $H\subseteq G$ be a subgroup, and define the set
\[
K=\{x\in G\mid Hx=xH\}.
\]
Prove that $K$ is a subgroup of $G$.
:::

::: {.solution}
Proof.
We prove thatK is a subgroup of G as follows.
(1) Let e be the identity element of G. Then He =H =eH, so e∈K. (2) Given a,b∈K, we have H(ab) = (Ha)b = (aH)b =a(Hb) =a(bH) = (ab)H. So ab∈K. (3) Given a∈K, we have Ha =aH. Multiplying by a−1 on the left and the right gives a−1(Ha)a−1 =a−1(aH)a−1 =⇒ a−1H(aa−1) = (a−1a)Ha−1, which implies a−1H =Ha−1. Thus a−1∈K, proving that K is a subgroup.
QED
:::
