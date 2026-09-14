---
schema: qual/card@1
id: P-BKF78-9
kind: problem
title: Orthogonality-preserving linear maps are scalar-unitary
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the deterministic MinerU Flash extraction. The extraction garbles the implication symbols; the surrounding text uniquely states that orthogonal vectors are sent to orthogonal vectors.
---

::: {.problem}
For $x,y\in\mathbb C^n$, let
\[
\langle x,y\rangle=\sum_j x_j\overline{y_j}
\]
be the Hermitian inner product.
Let $T$ be a linear operator on $\mathbb C^n$ such that
\[
\langle x,y\rangle=0
\quad\Longrightarrow\quad
\langle Tx,Ty\rangle=0.
\]
Prove that $T=kS$ for some scalar $k$ and some unitary operator $S$, i.e.
\[
\langle Sx,Sy\rangle=\langle x,y\rangle
\]
for all $x,y$.
:::
