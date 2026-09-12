---
schema: qual/card@1
id: E-HK-0H3A
kind: problem
title: Invertibility of upper-triangular matrices
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
An $n \times n$ matrix A is called upper-triangular if $A_{ij} = 0$ for i > j, that is, if every entry below the main diagonal is 0. Prove that an upper-triangular (square) matrix is invertible if and only if every entry on its main diagonal is different from 0.
:::


::: solution
For an upper-triangular matrix,
\[
\det A=A_{11}A_{22}\cdots A_{nn}.
\]
Indeed, in the Leibniz expansion every nonzero term must choose column $i$ in row $i$ successively: row $n$ has no nonzero entry left of column $n$, then row $n-1$ must use column $n-1$, and so on. Thus only the identity permutation contributes.

A square matrix over a field is invertible if and only if its determinant is nonzero. Therefore $A$ is invertible exactly when
\[
A_{11}A_{22}\cdots A_{nn}\ne0,
\]
which is equivalent to every diagonal entry $A_{ii}$ being nonzero.
:::
