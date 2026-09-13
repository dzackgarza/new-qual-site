---
schema: qual/card@1
id: P-BKF80-9
kind: problem
title: Distance from $\operatorname{diag}(1,2)$ to the singular two-by-two matrices
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction mangles the displayed generic matrix and the layout of A, but preserves the four coordinates x,y,z,t and the diagonal entries 1,2 of A. It also prints ||X||=x^2+y^2+z^2+t^2 while calling d(X,Y)=||X-Y|| a metric; this may have lost either a square root or a square on the norm symbol. The printed formula is preserved rather than silently repaired.
---

::: {.problem}
For
\[
X=\begin{pmatrix}x&y\\z&t\end{pmatrix},
\]
define
\[
\|X\|=x^2+y^2+z^2+t^2,
\qquad
d(X,Y)=\|X-Y\|.
\]
Let
\[
\Sigma=\{X:\det X=0\},
\qquad
A=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
\]
Find the minimum distance from $A$ to $\Sigma$, and exhibit a matrix $S\in\Sigma$ attaining the minimum.

The retained extraction prints the displayed formula for $\|X\|$ exactly as above, although with that formula $d$ is not literally a metric; the missing typographic detail is unrecovered.
:::
