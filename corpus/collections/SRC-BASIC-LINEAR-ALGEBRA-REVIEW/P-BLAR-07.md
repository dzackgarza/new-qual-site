---
schema: qual/card@1
id: P-BLAR-07
kind: problem
title: Decide linearity and find transformation matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md. In part (d), the deterministic source declares a map from R^3 to R^2 but writes the input as T(x,y); the card preserves this mismatch explicitly rather than silently inventing a third argument.
---

::: {.problem}
Decide which of the following transformations are linear. For those that are, find the matrix of the transformation (using the standard bases):

(a) $T\colon \RR^2 \to \RR^2$ is defined by $T(x,y) = (2x, y)$

(b) $T\colon \RR^2 \to \RR^2$ is defined by $T(x,y) = (x+1, y+2)$

(c) $T\colon \RR^2 \to \RR^2$ rotates an object by an angle of $\pi/3$

(d) $T\colon \RR^3 \to \RR^2$ is defined by $T(x,y) = (x+2y, x+3y)$
:::

::: {.remark}
In part (d) the declared domain is $\RR^3$, but the formula has two input variables. As a map $\RR^2\to\RR^2$, $T(x,y)=(x+2y,x+3y)$ is linear with matrix $\begin{pmatrix}1&2\\1&3\end{pmatrix}$.
:::
