---
schema: qual/card@1
id: P-BERK86S-08
kind: problem
title: Count the points in the unit disk where a polynomial matrix is singular
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The extraction garbles the matrix size, but the displayed source matrix is 3-by-3.
---

:::{.problem}
Let
\[
A(z)=\begin{pmatrix}
4z^2&1&-1\\
-1&2z^2&0\\
3&0&1
\end{pmatrix}.
\]
How many distinct values $z$ satisfy
\[
|z|<1
\]
and make $A(z)$ noninvertible?
:::
