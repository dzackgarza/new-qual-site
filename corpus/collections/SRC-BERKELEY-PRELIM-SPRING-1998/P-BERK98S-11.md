---
schema: qual/card@1
id: P-BERK98S-11
kind: problem
title: Sylvester's criterion for a real quadratic form in three variables
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
---

::: {.problem}
Let $A,B,C,D,E,F\in\mathbb R$. Show that
\[
Ax^2+2Bxy+Cy^2+2Dxz+2Eyz+Fz^2
\]
is positive definite if and only if
\[
A>0,
\qquad
\det\begin{pmatrix}A&B\\B&C\end{pmatrix}>0,
\qquad
\det\begin{pmatrix}A&B&D\\B&C&E\\D&E&F\end{pmatrix}>0.
\]
:::
