---
schema: qual/card@1
id: P-UCLAB03S-07
kind: problem
title: The annihilator of a sum of two subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Examination, May 2003 PDF. The source writes functionals $f:V\to F$ although $V$ is specified to be real and no field $F$ is defined; the intended real dual is used here.
---

::: {.problem}
Let $V$ be a finite-dimensional real vector space.
For a subspace $W\subset V$, define its annihilator by
\[
W^0=\{f:V\to\mathbb R\text{ linear}: f|_W=0\}.
\]
If $W_1,W_2\subset V$ are subspaces, prove that
\[
W_1^0\cap W_2^0=(W_1+W_2)^0.
\]
:::
