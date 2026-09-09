---
schema: qual/card@1
id: E-AMD-2MKY6V2W
kind: problem
title: Diagonalizability versus invertibility
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Matrices
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Does diagonalizable imply invertible?
The converse?
:::

::: {.solution}
Neither implication holds.

<1>1. A diagonalizable matrix need not be invertible.
::: {.proof}
For example,
\[
A=\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]
is diagonal, hence diagonalizable, but \(\det A=0\). More generally, a diagonalizable matrix is invertible exactly when none of its eigenvalues is zero.
:::

<1>2. An invertible matrix need not be diagonalizable.
::: {.proof}
Take
\[
B=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Then \(\det B=1\), so \(B\) is invertible. Its characteristic polynomial is \((t-1)^2\), while
\[
\ker(B-I)=\ker\begin{pmatrix}0&1\\0&0\end{pmatrix}
=\operatorname{span}\!\left\{\binom10\right\}
\]
has dimension \(1\). Thus the geometric multiplicity of the only eigenvalue is smaller than its algebraic multiplicity, so \(B\) is not diagonalizable.
:::
:::
