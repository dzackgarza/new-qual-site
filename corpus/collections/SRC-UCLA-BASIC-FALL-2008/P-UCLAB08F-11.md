---
schema: qual/card@1
id: P-UCLAB08F-11
kind: problem
title: Periodic finite-difference Poisson matrix solvability
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Consider the periodic Poisson problem on $[0,1]$
\[
u''=f,\qquad u(0)=u(1),
\]
and its second-order finite-difference system
\[
A\mathbf u=\Delta x^2\mathbf f,
\]
where $\Delta x=1/n$ and
\[
A=\begin{pmatrix}
-2&1&0&\cdots&0&1\\
1&-2&1&0&\cdots&0\\
0&1&-2&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&1&-2&1\\
1&0&\cdots&0&1&-2
\end{pmatrix}.
\]

<1>1. Show that $A$ is singular.

<1>2. Determine the condition on $\mathbf f$ necessary and sufficient for a solution to exist.
:::
