---
schema: qual/card@1
id: P-UCLAB05F-08
kind: problem
title: Operator norm and completeness of the matrix space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Examination, September 2005 PDF. The source's displayed definition of `\|A\|` is typographically incomplete; the associated map $T_A$ and all three requested parts determine the standard operator norm used here.
---

::: {.problem}
For a real $n\times n$ matrix $A$, let $T_A:\mathbb R^n\to\mathbb R^n$ be the associated linear map.
Use the operator norm
\[
\|A\|=\sup_{\|x\|_2=1}\|T_Ax\|_2,
\]
where $\|\cdot\|_2$ is the Euclidean norm.

(a) Prove that
\[
\|A+B\|\leq\|A\|+\|B\|.
\]

(b) Use part (a) to check that the set $M$ of all real $n\times n$ matrices is a metric space for
\[
d(A,B)=\|B-A\|.
\]

(c) Prove that $M$ is complete for this metric.

Suggestion: the $(i,j)$ entry of $A$ is $\langle T_Ae_j,e_i\rangle$, where $e_i$ is the $i$th standard basis vector.
:::
