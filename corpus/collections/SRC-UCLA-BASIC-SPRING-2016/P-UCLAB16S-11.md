---
schema: qual/card@1
id: P-UCLAB16S-11
kind: problem
title: Determinants of a skew-tridiagonal Toeplitz family
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $M_n$ be the tridiagonal $n\times n$ matrix, with $a,b>0$,
\[
M_n=
\begin{pmatrix}
a&b&0&\cdots&0\\
-b&a&b&\ddots&\vdots\\
0&-b&a&\ddots&0\\
\vdots&\ddots&\ddots&\ddots&b\\
0&\cdots&0&-b&a
\end{pmatrix}.
\]
Prove that $\det M_n>0$ for all $n$. Prove that the limit
\[
\lim_{n\to\infty}\log\det M_n
\]
exists and compute its value.
:::
