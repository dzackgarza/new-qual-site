---
schema: qual/card@1
id: P-VPB55
kind: problem
title: Jordan canonical form over a non-algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Canonical Forms
  - Rational Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Talk about Jordan canonical form.
What happens when the field is not algebraically closed?
:::

::: {.solution}
Over an algebraically closed field, every matrix is similar to a direct sum of Jordan blocks
\[
J_m(\lambda).
\]
For each eigenvalue $\lambda$, the numbers and sizes of the blocks are determined by the generalized eigenspaces, equivalently by the nullities of the powers
\[
(A-\lambda I)^k.
\]

Over a field $F$ that is not algebraically closed, the characteristic polynomial may not split, so a Jordan form over $F$ need not exist. For example, the real rotation
\[
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]
has no real eigenvalues and hence no Jordan form over $\mathbb R$.

The canonical substitute valid over every field is the rational canonical form. Viewing $F^n$ as an $F[x]$-module via $x\cdot v=Av$, the structure theorem over the PID $F[x]$ gives invariant factors
\[
d_1\mid d_2\mid\cdots\mid d_r,
\]
and the rational canonical form is the block diagonal matrix of their companion matrices. When all invariant factors split into powers of linear factors, this data refines to the usual Jordan form.
:::
