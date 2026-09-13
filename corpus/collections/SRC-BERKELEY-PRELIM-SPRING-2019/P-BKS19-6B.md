---
schema: qual/card@1
id: P-BKS19-6B
kind: problem
title: Berkeley Spring 2019 preliminary exam problem 6B
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
---

::: {.problem}
Let $\mathbb Z_2$ be the ring of integers modulo $2$.
Prove the identity in $\mathbb Z_2[x_1,\ldots,x_n]$
\[
\det\!\begin{pmatrix}
x_1&\cdots&x_n\\
x_1^2&\cdots&x_n^2\\
\vdots&&\vdots\\
x_1^{2^{n-1}}&\cdots&x_n^{2^{n-1}}
\end{pmatrix}
=
\prod_{(a_1,\ldots,a_n)\ne(0,\ldots,0)}(a_1x_1+\cdots+a_nx_n),
\]
where $(a_1,\ldots,a_n)$ runs over all nonzero elements of $\mathbb Z_2^n$.
:::
