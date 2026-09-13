---
schema: qual/card@1
id: P-UCLAB15S-09
kind: problem
title: Match two pairs of subspaces by a linear operator
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $V=\mathbb R^n$, and let $U_1,U_2,W_1,W_2\subset V$ be subspaces of dimension $d$ such that
\[
\dim(U_1\cap W_1)=\dim(U_2\cap W_2)=\ell,
\qquad \ell\le d\le n.
\]
Prove that there exists a linear operator $T:V\to V$ such that
\[
T(U_1)=U_2,\qquad T(W_1)=W_2.
\]
:::
