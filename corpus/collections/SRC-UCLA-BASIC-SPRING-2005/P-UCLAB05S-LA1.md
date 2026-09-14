---
schema: qual/card@1
id: P-UCLAB05S-LA1
kind: problem
title: Trace-zero matrices and sums of commutators
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 1 of the official UCLA Basic Exam, May 2005 PDF; the retained PDF has the commutator sum indexed from $j=1$ to $m$.
---

::: {.problem}
For $n\geq1$, let
\[
\operatorname{tr}:M_n(\mathbb C)\longrightarrow\mathbb C,
\qquad
\operatorname{tr}(A)=\sum_{k=1}^n A_{k,k}.
\]

(a) Determine a basis for the kernel of $\operatorname{tr}$.

(b) For $X\in M_n(\mathbb C)$, show that $\operatorname{tr}(X)=0$ if and only if there are an integer $m$ and matrices
\[
A_1,\ldots,A_m,B_1,\ldots,B_m\in M_n(\mathbb C)
\]
such that
\[
X=\sum_{j=1}^m(A_jB_j-B_jA_j).
\]
:::
