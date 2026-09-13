---
schema: qual/card@1
id: P-PRELIM82S-07
kind: problem
title: Determinant of $X\mapsto(AX+XA)/2$ on $M_3(\mathbb R)$
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
  note: The extraction garbles the matrix-space size as B-by-B, but the source displays A as 3-by-3 and AX+XA therefore forces V=M_3(R).
---

::: {.problem}
Let $V=M_3(\mathbb R)$ and let
\[
A=\begin{pmatrix}
1&0&0\\
0&2&0\\
0&0&1
\end{pmatrix}.
\]
Define the linear transformation $T:V\to V$ by
\[
T(X)=\frac12(AX+XA).
\]
Compute $\det T$.
:::
