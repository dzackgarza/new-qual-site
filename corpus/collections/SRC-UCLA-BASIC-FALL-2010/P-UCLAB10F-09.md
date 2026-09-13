---
schema: qual/card@1
id: P-UCLAB10F-09
kind: problem
title: Convergence of a linear stationary iteration
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 9. Consider the iteration
\[
\vec x_{k+1}=A^{-1}(B\vec x_k+\vec c),
\]
where
\[
\vec c=\begin{pmatrix}1\\1\end{pmatrix},\qquad
A=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
B=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

(a) Assuming the iteration converges, to what vector $\vec x$ does it converge?

(b) Does the iteration converge for arbitrary initial vectors $\vec x_0$? Justify your answer.
:::
