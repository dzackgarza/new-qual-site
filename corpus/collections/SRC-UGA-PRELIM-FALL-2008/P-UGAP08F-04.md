---
schema: qual/card@1
id: P-UGAP08F-04
kind: problem
title: Diagonalize the matrix displayed in the Fall 2008 prelim and compute its nineteenth power
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: "The retained markdown extraction does not preserve the displayed matrix A reliably: it declares a three-column array but emits four entry fields per row, with blank fields. Repository history contains the same damaged extraction and no independent statement of the matrix, so the missing entries are not guessed."
---

::: {.problem}
Let
$$
A=\begin{pmatrix}
-1&0&0\\
-2&3&-2\\
-2&3&-2
\end{pmatrix}.
$$

Prove that $A$ is diagonalizable and use this fact to compute
\[
A^{19}.
\]
:::
