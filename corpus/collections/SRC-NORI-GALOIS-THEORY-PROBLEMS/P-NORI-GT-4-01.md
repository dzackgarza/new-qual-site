---
schema: qual/card@1
id: P-NORI-GT-4-01
kind: problem
title: Adjugate matrix and solving $Tw=\det(T)v$ over a commutative ring
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.1 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let R be a commutative ring and let $T \in \mathrm { M } _ { n } ( R )$ . Show that for every $v \in R ^ { n }$ there exists $w \in R ^ { n }$ such that $T w = \operatorname* { d e t } ( T ) v$

Hint: This is a consequence of the definition of the adjoint matrix adj(T ) and the fact that $T . \mathrm { a d j } ( T )$ equals the scalar matrix det(T ).

Remark: In reality, the above adjoint matrix is simply $\Lambda ^ { n - 1 } ( T )$ Therefore this problem could be stated and solved entirely within the framework of exterior algebras, with no reference to matrices.
:::
