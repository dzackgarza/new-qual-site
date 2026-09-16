---
schema: qual/card@1
id: P-BERK89S-07
kind: problem
title: Solve the matrix ODE $X'=AXB$ for two nilpotent shift matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix},
\qquad
B=\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
\]
Find the general solution of
\[
\frac{dX}{dt}=AXB
\]
for an unknown $4\times4$ matrix-valued function $X(t)$.
:::
