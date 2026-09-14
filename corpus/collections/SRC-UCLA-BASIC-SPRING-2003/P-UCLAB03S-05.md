---
schema: qual/card@1
id: P-UCLAB03S-05
kind: problem
title: Extremizing a binary quadratic form on the unit circle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Examination, May 2003 PDF. The source defines the constraint set using the undefined symbol $s^2+y^2=1$; the variables everywhere else are $(x,y)$, so the intended unit-circle equation is $x^2+y^2=1$.
---

::: {.problem}
Consider
\[
F(x,y)=ax^2+2bxy+cy^2
\]
on the unit circle
\[
A=\{(x,y):x^2+y^2=1\}.
\]

(a) Show that $F$ has a maximum and a minimum on $A$.

(b) Use Lagrange multipliers to show that, if the maximum of $F$ on $A$ occurs at $(x_0,y_0)$, then $(x_0,y_0)$ is an eigenvector of
\[
\begin{pmatrix}
a&b\\
b&c
\end{pmatrix}.
\]
:::
